from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_List_View.as_view(), name='GameZone'),
    path('Games/', views.games_List_View.as_view(), name='Games list'),
    path('Game/<int:pk>', views.game_Detail_View.as_view(), name='Game information'),
    path("Game/<int:pk>/NewComment", views.commentCreateView.as_view(), name="add_comment"),
    path("comment/<int:pk>/update", views.commentUpdateView.as_view(), name="update_comment"),
    path("comment/<int:pk>/delete", views.commentDeleteClass.as_view(), name="delete_comment"),
    
    
]
