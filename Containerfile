FROM quay.io/fedora/fedora:latest

RUN dnf install -y python3
ADD app /app

# Important: put.py makes assumptions about this
WORKDIR /mnt/disk
ENTRYPOINT python3 -u /app/put.py ; sleep 12
