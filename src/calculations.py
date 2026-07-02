import pandas as pd


def calcular_cif_estimado(fob: float, frete: float, seguro: float) -> float:
    """
    Calcula o valor CIF estimado somando FOB, Frete e Seguro.

    ATENÇÃO: Este cálculo é uma aproximação puramente didática/acadêmica.
    No comércio exterior brasileiro real, o Valor Aduaneiro (base de cálculo
    dos impostos de importação) segue regras do Acordo de Valoração Aduaneira (AVA)
    e inclui outras despesas de movimentação no porto de destino (como capatazia/THC),
    além de taxas e ajustes oficiais. Esta função não deve ser utilizada para fins
    fiscais, aduaneiros, tributários ou operacionais oficiais.
    """
    return float(fob + frete + seguro)


def calcular_cif_dataframe_estimado(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adiciona ou atualiza a coluna 'valor_cif_usd_estimado' no DataFrame de processos
    de importação, aplicando a soma estimada (FOB + Frete + Seguro).

    Esta é uma implementação didática desenvolvida para o protótipo acadêmico.
    """
    df = df.copy()
    df["valor_cif_usd_estimado"] = (
        df["valor_fob_usd_estimado"]
        + df["frete_usd_estimado"]
        + df["seguro_usd_estimado"]
    )
    return df
