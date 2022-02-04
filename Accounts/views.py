from django.shortcuts import redirect, render
from django.contrib import messages, auth
from .models import Account
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
# Verification email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
# Create your views here.


def user_login(request):
    
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = auth.authenticate(email=email, password=password)
        
        if user is not None:
            auth.login(request,user)
            messages.success(request,'Authenticated Successfully.')
            return redirect('home')
        messages.error(request,'Invalid Credentials!')
    return render(request,'user/user_signin.html')


def user_register(request):
    
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            #if we use django form it is necessary to do cleaned_data/ to fetch the data from request
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            username = email.split('@')[0]

            request.session['first_name'] = first_name
            request.session['last_name'] = last_name
            request.session['email'] = email
            request.session['checkmobile'] = phone_number
            request.session['password'] = password
            request.session['username'] = username
            
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.phone_number = phone_number
            user.is_active = False
            user.save()
            
            # USER ACTIVATION
            current_site = get_current_site(request)
            mail_subject = 'Please activate your account'
            message = render_to_string('user/account_verification_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            # messages.success(request, 'Thank you for registering with us. We have sent you a verification email to your email address [pameeramrp@gmail.com]. Please verify it.')
            return redirect('/Accounts/user_login/?command=verification&email='+email)
    else:
        form = RegistrationForm(request.POST)
    context = {
        'form':form
    }
    return render(request,'user/user_register.html',context)



def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Congratulations! Your account is activated.')
        return redirect('user_login')
    else:
        messages.error(request, 'Invalid activation link')
        return redirect('user_register')
    

@login_required(login_url = 'user_login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('user_login')