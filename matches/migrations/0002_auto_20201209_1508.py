# Generated by Django 2.2.15 on 2020-12-09 20:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teams', '0001_initial'),
        ('matches', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchreport',
            name='reported_winner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='winnerreporting', to='teams.Team'),
        ),
        migrations.AddField(
            model_name='matchreport',
            name='reporting_team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teamreporting', to='teams.Team'),
        ),
        migrations.AddField(
            model_name='matchreport',
            name='reporting_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='userreporting', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='matchdispute',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disputedMatch', to='matches.Match'),
        ),
        migrations.AddField(
            model_name='matchdispute',
            name='team1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team1', to='teams.Team'),
        ),
        migrations.AddField(
            model_name='matchdispute',
            name='team1origreporter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team1OriginalReporter', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='matchdispute',
            name='team2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team2', to='teams.Team'),
        ),
        migrations.AddField(
            model_name='matchdispute',
            name='team2origreporter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team2OriginalReporter', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='matchdispute',
            name='teamreporter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team1Disputer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='matchcheckin',
            name='match',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='match_checkin', to='matches.Match'),
        ),
        migrations.AddField(
            model_name='matchcheckin',
            name='players',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='matchcheckin',
            name='reporter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='checkin_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='matchcheckin',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='checking_in_team', to='teams.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='awayteam',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='awayteam', to='teams.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='game',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='GameChoice', to='matches.GameChoice'),
        ),
        migrations.AddField(
            model_name='match',
            name='hometeam',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hometeam', to='teams.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='loser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='loser', to='teams.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='map',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='match_map', to='matches.MapChoice'),
        ),
        migrations.AddField(
            model_name='match',
            name='maps',
            field=models.ManyToManyField(to='matches.MapPoolChoice'),
        ),
        migrations.AddField(
            model_name='match',
            name='platform',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='PlatformChoice', to='matches.PlatformChoice'),
        ),
        migrations.AddField(
            model_name='match',
            name='sport',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='SportChoice', to='matches.SportChoice'),
        ),
        migrations.AddField(
            model_name='match',
            name='team1reportedwinner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team1reportedwinner', to='teams.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='team2reportedwinner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team2reportedwinner', to='teams.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='winner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='champions', to='teams.Team'),
        ),
        migrations.AddField(
            model_name='mappoolchoice',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='map_pool_for', to='matches.GameChoice'),
        ),
        migrations.AddField(
            model_name='mappoolchoice',
            name='maps',
            field=models.ManyToManyField(blank=True, to='matches.MapChoice'),
        ),
        migrations.AddField(
            model_name='mapchoice',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='map_for', to='matches.GameChoice'),
        ),
    ]
