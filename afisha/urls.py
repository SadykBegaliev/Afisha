from django.contrib import admin
from django.urls import path
from movie_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/directors/', views.director_list),
    path('api/v1/directors/<int:id>/', views.director_item),
    path('api/v1/movies/reviews/', views.movies_list),
    path('api/v1/movies/<int:id>/', views.movie_item),
    path('api/v1/reviews/', views.reviews_list),
    path('api/v1/reviews/<int:id>/', views.review_item),

]
