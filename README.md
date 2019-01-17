# krono-backend
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

# Run API on http://localhost:8000/
./manage.py runserver
```


## API general endpoints
| Endpoint | Parameters | Method | Description | Token |
| --- | --- | --- | --- | --- | --- | 
| / |  | GET | Admin Django - WEB | <ul><li>[ ] </li></ul> |
| /api/v1/ |  | GET | API root | <ul><li>[ ] </li></ul> |
| /api/v1/docs/ |  | GET | API documentation | <ul><li>[ ] </li></ul> |
| /api/v1/docs/schema.js |  | GET | API schema | <ul><li>[ ] </li></ul> |