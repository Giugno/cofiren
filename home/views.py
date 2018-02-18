from django.shortcuts import render

def presentation(request):
    return render(request, 'home/presentation.html')

def historique(request):
    return render(request, 'home/historique.html')

def services(request):
    return render(request, 'home/services.html')

def contact(request):
    return render(request, 'home/contact.html')

def liens(request):
    return render(request, 'home/liens.html')
