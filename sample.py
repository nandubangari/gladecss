#!/usr/bin/python
import gi , sys
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
from gi.repository import Gdk


abuilder=Gtk.Builder()
abuilder.add_from_file("c.glade")

ourForm1=abuilder.get_object("Form1")
css_provider = Gtk.CssProvider()
css_provider.load_from_path('my-blue-window.css')
Gtk.StyleContext.add_provider_for_screen(
    Gdk.Screen.get_default(),
    css_provider,
    Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
)
ourForm1.show()
Gtk.main()
