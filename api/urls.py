from django.urls import path
from .views import index, StartScrapingView, ScrapingStatusView, TerminateTaskView

urlpatterns=[
    path('',index),
    path('taskmanager/start_scraping',StartScrapingView.as_view(),name='start-scraping'),
    path('taskmanager/scraping_status/<str:job_id>',ScrapingStatusView.as_view(),name='scraping-status'),
    path('taskmanager/terminate_task/<str:job_id>',TerminateTaskView.as_view(),name='terminate-task'),
]