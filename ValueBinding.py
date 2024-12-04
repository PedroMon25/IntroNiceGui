from nicegui import ui

class Demo:
    def __init__(self):
        self.number = 1

demo = Demo()
v = ui.checkbox('visible', value=True)
with ui.column().bind_visibility_from(v, 'value'):
    ui.slider(min=1, max=6).bind_value(demo, 'number')
    ui.toggle({1: 'CONTABILIDAD', 2: 'PROGRAMACION', 3: 'PROBABILIDAD', 4:'CALCULO', 5:'QUIMICA'}).bind_value(demo, 'number')
    ui.number().bind_value(demo, 'number')

ui.run()
