from django.db import models

# Create your models here.
class Todo(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)

    class Meta:
        ordering = ['title']
 
    def __str__(self):
        return f"{self.title} : is complete : {self.complete}"