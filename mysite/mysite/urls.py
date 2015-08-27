from django.conf.urls import include, url
from django.contrib import admin
from filebrowser.sites import site
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    #url(r'^media/', name='media'),
    #url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^bid/', include('bid.urls', namespace="bid")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
	#url(r'^$', include(admin.site.urls)),
	#(r'^media/', include('django.contrib.admindocs.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

