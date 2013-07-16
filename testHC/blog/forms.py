from django import forms

class ShortDomain(forms.Form):
    longdomain = forms.CharField()
