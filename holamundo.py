import gi

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk


class DemoApplicationWindow(Gtk.ApplicationWindow):

    def on_saludame(self, _):
        nombre = self.entry.get_text()
        saludo = f"Hola, {nombre}"
        self.display.set_label(saludo)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_title('Saludador')

        self.entry = Gtk.Entry()
        self.entry.set_placeholder_text('Pon tu nombre')
        self.entry.set_hexpand(True)
        self.entry.set_width_chars(10)

        self.button = Gtk.Button()
        self.button.set_label('Enviar')
        self.button.connect('clicked', self.on_saludame)
        self.button.add_css_class('suggested-action')

        self.display = Gtk.Label()
        self.display.set_label('Hola')

        horizontal = Gtk.Box()
        horizontal.set_orientation(Gtk.Orientation.HORIZONTAL)
        horizontal.set_spacing(10)
        horizontal.append(self.entry)
        horizontal.append(self.button)
        vertical = Gtk.Box()
        vertical.set_orientation(Gtk.Orientation.VERTICAL)
        vertical.set_spacing(10)
        vertical.append(horizontal)
        vertical.append(self.display)
        vertical.set_margin_top(10)
        vertical.set_margin_bottom(10)
        vertical.set_margin_start(10)
        vertical.set_margin_end(10)
        self.set_child(vertical)


class DemoApplication(Gtk.Application):

    def __init__(self, **kwargs):
        super().__init__(**kwargs, application_id = 'es.makigas.Ejemplo')

    def do_activate(self):
        win = DemoApplicationWindow(application=self)
        win.present()


app = DemoApplication()
app.run()
