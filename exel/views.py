from django.http import FileResponse, HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import UpdateView
from django.contrib import messages
import openpyxl

from exel.models import Product
from .forms import ProductForm

from utils.func import changeProdcut, createExlx, getProducts, uploadFile

def index(request):
    session = request.session.get('ids', [])
    return render(request, 'index.html', {"products": getProducts(session)})

def loadFile(request):
    if request.POST:
        try:
            file = request.FILES['file']
            uploading_file = uploadFile({"file": file})
            
            if len(uploading_file) > 0:
                messages.success(request, "Файл загружен.")
                request.session['ids'] = uploading_file
                return render(request, 'index.html', {"products": getProducts(uploading_file)})
            else:
                messages.error(request, "Ошибка при загрузке файла.")
        except:
            messages.error(request, "Ошибка при загрузке файла.")
    return redirect("/")

def downLoadFile(request):
    return createExlx(request.session.get('ids', [])) 
    


def change(request):
    if request.POST:
        file = None
        id = request.POST['id']
        try:
            file = request.FILES['file']
        except:
            pass 
        name = request.POST['name']
        if changeProdcut({
            "file": file,
            "id": id,
            "name": name,
            "place":  request.POST['place'],
            "facturer": request.POST['facturer'],
            "facturer_сountry": request.POST['facturer_сountry'],
            "descripton": request.POST['descripton']
            }):
            messages.success(request, name + " запись обновленна.")
        else:
            messages.error(request, "Ошибка при обновлении записи.")
    return redirect("/#" + id)
    