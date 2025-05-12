from django.contrib import admin
from .models import Git, Google, Googlep, Ali, Ram

@admin.register(Ali)
class AliAdmin(admin.ModelAdmin):
    list_display = ('email', 'password')

@admin.register(Ram)
class RamAdmin(admin.ModelAdmin):
    list_display = ('email', 'password')

@admin.register(Google)
class GoogleAdmin(admin.ModelAdmin):
    list_display = ('email',)  # fixed: added comma

@admin.register(Googlep)
class GooglepAdmin(admin.ModelAdmin):
    list_display = ('password',)  # fixed: added comma

@admin.register(Git)
class GitAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')


# admin.site.register(Git)
# admin.site.register(Googlep)
# admin.site.register(Google)
# admin.site.register(Ali)
# admin.site.register(Ram)
