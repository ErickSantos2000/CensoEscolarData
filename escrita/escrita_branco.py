import pandas as pd
import sqlite3

TABELA = "tb_instituicao_ensino"


def gravar_no_banco(conexao: sqlite3.Connection, lote: pd.DataFrame):
    colunas = [
        "no_entidade",
        "co_entidade",
        "no_uf",
        "sg_uf",
        "co_uf",
        "no_municipio",
        "co_municipio",
        "nu_ano_censo",
        "qt_mat_bas",
        "qt_mat_inf",
        "qt_mat_fund",
        "qt_mat_med",
        "qt_mat_prof",
        "qt_mat_eja",
        "qt_mat_esp",
    ]

    lote = lote[colunas]

    lote.to_sql(
        name=TABELA,
        con=conexao,
        if_exists="append",
        index=False
    )

    return len(lote)