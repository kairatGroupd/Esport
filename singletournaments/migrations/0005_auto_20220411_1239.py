# Generated by Django 2.2.28 on 2022-04-11 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('singletournaments', '0004_alter_singleeliminationtournament_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singleeliminationtournament',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='singletournamentround',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='singletournamentruleset',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='singletournamentteam',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
