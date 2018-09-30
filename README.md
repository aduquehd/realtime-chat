# Realtime chat


## Description
Real Time Chat project is built on Django, Django Rest Framework, Vue.js and Django Channels.

Vue.js is used to consume the API to show the initial room chats, and also when a new message
come from the web socket, it use the power of Vue.js to update the DOM elements. 

The concept of the projects is the "Rooms", it has N number of rooms and the users can
interact with each room. The users need to be logged to can use the chat and the room's 
content is updated in real time using web sockets.

Also, an user can execute a bot command, writing "/stock=APPL". It will execute a web socket
call to another server dedicated to the bot process. The bot will get the data of 
APPL and show the result into the room for all users.

The application is using some good code practices, like documentation, query optimization
(select and prefetch related to improve foreign keys), structure of directories and files.

The project has unit test that coverage the Rest API to get a room's messages: 
`python manage.py test`


## Technical setup (It take about 5 minutes)


### Redis setup

1. We used docker to setup redis configuration.

    The port `6379` for realtime-chat and the port `6378` for 
    realtime-chat-bot projects

1. `docker run -p 6379:6379 -d redis:2.8`

1. `docker run -p 6378:6379 -d redis:2.8`

#### Development environment

1. Remember, This is for development environment. For production or any deployment setup,
this use environment variables.

1. Clone the project and go to the directory using the terminal/console

1. Install requirements with `pip install -r requirements.txt`

1. You need to create a file allocated into `realtime_chat/database_info.py` 
(At the same level that `settings.py`)

1. This file should contains the Database info and realtime chat bot URL (Second project
url/port execution)

    - Second project URL: https://github.com/saduqz/realtime-chat-bot
    
    ```python
        ENGINE = "django.db.backends.postgresql"
        NAME = "realtime_chat"
        HOST = "localhost"
        PORT = "5432"
        USER = "myuser"
        PASSWORD = "mypassword"
        REALTIME_CHAT_BOT_URL = "localhost:8001"
    ```    

1. Execute the commands:
     - `python manage.py makemigrations`
     - `python manage.py migrate`
     - `python manage.py create_super_user`
     - `python manage.py populate_rooms`
     - `python manage.py populate_users`
     
1. You can login into `/sysadmin` to see the admin interface.

    - The login credentials are:
        - username: `superadmin`
        - password: `123456`
        
    - Here you can create new users, rooms and see the chats
        
1. The command `populate_users` created some users to can interact with the realtime chat

    - Login credentials (The password is the same for all users):
        - users: `['andresduque', 'nelsonmartinez', 'wendylugo]`
        - password: `123456`
        
1. You can execute the unit test to the API with the command `python manage.py test`        
        
1. Go to `localhost:8000` or your project url execution and then, you will be redirected
to the login or rooms url. You can start having fun now ;)

1. You can go to `localhost:8000/chat/rooms/1` to see the API response 
with all chats of the room by the ID wrote in the URL.