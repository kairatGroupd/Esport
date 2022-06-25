# Generated by Django 2.2.15 on 2020-12-09 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='unknown', max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='game_images')),
            ],
        ),
        migrations.CreateModel(
            name='MapChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='default_map', max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('map_num', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MapPoolChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='default map pool', max_length=255)),
                ('description', models.CharField(default='No map pool description', max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=20, null=True)),
                ('matchnum', models.SmallIntegerField(default=0)),
                ('reported', models.BooleanField(default=False)),
                ('completed', models.BooleanField(default=False)),
                ('bestof', models.SmallIntegerField(choices=[(0, 'Best of 1'), (1, 'Best of 3'), (2, 'Best of 5'), (3, 'Best of 7'), (4, 'Best of 9')], default=0)),
                ('teamformat', models.SmallIntegerField(choices=[(0, '1v1'), (1, '2v2'), (2, '3v3'), (3, '4v4'), (4, '5v5'), (5, '6v6')], default=1)),
                ('team1reported', models.BooleanField(default=False)),
                ('team2reported', models.BooleanField(default=False)),
                ('info', models.TextField(default='Match Info: ')),
                ('disputed', models.BooleanField(default=False)),
                ('bye_1', models.BooleanField(default=False)),
                ('bye_2', models.BooleanField(default=False)),
                ('disable_userreport', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'matches',
            },
        ),
        migrations.CreateModel(
            name='MatchCheckIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='MatchDispute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('teamproof_1', models.URLField()),
                ('teamproof_2', models.URLField(blank=True)),
                ('teamproof_3', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='MatchStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matchid', models.PositiveIntegerField(default=0)),
                ('map', models.CharField(default='unknown', max_length=255)),
                ('team1', models.CharField(default='unknown', max_length=255)),
                ('team2', models.CharField(default='unknown', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PlatformChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='unknown', max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='platform_images')),
            ],
        ),
        migrations.CreateModel(
            name='SportChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='unknown sports', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='StatsPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('kills', models.IntegerField(default=0)),
                ('assists', models.IntegerField(default=0)),
                ('deaths', models.IntegerField(default=0)),
                ('killround', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('adr', models.IntegerField(default=0)),
                ('ud', models.IntegerField(default=0)),
                ('ef', models.IntegerField(default=0)),
                ('f_assists', models.IntegerField(default=0)),
                ('hs', models.IntegerField(default=0)),
                ('kast', models.IntegerField(default=0)),
                ('awp_k', models.IntegerField(default=0)),
                ('twok', models.IntegerField(default=0)),
                ('threek', models.IntegerField(default=0)),
                ('fourk', models.IntegerField(default=0)),
                ('fivek', models.IntegerField(default=0)),
                ('one_v_one', models.IntegerField(default=0)),
                ('one_v_two', models.IntegerField(default=0)),
                ('one_v_three', models.IntegerField(default=0)),
                ('one_v_four', models.IntegerField(default=0)),
                ('one_v_five', models.IntegerField(default=0)),
                ('f_kills', models.IntegerField(default=0)),
                ('f_deaths', models.IntegerField(default=0)),
                ('entries', models.IntegerField(default=0)),
                ('trades', models.IntegerField(default=0)),
                ('rounds', models.IntegerField(default=0)),
                ('rf', models.IntegerField(default=0)),
                ('ra', models.IntegerField(default=0)),
                ('damage', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TeamMatchStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rounds_won', models.PositiveSmallIntegerField(default=0)),
                ('rounds_lost', models.PositiveSmallIntegerField(default=0)),
                ('total_kills', models.PositiveSmallIntegerField(default=0)),
                ('total_deaths', models.PositiveSmallIntegerField(default=0)),
                ('avg_rating', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('avg_killround', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('avg_adr', models.IntegerField(default=0)),
                ('avg_ud', models.IntegerField(default=0)),
                ('avg_ef', models.IntegerField(default=0)),
                ('total_rating', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('total_killround', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('total_adr', models.IntegerField(default=0)),
                ('total_ud', models.IntegerField(default=0)),
                ('total_ef', models.IntegerField(default=0)),
                ('avg_hs', models.IntegerField(default=0)),
                ('avg_kast', models.IntegerField(default=0)),
                ('awp_k', models.IntegerField(default=0)),
                ('twok', models.IntegerField(default=0)),
                ('threek', models.IntegerField(default=0)),
                ('fourk', models.IntegerField(default=0)),
                ('fivek', models.IntegerField(default=0)),
                ('one_v_one', models.IntegerField(default=0)),
                ('one_v_two', models.IntegerField(default=0)),
                ('one_v_three', models.IntegerField(default=0)),
                ('one_v_four', models.IntegerField(default=0)),
                ('one_v_five', models.IntegerField(default=0)),
                ('f_kills', models.IntegerField(default=0)),
                ('f_deaths', models.IntegerField(default=0)),
                ('entries', models.IntegerField(default=0)),
                ('trades', models.IntegerField(default=0)),
                ('rounds', models.IntegerField(default=0)),
                ('avg_damage', models.IntegerField(default=0)),
                ('total_damage', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MatchReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('proof', models.CharField(default='no text inserted', max_length=300)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matchreporting', to='matches.Match')),
            ],
        ),
    ]