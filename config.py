##OPEN API STUFF
OPENAI_API_KEY = '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'



## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
