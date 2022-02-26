from flask import Flask
from flask.sessions import SecureCookieSessionInterface

app = Flask(__name__)
app.secret_key = b'fb+wwn!n1yo+9c(9s6!_3o#nqm&&_ej$tez)$_ik36n8d7o6mr#y'

session= SecureCookieSessionInterface().get_signing_serializer(app)

@app.route('/')
def index():
    print(session.dumps("admin"))

index()