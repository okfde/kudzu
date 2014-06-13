from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'kudzu.seeds.views.home', name='home'),
    url(r'^article$', 'kudzu.seeds.views.article', name='article'),
    url(r'^seed/(?P<seed_id>\d+)/', 'kudzu.seeds.views.show_seed', name='show_seed'),
    url(r'^question/(?P<question_id>\d+)/reply$', 'kudzu.seeds.views.create_reply', name='create_reply'),
    url(r'^upload/$', 'kudzu.seeds.views.create', name='create'),

    url(r'^user/(?P<user_id>\d+)/latest', 'kudzu.seeds.views.user_latest', name='user_latest'),
    url(r'^video/(?P<video_id>\d+)', 'kudzu.seeds.views.vine_video', name='vine_video'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
