from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("registration-success/", views.success, name="success"),
    path("admin-panel/login/", views.admin_login, name="admin_login"),
    path("admin-panel/logout/", views.admin_logout, name="admin_logout"),
    path("admin-panel/", views.dashboard, name="dashboard"),
    path("admin-panel/registration/<int:pk>/", views.registration_detail, name="registration_detail"),
    path("admin-panel/registration/<int:pk>/edit/", views.registration_edit, name="registration_edit"),
    path("admin-panel/registration/<int:pk>/delete/", views.registration_delete, name="registration_delete"),
    path("admin-panel/export/excel/", views.export_excel, name="export_excel"),
    path("admin-panel/export/pdf/", views.export_pdf, name="export_pdf"),
]
