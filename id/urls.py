from django.urls import path
from . import views

urlpatterns = [
    path(
        "json/",
        views.json,
    ),
    path("pdf/", views.GeneratePdf, name="GeneratePdf"),
    path("createpdf", views.pdf_report_create, name="createpdf"),
]
