from django import forms

class FormulaForm(forms.Form):
    formula = forms.CharField(label='Formula', max_length=800)