def update_report_inputs(report_type: str):
    """Show only the dropdown required for the selected report type."""

    if report_type == "Student":
        return (
            gr.update(visible=True),
            gr.update(visible=False),
        )

    if report_type == "Course":
        return (
            gr.update(visible=False),
            gr.update(visible=True),
        )

    return (
        gr.update(visible=False),
        gr.update(visible=False),
    )