# Generated by Django 3.1 on 2020-11-22 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0002_auto_20201121_1906'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=1000)),
                ('type', models.CharField(choices=[('true', 'true'), ('false', 'false')], max_length=10)),
            ],
            options={
                'verbose_name': 'Choices',
                'verbose_name_plural': 'Choicess',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.RemoveField(
            model_name='activity',
            name='add',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='lesson',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='solution',
        ),
        migrations.RemoveField(
            model_name='explanation',
            name='document',
        ),
        migrations.AddField(
            model_name='activity',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='activity',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='explanation',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.CreateModel(
            name='Examination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Courses.lesson')),
            ],
            options={
                'verbose_name': 'Examination',
                'verbose_name_plural': 'Examinations',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='activity',
            name='exam',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Courses.examination'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='suggestions',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Courses.choices'),
        ),
        migrations.DeleteModel(
            name='Suggestion',
        ),
    ]
