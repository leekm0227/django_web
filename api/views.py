from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework.generics import *
from rest_framework_mongoengine.generics import ListCreateAPIView as DocListCreateAPIView
from rest_framework_mongoengine.generics import RetrieveUpdateAPIView as DocRetrieveUpdateAPIView
from rest_framework_mongoengine.generics import get_object_or_404 as doc_get_object_or_404
from mongoengine.queryset.visitor import Q
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from api.permissions import Model, Document
from api import models, serializers
from util import tesseract


class Data(RetrieveAPIView):
    queryset = models.Data.objects.all()
    serializer_class = serializers.Data
    permission_classes = (Model.IsAuthenticated,)


# ======================================== MONGODB VIEW ================================================================
class Log(DocListCreateAPIView):
    queryset = models.Log.objects.all().order_by("-reg_date")
    serializer_class = serializers.Log
    permission_classes = (Document.IsAuthenticatedOrAdminOnly,)


class ArticleDetail(DocRetrieveUpdateAPIView):
    serializer_class = serializers.Article
    permission_classes = (Document.IsOwnerOrReadOnly,)

    def get_object(self):
        obj = doc_get_object_or_404(models.Article.objects.filter(id=self.kwargs['pk']))
        self.check_object_permissions(self.request, obj)
        return obj


class ArticleList(DocListCreateAPIView):
    lookup_field = 'article_id'
    queryset = models.Article.objects.all().order_by("-reg_date")
    serializer_class = serializers.Article
    permission_classes = (Document.IsAuthenticatedOrReadOnly,)
    doc_filterset_fields = ('title', 'content')

    def get_queryset(self):
        filter_kwargs = {}

        for field in self.doc_filterset_fields:
            if field in self.request.GET:
                filter_kwargs["{field}__contains".format(field=field)] = self.request.GET[field]

        if filter_kwargs:
            self.queryset = models.Article.objects.filter(**filter_kwargs).order_by("-reg_date")

        return self.queryset


class CommentDetail(DocRetrieveUpdateAPIView):
    serializer_class = serializers.Comment
    permission_classes = (Document.IsOwnerOrReadOnly,)

    def get_object(self):
        article = doc_get_object_or_404(models.Article.objects(id=self.kwargs['pk']))
        obj = doc_get_object_or_404(models.Comment.objects(Q(article=article) & Q(id=self.kwargs['comment_id'])))
        self.check_object_permissions(self.request, obj)
        return obj


class CommentList(DocListCreateAPIView):
    serializer_class = serializers.Comment
    permission_classes = (Document.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        article = doc_get_object_or_404(models.Article.objects(id=self.kwargs['pk']))
        serializer.save(article=article)

    def get_queryset(self):
        article = doc_get_object_or_404(models.Article.objects(id=self.kwargs['pk']))
        return models.Comment.objects(article=article).all().order_by("reg_date")


@api_view(['POST'])
@permission_classes((AllowAny,))
@renderer_classes((JSONRenderer,))
def tssr(req):
    data = {}

    try:
        data['txt'] = tesseract.run(req.FILES['img'].file)
    except Exception as e:
        print(e)

    return Response(data)
