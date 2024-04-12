from app import app
import os
from dotenv import load_dotenv

if __name__ == '__main__':
    
    load_dotenv()
    port=os.getenv('PORT')
    production=os.getenv('PRODUCTION')

    debug = True

    if production == 'False':
        debug = False

    app.run(port=port, debug=debug, host='0.0.0.0')