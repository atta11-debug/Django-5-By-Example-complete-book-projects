from django.urls import path
from django.contrib.sitemaps.views import sitemap
from blog import views
from blog.sitemaps import PostSitemap
from blog.feeds import LatestPostFeeds

app_name = "blog"

sitemaps = {"posts": PostSitemap}
urlpatterns = [
    path("", views.post_list, name="post_list"),
    # path("", views.PostListView.as_view(), name="post_list"),
    # path("post_detail/<int:pk>/",views.post_detail,name="post_detail"),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:post>/",
        views.post_detail,
        name="post_detail",
    ),
    path("<int:pk>/share/", views.post_share, name="post_share"),
    path("comment/<int:pk>/", views.post_comment, name="post_comment"),
    path("tag/<slug:tag_slug>/", views.post_list, name="post_list_by_tag"),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path("feed/",LatestPostFeeds(),name="post_feed"),
]
