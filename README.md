# Idea

1. Simple http server supporting GET and PUT
2. Assuming disk.img in a certain file, only serving this one file
3. Pod to mount either block or FS PVC and map the file
4. oauth-proxy sidecar to authenticate access
5. route to expose to public

Effect:
HTTP based upload/download of PVC, authenticated against Kube.

# Usage

## GET

    $ TOKEN=$(oc create token TBD)
    $ curl --insecure -L -v -H"Authorization: Bearer $TOKEN" https://proxy-default.example.com/disk.raw

## PUT

    $ TOKEN=$(oc create token TBD)
    $ curl --insecure -L -v -H"Authorization: Bearer $TOKEN" https://proxy-default.example.com/disk.raw --upload-file mydisk.raw
