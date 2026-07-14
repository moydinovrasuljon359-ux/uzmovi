from django.contrib import admin
from .models import Banner,  Kino, JanrCategory, DavlatCategory, YilCategory

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ("yozuv",)

admin.site.register(Kino)
admin.site.register(JanrCategory)
admin.site.register(DavlatCategory)
admin.site.register(YilCategory)