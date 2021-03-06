
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from tune import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    # The new URL entries we're adding:
    url(r'^about/$',
        TemplateView.as_view(template_name='about.html'),
        name='about'),
    url(r'^contact/$', 
        TemplateView.as_view(template_name='contact.html'),
        name='contact'),
     url(r'^songs/(?P<slug>[-\w]+)/$', views.song_detail, 
        name='song_detail'),

    url(r'^admin/', admin.site.urls),
]
