FROM quay.io/fedora/fedora:latest

RUN dnf install -y python3
ADD app /app

ENTRYPOINT python3 -u /app/put.py
