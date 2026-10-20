import sqlite3
from pathlib import Path

from leitura.ler_csv import ler_csv
from escrita.escrita_branco import gravar_no_banco

banco_dados = Path("/home/erick/atividade/censo-escolar/censoescolar.db")

def main():
    if not banco_dados.is_file():
        raise FileNotFoundError(
            f"Banco de dados não encontrado: {banco_dados.resolve()}"
        )

    total = 0

    with sqlite3.connect(banco_dados) as conexao:
        for lote in ler_csv():
            lote.columns = lote.columns.str.lower()

            quantidade = gravar_no_banco(conexao, lote)
            total += quantidade

            print(f"Total de registros inseridos: {total}")

    print(f"registros: {total} ")


if __name__ == "__main__":
    main()