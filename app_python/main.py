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


def write_time_in_file(time):
    f = open("/home/time.txt", "w")
    f.write(time)
    f.close()


@app.route("/", version="12.3.0")
async def index(request):
    write_time_in_file(get_moscow_time())
    return jinja.render("index.html",
                        request,
                        text="visit http://0.0.0.0:8000/v11.0.1/visits",
                        time="to check the time",
                        author="of your last visit"
                        )


@app.route("/visits", version="12.3.0")
async def index(request):
    """API to render html file and pass parameters in it"""
    text = "This is the time of your last visit!"
    f = open("/home/time.txt", "r")
    time = f.read()
    f.close()
    author = "developed by Anna Gorb"
    write_time_in_file(time)
    return jinja.render("index.html",
                        request,
                        text=text,
                        time=time,
                        author=author
                        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
