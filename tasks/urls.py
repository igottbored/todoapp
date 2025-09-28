from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter

router =DefaultRouter()
router.register(r'', views.TaskViewSet,basename='task')

urlpatterns = [
    path('', include(router.urls)),
]

