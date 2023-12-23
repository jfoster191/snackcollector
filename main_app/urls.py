from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'), 
  path('about/', views.about, name='about'),
  path('snacks/', views.SnackList.as_view(), name='snacks'),
  path('snacks/<int:snack_id>/', views.snack_detail, name='snack_detail'),
  path('snacks/<int:pk>/update', views.SnackUpdate.as_view(), name='snack_update'),
  path('snacks/<int:pk>/delete', views.SnackDelete.as_view(), name='snack_delete'),
  path('snacks/create/', views.SnackCreate.as_view(), name='snack_create'),
  path('snacks/<int:object_id>/add_comment', views.add_comment, name='add_comment' ),
  path('tastes/', views.TasteList.as_view(), name='tastes'),
  path('tastes/create/', views.TasteCreate.as_view(), name='taste_create'),
  path('snacks/<int:snack_id>/assoc_taste/<int:taste_id>/', views.assoc_taste, name='assoc_taste'),
  path('snacks/<int:snack_id>/unassoc_taste/<int:taste_id>/', views.unassoc_taste, name='unassoc_taste'),
]