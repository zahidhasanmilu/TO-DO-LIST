from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.title + " , " + "COMPLETE : " + str(self.complete)
