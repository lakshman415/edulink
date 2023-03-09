from django.shortcuts import render
from .models import Subject, Material
from django.conf import settings

import os
def subject_list(request):
    subjects = Subject.objects.all()
    context = {'subjects': subjects}
    return render(request, 'subject_list.html', context)


from django.http import HttpResponse

def material_list(request, subject_id):
    materials = Material.objects.filter(subject_id=subject_id)
    files = [{'name': material.file.name.split("/")[-1], 'url': material.file.url} for material in materials]
    context = {'files': files}
    return render(request, 'material_list.html', context)

def download_file(request, file_name:str):
    file_path = os.path.join(settings.MEDIA_ROOT, "materials/"+file_name)
    with open(file_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
        return response

