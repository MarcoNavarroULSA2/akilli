from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)
app.config["Debug"] = True
app.config['MYSQL_DATABASE_USER']= 'sepherot_dianac'
app.config['MYSQL_DATABASE_PASSWORD']= 'SIJ2e04sKLGh'
app.config['MYSQL_DATABASE_DB']= 'sepherot_dianacBD'
app.config['MYSQL_DATABASE_HOST']= 'nemonico.com.mx'

mysql = MySQL(app)