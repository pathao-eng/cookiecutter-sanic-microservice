from sanic import Sanic
from sanic.response import json

app = Sanic()


@app.route("/")
async def welcome_view(request):
    return json({"message": "Welcome to {{cookiecutter.app_name}} API"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
