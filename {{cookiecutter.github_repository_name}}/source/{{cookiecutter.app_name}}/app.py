from sanic import Sanic
import os

app = Sanic()


if __name__ == "__main__":
    port = os.environ['PORT']
    if port == "":
        port = 8000
    app.run(host="0.0.0.0", port=int(port))
