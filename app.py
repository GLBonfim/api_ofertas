from scrapers.manager import ScraperManager
from ai import gerar_texto
from publisher import publicar
from database import oferta_existe, salvar

manager = ScraperManager()

ofertas = manager.buscar_ofertas()

for oferta in ofertas:

    if oferta_existe(oferta["link"]):
        continue

    mensagem = gerar_texto(oferta)

    publicar(mensagem)

    salvar(oferta)