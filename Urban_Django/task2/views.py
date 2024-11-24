from django.shortcuts import render

def func(request):
    return render(request, 'second_task/func_templates.html')

def func2(request):
    return render(request, 'second_task/class_templates.html')

def func3(request):
    return render(request, 'second_task/my_templates.html')