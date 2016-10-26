import flask
from views import views_bp

app = flask.Flask(__name__)

@app.route('/_ah/warmup')
def warmup():
        return ''

app.register_blueprint(views_bp)
