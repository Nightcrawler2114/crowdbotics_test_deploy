from django.conf.urls import url
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    url(r'^$',views.AnimalListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$',views.AnimalDetailView.as_view(), name='detail'),
    url(r'^create/$',views.AnimalCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)/$',views.AnimalUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$',views.AnimalDeleteView.as_view(), name='delete')
]
