
import os
 
import psycopg
from dotenv import load_dotenv
 
from leitura.ler_csv import ler_csv
from escrita.escrita_branco import gravar_no_banco
 
load_dotenv()
 
def main():
    total = 0
 
    with psycopg.connect(
        host=os.environ["DB_HOST"],
        port=os.environ["DB_PORT"],
        dbname=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
    ) as conexao:
        for lote in ler_csv():
            lote.columns = lote.columns.str.lower()
 
            quantidade = gravar_no_banco(conexao, lote)
            conexao.commit()
 
            total += quantidade
 
            print(f"Total de registros inseridos: {total}")
 
    print(f"registros: {total} ")
 
 
if __name__ == "__main__":
    main()
 