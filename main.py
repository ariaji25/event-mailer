import datetime
from flask import Flask

from src.repositories import *

from database import *

from src.use_cases import *

from utils.date_time import *

init_database_connection()

app = Flask(__name__)
@app.route("/")
def root():
    return {"Hello World"}
    
