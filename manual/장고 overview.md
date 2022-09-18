#### 웹 어플리케이션 기본 구조

![](images/장고기본구조.png)

#### 장고 앱
현재 프로젝트의 블로그의 기능을 다른 프로젝트에서도 사용하고 싶다.   
앱을 하나의 작은 서비스로 보면 된다.  
재사용성의 단위로 끊어서 표현
```shell
python managy.py startapp blog1
```
새롭게 생성한 장고앱은 settings에 등록해야 됨

##### DB 생성하기
```shell
blog1.models.py 에서 Post DB 생성
python manage.py makemigrations blog1
python manage.py migrate blog1
blog.admin.py 페이지에 Post를 서브 페이지로 등록
```
웹브라우저에서 확인하면 방금생성한 Post 테이블 존재

##### 블로그 앱 만들기
* askcompany.settings에서 blog1.urls 등록
* blog1.urls.py에 views.post_list 매핑 
* blog1.views.py 에서 post_list 작성 및 html 파일 연결
* templates/blogs1 에 post_list.html 작성