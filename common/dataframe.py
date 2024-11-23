# https://stackoverflow.com/a/26887820

import pandas as pd


def filter_by_brasil(df: pd.DataFrame) -> pd.DataFrame:
    return df[df['mercado'] == 'BRASIL']


def filter_by_group_4(df: pd.DataFrame) -> pd.DataFrame:
    return df[df['Grupo de Produto'] == 'Grupo 4']

    
def create_nps_target(row: pd.Series) -> str:
    nota = row['nota']
    
    if nota >= 9:
        return 'Promotor'
    if nota >= 7:
        return 'Neutro'

    return 'Detrator'


def create_regiao_column(row: pd.Series) -> str | None:
    regioes = {
        'Sul': ['RS', 'SC', 'PR'],
        'Sudeste': ['SP', 'RJ', 'MG', 'ES'],
        'Centro-Oeste': ['MT', 'MS', 'GO', 'DF'],
        'Nordeste': ['SE', 'RN', 'PI', 'PE', 'PB', 'MA', 'CE', 'BA', 'AL'],
        'Norte': ['TO', 'RR', 'RO', 'PA', 'AM', 'AP', 'AC']
    }

    for regiao, siglas in regioes.items():
        if row['estado'] in siglas:
            return regiao
    
    return None
    

def create_safra_column(row: pd.Series) -> int:
    return pd.to_datetime(row['data_resposta'], dayfirst=True).year