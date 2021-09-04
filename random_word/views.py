from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def random_word(request):
    word = get_random_string(14)
    context = {'word': word}
    if not 'attempts' in request.session:
        request.session['attempts'] = 1
    else:
        request.session['attempts'] += 1
    return render(request, 'index.html', context)

def reset(request):
    if 'attempts' in request.session:
        request.session['attempts'] = 0
    return redirect('/random_word/')