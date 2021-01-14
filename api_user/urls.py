from django.urls import path

from api_user import views

app_name = 'api_user'


urlpatterns = [
    path('', views.UserView.as_view()),
    path('<int:user_id>', views.UserView.as_view()), # User pk id가 전달되는 경우
]