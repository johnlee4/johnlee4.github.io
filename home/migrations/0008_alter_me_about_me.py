# Generated by Django 5.1.2 on 2024-10-31 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_banner_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='me',
            name='about_me',
            field=models.TextField(help_text='Markdown text enabled'),
        ),
    ]