from django.contrib import admin
from django.urls import path, include
from player.views import get_profile
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from news.views import NewsListView, get_news
from account.views import home_page
from booth.views import BoothsListView, get_booths_map, redirect_zoom
from oc.views import get_contact
from player.views import get_rich_list, get_score_list, get_instructor_students, instructor_get_player

urlpatterns = [
    path('profile', get_profile, name='profile_by_userid'),
    # path('', views.get_profile, name='self_profile'),
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('', home_page, name='home'),
    path('oc/', include('oc.urls')),
    path('admin/', admin.site.urls),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('news/', get_news),
    path('contact/', get_contact, name='contact'),
    path('rich_list/', get_rich_list),
    path('score_list/', get_score_list),
    path('map/', TemplateView.as_view(template_name='map.html'), name='map'),
    path('room/', TemplateView.as_view(template_name='room.html'), name='room'),
    path('rundown/', TemplateView.as_view(template_name='rundown.html'), name='rundown'),
    path('rules/', TemplateView.as_view(template_name='rules.html'), name='rules'),
    path('instructor/', get_instructor_students, name='instructor_students'),
    path('instructor/<str:player_id>', instructor_get_player, name='instructor_get_player')
]