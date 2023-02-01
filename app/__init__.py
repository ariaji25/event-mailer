import datetime
from flask import Flask

from .repositories import *

from .database import *

from .usecases import *

from .utils.date_time import *

init_database_connection()

app = Flask(__name__)

# Register endpoint by import the api module
from .api import *
    
