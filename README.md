# ⚽ Estimativa de Gols de Jogadores com Machine Learning

## 📌 Sobre o projeto

Este projeto tem como objetivo desenvolver um modelo de Machine Learning capaz de estimar a quantidade de gols de jogadores de futebol a partir de suas estatísticas individuais.

A proposta é explorar conceitos de Ciência de Dados, com foco em **Regressão**, utilizando o algoritmo **Random Forest Regressor** para analisar dados de desempenho de jogadores e gerar estimativas.

Além do modelo preditivo, o projeto conta com um dashboard interativo desenvolvido com Streamlit, permitindo selecionar jogadores e visualizar suas estatísticas e os resultados estimados pelo modelo.

## 🎯 Objetivos

- Aplicar conceitos de Ciência de Dados em uma base de dados esportiva.
- Compreender como funciona um problema de regressão.
- Desenvolver um modelo utilizando Random Forest Regressor.
- Realizar o pré-processamento de dados numéricos e categóricos.
- Apresentar as estimativas do modelo por meio de uma aplicação interativa.

## 🧠 Tecnologias utilizadas

- **Python:** linguagem utilizada no desenvolvimento.
- **Pandas:** manipulação e análise dos dados.
- **Scikit-learn:** pré-processamento e construção do modelo de Machine Learning.
- **Joblib:** salvamento e carregamento do modelo treinado.
- **Streamlit:** desenvolvimento do dashboard interativo.

## 📊 Base de dados

O projeto utiliza um conjunto de dados com estatísticas individuais de jogadores de futebol.

Entre as informações disponíveis estão:

| Variável | Descrição |
|---|---|
| `Player` | Nome do jogador |
| `Age` | Idade |
| `Nation` | Nacionalidade |
| `Pos` | Posição em campo |
| `Squad` | Equipe |
| `Gls` | Gols marcados |
| `Ast` | Assistências |
| `Sh` | Finalizações |
| `SoT` | Finalizações no alvo |
| `Min` | Minutos jogados |
| `PKatt` | Pênaltis tentados |

A variável `Gls` foi definida como o alvo (*target*) do modelo, ou seja, a quantidade de gols que se deseja estimar.

## ⚙️ Desenvolvimento do modelo

### 1. Pré-processamento

O pré-processamento foi desenvolvido utilizando ferramentas do Scikit-learn, organizadas em um pipeline.

Foram utilizadas duas categorias de variáveis:

**Variáveis numéricas:**
- Age
- Min
- Sh
- SoT
- Ast
- PKatt

Para tratar valores ausentes, foi utilizado `SimpleImputer` com a estratégia `median`.

**Variável categórica:**
- Pos

Os valores ausentes foram tratados utilizando a estratégia `most_frequent`, seguida da transformação das categorias por meio de `OneHotEncoder`.

### 2. Algoritmo utilizado: Random Forest Regressor

O modelo utiliza o algoritmo Random Forest Regressor, um método de aprendizado supervisionado baseado na construção de múltiplas árvores de decisão.

Cada árvore realiza uma estimativa individual, e o resultado final da regressão é obtido pela média das previsões produzidas pelas árvores.

Principais parâmetros utilizados:

| Parâmetro | Valor | Descrição |
|---|---:|---|
| `n_estimators` | 300 | Quantidade de árvores |
| `min_samples_leaf` | 2 | Número mínimo de amostras por folha |
| `n_jobs` | -1 | Utilização dos processadores disponíveis |
| `random_state` | 42 | Reprodutibilidade dos resultados |

### 3. Pipeline

O pipeline reúne as etapas de pré-processamento e treinamento em uma única estrutura, facilitando a aplicação do mesmo tratamento aos dados utilizados nas previsões.

O modelo treinado é salvo com Joblib e posteriormente carregado pela aplicação Streamlit.

## 🖥️ Dashboard interativo

A aplicação foi desenvolvida utilizando Streamlit e permite:

- Visualizar informações dos jogadores.
- Selecionar um jogador pelo nome.
- Consultar estatísticas individuais.
- Visualizar a quantidade real de gols.
- Consultar a quantidade de gols estimada pelo modelo.
- Comparar a diferença entre os gols reais e estimados.

## 📁 Estrutura do projeto

```text
projeto/
│
├── Data/
│   └── players_data-2026_2027.csv
│
├── dashboard.py
├── modelo_gols.pkl
├── treinamento.py
├── requirements.txt
└── README.md
```

*Observação: ajuste os nomes dos arquivos e diretórios de acordo com a estrutura final do seu repositório.*

## 🚀 Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
```

### 2. Acesse a pasta do projeto

```bash
cd SEU-REPOSITORIO
```

### 3. Crie um ambiente virtual

```bash
python -m venv venv
```

### 4. Ative o ambiente virtual

No Windows (PowerShell):

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Instale as dependências

```bash
pip install -r requirements.txt
```

### 6. Execute o dashboard

```bash
streamlit run dashboard.py
```

Após a execução, o Streamlit disponibilizará o endereço local para acessar a aplicação pelo navegador.

## ⚠️ Limitações do projeto

As estimativas são baseadas nas estatísticas disponíveis no conjunto de dados utilizado.

É importante destacar que o modelo utiliza informações da mesma temporada para estimar a quantidade de gols. Portanto, seu objetivo é analisar a relação entre as estatísticas dos jogadores e seus gols registrados, e não prever antecipadamente o desempenho de uma próxima temporada.

As estimativas também não devem ser interpretadas como valores garantidos de desempenho futuro.

## 📚 Aprendizados

O desenvolvimento deste projeto proporcionou a aplicação prática de conceitos importantes de Ciência de Dados, como:

- Manipulação e preparação de dados com Pandas.
- Tratamento de valores ausentes.
- Codificação de variáveis categóricas.
- Aprendizado supervisionado.
- Regressão aplicada a dados esportivos.
- Utilização de pipelines do Scikit-learn.
- Desenvolvimento de aplicações interativas com Streamlit.

---

**Projeto desenvolvido com finalidade acadêmica e de aprendizado em Ciência de Dados e Machine Learning.**
