from django.shortcuts import render



def import_data(request):
    return render(request, 'dataentry/importdata.html')