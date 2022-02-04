from django import forms
from .models import Song


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields=['song_name','singers','song','genre','category','language','tags','image','year','movie','production_house']
        
        
    def  __init__(self,*args,**kwargs):
        super(SongForm,self).__init__(*args,**kwargs)
        self.fields['song_name'].widget.attrs['placeholder'] =  'Enter The Song Name' 
        self.fields['genre'].widget.attrs['placeholder'] =  'Mention the genre'
        self.fields['category'].widget.attrs['placeholder'] =  'Select category'
        self.fields['language'].widget.attrs['placeholder'] =  'Select the language'
        self.fields['tags'].widget.attrs['placeholder'] =  'Mention the tags'
        self.fields['year'].widget.attrs['placeholder'] =  'Select year'
        self.fields['movie'].widget.attrs['placeholder'] =  'Mention the movie name'
        self.fields['production_house'].widget.attrs['placeholder'] =  'Select the production house'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] =  'form-control' 