from django.shortcuts import render
from .models import Quotes

def landing_page(request):
    return render(request, 'landing_page.html')


def quotes(request):
    text = Quotes.text
    author = Quotes.author    
    return render(request, 'quotes.html', {
                                            'text': text,
                                            'author': author,
                                            })
