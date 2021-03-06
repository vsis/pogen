from django.conf.urls import url
from . import views

app_name = 'pos'
urlpatterns = [
    url(r'^$', views.ListView.as_view(), name='list_po'),
    url(r'^search$', views.search_po, name='search_po'),
    url(r'^filter/(?P<provider>[0-9]+)/(?P<area>[0-9]+)$', views.filter_po, name='filter_po'),
    url(r'^new$', views.new_po, name='new_po'),
    url(r'^new/preview$', views.preview_po, name='preview_po'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail_po'),
    url(r'^post$', views.post_po, name='post_po'),
]
