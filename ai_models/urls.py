from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.ai_dashboard, name='ai_dashboard'),
    
    path('predict/eggs/', views.predict_eggs_api, name='predict_eggs_api'),
    path('predict/feed/', views.predict_feed_api, name='predict_feed_api'),
    path('monitor/env/', views.monitor_env_api, name='monitor_env_api'),
]