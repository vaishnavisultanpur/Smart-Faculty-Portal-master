"""SSL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.conf.urls import path
# from django.contrib import admin
# from django.contrib.auth import views as auth_views
# from django.contrib.auth.views import LoginView, LogoutView

# from django.conf.urls.static import static

# from SSL import settings
# from . import views


# urlpatterns = [
#     # url(r'^login/$', auth_views.login, name='login'),
#     # url(r'^logout/$', views.logout_view, name='logout'),
#     path('login/', LoginView.as_view(template_name='login.html'), name='login'),
#     path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

#     path(r'^a/$', views.webmail, name='webmail'),
#     path(r'^accounts/profile/$', views.index,name='index'),
#     # url(r'^accounts/login/$', auth_views.login, name='login'),
#     path(r'^accounts/profile/user/$', views.edit_profile, name='user'),
#     path(r'^accounts/profile/table/$', views.teaching, name='table'),
#     path(r'^accounts/profile/publication/$', views.publication, name='publication'),
#     path(r'^accounts/profile/projects/$', views.projects, name='projects'),
#     path(r'^accounts/profile/achievements/$', views.achievements, name='achievements'),
#     path(r'^accounts/profile/education/$', views.education, name='education'),
#     path(r'^signup/$', views.signup, name='editprofile'),
#     path(r'^accounts/profile/table/delete/(?P<part_id>[0-9]+)/$', views.function, name='delete_view'),
#     path(r'^accounts/profile/publication/delete/(?P<part_id>[0-9]+)/$', views.function2, name='delete_view2'),
#     path(r'^accounts/profile/education/delete/(?P<part_id>[0-9]+)/$', views.function3, name='delete_view3'),
#     path(r'^accounts/profile/projects/delete/(?P<part_id>[0-9]+)/$', views.function4, name='delete_view4'),
#     path(r'^accounts/profile/achievements/delete/(?P<part_id>[0-9]+)/$', views.function5, name='delete_view5'),

#     path(r'^profile/(?P<username>.+)/$', views.show_main, name='show'),
#     path(r'^search/$', views.find_user_by_name, name='search1'),
#     path(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
#     path(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
#     path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth_views.password_reset_confirm, name='password_reset_confirm'),
#     path(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
# ]

# # from django.urls import path, re_path, include

# # urlpatterns = [
# #     path('admin/', admin.site.urls),
# #     re_path(r'^', include('sslproject.urls')),
# # ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path, re_path
from django.contrib import admin
from django.contrib.auth.views import (
    LoginView, LogoutView,
    PasswordResetView, PasswordResetDoneView,
    PasswordResetConfirmView, PasswordResetCompleteView
)

from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    # Authentication
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    # Other pages
    path('a/', views.webmail, name='webmail'),
    path('accounts/profile/', views.index, name='index'),
    path('accounts/profile/user/', views.edit_profile, name='user'),
    path('accounts/profile/table/', views.teaching, name='table'),
    path('accounts/profile/publication/', views.publication, name='publication'),
    path('accounts/profile/projects/', views.projects, name='projects'),
    path('accounts/profile/achievements/', views.achievements, name='achievements'),
    path('accounts/profile/education/', views.education, name='education'),
    path('signup/', views.signup, name='editprofile'),

    # Delete actions
    re_path(r'^accounts/profile/table/delete/(?P<part_id>[0-9]+)/$', views.function, name='delete_view'),
    re_path(r'^accounts/profile/publication/delete/(?P<part_id>[0-9]+)/$', views.function2, name='delete_view2'),
    re_path(r'^accounts/profile/education/delete/(?P<part_id>[0-9]+)/$', views.function3, name='delete_view3'),
    re_path(r'^accounts/profile/projects/delete/(?P<part_id>[0-9]+)/$', views.function4, name='delete_view4'),
    re_path(r'^accounts/profile/achievements/delete/(?P<part_id>[0-9]+)/$', views.function5, name='delete_view5'),

    # Profile + Search
    re_path(r'^profile/(?P<username>.+)/$', views.show_main, name='show'),
    path('search/', views.find_user_by_name, name='search1'),

    # Password Reset (modern Django)
    path('password_reset/', 
         PasswordResetView.as_view(template_name='password_reset.html'),
         name='password_reset'),

    path('password_reset/done/',
         PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done'),

    re_path(
        r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z\-]+)/$',
        PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'
    ),

    path('reset/done/',
         PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
