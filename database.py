import sqlite3

conn = sqlite3.connect("data/ofertas.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS ofertas(

id INTEGER PRIMARY KEY AUTOINCREMENT,

titulo TEXT,

preco REAL,

preco_antigo REAL,

desconto INTEGER,

loja TEXT,

categoria TEXT,

imagem TEXT,

link TEXT UNIQUE

)
""")

conn.commit()


def oferta_existe(link):

    cursor.execute(

        "SELECT id FROM ofertas WHERE link=?",

        (link,)
    )

    return cursor.fetchone() is not None


def salvar(oferta):

    cursor.execute("""

        INSERT INTO ofertas(

            titulo,

            preco,

            preco_antigo,

            desconto,

            loja,

            categoria,

            imagem,

            link

        )

        VALUES(?,?,?,?,?,?,?,?)

    """,

    (

        oferta["titulo"],

        oferta["preco"],

        oferta["preco_antigo"],

        oferta["desconto"],

        oferta["loja"],

        oferta["categoria"],

        oferta["imagem"],

        oferta["link"]

    ))

    conn.commit()