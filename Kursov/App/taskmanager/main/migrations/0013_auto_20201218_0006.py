# Generated by Django 3.1.4 on 2020-12-17 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20201217_2348'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProEmp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeesCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.employees')),
                ('projectCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.project')),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='employees',
        ),

        migrations.AddField(
            model_name='project',
            name='employees',
            field=models.ManyToManyField(through='main.ProEmp', to='main.Employees', verbose_name='Сотрудники'),
        ),
    ]
