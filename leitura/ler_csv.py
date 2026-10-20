import pandas as pd

ARQUIVO_CSV = "Tabela_Matricula_2025_V2.csv"

REGIOES = ["Nordeste", "Sudeste"]


def ler_csv():
    for lote in pd.read_csv(
        ARQUIVO_CSV,
        sep=";",
        encoding="latin1",
        dtype=str,
        chunksize=50_000
    ):
        lote.columns = lote.columns.str.strip().str.upper()

        # Filtra diretamente pela região presente no CSV
        lote = lote[lote["NO_REGIAO"].isin(REGIOES)]

        if not lote.empty:
            yield lote