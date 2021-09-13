from datetime import datetime

import pytz
from sanic import Sanic
from sanic_jinja2 import SanicJinja2

app = Sanic(__name__)
app.static("/static", "./static")
jinja = SanicJinja2(app, pkg_name="templates", pkg_path="./")


def get_moscow_time():
    """Returns current Moscow time"""
    tz = pytz.timezone("Europe/Moscow")
    moscow_time = datetime.now(tz)
    moscow_time = moscow_time.strftime("%H:%M")
    return moscow_time


@app.route("/", version="7.0.0")
async def index(request):
    """API to render html file and pass parameters in it"""
    text = "This is the current Moscow time!"
    time = get_moscow_time()
    author = "developed by Anna Gorb"
    return jinja.render("index.html",
                        request,
                        text=text,
                        time=time,
                        author=author
                        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
