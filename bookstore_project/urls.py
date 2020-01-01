from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    # Django admin (securely)
    path('mad/', admin.site.urls),

    # Auth app by django
    path('accounts/', include('allauth.urls')),

    # Local apps
    path('', include('pages.urls')),
    path('user/', include('users.urls')),
    path('books/', include('books.urls')),
    path('orders/', include('orders.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

