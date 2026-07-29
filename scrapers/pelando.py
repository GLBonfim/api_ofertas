from .base import BaseScraper

class PelandoScraper(BaseScraper):

    def buscar(self):
        # Implementação específica para buscar ofertas no Pelando
        return [
            {
                "titulo": "Oferta 1",
                "preco": "R$ 100,00",
                "preco_antigo": "R$ 150,00",
                "desconto": "33%",
                "loja": "Loja 1",
                "imagem": "",
                "categoria": "Categoria 1",
                "link": "https://exemplo.com/oferta1"
            },
            {
                "titulo": "Oferta 2",
                "preco": "R$ 200,00",
                "preco_antigo": "R$ 250,00",
                "desconto": "20%",
                "loja": "Loja 2",
                "imagem": "",
                "categoria": "Categoria 2",
                "link": "https://exemplo.com/oferta2"
            }
        ]