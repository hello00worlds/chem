from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('khiyaar/', include('khiyaar.urls', namespace='khiyaar')),
    path('', include('main.urls', namespace='main')),
]
