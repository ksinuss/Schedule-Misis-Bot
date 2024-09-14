from json import dump
from config import DATA_PATH, BOT_TOKEN_PATH, system_data

# reading bot_token from a file
def get_bot_token():
    with open(BOT_TOKEN_PATH, 'r') as f:
        return f.read().strip()
    
# recording system_data
def create_system_credits():
    with open(DATA_PATH, 'w') as f:
        dump(system_data, f)
