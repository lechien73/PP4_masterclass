from django.shortcuts import render
from .models import About

def about_me(request, *args, **kwargs):
    """
    Renders the About page
    """
    about = About.objects.all().first()

    return render(
        request,
        "about.html",
        {
            "about": about
        },
    )
