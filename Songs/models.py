from itertools import count
from unicodedata import category
from django.db import models

# Create your models here.


tags = (
    ('Classical','Classical'),
    ('Romantic','Romantic'),
    ('Pop','Pop'),
    ('Rock','Rock'),
    ('Devotional','Devotional'),
    ('Bhajan', 'Bhajan'),
    ('Dance','Dance'),
    ('Disco','Disco'),
    ('Ghazal','Ghazal'),
    ('Qawwali','Qawwali'),
)


genre = (
    ('Album','Album'),
    ('Bollywood','Bollywood'),
    ('Hollywood','Hollywood'),
)


language = (
    ('Hindi','Hindi'),
    ('Engligh','English'),
    ('Rajasthani','Rajasthani'),
    ('Haryanvi', 'Haryanvi'),
    ('Punjabi','Punjabi')
)


yearOfRelease = (
    ('2021','2021'),
    ('2020','2020'),
    ('2019','2019'),
    ('2018','2018'),
    ('2017','2017'),
    ('2016','2016'),
    ('2015', '2015'),
    ('2014', '2014'),
    ('2013', '2013'),
    ('2012', '2012'),
    ('2011', '2011'),
    ('2010', '2010'),
    ('2009', '2009'),
    ('2008', '2008'),
    ('2007', '2007'),
    ('2006', '2006'),
    ('2005', '2005'),
    ('2004','2004'),
    ('2003','2003'),
    ('2002','2002'),
    ('2001','2001'),
    ('2000','2000'),
    ('1995','1995'),
    ('1990','1990'),
    ('1985','1985'),
)



productionHouse = (
    ('T-Series','T-Series'),
    ('Sony Music','Sony Music'),
    ('Zee Music Company','Zee Music Company'),
    ('Unknown','Unknown')
)




class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    song_name = models.CharField(max_length=200)
    singers = models.CharField(max_length=200)
    song = models.FileField(upload_to='songs',max_length=254,null=True)
    genre = models. CharField(choices=genre, max_length=20, default='Album')
    category = models.CharField(max_length=200)
    language = models.CharField(choices=language, max_length=20, default='Hindi')
    tags = models.CharField(choices=tags, max_length=20, default='Classical')
    count = models.IntegerField(default=0)
    image = models.ImageField(upload_to='song_image',null=True)
    year =  models.CharField(choices=yearOfRelease, max_length=20, default='2021')
    movie = models.CharField(max_length=200)
    production_house = models.CharField(choices=productionHouse, max_length=20, default='Unknown')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.song_name