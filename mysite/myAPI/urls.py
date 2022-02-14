from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path("livre/<int:id>/", views.unLivre.as_view()),
    path("livres/<int:page>/", views.desLivres.as_view()),
    path("livres/", views.desLivres.as_view()),
    path("recherche/<str:strSearch>/", views.rechercheLivres.as_view()),
]