from django.shortcuts import render
from .forms import ArrForm, DepForm
from joblib import load
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path1 = os.path.join(BASE_DIR, 'goal3.model')
path2 = os.path.join(BASE_DIR, 'goal4.model')

model1 = load(path1)
model2 = load(path2)

def time(t):

    while len(t) < 4:
        t = '0'+t

    m = t[2:]
    h = t[:2]

    return h+"h"+m+"M"

# Create your views here.
def home(request):

    dep = ''
    arr = ''

    depform = DepForm()
    arrform = ArrForm()

    return render(request, 'prediction/index.html', locals())

def arr(request):

    arrform = ArrForm(request.POST or None)
    depform = DepForm()
    arr = ''

    if arrform.is_valid():
        val = np.array([[
            arrform.cleaned_data['week'], # week of day
            arrform.cleaned_data['crs_dep_time'], # crs_dep_time
            arrform.cleaned_data['dep_time'], # dep_time
            0, # dep_del15
            arrform.cleaned_data['air_time'], # air_time
            1, # flights
            arrform.cleaned_data['distance'], # distance
            0, # weather_delay
            9.94, # AWND
            0.06, # PRCP
            0.4, # SNOW
            32 # TMAX
        ]])

        t = model1.predict(val)[0]
        arr = time(str(int(t)))
        print("Arrivée:", t)
        

    return render(request, 'prediction/index.html', locals())


def dep(request):

    depform = DepForm(request.POST or None)
    arrform = ArrForm()
    dep = ""

    if depform.is_valid():

        val = np.array([[
            depform.cleaned_data['week'], # week of day
            depform.cleaned_data['crs_arr_time'], # crs_arr_time
            depform.cleaned_data['arr_time'], # arr_time
            0, # arr_del15
            depform.cleaned_data['air_time'], # air_time
            1, # flights
            depform.cleaned_data['distance'], # distance
            0, # weather_delay
            9.94, # AWND
            0.06, # PRCP
            0.4, # SNOW
            32 # TMAX
        ]])

        t = model2.predict(val)[0]
        dep = time(str(int(t)))

    return render(request, 'prediction/index.html', locals())