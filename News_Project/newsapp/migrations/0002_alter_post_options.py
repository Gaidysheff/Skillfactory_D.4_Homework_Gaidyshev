# Generated by Django 4.0.4 on 2022-05-13 02:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['dateCreation'], 'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
    ]
