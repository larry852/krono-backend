# Krono Backend
Backend module for the control of users and stores of the Krono system.



## ERD
![ERD](doc/ERD.png?raw=true "ERD")



## Requirements
```sh
sudo apt install python3
sudo apt install python-pip
sudo pip install virtualenv
```
## Run
```sh
git clone https://github.com/larry852/krono-backend
cd krono-backend
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt

./manage.py migrate
./manage.py createsuperuser --email admin@admin.com --username admin
# Default run on http://localhost:8000/
./manage.py runserver
```


## API general endpoints
| Endpoint | Method | Description | Token |
| --- | --- | --- | --- | 
| / | GET | Admin Django - WEB | <ul><li>[ ] </li></ul> |
| /api/v1/ | GET | API root | <ul><li>[ ] </li></ul> |
| /api/v1/docs/ | GET | API documentation | <ul><li>[ ] </li></ul> |
| /api/v1/docs/schema.js | GET | API schema | <ul><li>[ ] </li></ul> |


## Load fake data
```sh
./manage.py seedCities --number=30
./manage.py seedUsers --number=30
./manage.py seedStores --number=30
```
*[Fix locale](https://github.com/Brobin/django-seed/pull/49/files)*