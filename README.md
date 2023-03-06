# Test Task - Chat for Two

Test task of a simple chat for two.
Using technologies:
- django
- django rest framework
- django rest frameworth - jwt
- SQLite

## Installation

Commands shown for operating system Ubuntu 20.04+

Install project:

```bash
git clone git@github.com:StasGrinchak/ChatForTwo.git
```
Create a virtual environment:

```bash
python3 -m venv venv
```

Connect to a virtual environment:

```bash
source venv/ban/activate
```

Install all dependencies from file 'requirements.txt':

```bash
pip install -r requirements.txt
```

Go to the project folder with the file 'manage.py' and run it:

```bash
python manage.py runserver
```

## API points

```python
#creating a new thread, accepts the POST method
/api/create-thread

#deleting thread by pk in get parameter, accepts the DELETE method
/api/delete-thread/<pk>

#get all threads with messages by user, accepts the GET method
/api/get-threads-by-user

#getting jwt token
/api/token/

#jwt token update
/api/token/refresh/

#adding a new message, accepts the POST method
/api/add-new-message

#get all messages for a thread by pk in get parameter, accepts the GET method
/api/get-all-message/<pk>

#get the number of unread messages for the user, accepts the GET method
/api/get-count-unread-messages

#change status of unread message, accepts PUT method
/api/put-mark-read-message/<pk>


```

