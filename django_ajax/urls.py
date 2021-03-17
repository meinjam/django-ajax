from django.contrib import admin
from django.urls import path
from app_one import views as core_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_view.homepage, name='homepage'),
]
