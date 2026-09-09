#Erweiterung in with gr.Blocks(title="Student Grade Tracker") as app:
    current_student_id = gr.State("")
    current_role = gr.State("")

============================
with gr.Blocks(title="Student Grade Tracker") as app:
    current_student_id = gr.State("")
    current_role = gr.State("")

    with gr.Row():
========================
# gr.State ist ein unsichtbarer Speicher. Darin merkt sich Gradio die aktuelle Anmeldung.