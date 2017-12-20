### $Id: forms.py,v 1.3 2014/08/23 14:30:21 muntaza Exp $


from django import forms


class HargaTanahForm(forms.ModelForm):
    harga_bertambah = forms.DecimalField(label="Harga Bertambah", max_digits=15, decimal_places=0, localize=True, initial=0)
    harga_berkurang = forms.DecimalField(label="Harga Berkurang", max_digits=15, decimal_places=0, localize=True, initial=0)

