get_emails.py
=============

Script para obtener los correos de los miembros de la comunidad de un servidor PyBossa.

Notas
=====

pg_dump --table='user' --data-only pybossa > user_data_only.sql

python get_emails.py
