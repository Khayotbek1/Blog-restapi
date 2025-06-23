from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserRetrieveSerializer
from .models import *

class ArticleCreateSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all(),
        required=False
    )
    class Meta:
        model = Article
        fields = '__all__'

        extra_kwargs = {
            'author': {'read_only': True},
            'slug': {'read_only': True},
        }

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'slug')

        extra_kwargs = {
            'slug': {'read_only': True},
        }

class ArticleRetrieveSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    author = UserRetrieveSerializer(read_only=True)
    class Meta:
        model = Article
        fields = '__all__'


class ArticleRetrieveAPIView(APIView):
    def get(self,request, slug):
        article = get_object_or_404(Article, slug=slug)
        serializer = ArticleRetrieveSerializer(article)
        return Response(serializer.data)


class MyArticleSerializer(serializers.ModelSerializer):
    author = UserRetrieveSerializer(read_only=True)
    class Meta:
        model = Article
        fields = '__all__'

        extra_kwargs = {
            'author': {'read_only': True},
            'slug': {'read_only': True},
        }

