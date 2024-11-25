from django.contrib import admin
from .models import KakeiboPost, Total

# Register your models here.
    
class KakeiboPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    
class TotalAdimn(admin.ModelAdmin):
    list_display = ('id', 'datetime')
    list_display_links = ('id', 'datetime')
    
admin.site.register(KakeiboPost, KakeiboPostAdmin)
admin.site.register(Total, TotalAdimn)