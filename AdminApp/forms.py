
from django import forms
from Songs.models import Song


class EditSong(forms.ModelForm):
    class Meta:
        model = Song
        fields=['song_name','singers','song','genre','category','language','tags','image','year','movie','production_house']