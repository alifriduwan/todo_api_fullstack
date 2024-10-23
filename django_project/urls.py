
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/todos/', include('todos.urls')),
    path('api-auth', include('rest_framework.urls')),
    path('api/users/', include('accounts.urls'))
]