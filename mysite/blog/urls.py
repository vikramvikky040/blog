from django.conf.urls import url
from blog import views


urlpatterns = [
    url('',views.PostListView.as_view(),name='post_list'),
    url('about/',views.AboutView.as_view(),name='about'),

    url('post/(<int:pk>)',views.PostDetailView.as_view(),name='post_detail'),
    url('post/new/',views.CreatePostView.as_view(),name='post_new'),
    url('post/edit(<int:pk>)',views.PostUpdateView.as_view(),name='post_edit'),
    url('post/remove/(<int:pk>)',views.PostDeleteView.as_view(),name='post_remove'),
    url('drafts/',views.DraftListView.as_view(),name='post_draft_list'),
    url('post/comment/(<int:pk>)',views.add_comment_to_post,name='add_comment_to_post'),
    url('comment/approve/(<int:pk>)',views.comment_approve,name='comment_approve'),
    url('post/publish/(<int:pk>)',views.post_publish,name='post_publish'),
    url('comment/remove/(<int:pk>)',views.comment_remove,name='comment_remove'),
]
