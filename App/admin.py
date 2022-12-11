from django.contrib import admin
from .models import Patient


class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'gender', 'smoker', 'alcohol', 'drugs', 'created_at')
    search_fields = ('first_name', 'last_name', 'age')
    list_filter = ('gender',)
    list_per_page = 10


admin.site.register(Patient, PatientAdmin)
