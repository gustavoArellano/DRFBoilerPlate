# Generated by Django 3.0.5 on 2020-04-16 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_api', '0004_auto_20200415_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Email',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
