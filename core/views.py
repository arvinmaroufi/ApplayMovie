from django.shortcuts import render, redirect
from .forms import NewsletterForm, ContactUsForm
from .models import SiteSettings


def home(request):
    site_settings = SiteSettings.objects.first()

    context = {
        'site_settings': site_settings
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
