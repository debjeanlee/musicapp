# Generated by Django 3.1.4 on 2020-12-07 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_song_artist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='artist',
        ),
        migrations.AddField(
            model_name='song',
            name='artists',
            field=models.ManyToManyField(blank=True, related_name='artists', to='app.Artist'),
        ),
    ]