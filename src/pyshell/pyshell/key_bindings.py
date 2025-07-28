from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.key_binding.key_processor import KeyPressEvent

bindings = KeyBindings()


@bindings.add("tab")
def _(event: KeyPressEvent):
    buffer = event.app.current_buffer

    if not buffer.complete_state:
        buffer.insert_text("    ")
    else:
        buffer.complete_next()
