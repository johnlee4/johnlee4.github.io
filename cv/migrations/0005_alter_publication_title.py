# Generated by Django 5.1.2 on 2024-10-30 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0004_alter_publication_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]