from django.urls import path, include
from . import views

app_name = 'patients'

urlpatterns = [
    path('', views.FrontEnd.as_view(), name='frontend'),
    path('backend/', views.Backend.as_view(), name='backend'),
    path('login/', include('django.contrib.auth.urls')),
    path('create-patient', views.CreatePatient.as_view(), name='create_patient'),
    path('detail-patient/<int:pk>', views.DetailPatient.as_view(), name='detail_patient'),
    path('delete-patient/<int:pk>', views.delete_patient, name='delete_patient'),
]
