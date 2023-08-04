
from django.contrib import admin
from django.urls import path
# from configWVM import 
from WebViewMercury import views


urlpatterns = [
    # path('', views.index, name='home'),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('view_dbpp/', views.page_profil_power, name='view_dbpp'),
    path('view_dbic/', views.page_view_dbic, name='view_dbic'),
    path('view_dbc/', views.page_counters, name='view_dbc'),
    path('view_dbg/', views.view_dbg, name='view_dbg'),
    # path('add_counter/', views.add_counter, name='add_counter'),
    path('edit_counter/', views.edit_counter, name='edit_counter'),
    path('edit_group/', views.edit_group, name='edit_group'),
    path('add_group/', views.add_group, name='add_group'),
]
