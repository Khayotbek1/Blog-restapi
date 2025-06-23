from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import *

class TagCreateList(APIView):
    def get(self, request):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TagSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ArticleCreate(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ArticleCreateSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ArticleListAPIView(APIView):
    def get(self, request):
        articles = Article.objects.order_by('-created_at')
        serializer = ArticleRetrieveSerializer(articles, many=True)
        return Response(serializer.data)


class MyArticleListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        articles = Article.objects.filter(author=user).order_by('-created_at')
        serializer = MyArticleSerializer(articles, many=True)
        return Response(serializer.data)


