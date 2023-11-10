from data_manager import DataManager
from dotenv import load_dotenv

def configure():
    load_dotenv()
configure()


data_manager = DataManager()

data_manager.price_compare()