from pages.models import Quotes
from django.contrib import admin

@admin.register(Quotes)
class QuotesAdmin(admin.ModelAdmin):
    list_display = ('author', 'quote_text')
