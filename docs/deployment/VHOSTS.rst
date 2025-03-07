Apache + mod-wsgi configuration
===============================

An example Apache2 vhost configuration follows::

    WSGIDaemonProcess hotel_project-<target> threads=5 maximum-requests=1000 user=<user> group=staff
    WSGIRestrictStdout Off

    <VirtualHost *:80>
        ServerName my.domain.name

        ErrorLog "/srv/sites/hotel_project/log/apache2/error.log"
        CustomLog "/srv/sites/hotel_project/log/apache2/access.log" common

        WSGIProcessGroup hotel_project-<target>

        Alias /media "/srv/sites/hotel_project/media/"
        Alias /static "/srv/sites/hotel_project/static/"

        WSGIScriptAlias / "/srv/sites/hotel_project/src/hotel_project/wsgi/wsgi_<target>.py"
    </VirtualHost>


Nginx + uwsgi + supervisor configuration
========================================

Supervisor/uwsgi:
-----------------

.. code::

    [program:uwsgi-hotel_project-<target>]
    user = <user>
    command = /srv/sites/hotel_project/env/bin/uwsgi --socket 127.0.0.1:8001 --wsgi-file /srv/sites/hotel_project/src/hotel_project/wsgi/wsgi_<target>.py
    home = /srv/sites/hotel_project/env
    master = true
    processes = 8
    harakiri = 600
    autostart = true
    autorestart = true
    stderr_logfile = /srv/sites/hotel_project/log/uwsgi_err.log
    stdout_logfile = /srv/sites/hotel_project/log/uwsgi_out.log
    stopsignal = QUIT

Nginx
-----

.. code::

    upstream django_hotel_project_<target> {
      ip_hash;
      server 127.0.0.1:8001;
    }

    server {
      listen :80;
      server_name  my.domain.name;

      access_log /srv/sites/hotel_project/log/nginx-access.log;
      error_log /srv/sites/hotel_project/log/nginx-error.log;

      location /500.html {
        root /srv/sites/hotel_project/src/hotel_project/templates/;
      }
      error_page 500 502 503 504 /500.html;

      location /static/ {
        alias /srv/sites/hotel_project/static/;
        expires 30d;
      }

      location /media/ {
        alias /srv/sites/hotel_project/media/;
        expires 30d;
      }

      location / {
        uwsgi_pass django_hotel_project_<target>;
      }
    }
