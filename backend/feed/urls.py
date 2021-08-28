from django.urls import path

from feed.follow_feed.views import FollowFeedView

urlpatterns = [
    path('follow/feed', FollowFeedView.as_view())
]
