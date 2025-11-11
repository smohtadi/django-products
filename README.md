# Django Product List View (Demo)

## Installing
1. Create the virtual environment.
```
> python -m venv venv
```

2. Activate the virtual environment.
```
> source venv/bin/activate
```

3. Install the required packages.
```
> pip install -r requirements.txt
```
4. Run the application.
```
> python manage.py runserver`
```
5. The application will run on `http://127.0.0.1:8000/`. Navigate to `http://127.0.0.1:8000/admin/` to access the admin site. The username and password are `admin`.

## Techstack
**Bakend:** Django, Django REST Framework
**Frontend:** React, Vite


## Asumptions
* This application assumes products can only have one category and multiple tags attached to them.
