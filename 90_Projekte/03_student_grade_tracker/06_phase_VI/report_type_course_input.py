report_type_input.change(
    fn=update_report_inputs,
    inputs=report_type_input,
    outputs=[
        student_input,
        course_input,
    ],
)