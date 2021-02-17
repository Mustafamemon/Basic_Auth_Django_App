from django.urls import path, include
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from UserAuth import views


UserAuth = 'UserAuth'

urlpatterns = [
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.Activate, name='activate'),
    path('get-csrf', views.GetCsrf, name='get_csrf'),
    path('login-required', views.LoginRequired, name='login_required'),
    
    url(r'^password_reset/$', auth_views.PasswordResetView.as_view(), name='password_reset'),
    url(r'^password_reset/done', views.PasswordResetDoneView, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]