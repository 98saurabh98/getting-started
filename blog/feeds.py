from django.contrib.syndication.views import Feed
from .models import BlogPost

class RSSFeed(Feed):
	title = "My awesome blog feed"
	description = "The latest from my awesome blog"
	link = "/"
	item_link = link

def items(self):
	return BlogPost.objects.all()