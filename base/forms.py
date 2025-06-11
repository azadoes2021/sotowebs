from django import forms
from .models import Post, Collectingdb
         

class AskForm(forms.Form):
    name = forms.CharField(
        error_messages={
            'required': '이름 또는 상호를 입력해주세요.'
        },
        max_length=64, label='이름(상호)'
    )
    number = forms.CharField(
        error_messages={
            'required': '전화번호를 입력해주세요.'
        },
        max_length=64, label='전화번호'
    )
    #2403
    # promoperson = forms.CharField(        
    #     required=False, max_length=64, label='추천인(지인소개할인)'
    # )

    # dbcode = forms.CharField(
    #     error_messages={
            
    #     },
    #     required=False, max_length=64, label='DBCODE'
    # )
    # dbname = forms.CharField(
    #     error_messages={
            
    #     },
    #     required=False, max_length=64, label='DBNAME'
    # )
    # dbnamekr = forms.CharField(
    #     error_messages={
            
    #     },
    #     required=False, max_length=64, label='DBDBNAMEKR'
    # )  
    # subject = forms.CharField(
        
    #     required=False, max_length=64, label='문의종류'
    # )
    # subject02 = forms.CharField(
        
    #     required=False, max_length=64, label='과세유형'
    # )
    
    
    body = forms.CharField(
        error_messages={
            # 'required': '문의내용을 입력해주세요.'
        },
        required=False, max_length=2000, label='문의내용'
    )
     

    # terms_confirmed = forms.BooleanField(
    #     error_messages={
    #         'required': '동의여부를 체크해주세요.'
    #     },        
    #     label='개인정보 수집 및 이용 동의',
        
    # )    

    # terms_confirmed = forms.BooleanField(
        
    #     required=False, label='개인정보 수집 및 이용 동의',
    # )    
    
    

    def clean(self):        
        cleaned_data = super().clean()
        name = cleaned_data.get('name')        
        number = cleaned_data.get('number')

        # promoperson = cleaned_data.get('promoperson')

        # subject = cleaned_data.get('subject')

        # subject02 = cleaned_data.get('subject02')

        body = cleaned_data.get('body')
        
        
        # terms_confirmed = cleaned_data.get('terms_confirmed')  
        
        # dbcode = cleaned_data.get('dbcode')

        # dbname = cleaned_data.get('dbname')
        # dbnamekr = cleaned_data.get('dbnamekr')
        # if name and number and subject and body and dbcode and promoperson and terms_confirmed:
        # if name and number and body and terms_confirmed:
        if name or number:

            post = Post(
                name = name,
                number = number,
                # promoperson = promoperson,
                # subject = subject,
                # subject02 = subject02,
                body = body,
                # terms_confirmed = terms_confirmed,
                # dbcode = dbcode,
                # dbname = dbname,
                # dbnamekr = dbnamekr,
                
            )
            post.save()


class CollectingdbForm(forms.Form):
    name = forms.CharField(
        error_messages={
            'required': '이름 또는 상호를 입력해주세요.'
        },
        max_length=64, label='이름(상호)'
    )
    number = forms.CharField(
        error_messages={
            'required': '전화번호를 입력해주세요.'
        },
        max_length=64, label='전화번호'
    )
    address001 = forms.CharField(
        error_messages={
            'required': '이름 또는 상호를 입력해주세요.'
        },
        max_length=64, label='이름(상호)'
    )
    address002 = forms.CharField(
        error_messages={
            'required': '이름 또는 상호를 입력해주세요.'
        },
        max_length=64, label='이름(상호)'
    )
    promoperson = forms.CharField(        
        required=False, max_length=64, label='추천인(지인소개할인)'
    )

    # dbcode = forms.CharField(
    #     error_messages={
            
    #     },
    #     required=False, max_length=64, label='DBCODE'
    # )
    # dbname = forms.CharField(
    #     error_messages={
            
    #     },
    #     required=False, max_length=64, label='DBNAME'
    # )
    # dbnamekr = forms.CharField(
    #     error_messages={
            
    #     },
    #     required=False, max_length=64, label='DBDBNAMEKR'
    # )  
    # subject = forms.CharField(
        
    #     required=False, max_length=64, label='문의종류'
    # )
    # subject02 = forms.CharField(
        
    #     required=False, max_length=64, label='과세유형'
    # )
    
    
    body = forms.CharField(
        error_messages={
            # 'required': '문의내용을 입력해주세요.'
        },
        required=False, max_length=2000, label='문의내용'
    )
     

    # terms_confirmed = forms.BooleanField(
    #     error_messages={
    #         'required': '동의여부를 체크해주세요.'
    #     },        
    #     label='개인정보 수집 및 이용 동의',
        
    # )    

    # terms_confirmed = forms.BooleanField(
        
    #     required=False, label='개인정보 수집 및 이용 동의',
    # )    
    
    

    def clean(self):        
        cleaned_data = super().clean()
        name = cleaned_data.get('name')        
        number = cleaned_data.get('number')
        address001 = cleaned_data.get('address001')        
        address002 = cleaned_data.get('address002')        

        name = cleaned_data.get('name')        
        promoperson = cleaned_data.get('promoperson')

        # subject = cleaned_data.get('subject')

        # subject02 = cleaned_data.get('subject02')

        body = cleaned_data.get('body')
        
        
        # terms_confirmed = cleaned_data.get('terms_confirmed')  
        
        # dbcode = cleaned_data.get('dbcode')

        # dbname = cleaned_data.get('dbname')
        # dbnamekr = cleaned_data.get('dbnamekr')
        # if name and number and subject and body and dbcode and promoperson and terms_confirmed:
        # if name and number and body and terms_confirmed:
        if name or number:

            collectingdb = Collectingdb(
                name = name,
                number = number,
                address001 = address001,
                address002 = address002,
                promoperson = promoperson,
                # subject = subject,
                # subject02 = subject02,
                body = body,
                # terms_confirmed = terms_confirmed,
                # dbcode = dbcode,
                # dbname = dbname,
                # dbnamekr = dbnamekr,
                
            )
            collectingdb.save()