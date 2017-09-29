from django.conf.urls import url
from . import views
app_name = 'rango'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<cat_id>\d+)$', views.details, name='details'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    #url(r'^details/(?P<request>\d+)$$', views.details, name='details'),
    url(r'^detail/$', views.detail, name='detail'),
    url(r'^category/(?P<category_name_url>\w+)/$', views.category, name='category'),
]