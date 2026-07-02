from pathlib import Path

import pandas as pd
import streamlit as st

from src.calculations import calcular_cif_dataframe_estimado
from src.utils import formatar_moeda_brl, formatar_moeda_usd

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "mock" / "processos_mock.csv"


st.set_page_config(
    page_title="MVP Academico Comex Santos",
    layout="wide",
)


@st.cache_data
def carregar_processos() -> pd.DataFrame:
    dados = pd.read_csv(DATA_PATH, parse_dates=["eta_santos", "data_prevista_desembaraco"])
    dados = calcular_cif_dataframe_estimado(dados)
    return dados


processos = carregar_processos()

st.title("Controle Academico de Importacao Maritima")
st.caption("Simulacao ficticia de processos com destino ao Porto de Santos")

st.warning(
    "Protótipo acadêmico com dados 100% fictícios. "
    "Não há integração com Siscomex, Receita Federal, MDIC, Portal Único ou sistemas reais. "
    "Este app não define NCM, alíquotas, LI, LPCO ou regras oficiais."
)

with st.sidebar:
    st.header("Filtros")

    status_opcoes = sorted(processos["status_academico"].unique())
    status_selecionados = st.multiselect(
        "Status acadêmico",
        options=status_opcoes,
        default=status_opcoes,
    )

    pais_opcoes = sorted(processos["pais_origem"].unique())
    paises_selecionados = st.multiselect(
        "País de origem",
        options=pais_opcoes,
        default=pais_opcoes,
    )

    risco_opcoes = sorted(processos["risco_academico"].unique())
    riscos_selecionados = st.multiselect(
        "Risco acadêmico",
        options=risco_opcoes,
        default=risco_opcoes,
    )

    st.divider()
    st.caption("Filtros e classificações são apenas didáticos.")


filtrado = processos[
    processos["status_academico"].isin(status_selecionados)
    & processos["pais_origem"].isin(paises_selecionados)
    & processos["risco_academico"].isin(riscos_selecionados)
].copy()

total_processos = len(filtrado)
total_containers = int(filtrado["quantidade_containers"].sum()) if total_processos else 0
total_cif = float(filtrado["valor_cif_usd_estimado"].sum()) if total_processos else 0.0
total_armazenagem = float(filtrado["armazenagem_brl_estimada"].sum()) if total_processos else 0.0

col1, col2, col3, col4 = st.columns(4)
col1.metric("Processos filtrados", total_processos)
col2.metric("Contêineres", total_containers)
col3.metric("CIF estimado", formatar_moeda_usd(total_cif))
col4.metric("Armazenagem estimada", formatar_moeda_brl(total_armazenagem))

st.subheader("Painel de Acompanhamento")

if filtrado.empty:
    st.info("Nenhum processo encontrado para os filtros selecionados.")
else:
    visao_status = (
        filtrado.groupby("status_academico", as_index=False)["processo_id"]
        .count()
        .rename(columns={"processo_id": "quantidade"})
        .sort_values("quantidade", ascending=False)
    )

    visao_risco = (
        filtrado.groupby("risco_academico", as_index=False)["processo_id"]
        .count()
        .rename(columns={"processo_id": "quantidade"})
        .sort_values("quantidade", ascending=False)
    )

    grafico_col1, grafico_col2 = st.columns(2)
    with grafico_col1:
        st.markdown("**Processos por status acadêmico**")
        st.bar_chart(visao_status, x="status_academico", y="quantidade")

    with grafico_col2:
        st.markdown("**Processos por risco acadêmico**")
        st.bar_chart(visao_risco, x="risco_academico", y="quantidade")

    st.subheader("Processos Fictícios")
    tabela = filtrado[
        [
            "processo_id",
            "importador_ficticio",
            "pais_origem",
            "porto_origem",
            "navio_ficticio",
            "eta_santos",
            "data_prevista_desembaraco",
            "status_academico",
            "risco_academico",
            "produto_generico",
            "quantidade_containers",
            "valor_cif_usd_estimado",
            "observacoes_academicas",
        ]
    ].sort_values("eta_santos")

    st.dataframe(
        tabela,
        width="stretch",
        hide_index=True,
        column_config={
            "processo_id": "Processo",
            "importador_ficticio": "Importador fictício",
            "pais_origem": "País de origem",
            "porto_origem": "Porto de origem",
            "navio_ficticio": "Navio fictício",
            "eta_santos": st.column_config.DateColumn("ETA Santos", format="DD/MM/YYYY"),
            "data_prevista_desembaraco": st.column_config.DateColumn(
                "Previsão acadêmica", format="DD/MM/YYYY"
            ),
            "status_academico": "Status acadêmico",
            "risco_academico": "Risco acadêmico",
            "produto_generico": "Produto genérico",
            "quantidade_containers": "Contêineres",
            "valor_cif_usd_estimado": st.column_config.NumberColumn(
                "CIF estimado (USD)", format="US$ %.2f"
            ),
            "observacoes_academicas": "Observações acadêmicas",
        },
    )

st.divider()
st.caption(
    "Uso restrito a apresentação acadêmica. "
    "Não representa processo aduaneiro, fiscal, logístico ou portuário real."
)
