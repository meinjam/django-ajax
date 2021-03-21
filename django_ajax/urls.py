from django.contrib import admin
from django.urls import path
from app_one import views as core_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_view.homepage, name='homepage'),
    path('get-data/<types>', core_view.get_data, name='get_data'),
    path('data/<int:id>/delete', core_view.delete_data, name='data_todo'),
]
