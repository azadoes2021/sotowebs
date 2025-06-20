from django.urls import path
from . import views
from .views import HomeView, NewproductsView, ProductssearchView, ProductsflView, ContactView, CollectdbView, CollectdbView002
urlpatterns = [
    
    path('', HomeView.as_view(), name="home"),
    
    # path('newproducts', NewproductsView.as_view(), name="newproducts"),    

    
    # path('productsfl', ProductsflView.as_view(), name="productsfl"),    
    # path('productspo', ProductspoView.as_view(), name="productspo"),    
    
    path('productsearch', views.productsearch, name="productsearch"),
    path('contact', ContactView.as_view(), name="contact"),
    path('collectingdb', CollectdbView.as_view(), name="collectingdb"),
    path('collectingdb002', CollectdbView002.as_view(), name="collectingdb002"),
    # path('productssearch', ProductssearchView.as_view(), name="productssearch"),
    
    # product category
    path('newproducts',views.newproducts , name="newproducts"),
    path('productsfl',views.productsfl , name="productsfl"),
    path('productspo',views.productspo , name="productspo"),
    path('productswm',views.productswm , name="productswm"),    
    path('productscm',views.productscm , name="productscm"),        
    path('productsuv',views.productsuv , name="productsuv"),
    path('productsot',views.productsot , name="productsot"),
    # support
    path('suppom',views.suppom , name="suppom"),
    path('suppvi',views.suppvi , name="suppvi"),
    path('suppcert',views.suppcert , name="suppcert"),    
    path('suppserv',views.suppserv , name="suppserv"),

    path('company',views.company , name="company"),
    path('companycert',views.companycert , name="companycert"),

    # path('contact',views.contact , name="contact"),
    # soto products
    path('spg2',views.spg2 , name="spg2"),
    path('spg3',views.spg3 , name="spg3"),
    path('spg5',views.spg5 , name="spg5"),
    path('spg6',views.spg6 , name="spg6"),
    
    path('spy3',views.spy3 , name="spy3"),
    path('spy6',views.spy6 , name="spy6"),
    path('spy8',views.spy8 , name="spy8"),
    path('spy9',views.spy9 , name="spy9"),
    path('spyd1',views.spyd1 , name="spyd1"),
    path('spyd2',views.spyd2 , name="spyd2"),

    path('spbk100',views.spbk100 , name="spbk100"),
    path('spbk90',views.spbk90 , name="spbk90"),

    path('spx1',views.spx1 , name="spx1"),

    path('spu8',views.spu8 , name="spu8"),
    path('spux',views.spux , name="spux"),
    
    path('spuv360',views.spuv360 , name="spuv360"),
    path('spbiguv',views.spbiguv , name="spbiguv"),

    path('spq1',views.spq1 , name="spq1"),    
    path('spz3',views.spz3 , name="spz3"),
    path('spz1',views.spz1 , name="spz1"),
    path('spz2',views.spz2 , name="spz2"),
    path('spkj1',views.spkj1 , name="spkj1"),
    path('spkj2',views.spkj2 , name="spkj2"),
    
    path('success',views.success , name="success"),
    path('successori',views.successori , name="successori"),
    path('successori2',views.successori2 , name="successori2"),
    path('successori3',views.successori3 , name="successori3"),
    path('successree',views.successree , name="successree"),
    path('successree2',views.successree2 , name="successree2"),
    path('successree3',views.successree3 , name="successree3"),
    path('policy',views.policy , name="policy"),

    
    



]





























































