#!/bin/sh
port=$FIRST_SOCKS_PORT
while [ $port -le $LAST_SOCKS_PORT ]
  do
    echo "SocksPort 0.0.0.0:$port" >> /etc/torrc
    port=`expr $port + 1`
  done
cat /etc/torrc
$1
