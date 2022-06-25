# Generated by Django 2.2.7 on 2020-12-14 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='captain_teams',
            field=models.ManyToManyField(blank=True, related_name='profile_captain_teams', to='teams.Team'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='founder_teams',
            field=models.ManyToManyField(blank=True, related_name='profile_founder_teams', to='teams.Team'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='player_teams',
            field=models.ManyToManyField(blank=True, related_name='profile_player_teams', to='teams.Team'),
        ),
    ]
