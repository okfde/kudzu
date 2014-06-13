from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'kudzu.seeds.views.home', name='home'),
    url(r'^upload/$', 'kudzu.seeds.views.create', name='create'),
    url(r'^user/(?P<user_id>\d+)/latest', 'kudzu.seeds.views.user_latest', name='user_latest'),
    url(r'^video/(?P<video_id>\d+)', 'kudzu.seeds.views.vine_video', name='vine_video'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
