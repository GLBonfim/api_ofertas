def gerar_texto(oferta):

    return f"""
🔥 {oferta['titulo']}

💰 De R${oferta['preco_antigo']}

➡️ Por R${oferta['preco']}

✅ {oferta['desconto']}% OFF

👉 {oferta['link']}
"""