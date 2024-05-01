from django.shortcuts import render, redirect
from django.http import HttpResponse
from site_app.models import Cpu_Utilization
from site_app.forms import CpuForm
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def home_page(request):
    cpus = Cpu_Utilization.objects.order_by('-id')[:100]
    cpu_form = CpuForm()
    if request.method == "POST":
        formset = CpuForm(request.POST)
        if formset.is_valid():
            add_cpu = Cpu_Utilization.objects.create(curr_util=request.POST['curr_util'])
            add_cpu.save()
            return redirect('/')
    return render(request, "home.html", {'cpus': cpus})