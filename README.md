# hu-mentalhealth-backend

## Steps to run the app on local environment:
1. Clone this repository:

2. `cd hu-mentalhealth-backend`

3. Start a postgres container: `sudo docker run --name hutemplatedb -e POSTGRES_PASSWORD=python -e POSTGRES_DB=python -e POSTGRES_USER=python -p 5432:5432 -d postgres:13.2`  

    (You can verify if container is running using `docker ps`)


4. In the root directory of project 'hu-mentalhealth-backend', create a new virtual environment: `python3 -m venv venv`

5. Activate the virtual environment: `source venv/bin/activate`

6. Install the project dependencies: `pip install -r requirements.txt`

7. Go to the app sub-directory: `cd hu_calm`

8. Create a **`settings.py`** file inside **`hu_calm`** directory and add the following:
  
    ```

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'python',
            'USER': 'python',
            'PASSWORD': 'python',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

    _(The values should be the same as the values given while starting  the docker container.)_
    


9. Run db migrations: `python manage.py migrate`.

    (In case User model needs to be customized, please create a User model before running first migration and before first merge to main branch.
    ```
    from django.contrib.auth.models import AbstractUser

    class User(AbstractUser):
        pass
    ```
    Please refer: https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#substituting-a-custom-user-model)

10. Create an admin user: `python manage.py createsuperuser`. Enter the requested details accordingly.

11. Start the development server: `python manage.py runserver` 

12. Login to the admin portal from: http://localhost:8000/admin/ (Use the superuser credentials to login)
    
13. To run test cases: `python manage.py test `

