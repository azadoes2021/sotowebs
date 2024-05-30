from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Product(models.Model):
    # learn django - the easyway [youtube]
    


    STATUS_CHOICES = (
        ('yes','Yes'),
        ('no','No'),
    )

    # [중요 필드생성 필요함] 01 active, 02 nonactive  models.boolean


    pname = models.CharField(max_length=100, verbose_name='제품명')    
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='글쓴이')          
    # image = models.ImageField(null=True, blank=True, upload_to="static/images", default="static/images/defaultimg.jpg", verbose_name='이미지업로드')
    imglink = models.CharField(max_length=200, verbose_name='이미지링크', default='https://sotoairpurifier-oss.oss-cn-beijing.aliyuncs.com/attached/image/20210607/20210607135313_9390.jpg')    
    # learn django - the easyway [youtube]
    # author = models.ForeignKey(User, related_name='blog_posts')
    body = models.TextField(null=True,verbose_name='내용')
    created = models.DateTimeField(auto_now_add=True, verbose_name='등록일')
    updated = models.DateTimeField(auto_now=True)
    plink = models.CharField(max_length=100, verbose_name='링크주소[제품코드]')    
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='yes', verbose_name="노출여부")
    

    # object~~ 대신에 제목, 작성자 title author 로 나오도록
    def __str__(self):
        return self.pname + ' | ' + str(self.author)
    # 설명 : class AddPostView(CreateView) 로 만든 포스트 등록 폼 저장 후에 이동할 주소
    def get_absolute_url(self):
        # return reverse('article-detail', kwargs={'pk':self.id})
        return reverse('home')
    # admin에서 쉽게 사용하기 위해 meta를 사용 => 1.테이블명, 2.어드민에서 사용될 이름
    class Meta:
        # db_table = 'py_user'
        verbose_name = '제품등록'
        verbose_name_plural = '제품등록'
        ordering = ['-created']


class Post(models.Model):
    # learn django - the easyway [youtube]  
    
    STATUS_CHOICES = (
        ('신규','신규'),
        ('완료','완료'),
        ('진행중','진행중'),
        ('보류','보류'),
    )
    # [중요 title 없앨것입니다]
    # title = models.CharField(max_length=100, verbose_name='제목', default='') 

    name = models.CharField(max_length=50 ,null=True, verbose_name='이름(상호)')
    number = models.CharField(max_length=50 ,null=True, verbose_name='전화번호')
    # email = models.EmailField(max_length=50 ,null=True, verbose_name='이메일')

    # promoperson = models.CharField(max_length=24, default='없음', verbose_name="추천인")   
    # [중요 필드생성 필요함]
    # input == text : 전화번호
    # input = selectboxes : 세무기장, 법인세금 신고 기타 등등
    # subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES, default='', verbose_name='문의종류')
    # subject02 = models.CharField(max_length=50, choices=SUBJECT02_CHOICES, null=True, verbose_name='과세유형')
    # learn django - the easyway [youtube]
    # author = models.ForeignKey(User, related_name='blog_posts')
    body = models.TextField(null=True,verbose_name='내용')
    created = models.DateTimeField(auto_now_add=True, verbose_name='등록일')
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='신규', verbose_name='status')
    # input = hidden : dbcode db01 - 문의하기db  db02 -  랜딩페이지 db  db03 - 추가 홍보페이지
    terms_confirmed = models.BooleanField(max_length=10, null=True, verbose_name="개인정보 수집 동의")
    # code = models.CharField(max_length=10, default='as01') # code 문의하기, as01로 코드두어서 나중에 디비 join시킬때 사용
    # dbcode = models.CharField(max_length=20, default='db01', verbose_name='디비코드')# input = hidden : dbcode db01 - 문의하기db  db02 -  랜딩페이지 db  db03 - 추가 홍보페이지
    # dbname = models.CharField(max_length=20, default='', verbose_name='dbname')
    # dbnamekr = models.CharField(max_length=20, default='', verbose_name='DB종류')
            
    # object~~ 대신에 제목, 작성자 title name 로 나오도록
    def __str__(self):
        return self.name + ' | ' + str(self.number)
    # 설명 : class AddPostView(CreateView) 로 만든 포스트 등록 폼 저장 후에 이동할 주소
    def get_absolute_url(self):
        # return reverse('article-detail', kwargs={'pk':self.id})
        return reverse('home')
    # admin에서 쉽게 사용하기 위해 meta를 사용 => 1.테이블명, 2.어드민에서 사용될 이름
    class Meta:
        # db_table = 'py_user'
        verbose_name = '문의하기DB'
        verbose_name_plural = '문의하기DB'
        ordering = ['-created']