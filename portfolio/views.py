from django.shortcuts import render

from . import models
# Create your views here.


def dashboard(request):
    about_me = models.About_me.objects.get(id=1)
    projects = models.Portfolio.objects.all()
    my_contact = models.My_contact.objects.get(id=1)
    context = {
        'about_me': about_me,
        'projects': projects,
        'my_contact': my_contact,
    }
    return render(request, 'portfolio/dashboard.html', context)
