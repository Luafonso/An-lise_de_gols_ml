import streamlit as st
import pandas as pd
import joblib

# Configurações da página
st.set_page_config(
    page_title="Análise de gols",
    page_icon="⚽",
    layout="wide"
)
@st.cache_resource
def carregar_modelo():
    return joblib.load('modelo_gols.pkl')

modelo = carregar_modelo()

# Carregando os dados do csv
resultados_teste = pd.read_csv(
    './Data/resultados_teste.csv'
)

st.title("⚽ Análise de gols")

st.write(
    "Sistema de estimativa de gols de jogadores "
    "utilizando Machine Learning (Random Forest Regressor)."
)

jogadores = pd.read_csv("./Data/players_data-2026_2027.csv")

# Limpando os dados e removendo goleiro
dados_jogadores = [
    'Player',
    'Age',
    'Nation',
    'Pos',
    'Squad',
    'Gls',
    'PKatt',
    'Ast',
    'Sh',
    'SoT',
    'Min'
]

jogadores = jogadores[dados_jogadores]

sem_goleiros = jogadores['Pos'] != 'GK'
jogadores = jogadores[sem_goleiros]

# Filtros para escolher o jogador 


st.subheader("Filtros de jogadores")

col1, col2 = st.columns(2)

# Filtro de clube
clubes = ["Todos"] + sorted(
    jogadores["Squad"].dropna().unique().tolist()
)

with col1:
    clube_selecionado = st.selectbox(
        "Selecione o clube:",
        clubes
    )

# Filtro de posição
posicoes = ["Todas"] + sorted(
    jogadores["Pos"].dropna().unique().tolist()
)

with col2:
    posicao_selecionada = st.selectbox(
        "Selecione a posição:",
        posicoes
    )

# Aplicando os filtros
dados_filtrados = jogadores.copy()

if clube_selecionado != "Todos":
    dados_filtrados = dados_filtrados[
        dados_filtrados["Squad"] == clube_selecionado
    ]

if posicao_selecionada != "Todas":
    dados_filtrados = dados_filtrados[
        dados_filtrados["Pos"] == posicao_selecionada
    ]


# Fazendo uma lista para a busca de seleção de jogadores

lista_jogadores = sorted(
    dados_filtrados["Player"].dropna().unique()
)

jogador_selecionado = st.selectbox(
    "Escolha um jogador:",
    lista_jogadores
)

dados_selecionados = dados_filtrados[
    dados_filtrados["Player"] == jogador_selecionado
]
# Dados para o modelo 

features_modelo = [
    'Age',
    'Pos',
    'Min',
    'Sh',
    'SoT',
    'Ast',
    'PKatt'
]

dados_para_previsao = dados_selecionados[
    features_modelo
]

previsoes = modelo.predict(dados_para_previsao)


# Gols reais e gols estimaos 

gols_reais = dados_selecionados['Gls'].iloc[0]

gols_estimados = float(previsoes[0])

diferenca = gols_estimados - gols_reais

st.subheader("🏃 Resumo do jogador")

# Estilo de colunas 


col1, col2, col3 = st.columns(3, border=True)

col1.metric(
    label="⚽ Gols reais",
    value=int(gols_reais)
)

col2.metric(
    label="📈 Gols estimados",
    value=f"{gols_estimados:.2f}"
)

col3.metric(
    label="➖ Diferença de gols",
    value=f"{diferenca:+.2f}"
)

# Perfil do jogador

st.subheader("👨 Perfil do jogador")

col1, col2, col3 = st.columns(3, border=True)

col1.write(f"**Jogador:** {dados_selecionados['Player'].iloc[0]}")
col2.write(f"**Idade:** {dados_selecionados['Age'].iloc[0]}")
col3.write(f"**Posição:** {dados_selecionados['Pos'].iloc[0]}")

col1, col2, col3 = st.columns(3, border=True)

col1.write(f"**Clube:** {dados_selecionados['Squad'].iloc[0]}")
col2.write(f"**Nacionalidade:** {dados_selecionados['Nation'].iloc[0]}")
col3.write(f"**Minutos:** {dados_selecionados['Min'].iloc[0]}")
