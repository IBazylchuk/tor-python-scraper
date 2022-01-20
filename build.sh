#! /bin/sh

docker buildx build --platform=linux/amd64 -t bkbhub/tor-python-scraper:amd64 .

docker buildx build --platform=linux/arm64 -t bkbhub/tor-python-scraper:arm64 .

# docker tag bkbhub/tor-python-scraper:amd64 bkbhub/tor-python-scraper:amd64

docker manifest create bkbhub/tor-python-scraper:latest bkbhub/tor-python-scraper:amd64 bkbhub/tor-python-scraper:armv64

docker push bkbhub/tor-python-scraper:amd64

docker push bkbhub/tor-python-scraper:arm64
