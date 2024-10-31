# Generated by Django 5.1.2 on 2024-10-30 14:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_banner', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('blog_banner', models.ImageField(blank=True, null=True, upload_to='photos/')),
            ],
        ),
        migrations.CreateModel(
            name='Me',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.person')),
                ('about_me', models.TextField()),
                ('github', models.URLField(blank=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='photos/')),
            ],
            bases=('home.person',),
        ),
    ]