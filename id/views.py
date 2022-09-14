from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic import View
from io import BytesIO
from xhtml2pdf import pisa
from django.template.loader import render_to_string
from django import template
from django.template import loader

# json
def json(request):
    personids = list(Id.objects.values())
    arrivaltimes = list(Arival_time.objects.values())
    return JsonResponse(
        {"personids": personids, "arrivaltimes": arrivaltimes}, safe=False
    )


# wokring on html and pdf
def GeneratePdf(request):
    products = Id.objects.all()
    context = {"products": products}
    return render(request, "base.html", context)


def pdf_report_create(request):
    products = Id.objects.all()

    template_path = "pdfcreate.html"
    context = {"products": products}
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'filename="products_report.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse("We had some errors <pre>" + html + "</pre>")
    return response
