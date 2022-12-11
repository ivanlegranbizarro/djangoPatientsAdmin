from django.db import models
from django.urls import reverse


class Patient(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('TM', 'TransMale'),
        ('TF', 'TransFemale'),
        ('GF', 'GenderFluid'),
        ('O', 'Other'),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    notes = models.TextField(blank=True, null=True)
    smoker = models.BooleanField(default=False)
    alcohol = models.BooleanField(default=False)
    drugs = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ('first_name', 'last_name', 'age',)

    def get_absolute_url(self):
        return reverse('patients:detail_patient', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
