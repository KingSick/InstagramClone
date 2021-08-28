# from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from account.models import Member
from feed.models import Feed
from feed.serializers import FeedSerializer


class FollowFeedView(APIView):

    # view endpoint 접근권한 설정
    # permissions.IsAuthenticated: 로그인한 사람
    # permissions.IsAdmin: staff 권한 이상
    # permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def get(request):
        # Feed all data query (select * from feed)
        feed_query_set = Feed.objects.all()

        # serialize feed_query_set (query_set -> dict)
        feed_data = FeedSerializer(feed_query_set, many=True).data

        return Response({'success': True, 'data': feed_data})

    @staticmethod
    def post(request):
        if 'content' not in request.data or 'image_url' not in request.data:
            return Response({'success': False, 'message': 'query params is not available'})

        body_data = request.data

        # find user
        # author = Member.objects.filter(user=request.user)
        temp_author = Member.objects.all().first()

        # feed data create
        feed_object = Feed.objects.create(author=temp_author,
                                          content=body_data['content'],
                                          image_url=body_data['image_url'])

        feed_data = FeedSerializer(feed_object).data

        return Response({'success': True, 'feed': feed_data})


class FollowFeedDetailView(APIView):

    # view endpoint 접근권한 설정
    # permissions.IsAuthenticated: 로그인한 사람
    # permissions.IsAdmin: staff 권한 이상
    # permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def get(request, feed_id):
        # Feed all data query (select * from feed)
        feed_query_set = Feed.objects.filter(id=feed_id)

        if not feed_query_set.exists():
            return Response({'success': False, 'message': 'not found data'})

        feed_query_set = feed_query_set.first()
        # serialize feed_query_set (query_set -> dict)
        feed_data = FeedSerializer(feed_query_set).data

        return Response({'success': True, 'data': feed_data})

    @staticmethod
    def put(request, feed_id):
        content = None
        image_url = None

        if 'content' in request.data:
            content = request.data.get('content')

        if 'image_url' in request.data:
            image_url = request.data.get('image_url')

        # feed data query (select * from feed where name=key_name)
        feed_query_set = Feed.objects.filter(id=feed_id)
        if not feed_query_set.exists():
            return Response({'success': False, 'message': 'not found data'})

        # feed query 데이터에 첫번째 데이터를 가져옴 (filter return -> array)
        feed_data = feed_query_set.first()
        if content is not None:
            feed_data.content = content
        if image_url is not None:
            feed_data.image_url = image_url
        feed_data.save()

        return Response({'success': True})

    @staticmethod
    def delete(request, feed_id):
        feed_query_set = Feed.objects.filter(id=feed_id)
        if not feed_query_set.exists():
            return Response({'success': False, 'message': 'not found data'})

        feed_data = feed_query_set.first()
        feed_data.delete()

        return Response({'success': True})
