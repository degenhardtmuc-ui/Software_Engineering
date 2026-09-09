import gradio as gr


def welcome(name: str) -> str:
    return f"Willkommen bei der Notenverwaltung, {name}!"


app = gr.Interface(
    fn=welcome,
    inputs=gr.Textbox(label="Name"),
    outputs=gr.Textbox(label="Ausgabe"),
    title="Student Grade Tracker",
)


if __name__ == "__main__":
    app.launch()