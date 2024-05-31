set -ex

podman -r build -t quay.io/fdeutsch/uploadav .
podman -r run -p 8000:8000 --mount type=bind,src=$PWD/tmp/disk.img,dst=/mnt/disk/disk.img,relabel=shared,chown=true quay.io/fdeutsch/uploadav
