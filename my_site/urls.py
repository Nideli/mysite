from django.contrib import admin
from django.urls import path,include

from Our_site.views import PageNotFound

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Our_site.urls')),
]
handler404 = PageNotFound