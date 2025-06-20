from django.contrib import admin
from .models import Product, Post, Collectingdb


class ProductAdmin(admin.ModelAdmin):
    
    list_filter = ('pname','author', 'plink', 'status','created',)
    list_display = ('pname', 'author', 'plink','status', 'created',)



    def changelist_view(self, request, extra_context = None):
        extra_context = { 'title': '제품등록' }
        return super().changelist_view(request, extra_context)


    
admin.site.register(Product, ProductAdmin)

class PostAdmin(admin.ModelAdmin):
    # list_filter = ('price', 'name', ) 추후에 상태 컬럼이 필요한 모델에는 
    # 'status' ex. 완료 진행중 둘중 하나로 어드민에서 '필터' 가능하도록 할 것
    #
    list_filter = ('name', 'status', 'created', )
    list_display = ('name', 'number', 'status', 'created')
    # 



    def changelist_view(self, request, extra_context = None):
        extra_context = { 'title': '문의하기DB' }
        return super().changelist_view(request, extra_context)

class CollectingdbAdmin(admin.ModelAdmin):
    # list_filter = ('price', 'name', ) 추후에 상태 컬럼이 필요한 모델에는 
    # 'status' ex. 완료 진행중 둘중 하나로 어드민에서 '필터' 가능하도록 할 것
    #
    list_filter = ('dhname', 'cate001', 'name', 'number', 'address001', 'promoperson', 'status2', 'created', )
    list_display = ('dhname', 'cate001', 'name', 'number', 'address001', 'promoperson', 'status2', 'created', )
    # 



    def changelist_view(self, request, extra_context = None):
        extra_context = { 'title': '상담신청DB' }
        return super().changelist_view(request, extra_context)

admin.site.register(Post, PostAdmin)
admin.site.register(Collectingdb, CollectingdbAdmin)
admin.site.site_header = '관리자 페이지'

admin.site.index_title = '관리자 페이지'
admin.site.site_title = '관리자 페이지'
