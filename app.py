import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Gráficos Sobre Trabalho e Desemprego", layout="wide")


st.title("Dashboard de Análise de Estatísticas de IBGE")

@st.cache_data
def carregar_dados_estado():
    df_estado = pd.read_csv("ibge_trabalho_estado_2012_2022.csv", delimiter=';')
    return df_estado

def carregar_dados_genero():
    df_genero = pd.read_csv("ibge_trabalho_genero_2012_2022.csv", delimiter=';')
    return df_genero

def carregar_dados_geral():
    df_geral = pd.read_csv("ibge_trabalho_geral_2012_2022.csv", delimiter=';')
    return df_geral

def carregar_dados_idade():
    df_idade = pd.read_csv("ibge_trabalho_idade_2012_2022.csv", delimiter=';')
    return df_idade

def carregar_dados_raca():
    df_raca = pd.read_csv("ibge_trabalho_raca_2012_2022.csv", delimiter=';')
    return df_raca


df_estado = carregar_dados_estado()
df_genero = carregar_dados_genero()
df_geral = carregar_dados_geral()
df_idade = carregar_dados_idade()
df_raca = carregar_dados_raca()

col1, col2 = st.columns(2)

with col1:
    fig_barras = px.bar(
        df_genero, x="Genero", y="Taxa_Participacao_Pct", color="Ano",
        title="Participação de genero", barmode="group"
    )
    st.plotly_chart(fig_barras, use_container_width=True)

with col2:
    fig_linhas = px.line(
        df_estado, x="UF", y="Taxa_Desocupacao_Pct", color="Taxa_Desocupacao_Pct",
        title="Taxa por estado", markers=True
    )
    st.plotly_chart(fig_linhas, use_container_width=True)

col3, col4, col5 = st.columns(3)

st.divider()

with col3:
    fig_linhass = px.line(
        df_geral, x="Ano", y="Taxa_Desocupacao_Pct", color="Taxa_Desocupacao_Pct",
        title="Taxa por Ano", markers=True
    )
    st.plotly_chart(fig_linhass, use_container_width=True)

with col4:
    fig_linhasss = px.line(
        df_idade, x="Ano", y="Faixa_Etaria", color="Faixa_Etaria",
        title="Faixa etária por ano", markers=True
    )
    st.plotly_chart(fig_linhasss, use_container_width=True)

with col5:
    fig_linhassss = px.line(
        df_raca, x="Ano", y="Cor_Raca", color="Taxa_Desocupacao_Pct",
        title="Taxa por Cor", markers=True
    )
    st.plotly_chart(fig_linhassss, use_container_width=True)
