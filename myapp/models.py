from django.db import models

"""super usuario administrador
   usuario : chronos
   password: ale123
   correo  : alexander.osiel1993@gmail.com  """
# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title + '-->' + self.project.name
    
