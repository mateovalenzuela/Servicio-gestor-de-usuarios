import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

# Definir las rutas de los archivos de claves
SIGNING_KEY_FILE = os.getenv('SIGNING_KEY_NAME_FILE', '')
VERIFYING_KEY_FILE = os.getenv('VERIFYING_KEY_NAME_FILE', '')

# Configuraciones de Simple JWT
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'BLACKLIST_ENABLED': True,
    'SIGNING_KEY': SIGNING_KEY_FILE,
    'VERIFYING_KEY': VERIFYING_KEY_FILE,
    'ALGORITHM': 'RS256',
}