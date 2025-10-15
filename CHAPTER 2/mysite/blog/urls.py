from django.urls import path
from blog import views

app_name = "blog"

urlpatterns = [
    # path("",views.post_list,name="post_list"),
    path("", views.PostListView.as_view(), name="post_list"),
    # path("post_detail/<int:pk>/",views.post_detail,name="post_detail"),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:post>/",
        views.post_detail,
        name="post_detail",
    ),
    path("<int:pk>/share/", views.post_share, name="post_share"),
    path("comment/<int:pk>/", views.post_comment, name="post_comment"),
]
