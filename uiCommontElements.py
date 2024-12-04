from nicegui import ui
from nicegui.events import ValueChangeEventArguments

def show(event: ValueChangeEventArguments):
    name = type(event.sender).__name__
    ui.notify(f'{name}: {event.value}')

ui.button('Haz clic aqui', on_click=lambda: ui.notify('clic'))
with ui.row():
    ui.checkbox('Terminos y condiciones', on_change=show)
    ui.switch('Activado/Desactivado', on_change=show)
ui.radio(['X', 'Y', 'Z'], value='X', on_change=show).props('line')
with ui.row():
    ui.input('Inserte un texto', on_change=show)
    ui.select(['Abierto', 'Cerrado'], value='Abierto', on_change=show)
ui.link('Para mas informacion...', '/documentation').classes('mt-8')

ui.run()