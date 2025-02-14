import os

HH_CLIENT_ID = os.getenv('HH_CLIENT_ID')
HH_CLIENT_SECRET = os.getenv('HH_CLIENT_SECRET')
AI_TOKEN = os.getenv('AI_TOKEN')
AI_ADDRESS = 'https://api.openai.com/v1/chat/completions'
PROXY_URL = os.getenv('PROXYURL')
ERROR_HANDLER_LIST = [403, 404, 408, 410, 504, 500]


# TODO create base hh address

