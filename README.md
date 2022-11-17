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

### Crear una máquina virtual

```bash
virtualenv venv --python=python3.10
```

### Activar la máquina virtual

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
export FLASK_APP=main.py
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

## Migraciones en la base de datos

No serán necesarias las migraciones ya que estamos usando `create_all`:

```python
db.init_app(app)
with app.app_context():
    db.create_all()
```

En otros escenarios se requeriría:

```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

# SQLALCHEMY_DATABASE_URI

```
SQLALCHEMY_DATABASE_URI = "mysql://root:password@localhost/database"
SQLALCHEMY_DATABASE_URI = "mysql://root:password@127.0.0.1:33060/database"
```

# Referencias

- Estructurada basada en [intro-flask-silabuz](https://github.com/linder3hs/intro-flask-silabuz)
- Microblog adaptado de [Flask Web Development de Miguel Grinberg](https://www.oreilly.com/library/view/flask-web-development/9781491991725/)