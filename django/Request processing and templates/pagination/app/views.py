from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.conf import settings
from csv import DictReader


with open(settings.BUS_STATION_CSV) as file:
    reader = DictReader(file)
    reader_list = [dict(filter(lambda item: item[0] in ('Name', 'Street', 'Destrict'), dict_.items())) for dict_ in reader]


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    current_page = int(request.GET.get('page', 1))
    paginator = Paginator(reader_list, 10)
    bus_stations = paginator.get_page(current_page)
    next_page_url = bus_stations.next_page_number() if bus_stations.has_next() else None
    prev_page_url = bus_stations.previous_page_number() if bus_stations.has_previous() else None
    range_ = paginator.page_range

    context = {
        'bus_stations': bus_stations,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
        'range_': range_
    }

    return render(request, 'index.html', context=context)
