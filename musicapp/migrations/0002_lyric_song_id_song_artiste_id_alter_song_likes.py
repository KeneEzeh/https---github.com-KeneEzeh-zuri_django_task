# Generated by Django 4.1.2 on 2022-10-13 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lyric',
            name='song_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='song',
            name='artiste_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='song',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
