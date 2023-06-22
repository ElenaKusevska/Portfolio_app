from dotenv import load_dotenv   
load_dotenv()                   

import os 

SECRET_KEY = 'ABCDEFGH'
MAIL_SERVER ='smtp.gmail.com'
MAIL_PORT = 465
MAIL_USERNAME = os.environ.get('EMAIL')
MAIL_PASSWORD = os.environ.get('PASSWORD')
MAIL_USE_TLS = False
MAIL_USE_SSL = True