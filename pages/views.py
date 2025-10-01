# pages/views.py

from django.shortcuts import render

def home_view(request):
    """View for the home page."""
    return render(request, 'home.html')

def about_view(request):
    """View for the about page, using template inheritance."""
    # We don't need to pass context here, but we could if needed.
    return render(request, 'about.html')