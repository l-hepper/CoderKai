# Generated by Django 4.2.2 on 2023-08-26 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0021_rename_coderkaipoints_post_kudos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileinfo',
            name='kudos',
            field=models.IntegerField(default=1),
        ),
    ]
