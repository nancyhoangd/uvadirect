# Generated by Django 3.1.5 on 2021-04-05 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_page', '0006_auto_20210403_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='_profile_friends_+', to='profile_page.profile'),
        ),
    ]
