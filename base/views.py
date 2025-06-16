from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .forms import AskForm, CollectingdbForm
from django.core.mail import send_mail
from .utils import searchposts, paginatePosts
from .models import Product
class HomeView(FormView):
    # model = Post     
    template_name = 'home.html'
    form_class = AskForm

    success_url = 'success'    
    # fields = ['name', 'number', 'subject', 'body', 'terms_confirmed']
    # success_url = 'success'    
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)       
        # .objects.all() 로 진행하니 잘 작동되었음.
        # context ['blog'] = Blog.objects.get(pk=self.kwargs['pk']) => createview에는 pk가 들어가면 에러남.
        # context ['blog'] = Blog.objects.all()
        
        return context

class NewproductsView(FormView):
    # model = Post     
    template_name = 'newproducts.html'
    form_class = AskForm

    success_url = 'success'    
    # fields = ['name', 'number', 'subject', 'body', 'terms_confirmed']
    # success_url = 'success'    
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)       
        # .objects.all() 로 진행하니 잘 작동되었음.
        # context ['blog'] = Blog.objects.get(pk=self.kwargs['pk']) => createview에는 pk가 들어가면 에러남.
        # context ['product'] = Product.objects.all()
        
        return context

class ProductsflView(FormView):
    # model = Post     
    template_name = 'productsfl.html'
    form_class = AskForm

    success_url = 'success'    
    # fields = ['name', 'number', 'subject', 'body', 'terms_confirmed']
    # success_url = 'success'    
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)       
        # .objects.all() 로 진행하니 잘 작동되었음.
        # context ['blog'] = Blog.objects.get(pk=self.kwargs['pk']) => createview에는 pk가 들어가면 에러남.
        # context ['product'] = Product.objects.all()
        
        return context
    
class ContactView(FormView):
    # model = Post     
    template_name = 'contact.html'
    form_class = AskForm

    success_url = 'successori'    
    # fields = ['name', 'number', 'subject', 'body', 'terms_confirmed']
    # success_url = 'success'    
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)       
        # .objects.all() 로 진행하니 잘 작동되었음.
        # context ['blog'] = Blog.objects.get(pk=self.kwargs['pk']) => createview에는 pk가 들어가면 에러남.
        # context ['blog'] = Blog.objects.all()
        
        return context
    


class CollectdbView(FormView):
    # model = Post     
    template_name = 'collectingdb.html'
    form_class = CollectingdbForm

    success_url = 'successori2'    
    # fields = ['name', 'number', 'subject', 'body', 'terms_confirmed']
    # success_url = 'success'    
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)       
        # .objects.all() 로 진행하니 잘 작동되었음.
        # context ['blog'] = Blog.objects.get(pk=self.kwargs['pk']) => createview에는 pk가 들어가면 에러남.
        # context ['blog'] = Blog.objects.all()
        
        return context

class ProductssearchView(FormView):
    # model = Post     
    template_name = 'productssearch.html'
    form_class = AskForm

    success_url = 'success'    
    # fields = ['name', 'number', 'subject', 'body', 'terms_confirmed']
    # success_url = 'success'    
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)       
        # .objects.all() 로 진행하니 잘 작동되었음.
        # context ['blog'] = Blog.objects.get(pk=self.kwargs['pk']) => createview에는 pk가 들어가면 에러남.
        context ['product'] = Product.objects.all()
        
        return context
def productsearch(request):
# def posts(request):    
    posts, search_query = searchposts(request)

    # paginatePosts(request, posts, 숫자) 숫자 넣어도 변화없음. utils의 result에 숫자를 넣어야 적용됨. 동영상과 조금 다른점임. 
    custom_range, posts = paginatePosts(request, posts, 5)

    
    context = {'posts': posts, 'search_query': search_query, 'custom_range': custom_range}
    return render(request, 'productsearch.html', context)

def newproducts(request):
    return render(request, 'newproducts.html', {})
def productsfl(request):
    return render(request, 'productsfl.html', {})
def productspo(request):
    return render(request, 'productspo.html', {})
def productswm(request):
    return render(request, 'productswm.html', {})
def productscm(request):
    return render(request, 'productscm.html', {})
def productsuv(request):
    return render(request, 'productsuv.html', {})
def productsot(request):
    return render(request, 'productsot.html', {})


def suppom(request):
    return render(request, 'suppom.html', {})
def suppvi(request):
    return render(request, 'suppvi.html', {})
def suppcert(request):
    return render(request, 'suppcert.html', {})
def suppserv(request):
    return render(request, 'suppserv.html', {})
def company(request):
    return render(request, 'company.html', {})
def companycert(request):
    return render(request, 'companycert.html', {})
# def contact(request):
#     return render(request, 'contact.html', {})


def spg2(request):
    return render(request, 'spg2.html', {})
def spg3(request):
    return render(request, 'spg3.html', {})
def spg5(request):
    return render(request, 'spg5.html', {})
def spg6(request):
    return render(request, 'spg6.html', {})

def spy3(request):
    return render(request, 'spy3.html', {})
def spy6(request):
    return render(request, 'spy6.html', {})
def spy8(request):
    return render(request, 'spy8.html', {})
def spy9(request):
    return render(request, 'spy9.html', {})
def spyd1(request):
    return render(request, 'spyd1.html', {})
def spyd2(request):
    return render(request, 'spyd2.html', {})

def spbk100(request):
    return render(request, 'spbk100.html', {})
def spbk90(request):
    return render(request, 'spbk90.html', {})

def spx1(request):
    return render(request, 'spx1.html', {})

def spu8(request):
    return render(request, 'spu8.html', {})
def spux(request):
    return render(request, 'spux.html', {})
def spuv360(request):
    return render(request, 'spuv360.html', {})
def spbiguv(request):
    return render(request, 'spbiguv.html', {})

def spq1(request):
    return render(request, 'spq1.html', {})
def spz3(request):
    return render(request, 'spz3.html', {})
def spz1(request):
    return render(request, 'spz1.html', {})
def spz2(request):
    return render(request, 'spz2.html', {})
def spkj1(request):
    return render(request, 'spkj1.html', {})
def spkj2(request):
    return render(request, 'spkj2.html', {})

def success(request):    
    return render(request, 'success.html', {})    
    
def successori(request): 
    # send_mail(
    #     '[SOTOPLUS] 문의 접수가 들어왔습니다.',
    #     '문의 접수가 들어왔습니다. 관리자페이지를 확인해주세요! https://sotoplus.co.kr/admin/',
    #     'bluewate02@naver.com',
    #     ['bluewate02@naver.com'],
    # )
    return redirect("successree")
def successori2(request): 
    # send_mail(
    #     '[SOTOPLUS] 검사 신청 접수가 들어왔습니다.',
    #     '검사 신청 접수가 들어왔습니다. 관리자페이지를 확인해주세요! https://sotoplus.co.kr/admin/',
    #     'bluewate02@naver.com',
    #     ['bluewate02@naver.com'],
    # )
    return redirect("successree2")
def successree(request): 
    return render(request, 'successree.html', {})    
def successree2(request): 
    return render(request, 'successree2.html', {}) 
def policy(request):
    return render(request, 'policy.html', {})  
def error_500(request):
    return render(request, '500.html')
def error_404(request, exception):
    return render(request, '404.html')  