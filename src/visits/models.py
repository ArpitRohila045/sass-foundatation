from django.db import models

# Create your models here.
class PageVisits(models.Model):

    page_name = models.CharField(max_length=255)
    visit_time = models.DateTimeField(auto_now_add=True)