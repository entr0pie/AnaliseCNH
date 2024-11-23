import pandas as pd


def calcular_volumetria_safra(df_safra: pd.DataFrame, safra: str) -> pd.DataFrame:
    total = len(df_safra)

    promotores = len(df_safra[df_safra['target'] == 'Promotor'])
    neutros = len(df_safra[df_safra['target'] == 'Neutro'])
    detratores = len(df_safra[df_safra['target'] == 'Detrator'])

    porcentagem_promotores = promotores / total * 100    
    porcentagem_neutros = neutros / total * 100
    porcentagem_detratores = detratores / total * 100

    return pd.DataFrame({
        'Safra': [safra],
        'Total': [total],
        'Promotores': [promotores],
        'Neutros': [neutros],
        'Detratores': [detratores],
        '(%) Promotores': [porcentagem_promotores],
        '(%) Neutros': [porcentagem_neutros],
        '(%) Detratores': [porcentagem_detratores],
    })