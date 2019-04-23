from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MusicSerializer
from .models import Music
# Create your views here.

# Response 를 통해 Serializer 를 반환
# Serializer : 특정한 딕셔너리 혹은 쿼리셋 등의 파이썬 형식 데이터 타입을 반환하도록 하는 아이

# music 은 쿼리셋, 일종의 리스트인데 우리가 응답하려고 하는 것은 json
# Serializer 가 해주는 것은 리스트를 하나 하나씩 json 타입으로 바꿔주는 고마운 도구
# 그리고 응답하는 함수는 Response 이다.
# 결과로 보내줄 데이터는 .data 로 가져온다.

@api_view(['GET'])
def music_list(request):
    musics = Music.objects.all()
    # 단일 객체가 아닐 때 many=True 를 꼭 써야 함
    serializer = MusicSerializer(musics, many=True)
    return Response(serializer.data)