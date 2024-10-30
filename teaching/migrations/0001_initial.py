# Generated by Django 5.1.2 on 2024-10-30 02:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('identifier', models.CharField(blank=True, max_length=60)),
                ('description', models.TextField(blank=True)),
                ('date', models.DateField(blank=True, db_index=True, null=True)),
                ('schedule', models.CharField(blank=True, max_length=60)),
                ('office_hour', models.CharField(blank=True, max_length=60)),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='course', to='home.person')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='course', to='home.location')),
                ('reading', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='course', to='teaching.reading')),
            ],
        ),
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=60)),
                ('due_date', models.DateField()),
                ('pdf', models.FileField(blank=True, null=True, upload_to='homeworks/pdfs/')),
                ('course', models.ManyToManyField(related_name='homework', to='teaching.course')),
            ],
        ),
    ]