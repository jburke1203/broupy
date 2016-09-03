from . import app

@app.route('/user')
def index():
    return 'Hello User! --'