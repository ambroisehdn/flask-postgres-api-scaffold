import os

# Obtenez le répertoire parent du répertoire courant
APP_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Définissez le chemin d'accès absolu pour le répertoire des logs
LOG_BASE_PATH = os.path.join(APP_ROOT, "logs")

# Assurez-vous que le répertoire des logs existe
os.makedirs(LOG_BASE_PATH, exist_ok=True)

# Configuration du logging
APP_LOG_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s'
        }
    },
    'handlers': {
        'app': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(LOG_BASE_PATH, "app.log")
        }
    },
    'loggers': {
        'app': {
            'handlers': ['app'],
            'level': 'INFO',
            'formatter': 'verbose',
            'propagate': True,
        }
    }
}
