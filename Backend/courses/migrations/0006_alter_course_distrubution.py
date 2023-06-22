# Generated by Django 4.2.2 on 2023-06-19 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_rename_prerequisites_course_pre_req'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='distrubution',
            field=models.CharField(choices=[('Science', 'SCI'), ('Humanities', 'HUM'), ('Social Science', 'SSC'), ('None', 'N/A')], max_length=14),
        ),
    ]
