# Generated by Django 3.1.4 on 2020-12-19 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20201219_0443'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employees',
            name='pr',
        ),
        migrations.RemoveField(
            model_name='project',
            name='employee',
        ),
        migrations.AddField(
            model_name='project',
            name='employee',
            field=models.ManyToManyField(to='main.Employees', verbose_name='Сотрудники'),
        ),
    ]