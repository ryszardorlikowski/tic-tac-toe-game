import environs

env = environs.Env()

SECRET_KEY = env.str('SECRET_KEY', 'supersecretkey')
SQLALCHEMY_DATABASE_URI = env.str('SQLALCHEMY_DATABASE_URI', 'sqlite:///:memory:')
