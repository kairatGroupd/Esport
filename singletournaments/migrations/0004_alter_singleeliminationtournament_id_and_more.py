# Generated by Django 4.0.4 on 2022-04-11 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('singletournaments', '0003_auto_20201209_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singleeliminationtournament',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='singletournamentround',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='singletournamentruleset',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='singletournamentteam',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]