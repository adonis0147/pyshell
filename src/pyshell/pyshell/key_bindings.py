from prompt_toolkit.key_binding import KeyBindings

bindings = KeyBindings()


@bindings.add("tab")
def _(event):
    buffer = event.app.current_buffer
    buffer.insert_text("    ")
