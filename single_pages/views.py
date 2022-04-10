from django.shortcuts import render

def landing(request):
    return render(
        request,
        'single_pages/landing.html'
    )

def Pig(request):
    return render(
        request,
        'single_pages/Pig.html'
    )


# Create your views here.
