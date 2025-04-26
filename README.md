# Backend-App

### install the dependencies of the backend code

> First locate in your shell in the root directory of the project

````bash
pip install -r requirements.txt
````

and execute the code with this command:

````bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
````

Also remember the .env file is needed in the root of the project for the connection with Supabase.
