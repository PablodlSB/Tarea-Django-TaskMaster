from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateField()
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='owned_projects'
    )
    collaborators = models.ManyToManyField(
        User,
        related_name='collaborated_projects',
        blank=True
    )

    def clean(self):
        if self.deadline < timezone.now().date():
            raise ValidationError("La fecha límite no puede estar en el pasado.")

    def __str__(self):
        return self.title


class Task(models.Model):
    STATUS_CHOICES = [
        ('TODO', 'Pendiente'),
        ('INPROG', 'En Progreso'),
        ('DONE', 'Completada'),
    ]

    PRIORITY_CHOICES = [
        ('L', 'Baja'),
        ('M', 'Media'),
        ('H', 'Alta'),
    ]

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=6,
        choices=STATUS_CHOICES,
        default='TODO'
    )
    priority = models.CharField(
        max_length=1,
        choices=PRIORITY_CHOICES,
        default='M'
    )
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.title} ({self.project.title})"
