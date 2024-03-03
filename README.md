# Steps to run the project

**Create a virtual environment**
```python
python3 -m venv venv
```

**Initialize the virtual environment**

- For Linux/Mac
    ```python
    source venv/bin/activate
    ```

- For Windows
    ```python
    venv\scripts\activate
    ```

**Move inside directory**
```python
cd untill u see requirements.txt
```

**Install the requirements**
```python
pip install -r requirements.txt
```

**Make migrations**
```python
python manage.py migrate
```

**Create superuser**
```python
python manage.py createsuperuser
```

**Create random data**
```python
python manage.py utils
```

**Run the server**
```python
python manage.py runserver
```

Your project is available at http://127.0.0.1:8000

------
