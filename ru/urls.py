from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('news', views.news_index, name='news_index'),
    path('news/', views.news_index, name='news_index'),
    path('news/positions', views.positions_index, name='positions_index'),
    path('center', views.mission, name='mission'),
    path('center/history', views.history, name='history'),
    path('center/contacts', views.contacts, name='contacts'),
    path('center/reports', views.reports, name='reports'),
    path('center/maindocs', views.maindocs, name='maindocs'),
    path('center/attestation', views.attestation, name='attestation'),
    path('center/fazly', views.fazly, name='fazly'),
    path('structure', views.prinvestigator_index, name='prinvestigator_index'),
    path('structure/staff', views.staff_index, name='staff_index'),
    path('research', views.research_index, name='research_index'),
    path('research/etics', views.etics, name='etics'),
    path('research/senate', views.senate, name='senate'),
    path('research/publications', views.publications, name='publications'),
    path('research/<str:nc>', views.detail, name='detail'),
    path('research/<str:nc>/people', views.members, name='members'),
    path('research/<str:nc>/profile', views.profile, name='profile'),
    path('research/<str:nc>/publications', views.pipub, name='pipub'),
    path('education', views.course_index, name='course_index'),
    path('education/phd', views.phd, name='phd'),
    path('pages/<str:name>', views.pages_index, name='pages_index'),
]