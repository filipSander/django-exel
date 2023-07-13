from django.shortcuts import render
from django.views import View
from django.contrib import messages

from utils.uploadings import uploadFile


def index(request):
    if request.POST:
        print(request.POST)
        print(request.FILES)
        file = request.FILES['file']
        uploading_file = uploadFile({"file": file})
        if uploading_file:
            messages.success(request, "Файл загружен.")
        else:
            messages.error(request, "Ошибка при загрузке файла.")

            
    return render(request, 'index.html', locals())