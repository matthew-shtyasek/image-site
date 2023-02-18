from django.contrib import admin

from news.models import Img


# Register your models here.
@admin.register(Img)
class ImgAdmin(admin.ModelAdmin):
    list_display = ('title', 'date',)
    readonly_fields = ('date',)
    list_filter = ('date',)
    search_fields = ('title', )
    fields = ('title', 'date', 'img',)




