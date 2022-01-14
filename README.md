# SurveyDjango

## Technology stack:
- Python 3.8.5
- Django 3.2.7
- PostgreSQL 5.2

## Сommands to start the service:
- python -m venv
- .\survey\Scripts\activate
- pip install -r requirements.txt
- python manage.py runserver
- create admin: python manage.py createsuperuser

## Database:
- Create database django_surveys

## Enviroment variables: 
```
PORT=8000

# variables for DB connection:
DB_DATABASE=django_surveys
DB_USER=replace_me
DB_PASSWORD=replace_me
DB_HOST=localhost
DB_PORT=5432
```


## Endpoints

#### Add a new survey

```
curl --request POST \
  --url http://127.0.0.1:8000/api/survey/ \
  --header 'Authorization: Basic aGVsZW46MTIzNA==' \
  --header 'Content-Type: application/json' \
  --data '{
		"title": "Test2",
		"description": "Test description"
}'
```


#### Add a new question

```
curl --request POST \
  --url http://127.0.0.1:8000/api/question/ \
  --header 'Authorization: Basic aGVsZW46MTIzNA==' \
  --header 'Content-Type: application/json' \
  --data '{
		"question_text": "Where are you from?",
		"pub_date": "2022-01-15T14:12:43Z",
		"survey": 1
}'
```

#### Get list of surveys

```
curl --request GET \
  --url http://127.0.0.1:8000/api/survey/ \
  --header 'Authorization: Basic aGVsZW46MTIzNA=='
```

#### Get list of questions

```
curl --request GET \
  --url http://127.0.0.1:8000/api/question/ \
  --header 'Authorization: Basic aGVsZW46MTIzNA=='
```




