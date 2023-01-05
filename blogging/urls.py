from django.urls import path
from blogging.views import stub_view
# from blogging.views import list_view
# from blogging.views import detail_view
from blogging.views import PostListView, PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name="blog_index"),
    path('posts/<int:pk>/', PostDetailView.as_view(), name="blog_detail"),
]