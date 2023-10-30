from django.shortcuts import render,redirect
from .models import Country
import random

def game(request):
    correct=None
    if 'random_country_id' not in request.session:
        # If a random country is not already stored in the session, generate one.
        random_country = random.choice(Country.objects.all())
        request.session['random_country_id'] = random_country.id
    else:
        # Retrieve the random country from the session.
        
        random_country_id = request.session['random_country_id']
        random_country = Country.objects.get(pk=random_country_id)

    if request.method == 'POST':
        #if request method is of type POST, fetch the guess which user submitted while guessing capital
        guess = str(request.POST.get('guess'))
        #check if the guessed capital is same as actual capital ,as per the check setting the correct value to either True or False
        if guess.lower().strip() == random_country.capital.lower():
            correct = True
        else:
            correct = False
        # Clear the stored country from the session.
        del request.session['random_country_id']
        
        return render(request, 'capitals/game.html', {'country': random_country, 'correct': correct})

    return render(request, 'capitals/game.html', {'country': random_country, 'correct': correct})
