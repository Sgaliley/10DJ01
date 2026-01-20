from django.http import HttpResponse

def data(request):
    return HttpResponse("<h1>DATA page</h1><p>Здесь будут данные</p>")

def test(request):
    return HttpResponse("<h1>TEST page</h1><p>Здесь тестовая страница</p>")
