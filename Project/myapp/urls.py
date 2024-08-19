from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.list,name='list'),
    path('create/',views.create,name='create'),
    path('list/<pk>',views.list,name='list'),
    path('edit/<pk>',views.edit,name='edit'),
    path('delete/<pk>',views.delete,name='delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
