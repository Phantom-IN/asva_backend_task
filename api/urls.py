from django.urls import path
from .views import BenchmarkView, HealthCheckView, TaskView

urlpatterns = [
    # path('evaluate/<str:task>/', ModelEvaluationView.as_view(), name='evaluate'),
    
    path('task/', TaskView.as_view(), name='task'),
    path('benchmark/', BenchmarkView.as_view(), name='benchmark'),
    path('health/', HealthCheckView.as_view(), name='health'),
]
