from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from web.form import BaseDataForm


def home(request):
    if request.method == "POST" and request.is_ajax:
        form = BaseDataForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"toster": True,'data':form.cleaned_data}, status=200)
        print({'error':form.errors})
        return JsonResponse(form.errors, status=400)
    return render(request, 'new.html', {'form': BaseDataForm()})
