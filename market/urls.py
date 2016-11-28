from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index_home, name="index"),
    url(r'^login/', views.login_view, name="Login"),
    url(r'^logout/', views.logout_view, name="Logout"),
    url(r'^register/', views.UserFormView.as_view(), name="Register"),
    url(r'^profile/$', views.ProfileView.as_view(), name="Profile"),
    url(r'^profile/(?P<pk>[0-9]+)/$', views.profile_view, name="OProfile"),
    url(r'^store/(?P<pk>[0-9]+)/$', views.store_view, name="Store"),
    url(r'^item/(?P<pk>[0-9]+)/$', views.item_details, name="ItemDetail"),
    url(r'^item/add/', views.PostItem.as_view(), name="ItemAdd"),
    url(r'^store/add/', views.store_form, name="StoreAdd"),
    url(r'^item/edit/(?P<pk>[0-9]+)/$', views.ItemUpdate.as_view(), name="ItemEdit"),
    url(r'^item/delete/(?P<pk>[0-9]+)/$', views.ItemDelete.as_view(), name="ItemDelete"),

]
