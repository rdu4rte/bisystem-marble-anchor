import os
from dotenv import load_dotenv

load_dotenv()

mongo_username: str = os.getenv('MONGO_USERNAME')
mongo_password: str = os.getenv('MONGO_PASSWORD')
mongo_host: str = os.getenv('MONGO_HOST')
mongo_db: str = os.getenv('MONGO_DB')
mongo_port: int = os.getenv('MONGO_PORT')

mongo_uri: str = 'mongodb://{host}:{port}'.format(
    host=mongo_host,
    port=mongo_port
)
