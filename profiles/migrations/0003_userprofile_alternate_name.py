# Generated by Django 2.2.15 on 2021-01-01 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20201214_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='alternate_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
