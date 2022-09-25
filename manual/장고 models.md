### 장고 ORM
Object Relational mapping   
어떤 sql이 쓰여 있는지 파악을 하고 최적화 할 수 있어야 함   
RDB 만을 지원한다.    
mysql, oracle, postgresql 등을 지원   

### 장고 Shell에서 테스트하기

```shell
python manage.py shell
>>> from django.db import connection
>>> cursor = connection.cursor()
>>> with connection.cursor() as cursor:
    cursor.execute("UPDATE bar SET foo =1 WHERE baz= %s", [self.baz])
    cursor.execute("SELECT foo FROM bar WHERE bar= %s", [self.baz])
    row = cursor.fetchone()
    print(row)
>>> cursor.close()
```

### 장고 Model
클래스 명은 Pascal Case 네이밍   

모델 생성 순서
* 모델 클래스 작성
* 마이그레이션 파일 생성: makemigrations
* 마이그레이션 파일을 적용: migrate
* 모델을 적용

외부 데이터베이스 형상을 활용하는 경우
* inspectdb 명령 사용

### 장고 Model 실습

장고 앱 만들고 등록 하기 
* instagram 앱 생성
    ```shell
    python manage.py startapp instagram
    ```
* settings에 INSTALLED_APPS에 instagram 추가
* urls.py 추가하고 urlpatterns 리스트 생성
* 프로젝트의 urls.py에서 include('instagram.urls') 매핑
* instagram의 models.py에서 Post 클래스 만들기
    ```python
  class Post(models.Model):
        message = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
    ```
* makemigrations instagram
* migrate instagram
* 쿼리 보기
    ```shell
    python manage.py sqlmigrate instagram 0001_initial
    ```
* DBshell (sqllist 설치되어 있어야 함)
    ```shell
    python manage.py dbshell
    sqlite>.tables
    sqlite>.schedma shop_item
    sqlite>.quit
    ```
### 장고 모델 필드 타입

* primary Key: AutoField
* 문자열 
* 날짜/시간
* Relationship Types
  * ForeignKey
  * ManyToManyField
  * OneToOneField

### 장고 모델 예제

```python
from django.conf import settings
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    blog_url = models.URLField(blank=True)

class Post(models.Model):
    '''
    블로그 포스트
    '''
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(allow_unicode=True, db_column=True) #제목과 숫자로 이루어진 url 생성시 사용
    desc = models.TextField(blank=True) # 빈문자열도 허용
    image = models.ImageField(blank=True)
    comment_count = models.PositiveIntegerField(default=0) # 양수만 처리
    tag_set = models.ManyToManyField('Tag', blank=True) # 하나의 포스트는 다수의 태그
    is_publish = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Comment(models.Model):
    '''
    한명의 유저가 여러 개의 댓글
    '''
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now==True)
    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

```

### 중요

* blank/null 은 최소화
* 직접 유효성 로직을 만들지 말고 장고의 기능을 가져다 쓸 것 !!!
* validation은 Tight 하게 지정
* 