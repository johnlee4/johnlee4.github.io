# Generated by Django 5.1.2 on 2024-10-31 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_rename_blog_banner_banner_banner_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='page',
            field=models.SlugField(blank=True, help_text="Enter the template name, e.g., 'home', 'about'", unique=True),
        ),
    ]
