        gr.Markdown("### Bestehensverteilung")

        gr.BarPlot(
            value=generate_pass_chart(),
            x="Status",
            y="Anzahl",
            title="Bestanden und nicht bestanden",
            x_title="Status",
            y_title="Anzahl der Noten",
        )