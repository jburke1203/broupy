#!ENV/bin/python
from bottle import Bottle, route, run, template
import builtins

builtins.app = Bottle()
app = builtins.app

import lists.views

if __name__ == "__main__":
    app.run(reloader=True, debug=True)