from django.shortcuts import render
from phones.models import Phone

def show_catalog(request):
    all_telephones = Phone.objects.all()
    sort_pages = request.GET.get('sort')
    template = 'catalog.html'
    if sort_pages == 'low':
        all_telephones = all_telephones.order_by('price')
    elif sort_pages == 'high':
        all_telephones = all_telephones.order_by('-price')
    elif sort_pages == 'alph':
        all_telephones = all_telephones.order_by('name')
    context = {'phones': all_telephones}
    return render(request, template, context=context)


def show_product(request, slug):
    phone = Phone.objects.filter(slug__contains=slug)
    template = 'product.html'
    context = {'phone': phone}
    return render(request, template, context=context)
