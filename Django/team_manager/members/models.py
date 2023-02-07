from django.db import models

class TeamMember(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    ROLE_CHOICES = [
        ('regular', 'Regular'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(
        max_length=7,
        choices=ROLE_CHOICES,
        default='regular',
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

