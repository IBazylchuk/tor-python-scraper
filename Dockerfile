FROM python:3.10.1-alpine

RUN apk update && apk add tor

ENV FIRST_SOCKS_PORT=9101
ENV LAST_SOCKS_PORT=9199

WORKDIR /app
COPY . /app
RUN pip --no-cache-dir install -r requirements.txt

RUN echo "ExitNodes {us}" >> /etc/torrc

ADD configure_socks_ports.sh /tmp/configure_socks_ports.sh
RUN chmod +x /tmp/configure_socks_ports.sh

ADD start.sh /
RUN chmod +x /start.sh

CMD ["/start.sh"]
EXPOSE 5000
