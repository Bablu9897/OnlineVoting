from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('ajax/', views.ajax, name='ajax'),
    path('set_vote/', views.set_vote, name="set_vote"),
    path('vote_machine/', views.vote_machine, name="vote_machine"),
    path('win_election/', views.win_election, name="win_election"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)