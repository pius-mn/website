from django.contrib import admin
from .models import SearchResults
# Register your models here.
@admin.register(SearchResults)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display= [field.name for field in SearchResults._meta.get_fields()]
