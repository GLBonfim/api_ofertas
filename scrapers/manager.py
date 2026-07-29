from .pelando import PelandoScraper

class ScraperManager:

    def __init__(self):
        self.scrapers = [
            PelandoScraper()
            # Adicione outros scrapers aqui, se necessário
        ]

    def buscar_ofertas(self):

        ofertas = []

        for scraper in self.scrapers:

            try:
                

                ofertas.extend(scraper.buscar())

            except Exception as e:
            
                print(f"Erro: {e}")

        return ofertas