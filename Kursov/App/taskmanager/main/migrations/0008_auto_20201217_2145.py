# Generated by Django 3.1.4 on 2020-12-17 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20201217_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post',
            field=models.CharField(max_length=50, verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='project',
            name='describe',
            field=models.CharField(help_text='Не больше 300 символов', max_length=300, verbose_name='Описание'),
        ),
    ]
