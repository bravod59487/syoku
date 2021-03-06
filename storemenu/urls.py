from django.urls import path
from . import views
app_name='storemenu'
urlpatterns = [
    path('', views.index,name='index'),
    path('create/', views.create,name='create'),
    path('update/<int:id>', views.update,name='update'),
    path('delete/<int:id>', views.delete,name='delete'),
    path('userindex/', views.userindex,name='userindex'),
    path('search/', views.search,name='search'),
    path('cindex/<str:id>', views.cindex,name='cindex'),
]