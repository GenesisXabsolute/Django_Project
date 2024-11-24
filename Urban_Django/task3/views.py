from django.shortcuts import render

def index(request):
    return render(request, 'third_task/main_page.html')

def games(request):
    return render(request, 'third_task/first_page.html')

def basket(request):
    return render(request, 'third_task/second_page.html')