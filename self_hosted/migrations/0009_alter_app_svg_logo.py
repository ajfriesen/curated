# Generated by Django 4.0.3 on 2022-04-08 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('self_hosted', '0008_alter_app_svg_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='svg_logo',
            field=models.FileField(default='300x300.svg', upload_to='logos'),
        ),
    ]
