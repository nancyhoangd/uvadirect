# Generated by Django 3.1.5 on 2021-04-16 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_page', '0015_auto_20210412_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='_profile_friends_+', to='profile_page.profile'),
        ),
    ]