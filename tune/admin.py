from django.contrib import admin

from tune.models import Songs
class SongsAdmin(admin.ModelAdmin):
    model = Songs
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Songs, SongsAdmin)

