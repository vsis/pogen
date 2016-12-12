from django.conf.urls import url
from . import views

app_name = 'pos'
urlpatterns = [
    url(r'^$', views.new_po, name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<purchase_order_id>[0-9]+)/vote/$', views.post_po, name='post'),
]
