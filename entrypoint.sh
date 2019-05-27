echo "Present Directory: $(pwd)"
echo "Contents:"
ls
python manage.py runserver 0.0.0.0:8000 &
cd python-flask-server
echo "Present Directory: $(pwd)"
echo "Contents:"
ls
python -m swagger_server 0.0.0.0
