    with gr.Tab("SQLite-Datenbank"):
        table_selection = gr.Dropdown(
            choices=["students", "courses", "grades"],
            value="students",
            label="Tabelle auswählen",
        )

        load_button = gr.Button(
            "Tabelle laden",
            variant="primary",
        )

        database_output = gr.Dataframe(
            label="Datenbankinhalt",
            interactive=False,
        )

        export_button = gr.Button(
            "Als CSV exportieren"
        )

        export_output = gr.File(
            label="CSV-Datei herunterladen"
        )

        load_button.click(
            fn=load_table,
            inputs=table_selection,
            outputs=database_output,
        )

        export_button.click(
            fn=export_table_to_csv,
            inputs=table_selection,
            outputs=export_output,
        )