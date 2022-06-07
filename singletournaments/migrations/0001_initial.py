# Generated by Django 2.2.15 on 2020-12-09 20:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teams', '0001_initial'),
        ('matches', '0002_auto_20201209_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='SingleEliminationTournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='No name provided', max_length=50, unique=True)),
                ('teamformat', models.SmallIntegerField(choices=[(0, '1v1'), (1, '2v2'), (2, '3v3'), (3, '4v4'), (4, '5v5'), (5, '6v6')], default=1)),
                ('bestof', models.SmallIntegerField(choices=[(0, 'Best of 1'), (1, 'Best of 3'), (2, 'Best of 5'), (3, 'Best of 7'), (4, 'Best of 9')], default=0)),
                ('active', models.BooleanField(default=False)),
                ('twitch', models.CharField(default='twitch', max_length=60)),
                ('open_register', models.DateTimeField()),
                ('close_register', models.DateTimeField()),
                ('allow_register', models.BooleanField(default=False)),
                ('info', models.TextField(default='No information provided')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('req_credits', models.PositiveSmallIntegerField(default=0)),
                ('start', models.DateTimeField()),
                ('current_round', models.SmallIntegerField(blank=True, default=1)),
                ('size', models.PositiveSmallIntegerField(choices=[(4, 4), (8, 8), (16, 16), (32, 32), (64, 64), (128, 128)], default=32)),
                ('xp_seed', models.BooleanField(default=False)),
                ('bracket_generated', models.BooleanField(default=False)),
                ('prize1', models.CharField(default='no prize specified', max_length=50)),
                ('prize2', models.CharField(default='no prize specified', max_length=50)),
                ('prize3', models.CharField(default='no prize specified', max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='tournament_images')),
                ('disable_userreport', models.BooleanField(default=True)),
                ('game', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='game', to='matches.GameChoice')),
                ('map_pool', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='map_pool', to='matches.MapPoolChoice')),
                ('platform', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='matches.PlatformChoice')),
            ],
        ),
        migrations.CreateModel(
            name='SingleTournamentTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seed', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='actualteam', to='teams.Team')),
                ('tournament', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='intournament', to='singletournaments.SingleEliminationTournament')),
            ],
        ),
        migrations.CreateModel(
            name='SingleTournamentRuleset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('text', models.TextField()),
                ('name', models.CharField(max_length=25)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rulesetCreator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SingleTournamentRound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roundnum', models.PositiveSmallIntegerField(default=1)),
                ('matchesnum', models.PositiveSmallIntegerField(default=2)),
                ('info', models.TextField(default='No info specified')),
                ('matches', models.ManyToManyField(to='matches.Match')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='withtournamentround', to='singletournaments.SingleEliminationTournament')),
            ],
        ),
        migrations.AddField(
            model_name='singleeliminationtournament',
            name='ruleset',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tournamentruleset', to='singletournaments.SingleTournamentRuleset'),
        ),
        migrations.AddField(
            model_name='singleeliminationtournament',
            name='second',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='secondplaceteam', to='teams.Team'),
        ),
        migrations.AddField(
            model_name='singleeliminationtournament',
            name='sport',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sport', to='matches.SportChoice'),
        ),
        migrations.AddField(
            model_name='singleeliminationtournament',
            name='teams',
            field=models.ManyToManyField(blank=True, to='teams.Team'),
        ),
        migrations.AddField(
            model_name='singleeliminationtournament',
            name='third',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='thirdplaceteam', to='teams.Team'),
        ),
        migrations.AddField(
            model_name='singleeliminationtournament',
            name='winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='winningteam', to='teams.Team'),
        ),
    ]