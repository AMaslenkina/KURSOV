# Generated by Django 3.1.4 on 2020-12-16 10:32

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('clientCode', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='Номер клиента')),
                ('FIO', models.CharField(max_length=50, verbose_name='ФИО')),
                ('address', models.CharField(max_length=50, verbose_name='Адресс')),
                ('phone', models.CharField(max_length=13, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('passportCode', models.CharField(help_text='2 буквы и 7 цифр', max_length=9, verbose_name='Код поспорта')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('employeeCode', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='Номер сотрудника')),
                ('FIO', models.CharField(max_length=50, verbose_name='ФИО')),
                ('post', models.CharField(max_length=50, verbose_name='Должность')),
                ('passportCode', models.CharField(help_text='2 буквы и 7 цифр', max_length=9, verbose_name='Номер паспорта')),
                ('address', models.CharField(max_length=50, verbose_name='Адресс')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('phone', models.CharField(max_length=13, verbose_name='Телефон')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('projectCode', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='Номер проекта')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('describe', models.CharField(max_length=300, verbose_name='Описание')),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.client', verbose_name='Клиент')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.employees', verbose_name='Сотрудник')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
