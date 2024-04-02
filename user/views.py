from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView, Response, status
from .models import MyUser
from .serializers import UserCreateSerializer, UserProfileSerializer, UserUpdateSerializer


class UserCreateView(APIView):

    def post(self, request):

        serializer = UserCreateSerializer(data=request.data, context={'request': request})

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView):
    def get(self, request):
        user = MyUser.objects.get(id=request.user.id)

        serializer = UserProfileSerializer(user)

        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=UserProfileSerializer()
    )
    def patch(self, request):
        user = MyUser.objects.get(id=request.user.id)
        serializer = UserProfileSerializer(instance=user, data=request.data, partial=True,
                                             context={'request': request})

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)












