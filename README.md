Requisitos:
- Tener pip instalado.

(Para instalar pip en linux se debe crear un entorno virtual)
Pasos para crear e instalar en linxu:
Despues de haber clonado el repositorio, crear el entorno virtual dentro de la misma carpeta del proyecto.

Paso 1: Instalar el paquete python3-venv.
(Dependiendo la distro, sudo dnf python3-venv)

Paso 2: Estar dentro del proyecto y ejecutar: python3 -m venv nombre_del_entorno (llamarlo venv).

Paso 3: Ejecutarlo (recomiendo llamarlo venv para hacerlo mas facil) source nombre_del_entorno/bin/activate

Y se tendria que ver algo asi para ejecutarlo: source venv/bin/activate

Seguir los siguientes pasos una vez ya clonado:
Para instalar los requerimientos, deben ejecutar en la terminal del proyecto: pip install -r requirements.txt
(En linux asegurarse que este activo el entorno virtual: source venv/bin/activate)

Despues de instalar pip: python manage.py migrate

Bueno, para inciarlo ya se la sabe, python manage.py runserver
