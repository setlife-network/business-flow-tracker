from django.shortcuts import render
from django.http import JsonResponse
from .models import Project, Service
from .forms import ConsultationRequestForm

def homepage(request):
    projects = Project.objects.all()
    services = Service.objects.all()
    form = ConsultationRequestForm()

    context = {
        'projects': projects,
        'services': services,
        'form': form
    }

    return render(request, 'index.html', context)

def portfolio(request):
    projects = Project.objects.all()

    context = {
        'projects': projects
    }

    return render(request, 'portfolio.html', context)

def services(request):
    services = Service.objects.all()

    context = {
        'services': services
    }

    return render(request, 'services.html', context)

def contact(request):
    if request.method == 'POST':
        form = ConsultationRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Consultation request submitted successfully'})
        else:
            return JsonResponse({'message': 'Invalid form data'}, status=400)
    else:
        form = ConsultationRequestForm()

    context = {
        'form': form
    }

    return render(request, 'contact.html', context)
