# Generated by Django 4.0.6 on 2022-07-30 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('self_hosted_apps', '0003_rename_feed_image_apppage_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='apppage',
            name='github_link',
            field=models.URLField(blank=True),
        ),
    ]