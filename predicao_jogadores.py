# %%
# importação
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor

# %%
# Dados

jogadores = pd.read_csv("Data/players_data-2026_2027.csv")
jogadores

# %%
# limpeza dos dados 
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
jogadores

sem_goleiros = jogadores['Pos'] != 'GK'
jogadores = jogadores[sem_goleiros]

jogadores.isnull().sum()
jogadores = jogadores.dropna()

# %%
# Preparando dados para o ML 

X = jogadores[
    ['Player',
    'Age',
    'Nation',
    'Pos',
    'Squad',
    'Gls',
    'PKatt',
    'Ast',
    'Sh',
    'SoT',
    'Min']
]

y = jogadores['Gls']

# %%
# Separando treino e teste

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# %% 
# Transformar os dados que são string em númericos 

numericos = [
    'Age',
    'Min',
    'Sh',
    'SoT',
    'Ast',
    'PKatt'
]

categoricas = ['Pos']

preprocessamento = ColumnTransformer(
    transformers=[
        (
            'numericos',
            SimpleImputer(strategy='median'),
            numericos
        ),
        (
            'categoricas',
            Pipeline([
                ('imputer', SimpleImputer(strategy='most_frequent')),
                ('encoder', OneHotEncoder(handle_unknown='ignore'))
            ]),
            categoricas
        )
    ]
)

# %%
# treinamento do modelo

modelo = Pipeline([
    ('preprocessamento', preprocessamento),
    (
        'modelo',
        RandomForestRegressor(
            n_estimators=300,
            min_samples_leaf=2,
            random_state=42,
            n_jobs=-1
        )
    )
])

modelo.fit(X_train, y_train)
joblib.dump(modelo, 'modelo_gols.pkl')

