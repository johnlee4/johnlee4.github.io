# Generated by Django 5.1.2 on 2024-10-31 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='me',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
