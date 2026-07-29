from .mercadolivre import MercadoLivreProvider


class ScraperManager:

    def __init__(self):
        self.providers = [
            MercadoLivreProvider()
        ]

    def buscar_ofertas(self):

        ofertas = []

        for provider in self.providers:

            print(f"Executando {provider.__class__.__name__}")

            try:
                resultado = provider.buscar()

                print(f"{len(resultado)} ofertas")

                ofertas.extend(resultado)

            except Exception as e:
                print(f"Erro: {e}")

        return ofertas