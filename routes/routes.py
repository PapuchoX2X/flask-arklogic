from flask import Blueprint, render_template, request, redirect, url_for
#from flask_mail import Message  # Importamos Message para enviar correos
#from app import mail  # Importamos mail directamente desde app.py

routes = Blueprint('routes', __name__)

@routes.route("/")
def home():
    return render_template('land/landingPage.html')

@routes.route("/login")
def login():
    return render_template('login/login.html')

