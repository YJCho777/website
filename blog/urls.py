from django.conf.urls import url
from . import views
from .views import ChartData

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^about$', views.about, name='about'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^useful_sites$', views.useful_sites, name='useful_sites'),
    url(r'^finance_econ$', views.finance_econ, name='finance_econ'),
    url(r'^statistics$', views.statistics, name='statistics'),
    url(r'^computing$', views.computing, name='computing'),       
    url(r'^django_css$', views.django_css, name='django_css'),
    url(r'^stock_market$', views.stock_market, name='stock_market'),       
    url(r'^simulation$', views.simulation, name='simulation'),
    url(r'^stock_market/data/$', ChartData.as_view()), 

]
