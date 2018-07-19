from django.shortcuts import render
from django.http import HttpResponse

from apps.mascota.forms import MascotaForm


def index(request):
    return render(request, 'mascota/index.html')


def mascota_view(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('mascota:index')
    else:
        form = MascotaForm()    
    return render(request, 'mascota/mascota_form.html', {'form':form})
