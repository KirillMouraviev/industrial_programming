from python:3
copy requirements.txt ./
run pip install -r requirements.txt

copy . .

run python manage.py makemigrations
run python manage.py migrate
run python manage.py makemigrations todos
run python manage.py migrate
cmd ["python", "manage.py runserver 8080"]
