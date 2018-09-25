from rest_framework import viewsets

from .models import Category,Item,Tag,Article,Ad,UserFav,User

from .serializers import  UserRegSerializer, UserDetailSerializer,UserLoginSerializer,UserSetPasswordSerializer

from .serializers import UserFavSerializer, UserFavDetailSerializer,CategoryStringSerializer,\
    CategoryPrimaryKeySerializer,CategorySlugSerializer

from .serializers import CategorySerializer,ItemSerializer,TagSerializer,AdSerializer,\
    ArticleSerializer,Hot_articleSerializer,CategoryitemsSerializer

from rest_framework.decorators import api_view
from rest_framework import mixins

class CategoryViewset(viewsets.ModelViewSet):
    """
    list:
       GET url: /category/   分类列表数据
    creat:
       POST url: /category/  创建分类详情
    retrieve:
       GET url: /category/1/  获取分类详情
    update:
       PUT url: /category/1/  修改分类详情
    delete:
       DELETE url: /category/1/  删除分类详情
    """
    # 查询对象集
    queryset = Category.objects.all()
    # 序列化的类名
    serializer_class = CategorySerializer
    lookup_field = "id"

#class CategoryitemsViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
class CategoryitemsViewset(viewsets.ReadOnlyModelViewSet):
    """
    list:
        分类列表数据
    retrieve:
        获取分类详情
    """
    # 查询对象集
    queryset = Category.objects.all()
    # 序列化的类名
    serializer_class = CategoryitemsSerializer
    lookup_field = "id"

#class ItemViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
class ItemViewset(viewsets.ModelViewSet):
    """
    list:
       GET url: /item/   子类列表数据
    creat:
       POST url: /item/  创建子类详情，返回新生成的子类对像
    retrieve:
       GET url: /item/1/  获取子类详情，返回子类对像
    update:
       PUT url: /item/1/  修改子类详情，返回子类对像
    delete:
       DELETE url: /item/1/  删除子类详情，返回空对像
    """
    #用于从此视图返回对象的查询器集。

    queryset = Item.objects.all()


    #filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    #查询
    #filter_class = ItemFilter
    # SearchFilter对应search_fields，对应模糊查询,也可用关连表的字段进行查询，但需要二个下划线连接，如categorys__title
    search_fields = ('title','categorys__title')
    #用于验证和反序列化输入以及序列化输出的serializer类。通常，您必须设置此属性，或覆盖该get_serializer_class()方法。
    serializer_class = ItemSerializer
    # 应用于执行单个模型实例的对象查找的模型字段。默认为’pk’。
    lookup_field = "id"

