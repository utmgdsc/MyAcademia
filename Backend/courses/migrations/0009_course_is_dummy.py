# Generated by Django 4.2.2 on 2023-07-16 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_course_exclusions_algo_course_pre_req_algo'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_dummy',
            field=models.BooleanField(default=False),
        ),
    ]
