# Generated by Django 4.0.3 on 2022-03-29 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('self_hosted', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='app_name',
            field=models.CharField(default='test', max_length=250),
            preserve_default=False,
        ),
    ]
