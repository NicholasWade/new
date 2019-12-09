from django.conf.urls import url
from . import views
from django.urls import path, re_path
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView

app_name = 'rhymesapp'
urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    path('audio_list', views.audio_list, name='audio_list'),
    path('rhymes_list', views.rhymes_list, name='rhymes_list'),
    path('account_information', views.infoView, name='account_information'),
    path('londonBridge', views.londonBridge, name = 'londonBridge'),
    path('littleStar', views.littleStar, name = 'littleStar'),
    path('jackJill', views.jackJill, name = 'jackJill'),
    path('rhymeslist', views.rhymes_list, name='rhymeslist'),
    path('itsySpider', views.itsySpider, name = 'itsySpider'),
    path('humptyDumpty', views.humptyDumpty, name = 'humptyDumpty'),
    path('hickoryDock', views.hickoryDock, name = 'hickoryDock'),
    path('blackSheep', views.blackSheep, name = 'blackSheep'),
    path('heyDiddle', views.heyDiddle, name='heyDiddle'),
    path('hotBuns', views.hotBuns, name='hotBuns'),
    path('jackNimble', views.jackNimble, name='jackNimble'),
    path('market', views.market, name='market'),
    path('muffins', views.muffins, name='muffins'),
    path('peterPiper', views.peterPiper, name='peterPiper'),
    path('piggy', views.piggy, name='piggy'),
    path('rainPour', views.rainPour, name='rainPour'),
    path('ringPosies', views.ringPosies, name='ringPosies'),
    path('roses', views.roses, name='roses'),
    path('rowBoat', views.rowBoat, name='rowBoat'),
    path('sticks', views.sticks, name='sticks'),
    path('threeMice', views.threeMice, name='threeMice'),
    path('tweedle', views.tweedle, name='tweedle'),
    path('upgrade', views.upgradeView.as_view(), name='upgrade'),
    path('account_created', views.account_created, name='account_created'),
    url(r'^register/$', views.user_register, name='user_register'),
    url(r'^register/account_created/$', views.account_created, name='account_created'),
    path('email/', views.emailView, name='email'),
    url(r'^email/success/$', views.success, name='success'),
    url(r'^account_information/$', views.infoView, name='edit_profile'),
    url(r'^account_information/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^change_password/$', views.change_password, name='change_password'),
    url(r'^login/reset_password/$', PasswordResetView.as_view(), {'template_name': 'rhymesapp/reset_password.html'}, name='PasswordResetView'),
    url(r'^login/reset_password/done/$', PasswordResetDoneView.as_view(), name='PasswordResetDoneView'),
    url(r'^login/reset_password/confirm/$', PasswordResetConfirmView.as_view(), name='PasswordResetConfirmView'),

]
# (?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/

