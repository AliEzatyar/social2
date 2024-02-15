from django import forms


class Myform(forms.Form):
    x = forms.CharField()
    y = forms.CharField(widget=forms.HiddenInput) # in any get request, we should fill /?y=ssdfdsf not any other name, since this field is a hidden field
