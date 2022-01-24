#!/bin/sh

/tmp/configure_socks_ports.sh
tor -f /etc/torrc &
nginx &
cd /app && gunicorn --workers=5 --bind 0.0.0.0:5000 -t 60 wsgi:app
