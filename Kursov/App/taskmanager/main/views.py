from django.shortcuts import render, redirect

from .models import Employees
from .models import Client
from .models import Project
from .models import Post


from .forms import FindProject, FindPrice, FindEmpl


def index(request):
    return render(request, 'main/index.html')


def tables(request):
    employee = Employees.objects.all()
    projects = Project.objects.all()
    client = Client.objects.all()

    return render(request, 'main/tables.html', {
        'employee': employee,
        'projects': projects,
        'client': client,
    })


def requests(request):
    # name = Project.objects.all()

    submitbutton = request.POST.get("submit")

    name = ''
    project = ''
    FIO = ''

    form1 = FindProject(request.POST or None)
    form2 = FindEmpl(request.POST or None)

    # if form1.is_valid():
    #     name = form1.cleaned_data.get("name")
    #     project = Project.objects.filter(name__contains=name)
    #
    # if form2.is_valid():
    #     FIO = form2.cleaned_data.get("FIO")
    #     project = Project.objects.filter(name=name)
    # # project = Project.objects.all()

    if form1.is_valid() and form2.is_valid():
        name = form1.cleaned_data.get("name")
        FIO = form2.cleaned_data.get("FIO")

        if name is None:
            name = None
            if name is not None and FIO is not None:
                project = Project.objects.filter(name=name, FIO=FIO)
            elif name is not None:
                project = Project.objects.filter(name=name)
            elif FIO is not None:
                project = Project.objects.filter(FIO=FIO)
        else:
            project = Project.objects.all()

    context = {'form1': form1,
               'form2': form2,
               'name': name,
               'FIO': FIO,
               'submitbutton': submitbutton,
               'project': project,
               }
    return render(request, 'main/requests.html', context)


def employees(request):
    submitbutton = request.POST.get("submit")
    FIO = ''
    empl = ''

    form3 = FindEmpl(request.POST or None)

    if form3.is_valid():
        FIO = form3.cleaned_data.get("FIO")
        empl = Employees.objects.filter(FIO__contains=FIO)

    else:
        empl = Employees.objects.all()

    context = {
        'form3': form3,
        'empl': empl,
        'FIO': FIO,
        'submitbutton': submitbutton,
                }
    return render(request, 'main/employees.html', context)