from django import forms
class ArrForm(forms.Form):
    week = forms.FloatField(label="Jour de la semaine (0:Dimanche, 1:Lundi...)")
    crs_dep_time = forms.FloatField(label="Heure de départ CRS(hhmm)")
    dep_time = forms.FloatField(label="Heure de depart(hhmm)")
    air_time = forms.FloatField(label="Durée de vol prévue en minute")
    distance = forms.FloatField(label="Distance de vol en miies")

class DepForm(forms.Form):
    week = forms.FloatField(label="Jour de la semaine (0:Dimanche, 1:Lundi...)")
    crs_arr_time = forms.FloatField(label="Heure d'arrivée CRS(hhmm)")
    arr_time = forms.FloatField(label="Heure d'arrivée(hhmm)")
    air_time = forms.FloatField(label="Durée de vol prévue en minute")
    distance = forms.FloatField(label="Distance de vol en miles")
