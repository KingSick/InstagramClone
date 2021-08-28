from django.urls import path

from feed.follow_feed.views import FollowFeedView, FollowFeedDetailView

urlpatterns = [
    path('follow/', FollowFeedView.as_view()),
    path('follow/<int:feed_id>/', FollowFeedDetailView.as_view())
]
