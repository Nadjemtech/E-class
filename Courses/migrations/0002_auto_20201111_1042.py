# Generated by Django 3.1 on 2020-11-11 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, max_length=2000, null=True, upload_to=''),
        ),
    ]
