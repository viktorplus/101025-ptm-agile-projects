# from rest_framework.routers import DefaultRouter
from django.urls import path

from projects.views.user import UserViewSet, UserListGenericView

# router = DefaultRouter()
# router.register('', UserViewSet, basename='users')

# Зарегистрируйте новый эндпоинт, протестируйте его, чтобы убедиться, что он работает.
urlpatterns = [
    path("users/", UserListGenericView.as_view())
]

# urlpatterns += router.urls
