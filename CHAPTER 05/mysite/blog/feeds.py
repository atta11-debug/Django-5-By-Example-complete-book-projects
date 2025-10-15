import markdown
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords_html
from django.urls import reverse_lazy
from blog.models import Post


class LatestPostFeeds(Feed):
    title = "My Blog"
    link = reverse_lazy("blog:post_list")
    description = "New posts of my Blog."

    def items(self):
        return Post.objects.all()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords_html(markdown.markdown(item.body), 30)

    def item_pubdate(self, item):
        return item.publish
