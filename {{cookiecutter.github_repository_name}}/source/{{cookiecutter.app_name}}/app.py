import sentry_sdk
from sanic import Sanic
from sanic.response import json
from sentry_sdk.integrations.sanic import SanicIntegration
import os

from .config import SENTRY_DSN


sentry_sdk.init(
    dsn=SENTRY_DSN,
    integrations=[SanicIntegration()]
)

app = Sanic()


@app.route("/")
async def welcome_view(request):
    return json({"message": "Welcome to {{cookiecutter.app_name}} API"})

if __name__ == "__main__":
    port = os.environ['PORT']
    if port == "":
        port = 8000
    app.run(host="0.0.0.0", port=int(port))
