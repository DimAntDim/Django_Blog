from django.db import models


class Quotes(models.Model):
    author = models.CharField(max_length=200)
    quote_text = models.TextField(blank=True)

    def __str__(self):
        return self.author
