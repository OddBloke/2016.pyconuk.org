from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^programme/$', views.schedule_view, name='programme'),
    url(r'^schedule/$', views.schedule_view, name='schedule'),  # We need to keep this URL since it is referenced on visa invitation letters
    url(r'^open-day/$', views.open_day_view, name='open_day'),
    url(r'^news/$', views.news_items_view, name='news_items'),
    url(r'^news/(?P<datestamp>\d+)-(?P<key>[\w-]+)/$', views.news_item_view, name='news_item'),
    url(r'^(?P<session_type>talks|workshops|keynotes)/(?P<slug>[\w-]+)/$', views.session_view, name='session'),
    url(r'^sessions/$', views.sessions_view, name='sessions'),
    url(r'^speakers/(?P<key>[\w-]+)/$', views.speaker_view, name='speaker'),
    url(r'^speakers/$', views.speakers_view, name='speakers'),
    url(r'^sponsors/(?P<key>[\w-]+)/$', views.sponsor_view, name='sponsor'),
    url(r'^sponsors/$', views.sponsors_view, name='sponsors'),
    url(r'^$', views.page_view, name='index'),
    url(r'^(?P<key>.*?)/$', views.page_view, name='page'),
]
