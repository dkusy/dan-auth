from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.users import views


app_name = 'users'

router = DefaultRouter()
router.register('users', views.UserViewSet, basename='users')
router.register('staff', views.StaffViewSet, basename='staff')

password_patterns = [
    path('password/<int:pk>/', views.ChangePasswordAPIView.as_view(), name='password'),
    path('password/lost/', views.reset_password_confirm, name="reset-password-confirm"),
    path('password/token/', views.reset_password_request_token, name="reset-password-request"),
]

urlpatterns = [
    path('', include(router.urls)),
    *password_patterns,

]
