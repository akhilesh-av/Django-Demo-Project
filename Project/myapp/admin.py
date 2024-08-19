from django.contrib import admin
from . models import MovieInfo,CensorInfo,Director


admin.site.register(MovieInfo)
admin.site.register(CensorInfo)
admin.site.register(Director)
