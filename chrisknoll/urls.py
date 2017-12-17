from django.urls import include, path
from django.contrib import admin

urlpatterns = [
	path('', include('main.urls')),
   path('main/', include('main.urls')),
   path('admin/', admin.site.urls),
]