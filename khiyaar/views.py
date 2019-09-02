from django.shortcuts import render
from .forms import FormulaForm
from chempy import Reaction, Substance, balance_stoichiometry


def reactionToHtml(reac, prod):
    output = ''
    for i in reac:
        output += f'{reac[i]} {Substance.from_formula(i).html_name} + '
    output = output[:-3]
    output += ' => '
    for i in prod:
        output += f'{prod[i]} {Substance.from_formula(i).html_name} + '
    output = output[:-3]
    return output

def home(request):
    form = FormulaForm()
    formula = request.POST['formula'] if request.method == 'POST' else 'H2 + O2 -> H2O'
    r = Reaction.from_string(formula)
    reac, prod = balance_stoichiometry({sub for sub in r.reac}, {sub for sub in r.prod})
    return render(request, 'formula.html', {'form': form, 'balanced': reactionToHtml(reac, prod)})

