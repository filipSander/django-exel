from django.shortcuts import render
from django.views.generic import UpdateView
from django.contrib import messages

from exel.models import Product
from .forms import ProductForm

from utils.uploadings import uploadFile


class ProdcutUpdate(UpdateView):
    model = Product
    template_name = 'change.html'
    fields = [
            'name',
            'place',
            'facturer',
            'facturer_сountry',
            'descripton',
            'image'
            ]

def index(request):

    if request.POST:
        try:
            file = request.FILES['file']
            uploading_file = uploadFile({"file": file})
            
            if len(uploading_file) > 0:
                messages.success(request, "Файл загружен.")
                request.session['ids'] = uploading_file
                products = []
                for id in uploading_file:
                    products.append(Product.objects.get(pk=id))
            else:
                messages.error(request, "Ошибка при загрузке файла.")
        except:
            messages.error(request, "Ошибка при загрузке файла.")

    cheeck_session = request.session.get('ids', [])
    if len(cheeck_session) > 0:
        products = []
        for id in cheeck_session:
            products.append(Product.objects.get(pk=id))

    return render(request, 'index.html', {"products": products})
        

def change(request):

    if request.POST:
        print(request.POST)
        print(request.FILES)
        form = ProductForm(request.POST)
        if form.is_valid():
            messages.success(request, "Информация о товаре изменена.")
            form.save()
        else:
            messages.error(request, "Данные заполнены некорректно.")

    form = ProductForm()
    data = {
        'form': form
    }

    return render(request, 'change.html', data)