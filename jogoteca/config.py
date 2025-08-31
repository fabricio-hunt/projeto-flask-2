SECRET_KEY = 'alura'

SQLALCHEMY_DATABASE_URI = (
    "{SGBD}://{usuario}:{senha}@{servidor}:{porta}/{database}?charset=utf8mb4".format(
        SGBD="mysql+mysqlconnector",
        usuario="root",
        senha="admin",
        servidor="127.0.0.1",
        porta=3306,
        database="jogoteca",
    )
)
