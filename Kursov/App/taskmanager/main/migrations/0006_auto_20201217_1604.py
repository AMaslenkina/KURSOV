# Generated by Django 3.1.4 on 2020-12-17 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_project_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='employee',
        ),
        migrations.AddField(
            model_name='project',
            name='employees',
            field=models.ManyToManyField(to='main.Employees', verbose_name='Сотрудники'),
        ),
    ]
