# Generated by Django 4.2.2 on 2023-06-29 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_program'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='program',
            field=models.CharField(default='', max_length=100),
        ),
    ]
