from providers.manager import ScraperManager

manager = ScraperManager()

ofertas = manager.buscar_ofertas()

print(f"Total de ofertas: {len(ofertas)}")

for oferta in ofertas:
    print(oferta)