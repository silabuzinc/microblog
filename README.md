# Flask docs

Doc for setting up Flask

## Setup

### Install Python

Install Python 3.10

### Install pip

```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

### Install Flask

```bash
pip install Flask
```

### Install virtualenv

Virtualenv una herramienta para crear entornos virtuales de Python. Esto es útil para aislar las dependencias de un proyecto de las dependencias de otros proyectos.

```bash
pip install virtualenv
```

### Crear una maquina virtual

```bash
virtualenv venv --python=python3.10
```

### Activar la maquina virtual

```bash
source venv/bin/activate
```

- windows

```bash
venv\Scripts\activate

venv/Scripts/activate.ps1
```

### Varaible Flask

Unix

```bash
export FLASK_APP=app.py
export FLASK_DEBUG=1
```

window

```bash
set FLASK_APP=app.py
set FLASK_DEBUG=1
```

### Run

```bash
flask run
```

### End virtualenv

```bash
deactivate
```

### Requirements

Si han clonado un proyecto de github y quieren instalar las dependencias, pueden usar el archivo requirements.txt

```bash
pip install -r requirements.txt
```

# Para la base de datos

# Aplicando migraciones en la base de datos

Acorde a la documentación de [Flask Migrate](https://flask-migrate.readthedocs.io/en/latest/)

Y debido a que usamos `create_all`:

```python
db.init_app(app)
with app.app_context():
    db.create_all()
```

Solo necesitaríamos:

```bash
flask db init
```

# SQLALCHEMY_DATABASE_URI

```
SQLALCHEMY_DATABASE_URI = "mysql://root:password@localhost/database"
SQLALCHEMY_DATABASE_URI = "mysql://root:password@127.0.0.1:33060/database"
```

# Referencias

- Estructurada basada en [intro-flask-silabuz](https://github.com/linder3hs/intro-flask-silabuz)
- Microblog adaptado de [Flask Web Development de Miguel Grinberg](https://www.oreilly.com/library/view/flask-web-development/9781491991725/)