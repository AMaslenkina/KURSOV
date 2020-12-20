from django.db import models
import uuid


class Client(models.Model):
    clientCode = models.UUIDField(default=uuid.uuid4, verbose_name='Код клиента', primary_key=True)
    FIO = models.CharField(verbose_name='ФИО', max_length=50)
    address = models.CharField(verbose_name='Адресс', max_length=50)
    phone = models.CharField(verbose_name='Телефон', max_length=13, unique=True)
    email = models.EmailField(verbose_name='E-mail', unique=True)
    passportCode = models.CharField(verbose_name='Код поспорта', help_text='2 буквы и 7 цифр', max_length=9, unique=True)

    def __str__(self):
        return self.FIO

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Post(models.Model):
    postCode = models.UUIDField(default=uuid.uuid4, verbose_name='Код должности', primary_key=True)
    post = models.CharField(verbose_name='Должность', max_length=50)

    def __str__(self):
        return self.post

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

class Employees(models.Model):
    employeeCode = models.UUIDField(default=uuid.uuid4, verbose_name='Код сотрудника', primary_key=True, )
    FIO = models.CharField(verbose_name='ФИО', max_length=50)
    passportCode = models.CharField(verbose_name='Номер паспорта', help_text='2 буквы и 7 цифр', max_length=9, unique=True)
    address = models.CharField(verbose_name='Адресс', max_length=50)
    email = models.EmailField(verbose_name='E-mail', unique=True)
    phone = models.CharField(verbose_name='Телефон', max_length=13, unique=True)
    post = models.ForeignKey(
        Post,
        verbose_name='Должность',
        on_delete=models.PROTECT,
        null=True
    )

    def __str__(self):
        return self.FIO

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

class Project(models.Model):
    projectCode = models.UUIDField(default=uuid.uuid4, verbose_name='Код проекта', primary_key=True)
    name = models.CharField(verbose_name='Название', max_length=50)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    describe = models.CharField(verbose_name='Описание', help_text='Не больше 300 символов', max_length=300)
    employee = models.ManyToManyField(
        'Employees',
        verbose_name='Сотрудники',
        db_table='main_mm'
        # on_delete=models.CASCADE,
        # null=True
        # through='ProEmp'
    )

    client = models.ForeignKey(
        'Client',
        verbose_name='Клиент',
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.name
    '''def __str__(self):
        a = self.name
        return str(a)'''

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

'''class ProEmplo(models.Model):

    employee = models.ForeignKey(
        Employees,
        related_name='eml',
        on_delete=models.CASCADE
    )
    projects = models.ForeignKey(
        Project,
        related_name='pro',
        on_delete=models.CASCADE
    )
def __str__(self):
    return str(self.id)'''
'''def __str__(self):
    return str(self.eployee.id) + str(self.projects.id)'''