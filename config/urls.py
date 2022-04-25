from django.conf import settings
from django.contrib import admin
from django.urls import include, path

admin.site.site_header = "IGS Employee Administration"
admin.site.index_title = "IGS"
admin.site.site_title = "Administration"

urlpatterns = [
    path("admin/", admin.site.urls, name='admin'),
    path("accounts/", include("allauth.urls")),
    path("", include("pages.urls")),
    path("", include("api.urls")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
