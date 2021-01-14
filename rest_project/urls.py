from django.contrib import admin
from django.urls import include, path

from django.conf.urls import url
from rest_framework import routers
import polls.serializer

# app_name='polls'

router = routers.DefaultRouter()
router.register('questions', polls.serializer.QuestionViewSet)
router.register('choices', polls.serializer.ChoiceViewSet)

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    url('api/', include((router.urls, 'polls'), namespace='rest_framework')),
    path('users/', include('api_user.urls'), name='api_user'),
]