from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from api.permissions import Model, Document
from api import models, serializers
from util import tesseract


class TestDetail(RetrieveUpdateDestroyAPIView):
    queryset = models.Test.objects.all()
    serializer_class = serializers.Test
    permission_classes = (Model.IsOwnerOrReadOnly,)


class TestList(ListCreateAPIView):
    queryset = models.Test.objects.all().order_by("-reg_date")
    serializer_class = serializers.Test
    permission_classes = (Model.IsAuthenticatedOrReadOnly,)


class Log(ListCreateAPIView):
    queryset = models.Log.objects.all().order_by("-reg_date")
    serializer_class = serializers.Log
    permission_classes = (Document.IsAuthenticatedOrAdminOnly,)


class ArticleList(ListCreateAPIView):
    queryset = models.Article.objects.no_cache().all().order_by("-reg_date")
    serializer_class = serializers.Article
    permission_classes = (Document.IsAuthenticatedOrReadOnly,)


class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset = models.Article.objects.all()
    serializer_class = serializers.Article
    permission_classes = (Document.IsOwnerOrReadOnly,)


class CommentList(ListCreateAPIView):
    queryset = models.Comment.objects.no_cache().all().order_by("-reg_date")
    serializer_class = serializers.Comment


@api_view(['POST'])
@permission_classes((AllowAny,))
@renderer_classes((JSONRenderer,))
def tssr(req):
    data = {}

    if req.method == 'POST':
        try:
            data['txt'] = tesseract.run(req.FILES['img'].file)
        except Exception as e:
            print(e)

    return Response(data)
