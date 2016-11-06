from django.contrib import admin
from .models import ParsedData


class ParsedDataAdmin(admin.ModelAdmin):
    list_display = ["region", "city", "value"]
    list_filter = ["region"]
    search_fields = ["region", "city", "value"]

admin.site.register(ParsedData, ParsedDataAdmin)
