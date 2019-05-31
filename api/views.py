from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from api.permissions import *
from api import models, serializers
from util import tesseract


class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset = models.Article.objects.all()
    serializer_class = serializers.Article
    permission_classes = (IsOwnerOrReadOnly,)


class ArticleList(ListCreateAPIView):
    queryset = models.Article.objects.all().order_by("-regDate")
    serializer_class = serializers.Article
    permission_classes = (IsAuthenticatedOrReadOnly,)


class Log(ListCreateAPIView):
    queryset = models.Log.objects.all().order_by("-regDate")
    serializer_class = serializers.Log
    permission_classes = (IsAuthenticatedOrAdminOnly,)


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
