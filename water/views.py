from django.shortcuts import render
from .models import Introduction, Water
from django.shortcuts import get_object_or_404


def introduction(request):
    item = Introduction.objects.all()
    context = {'item': item}
    return render(request, 'watering/introduction.html', context)


def water(request, introduction_pk):
    waters = get_object_or_404(Introduction, pk=introduction_pk)
    return render(request, 'watering/water.html', {'waters': waters})
