login_button.click(
    fn=login_from_form,
    inputs=[
        login_id_input,
        login_password_input,
    ],
    outputs=login_output,
)

================================

login_button.click(
    fn=login_from_form,
    inputs=[
        login_id_input,
        login_password_input,
    ],
    outputs=[
        login_output,
        current_student_id,
        current_role,
    ],
)