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