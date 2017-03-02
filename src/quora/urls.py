from django.contrib.auth.views import login, logout
from django.conf.urls import include, url
from django.conf import settings as conf_settings
from django.conf.urls.static import static
from django.contrib import admin

from core.views import (
    fblogin,
    home,
    password,
    picture,
    profile,
    public_profile,
    settings,
)
from search.views import search
from profile.views import signup

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hidden_login', login, {'template_name': 'core/cover.html'}, name='login'),
    url(r'^fblogin', fblogin, name='fblogin'),
    url(r'^logout', logout, {'next_page': '/'}, name='logout'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^public_profile/(?P<id>\d+)/$', public_profile, name='public_profile'),
    url(r'^settings/$', settings, name='settings'),
    url(r'^settings/profile/$', profile, name='profile'),
    url(r'^settings/password/$', password, name='password'),
    url(r'^questions/', include('quora.questions.urls')),
    url(r'^search/$', search, name='search'),
    url(r'^(?P<username>[^/]+)/$', profile, name='profile'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^$', home, name='home'),
]

if conf_settings.DEBUG:
    urlpatterns += static(conf_settings.STATIC_URL, document_root=conf_settings.STATIC_ROOT)
    urlpatterns += static(conf_settings.MEDIA_URL, document_root=conf_settings.MEDIA_ROOT)