set -ex

podman -r build -t quay.io/fdeutsch/uploadav .
podman -r run -p 8000:8000 quay.io/fdeutsch/uploadav
