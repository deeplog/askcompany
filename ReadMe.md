#### 시작하기

프로젝트 만들기

```bash
python -m venv venv
\venv\Scripts\activate
pip install "django~=3.0.0"
django-admin startproject askcompany
cd askcompany
```
초기화 하기  
```bash
python manage.py migrate
python createsuperuser
python manage.py runserver
```
접속하기  
`http://localhost:8000/admin/`
