from flask inport Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from mysite import routes