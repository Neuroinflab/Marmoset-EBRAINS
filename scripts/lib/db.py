import os
from databases import Database
from dotenv import load_dotenv

#BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.getcwd()
print ('BASEDIR', BASE_DIR)
load_dotenv(os.path.join(BASE_DIR, '.env'))

silo_db = Database(os.environ['DATABASE_URL'])
crop_db = Database(os.environ['CROP_DATABASE_URL'])
marmoset_db = Database(os.environ['MARMOSET_DATABASE_URL'])

