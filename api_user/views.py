from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api_user.models import User
from api_user.serializer import UserSerializer


class UserView(APIView):
    # def get(self, request):
    #     return Response("ok", status=200)

    # POST /user ==> Create
    def post(self, request):
        user_serializer = UserSerializer(data=request.data)

        if user_serializer.is_valid():
            user_serializer.save() # UserSerializer가 있으면 DB저장
            return Response(user_serializer.data, status=status.HTTP_201_CREATED) #client에게 JSON response 전달
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # GET /user ==> Read
    # GET /user/{user_id}
    # *args: 어떤 값인지는 몰라도 변수가 튜플형태로 입력
    # **kwargs: 어떤 값인지는 몰라도 변수가 딕셔너리 형태로 입력
    def get(self, request, **kwargs):
        if kwargs.get('user_id') is None:
            user_queryset = User.objects.all()
            user_queryset_serializer = UserSerializer(user_queryset, many=True) # id에 해당하는 User의 정보를 불러온다
            return Response(user_queryset_serializer.data, status=status.HTTP_200_OK)
        else:
            user_id = kwargs.get('user_id')
            user_serializer = UserSerializer(User.objects.get(id=user_id)) # id에 해당하는 User의 정보를 불러온다
            return Response(user_serializer.data, status=status.HTTP_200_OK)

    # PUT /user/{user_id} ==> Update
    def put(self, request, **kwargs):
        if kwargs.get('user_id') is None:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        else:
            user_id = kwargs.get('user_id')
            user_object = User.objects.get(id=user_id)

            update_user_serializer = UserSerializer(user_object, data=request.data)
            if update_user_serializer.is_valid():
                update_user_serializer.save()
                return Response(update_user_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)

    # DELETE /user/{user_id}
    def delete(self, request, **kwargs):
        if kwargs.get('user_id') is None:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        else:
            user_id = kwargs.get('user_id')
            user_object = User.objects.get(id=user_id)
            user_object.delete()
            return Response("test ok", status=status.HTTP_200_OK)
