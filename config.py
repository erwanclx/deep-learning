class Config:
    DATASET_PATH = 'data/dataset.csv'
    
class DevelopmentConfig(Config):
    """Configuration développement"""
    DEBUG = True
    
class ProductionConfig(Config):
    """Configuration production"""
    DEBUG = False
    
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}