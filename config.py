SECRET_KEY = 'jogoteca'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = 'password',
        servidor = 'localhost',
        database = 'jogoteca'
    )