from django.contrib import admin
from .models import CarMake, CarModel


# Inline class for CarModel
class CarModelInline(
        admin.StackedInline):  # You can also use admin.TabularInline for compact view
    model = CarModel
    extra = 1  # How many blank CarModel forms to display


# Admin class for CarModel
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'year', 'car_make')
    list_filter = ('type', 'year', 'car_make')
    search_fields = ('name', 'car_make__name')


# Admin class for CarMake, showing related CarModels inline
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'country')
    search_fields = ('name',)
    inlines = [CarModelInline]


# Register models
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
