from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from pickle import load

from flask_server.neural_network.network import Network
from flask_server.neural_network.data_scaler import DataScaler



SQLALCHEMY_TRACK_MODIFICATIONS = True

app = Flask(__name__)
cors = CORS(app, supports_credentials = True)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'test_key' #change in production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['JSON_SORT_KEYS'] = False
app.config['URL'] = 'http://localhost:8080'

db = SQLAlchemy(app)
encryptionHandler = Bcrypt()

#load body fat prediction model and scalers
print('Loading Body fat prediction model ...')

PATH = 'C:/Users/pl156\Documents/schoolwork/Computer Science A-Level/gym_bot_v2/flask_server/models/body_fat_predictor'
bodyFatPredictor = Network()
bodyFatPredictor = bodyFatPredictor.load(f'{PATH}/model.pickle')

bodyFatScalerX = DataScaler()
bodyFatScalerX.load(f'{PATH}/x_scaler.pickle')

bodyFatScalerY = DataScaler()
bodyFatScalerY.load(f'{PATH}/y_scaler.pickle')

print('Loaded Body fat prediction model')



from flask_server import views
from flask_server import models 