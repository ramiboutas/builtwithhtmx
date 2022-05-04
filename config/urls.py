

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

from .sitemaps import sitemaps

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("", include("pages.urls")),
        path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap",),
        path("projects/", include("projects.urls")),
        path('htmx-on-youtube', include('youtube.urls')),
        path("jobs/", include("jobs.urls")),
        path("makers/", include("makers.urls")),
        path("blog/", include("blog.urls")),
        path("users/", include("allauth.urls")),

        # dev stuff
        path("__reload__/", include("django_browser_reload.urls")),
        path('__debug__/', include('debug_toolbar.urls')),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
