#! /bin/sh

docker buildx build --load --platform=linux/amd64 -t bkbhub/tor-python-scraper:amd64 .

docker buildx build --load --platform=linux/arm64 -t bkbhub/tor-python-scraper:arm64 .

docker push bkbhub/tor-python-scraper:amd64

docker push bkbhub/tor-python-scraper:arm64

docker manifest rm bkbhub/tor-python-scraper:latest

docker manifest create --amend bkbhub/tor-python-scraper:latest bkbhub/tor-python-scraper:amd64 bkbhub/tor-python-scraper:arm64

docker manifest push bkbhub/tor-python-scraper:latest
