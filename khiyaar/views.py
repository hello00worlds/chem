from django.shortcuts import render
from .forms import FormulaForm
from chempy import Reaction, Substance, balance_stoichiometry, mass_fractions


def reactionToHtml(reac, prod):
    output = ''
    for i in reac:
        output += f'{reac[i]} {Substance.from_formula(i).html_name} + '
    output = output[:-3]
    output += ' → '
    for i in prod:
        output += f'{prod[i]} {Substance.from_formula(i).html_name} + '
    output = output[:-3]
    return output

def el(reac, prod):
    elr = []
    elp = []
    for i in reac:
        elr.append(Substance.from_formula(i).html_name)
    for i in prod:
        elp.append(Substance.from_formula(i).html_name)
    return elr, elp

def weight(r, p):
    rs = []
    ps = []
    for fractions in map(mass_fractions, [r, p]):
        a = mass_fractions(r)
        b = mass_fractions(p)
        for i in a:
            rs.append(a[i]//0.01)
        for i in b:
            ps.append(b[i]//0.01)
        return rs, ps

# def weight(element, r, p, g):
#     wet = 0
#     for fractions in map(mass_fractions, [r, p]):
#         for k, v in fractions.items():
#             if k == element:
#                 wet = g/v*100
#     return {k: '{0:.3g} wt%'.format(v*100*g) for k, v in fractions.items()}


def home(request):
    form = FormulaForm()
    formula = request.POST['formula'] if request.method == 'POST' else 'H2 + O2 -> H2O'
    r = Reaction.from_string(formula)
    reac, prod = balance_stoichiometry({sub for sub in r.reac}, {sub for sub in r.prod})
    elr, elp = el(reac, prod)
    rs, ps = weight(reac, prod)
    return render(request, 'formula.html', {'form': form, 'balanced': reactionToHtml(reac, prod), 'rs': rs, 'ps': ps, 'elr': elr, 'elp': elp})