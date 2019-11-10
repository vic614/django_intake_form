from django.conf.urls import url,include
from personal_info import views

urlpatterns = [
    url(r'^$', views.PersonalInfoList.as_view(), name='personal_info_list'),
    url(r'^add/$', views.PersonalInfoCreate.as_view(), name='personal_info_create'),
    url(r'(?P<pk>[0-9]+)/$', views.PersonalInfoUpdate.as_view(), name='personal_info_update'),
    url(r'(?P<pk>[0-9]+)/delete/$', views.PersonalInfoDelete.as_view(), name='personal_info_delete'),
]