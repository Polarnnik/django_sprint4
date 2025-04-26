from django.contrib import admin
from django.urls import include, path
from pages import views as pages_views

urlpatterns = [
    path('', include('blog.urls')),
    path('pages/', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls', namespace='users')),
    path('auth/', include('django.contrib.auth.urls')),
]

handler404 = pages_views.page_not_found
handler500 = pages_views.server_error
