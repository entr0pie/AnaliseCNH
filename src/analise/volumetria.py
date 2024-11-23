import pandas as pd


def calcular_volumetria(df: pd.DataFrame, nome_coluna: str, valor_coluna: str) -> pd.DataFrame:
    """
    Calcula a volumetria de Detratores, Neutros e Promotores em um DataFrame.
    Retorna um DataFrame de apenas uma linha.
    """
    
    total = len(df)

    promotores = len(df[df['target'] == 'Promotor'])
    neutros = len(df[df['target'] == 'Neutro'])
    detratores = len(df[df['target'] == 'Detrator'])

    porcentagem_promotores = promotores / total * 100    
    porcentagem_neutros = neutros / total * 100
    porcentagem_detratores = detratores / total * 100

    return pd.DataFrame({
        f'{nome_coluna}': [valor_coluna],
        'Total': [total],
        'Promotores': [promotores],
        'Neutros': [neutros],
        'Detratores': [detratores],
        '(%) Promotores': [porcentagem_promotores],
        '(%) Neutros': [porcentagem_neutros],
        '(%) Detratores': [porcentagem_detratores],
    })