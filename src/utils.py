def formatar_moeda_usd(valor: float) -> str:
    """
    Formata um valor float para string monetária no padrão brasileiro
    com o prefixo 'US$'. Exemplo: 1000.5 -> US$ 1.000,50
    """
    texto = f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return f"US$ {texto}"


def formatar_moeda_brl(valor: float) -> str:
    """
    Formata um valor float para string monetária no padrão brasileiro
    com o prefixo 'R$'. Exemplo: 1000.5 -> R$ 1.000,50
    """
    texto = f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {texto}"
