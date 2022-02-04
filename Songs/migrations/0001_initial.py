# Generated by Django 4.0.1 on 2022-02-03 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('song_id', models.AutoField(primary_key=True, serialize=False)),
                ('song_name', models.CharField(max_length=200)),
                ('singers', models.CharField(max_length=200)),
                ('song', models.FileField(max_length=254, null=True, upload_to='songs')),
                ('genre', models.CharField(choices=[('Album', 'Album'), ('Bollywood', 'Bollywood'), ('Hollywood', 'Hollywood')], default='Album', max_length=20)),
                ('category', models.CharField(max_length=200)),
                ('language', models.CharField(choices=[('Hindi', 'Hindi'), ('Engligh', 'English'), ('Rajasthani', 'Rajasthani'), ('Haryanvi', 'Haryanvi'), ('Punjabi', 'Punjabi')], default='Hindi', max_length=20)),
                ('tags', models.CharField(choices=[('Classical', 'Classical'), ('Romantic', 'Romantic'), ('Pop', 'Pop'), ('Rock', 'Rock'), ('Devotional', 'Devotional'), ('Bhajan', 'Bhajan'), ('Dance', 'Dance'), ('Disco', 'Disco'), ('Ghazal', 'Ghazal'), ('Qawwali', 'Qawwali')], default='Classical', max_length=20)),
                ('count', models.IntegerField(default=0)),
                ('image', models.ImageField(null=True, upload_to='song_image')),
                ('year', models.CharField(choices=[('2021', '2021'), ('2020', '2020'), ('2019', '2019'), ('2018', '2018'), ('2017', '2017'), ('2016', '2016'), ('2015', '2015'), ('2014', '2014'), ('2013', '2013'), ('2012', '2012'), ('2011', '2011'), ('2010', '2010'), ('2009', '2009'), ('2008', '2008'), ('2007', '2007'), ('2006', '2006'), ('2005', '2005'), ('2004', '2004'), ('2003', '2003'), ('2002', '2002'), ('2001', '2001'), ('2000', '2000'), ('1995', '1995'), ('1990', '1990'), ('1985', '1985')], default='2021', max_length=20)),
                ('movie', models.CharField(max_length=200)),
                ('production_house', models.CharField(choices=[('T-Series', 'T-Series'), ('Sony Music', 'Sony Music'), ('Zee Music Company', 'Zee Music Company'), ('Unknown', 'Unknown')], default='Unknown', max_length=20)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
