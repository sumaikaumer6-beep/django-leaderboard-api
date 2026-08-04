from django.urls import path
from . import views
urlpatterns = [
    path('save',views.save_score,name='save_score'),
    path('leaderboard/',views.get_leaderboard,name='leaderboard'),
]