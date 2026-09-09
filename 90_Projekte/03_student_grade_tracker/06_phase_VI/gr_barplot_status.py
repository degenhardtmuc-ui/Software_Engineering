        gr.BarPlot(
            value=generate_pass_chart(),
            x="Status",
            y="Anzahl",
            color="Status",
            title="Bestanden und nicht bestanden",
            x_title="Status",
            y_title="Anzahl der Noten",
            y_lim=[0, 2],
            height=400,
        )