from django.contrib import admin

from .models import About_me, My_contact, Portfolio
# Register your models here.


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'link')


class Abaut_meAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')


class My_contactAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'email', 'telegram')


admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(About_me, Abaut_meAdmin)
admin.site.register(My_contact, My_contactAdmin)
