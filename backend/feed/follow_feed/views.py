# from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from feed.models import Feed
from feed.serializers import FeedSerializer


class FollowFeedView(APIView):

    # view endpoint 접근권한 설정
    # permissions.IsAuthenticated: 로그인한 사람
    # permissions.IsAdmin: staff 권한 이상
    # permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def get(request):
        param = request.query_params.get('key_name')
        print(f'get param: {param}')

        # Feed all data query (select * from feed)
        feed_query_set = Feed.objects.all()

        # serialize feed_query_set (query_set -> dict)
        feed_data = FeedSerializer(feed_query_set, many=True).data

        return Response({'success': True, 'data': feed_data})

    @staticmethod
    def put(request):
        body_data = request.data.get('key_name')
        print(f'put body_data: {body_data}')

        # feed data query (select * from feed where name=key_name)
        feed_query_set = Feed.objects.filter(name='key_name')
        if not feed_query_set.exists():
            return {'success': False, 'message': 'not found data'}

        # feed query 데이터에 첫번째 데이터를 가져옴 (filter return -> array)
        feed_data = feed_query_set.first()
        feed_data.name = body_data
        feed_data.save()

        return Response({'success': True})

    @staticmethod
    def post(request):
        body_data = request.data.get('key_name')
        print(f'post body_data: {body_data}')

        # feed data create
        Feed.objects.create(name=body_data)

        return Response({'success': True})

    @staticmethod
    def delete(request):
        body_data = request.data.get('key_name')
        print(f'delete body_data: {body_data}')

        feed_query_set = Feed.objects.filter(name='key_name')
        if not feed_query_set.exists():
            return Response({'success': False, 'message': 'not found data'})

        feed_data = feed_query_set.first()
        feed_data.delete()

        return Response({'success': True})
