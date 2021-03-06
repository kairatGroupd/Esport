# Generated by Django 2.2.12 on 2021-07-27 23:08

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20210721_1925'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaticPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=50)),
                ('page_name', models.CharField(max_length=50)),
                ('content', ckeditor.fields.RichTextField(default='')),
            ],
        ),
    ]
