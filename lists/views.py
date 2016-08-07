import builtins
import bottle

app = builtins.app

@app.route('/')
def index():
    return bottle.template("<p>Hello, {{name}}<p>", name='World!')