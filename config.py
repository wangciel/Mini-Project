class Config(object):
    DEBUG = False
    TESTING = False
    # DATABASE_URI = 'sqlite:///:memory:'

class ProductionConfig(Config):
    # DATABASE_URI = 'mysql://user@localhost/foo'
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

config_map = {
    "production" : ProductionConfig,
    "develop" : DevelopmentConfig,
    "test": TestingConfig
}