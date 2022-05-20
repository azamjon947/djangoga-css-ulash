from django.shortcuts import render

def home(request):
    return render(request, 'base.html')
def about(request):
    return render(request, 'about.html')
def section(request):
    return render(request, 'section.html')
def web(request):
    return render(request, 'web.html')
def navbar(request):
    return render(request, 'navbar.html')
def footer(request):
    return render(request, 'footer.html')