mkdir -p .env;
python -m venv .env;
source ./.env/scripts/activate;
python -m pip install --upgrade pip;
pip install -r requirements.txt;
python manage.py makemigrations;
python manage.py makemigrations RestAPI;
python manage.py migrate --run-syncdb && python manage.py runserver 0.0.0.0:8000
# python manage.py test 
