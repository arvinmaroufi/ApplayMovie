from django.shortcuts import render, redirect
from .forms import NewsletterForm, ContactUsForm
from movie.models import Movie, Series
import random


def home(request):
    movies_recommended = Movie.objects.filter(is_recommended=True)[:10]

    movies = Movie.objects.filter(status='published').order_by('-created_at')[:3]
    series = Series.objects.filter(status='published').order_by('-created_at')[:3]
    items = list(movies) + list(series)
    random.shuffle(items)

    context = {
        'movies_recommended': movies_recommended,
        'items': items,
    }
    return render(request, 'core/home.html', context)


def newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:home')


def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:home')
    else:
        form = ContactUsForm()

    context = {
        'form': form
    }
    return render(request, 'core/contact.html', context)
