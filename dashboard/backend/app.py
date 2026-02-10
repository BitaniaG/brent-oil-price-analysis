from flask import Flask
from routes.prices import prices_bp
from routes.events import events_bp
from routes.changepoints import changepoints_bp

app = Flask(__name__)

app.register_blueprint(prices_bp, url_prefix="/api/prices")
app.register_blueprint(events_bp, url_prefix="/api/events")
app.register_blueprint(changepoints_bp, url_prefix="/api/changepoints")

@app.route("/")
def home():
    return {"status": "Dashboard backend running"}

if __name__ == "__main__":
    app.run(debug=True)
