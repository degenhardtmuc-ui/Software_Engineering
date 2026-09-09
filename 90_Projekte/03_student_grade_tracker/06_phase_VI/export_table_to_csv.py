def export_table_to_csv(table_name: str) -> str:
    """Export one permitted SQLite table as a CSV file."""

    if table_name not in ALLOWED_TABLES:
        raise gr.Error("Diese Tabelle darf nicht exportiert werden.")

    if not DATABASE_PATH.exists():
        raise gr.Error(f"Datenbank nicht gefunden: {DATABASE_PATH}")

    export_directory = DATABASE_PATH.parent / "exports"
    export_directory.mkdir(exist_ok=True)

    export_path = export_directory / f"{table_name}.csv"

    with sqlite3.connect(DATABASE_PATH) as connection:
        query = f"SELECT * FROM {table_name}"
        table_data = pd.read_sql_query(query, connection)

    table_data.to_csv(
        export_path,
        index=False,
        encoding="utf-8",
    )

    return str(export_path)