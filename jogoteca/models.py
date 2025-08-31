from jogoteca import db

# --- Tabela: jogos ---
class Jogo(db.Model):
    __tablename__ = 'jogos'  # <- nome real da tabela no MySQL

    id        = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome      = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(40), nullable=False)
    console   = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"<Jogo {self.nome}>"

# --- Tabela: usuarios ---
class Usuario(db.Model):
    __tablename__ = 'usuarios'  # <- nome real da tabela no MySQL

    # A PK no seu banco é 'nickname' (veja o CREATE TABLE)
    nickname = db.Column(db.String(8), primary_key=True)   # <- PK
    nome     = db.Column(db.String(20), nullable=False)
    senha    = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Usuario {self.nickname}>"
