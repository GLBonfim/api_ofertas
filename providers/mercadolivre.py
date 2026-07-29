import requests

from .base import BaseScraper


class MercadoLivreProvider(BaseScraper):

    URL = "https://api.mercadolibre.com/sites/MLB/search"

    def buscar(self, pesquisa="notebook"):

        resposta = requests.get(
            self.URL,
            params={
                "q": pesquisa,
                "limit": 20
            },
            timeout=10
        )

        resposta.raise_for_status()

        dados = resposta.json()

        ofertas = []

        for item in dados["results"]:

            print(item["title"])

            preco = item["price"]

            ofertas.append({

                "titulo": item["title"],
                "preco": preco,
                "preco_antigo": preco,
                "desconto": 0,
                "loja": "Mercado Livre",
                "categoria": "",
                "imagem": item["thumbnail"],
                "link": item["permalink"]

            })

        print(f"Produtos encontrados: {len(ofertas)}")

        return ofertas