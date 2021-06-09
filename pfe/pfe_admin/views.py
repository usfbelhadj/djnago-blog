from django.shortcuts import render, HttpResponse
from .models import DigitalTeam, Blog, Event
from pfe.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.signals import request_finished

@receiver(post_save, sender=Blog)
def notify(instance, created, *args, **kwargs):
    f = open("notifiction.txt", 'a')
    if created:
        crt = "Create a Blog {} \n ".format(instance.name)
    else:
        crt = "Update a blog {} \n ".format(instance.name)
    f.write(crt)


def index(request):
    pers = DigitalTeam.objects.all()
    event = Event.objects.all()[::-1]
    return render(request, 'index.html', {'pers':pers, 'event':event, })

def blog(request):
    crt = []
    pers = DigitalTeam.objects.all()
    event = Event.objects.all()[::-1]
    blogs = Blog.objects.all()[::-1]
    f = open("notifiction.txt", 'r')
    crt += f.readlines()[::-1]
    crt.pop(0)
    f.close()
    return render(request, 'blog.html', {'pers': pers, 'blogs': blogs, 'event': event, 'crt': crt,})
    

