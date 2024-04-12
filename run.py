from app import app
import os
from dotenv import load_dotenv


load_dotenv()
app=app

if __name__ == '__main__':
    
    port=os.getenv('PORT')
    production=os.getenv('PRODUCTION')

    debug = True

    if production == 'True':
        debug = False

    app.run(port=port, debug=debug, host='0.0.0.0')