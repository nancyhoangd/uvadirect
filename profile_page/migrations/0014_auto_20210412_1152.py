# Generated by Django 3.1.6 on 2021-04-12 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_page', '0013_auto_20210412_1142'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='class',
            options={'ordering': ['days', 'time']},
        ),
        migrations.RemoveField(
            model_name='class',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='class',
            name='start_time',
        ),
        migrations.AlterField(
            model_name='profile',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='_profile_friends_+', to='profile_page.profile'),
        ),
    ]
