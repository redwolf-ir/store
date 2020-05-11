from accounts.views import register, login, logout
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
# from blog.views import index
from django.urls import path

urlpatterns = [
    url(r'^register/$(?i)', register, name = 'register'),
    url('account/', include('accounts.urls')),
    url(r'^logout/?$(?i)', logout, name='logout'),
    url(r'^login/?$(?i)', login, name = 'login'),
    # url(r'^$', index, name='index'),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
