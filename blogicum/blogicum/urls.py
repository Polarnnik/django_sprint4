from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from blog.views import SignUp

urlpatterns = [
    path('auth/registration/', SignUp.as_view(), name='signup'),
    path('', include('blog.urls')),
    path('pages/', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
]

handler404 = 'pages.views.page_not_found'
handler500 = 'pages.views.server_error'
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
