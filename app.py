from flask import Flask
#from flask_mail import Mail

# Configuración de la aplicación
app = Flask(__name__)
"""
# Configuración de Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.office365.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'info@ark-logic.com'  # Cambia esto por tu dirección de correo
app.config['MAIL_PASSWORD'] = 'arklogic2024!'       # Cambia esto por tu contraseña
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)
"""
# Importar y registrar las rutas
from routes.routes import routes
app.register_blueprint(routes)
