from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages, auth
from Songs.forms import SongForm
from Songs.models import Song
from AdminApp.forms import EditSong
# Create your views here.


@csrf_exempt                                                                                                                                                       
def admin_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(
            email=email, password=password, is_superadmin=True)
        if user is not None and user.is_superadmin == True:
            request.session['key'] = 'value'
            #  auth.login(request,user)
            messages.success(request, 'Admin Online')
            return redirect('dashboard')
        else:
            messages.error(request, 'You are not an admin')
            return redirect('admin_login')
    # messages.error(request,'Invalid Entry')
    return render(request, 'admin/login.html')





def dashboard(request):
    return render(request, 'admin/dashboard.html')


def upload_song(request):
    
    form = SongForm()

    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('song_list')

    context = {
        'form': form
    }
    return render(request, 'admin/upload_song.html', context)
    
    
def song_list(request):
    if request.session.has_key('key'):
        songs = Song.objects.all()[::-1]
        return render(request, 'admin/songlist.html', {'songs': songs, })
    else:
        return redirect('dashboard')
    
    
def edit_song(request,song_id):
    song = Song.objects.get(song_id=song_id)
    form = EditSong(instance = song)
    
    if request.method == 'POST':
        form = EditSong(request.POST,instance = song)
        if form.is_valid():
            try :
                form.save()
            except:
                context = {
                    'form':form
                }
                return render(request, 'admin/edit_song.html',context)
            return redirect('song_list')
    context = {'form': form}
    return render(request, 'admin/edit_song.html', context)
    
def delete_song(request,song_id):
    song = Song.objects.get(song_id = song_id)
    song.delete()
    return redirect('song_list')