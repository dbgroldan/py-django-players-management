from django.urls import path, include

from src.players.views import infoJsonView, infoHttpView, infoJsonParamView
from src.players.views import CubeListView, CubeCreateView, PlayerCreateView, \
    CubeDetailView, CubeUpdateView, CubeDeleteView


from django.views.generic.base import TemplateView

urlpatterns = [
    # Players
    path('', include('django.contrib.auth.urls'), name='login'),
    path('signup', PlayerCreateView, name='signup'),

    # Cubes
    path('cubes', CubeListView.as_view(), name='list_cubes'),
    path('register_cube', CubeCreateView.as_view(), name='register_cube'),
    path('cubes/<int:id>', CubeDetailView.as_view(), name='detail_cube'),
    path('cubes/<int:pk>/update', CubeUpdateView.as_view(), name='update_cube'),
    path('cubes/<int:pk>/delete', CubeDeleteView.as_view(), name='delete_cube'),

    # Other Test Views
    path('json/', infoJsonView),
    path('jsonparam/<str:param>', infoJsonParamView),
    path('http', infoHttpView)
]
