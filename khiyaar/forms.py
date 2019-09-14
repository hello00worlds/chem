from django import forms

class FormulaForm(forms.Form):
    formula = forms.CharField(label="", help_text="", max_length=800, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Formula'}))