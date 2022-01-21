#!/bin/sh

/tmp/configure_socks_ports.sh
tor -f /etc/torrc &
cd /app && gunicorn --bind 0.0.0.0:5000 -t 60 wsgi:app
