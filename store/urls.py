from accounts.views import register
# , register, logout
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
# from blog.views import index
from django.urls import path

urlpatterns = [
    url(r'^register/?$', register, name = 'register'),
    # url('settings/', include('accounts.urls')),
    # url(r'^logout/?$', logout, name='logout'),
    # url(r'^login/?$', login, name = 'login'),
    # url(r'^$', index, name='index'),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
