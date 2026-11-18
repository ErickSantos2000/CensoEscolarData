
import io
 
import pandas as pd
import psycopg
 
TABELA = "tb_instituicao_ensino"
 
 
def gravar_no_banco(conexao: psycopg.Connection, lote: pd.DataFrame):
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
 
    buffer = io.StringIO()
    lote.to_csv(buffer, index=False, header=False)
    
    comando = f"COPY {TABELA} ({', '.join(colunas)}) FROM STDIN WITH (FORMAT csv)"
 
    with conexao.cursor() as cursor:
        with cursor.copy(comando) as copy:
            copy.write(buffer.getvalue())
 
    return len(lote)
 