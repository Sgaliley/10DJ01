from django.shortcuts import render

def index(request):
    return render(request, 'pages/index.html')

def new(request):
    return render(request, 'pages/new.html')

def data(request):
    return render(request, 'pages/data.html')

def test(request):
    return render(request, 'pages/test.html')
