from django.contrib import admin
from .models import Introduction, Water


class IntroductionAdmin(admin.ModelAdmin):
    list_display = ['Brief_History', 'Objectives']
    list_filter = ['date_pub']
    search_fields = ['Objectives']


class WaterInline(admin.StackedInline):
    model = Water
    extra = 1

class WaterAdmin(admin.ModelAdmin):
    list_display = [' Mission_Statement', 'Quality_control_unit', 'Laboratory_instrument']
    list_filter = ['Mission_Statement']
    search_fields = ['Mission_Statement']

admin.site.register(Introduction, IntroductionAdmin)
admin.site.register(Water)