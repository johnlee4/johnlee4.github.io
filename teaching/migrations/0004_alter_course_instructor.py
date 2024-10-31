# Generated by Django 5.1.2 on 2024-10-31 18:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
        ('teaching', '0003_alter_course_instructor_alter_course_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='instructor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='course', to='home.person'),
        ),
    ]