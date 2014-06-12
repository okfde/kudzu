virtualenv ENV
source ENV/bin/activate
pip install requirements.txt
python manage.py syncdb --migrate
python manage.py runserver