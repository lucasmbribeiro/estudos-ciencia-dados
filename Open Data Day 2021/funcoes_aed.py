import pandas as pd
import numpy as np

def cria_dataframe_vacinas():
    df = pd.read_excel(
        "./base/bancoOPENCOMPLETO.xlsx"
        , sheet_name = 0
        , na_values = ['', ' ']
        , dtype  = {'ano': np.int32, 'Estado': 'category'
            , 'CV_SCR1 (1 ano)': np.float32, 'CV_SCR2 (15 meses)': np.float32, 'Poprural': np.float32
            , 'PopUrb': np.float32, 'RDPC': np.float32, 'PEA': np.float32, 'PEA_A': np.float32
            , 'IDHM': np.float32, 'IDHM_E': np.float32, 'IDHM_L': np.float32, 'IDHM_R': np.float32
            , 'T_ANALF18M': np.float32, 'T_MED18M': np.float32,'T_SUPER25M': np.float32, 'T_AGUA': np.float32
            , 'T_BANAGUA': np.float32, 'T_DENS': np.float32, 'T_LIXO': np.float32
            , 'T_LUZ': np.float32,'AGUA_ESGOTO': np.float32, 'POPDOMCHEFMULHERES': np.float32, 'DENSDEMOG2010': np.float32
            , 'PERC_NV_7CPN': np.float32,'CoberturaAB': np.float32
    })


    df.rename(columns={'Estado': 'UF', 'ano':'ANO','Nome': 'MUNICIPIO', 'CV_SCR1 (1 ano)': 'SCR1'
                              , 'CV_SCR2 (15 meses)': 'SCR2', 'Poprural': 'POPRURAL', 'PopUrb': 'POPURB'
                              , 'CoberturaAB': 'COBERTURA_AB'}, inplace=True)

    df['GP_SCR1'] = np.where(df['SCR1'] <= 50, 'Muito Baixa'
             , np.where(df['SCR1'] <= 95, 'Baixa'
                        , np.where(df['SCR1'] <= 120, 'Adequada', 'Elevada'
                                  )
                       )
            )

    df['GP_SCR2'] = np.where(df['SCR2'] <= 50, 'Muito Baixa'
             , np.where(df['SCR2'] <= 95, 'Baixa'
                        , np.where(df['SCR2'] <= 120, 'Adequada', 'Elevada'
                                  )
                       )
            )

    df_cidade_correto = pd.read_csv("./base/cidades_corretas.csv", sep='|')
    del df_cidade_correto['idx']

    df = pd.merge(df, df_cidade_correto, how = 'left', on = 'CODMUN7')
    df['MUNICIPIO'] = df['NOME_CIDADE']
    del df['NOME_CIDADE']

    df['UF'] = np.where(df['UF'] == 'acre', 'Acre'
                        , np.where(df['UF'] == 'amazonas', 'Amazonas', df['UF']))


    del df_cidade_correto
    return df