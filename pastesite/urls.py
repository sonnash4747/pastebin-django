from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin

from pastes import views as paste_views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pastesite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # Django's in-built admin interface
    url(r'^admin/', include(admin.site.urls)),
    
    # Home page
    #url(r'^$', TemplateView.as_view(template_name='homepage.html'), name="homepage"),
    url(r'^$', include("home.urls", namespace="home")),
    url(r'^pastes/', include("pastes.urls", namespace="pastes")),
    url(r'^users/', include("users.urls", namespace="users")),
    
    url(r'^(?P<char_id>\w{8})/', paste_views.show_paste, name="show_paste"),
)