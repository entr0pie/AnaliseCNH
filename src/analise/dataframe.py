# https://stackoverflow.com/a/26887820

import pandas as pd


def aplicar_transformacoes_padrao(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aplica todas as filtragens e criações de coluna padrão.
    """
    
    df = filtrar_por_brasil(df)
    df = filtrar_por_grupo_4(df)
    
    df['target'] = df.apply(criar_coluna_target, axis=1)
    df['regiao'] = df.apply(criar_coluna_regiao, axis=1)
    df['safra'] = df.apply(criar_coluna_safra, axis=1)
    df = normalizar_periodo_pesquisa(df)

    return df
    

def filtrar_por_brasil(df: pd.DataFrame) -> pd.DataFrame:
    """
    Filtra o DataFrame para registros no mercado do BRASIL.
    """
    
    return df[df['mercado'] == 'BRASIL']


def filtrar_por_grupo_4(df: pd.DataFrame) -> pd.DataFrame:
    """
    Filtra o DataFrame para registros que estão no Grupo de Produto 4.
    """
    
    return df[df['Grupo de Produto'] == 'Grupo 4']

    
def criar_coluna_target(row: pd.Series) -> str:
    """
    Gera uma nova coluna, classificando cada linha em
    Detrator, Neutro e Promtor, com base no NPS e utilizando a coluna
    'nota'.
    """
    
    nota = row['nota']
    
    if nota >= 9:
        return 'Promotor'
    if nota >= 7:
        return 'Neutro'

    return 'Detrator'


def criar_coluna_regiao(row: pd.Series) -> str | None:
    """
    Gera uma nova coluna, classificando cada linha em sua região brasileira
    (Sul, Sudeste, Centro-Oeste, Norte e Nordeste) com base na sigla da coluna 
    'estado'.
    """
    
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
    

def criar_coluna_safra(row: pd.Series) -> int:
    """
    Gera uma nova coluna com o ano presente em 'data_resposta'.
    """
    
    return pd.to_datetime(row['data_resposta'], dayfirst=True).year


def normalizar_periodo_pesquisa(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normaliza a coluna 'Periodo de Pesquisa'.
    """
    
    df['Periodo de Pesquisa'] = df['Periodo de Pesquisa'].apply(lambda periodo: periodo.strip())
    return df

    