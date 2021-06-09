from django.db import models

class DigitalTeam(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="pics", blank=True, null=True)
    job = models.TextField(blank=True, null=True)
    
class Blog(models.Model):
    name = models.CharField(max_length=200)
    name_url = models.URLField(blank=True, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    img = models.ImageField(upload_to='pics',)
    created_at = models.DateTimeField(auto_now=True)
    
    
class Event(models.Model):
    category = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    event_url = models.URLField(blank=True, null=True)
    day = models.DateField(u'Day of the event', help_text=u'Day of the event', blank=True, null=True )
    img = models.ImageField(upload_to='pics', )
    start_time = models.TimeField(u'Starting time', help_text=u'Starting time', blank=True, null=True)
    
    end_time = models.TimeField(u'Final time', help_text=u'Final time', blank=True, null=True)
    
    notes = models.TextField(u'Textual Notes', help_text=u'Textual Notes', blank=True, null=True)
 
    class Meta:
        verbose_name = u'Event'
        verbose_name_plural = u'Event'