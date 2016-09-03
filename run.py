#!env/bin/python
import builtins
from bottle import Bottle

builtins.app = Bottle()
app = builtins.app

import lists.views
import users.views

if __name__ == "__main__":
    app.run(reloader=True, debug=True)
