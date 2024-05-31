# python3 -m SimpleHTTPPutServer 8080

from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

def forceDisk(func):
    def wrapper(self):
        print(self.headers)
        print(self.path)
        if(self.command not in ("GET", "PUT") or self.path != "/disk.img"):
            self.send_error(500, "Only GET and PUT to /disk.img permitted")
            self.end_headers()
        else:
            return func(self)
    return wrapper

# curl localhost:8000/disk.img
# curl localhost:8000/disk.img --upload-file local.disk.img
class PutHTTPRequestHandler(SimpleHTTPRequestHandler):
    @forceDisk
    def do_GET(self):
        return SimpleHTTPRequestHandler.do_GET(self)

    @forceDisk
    def do_PUT(self):
        print(self.headers)
        print(self.path)
        assert(self.path == "/disk.img")
        length = int(self.headers["Content-Length"])
        path = self.translate_path(self.path)
        with open(path, "wb") as dst:
            dst.write(self.rfile.read(length))
        self.send_response(200)
        self.end_headers()


def run(server_class=HTTPServer, handler_class=PutHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print("Listening", server_address)
    httpd.serve_forever()

if __name__ == '__main__':
    # Intentionally not absolute
    assert os.path.exists("disk.img"), "disk.img does not exist. Attach/Mount it!"
    run()
