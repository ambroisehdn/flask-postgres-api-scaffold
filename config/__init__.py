import os

def get_config():
    env = os.environ.get('FLASK_ENV', 'dev')

    if env == 'dev':
        from config.dev import Config
        return Config
    else:
        from config.dev import Config
        return Config


def load_config() :
    """Convert class attributes to a dictionary."""
    return {key: value for key, value in get_config().__dict__.items() if not key.startswith('__')}