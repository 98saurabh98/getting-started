from django.urls import path, include
#from django.contrib.syndication.views import Feed
from .feeds import RSSFeed

from . import views
# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
	path("", views.archive, name="archive"),
	path(r'feeds/', RSSFeed()),
#	path(r'^feeds/(?P<url>.*)/$', feed, {'feed_dict': {'rss': RSSFeed}}),
]
