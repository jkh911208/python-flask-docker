# flask_web/app.py

from flask import Flask
app = Flask(__name__)

import logging                                                                  
import logging.handlers                                                         
logger = logging.getLogger("alert-connector")                                                    
sh = logging.handlers.SysLogHandler(address=("localhost", 514), facility="local0")                 
formatter =  logging.Formatter('%(name)s:%(message)s')                          
sh.setFormatter(formatter)                                                      
logger.addHandler(sh)                                                           


@app.route('/')
def hello_world():
    return 'Hey, we have Flask in a Docker container!'

@app.route("/logging")
def logging():
    logger.error("test")
    return "log written"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
