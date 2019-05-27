from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=128)
    users = models.ManyToManyField(User, through='Project_User', related_name = "projects")

    def __str__(self):
        return self.name

class Project_User(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    project = models.ForeignKey(Project, on_delete = models.CASCADE)
    is_mentor = models.BooleanField(default = False)

    class Meta:
        unique_together = ("user", "project")
    
