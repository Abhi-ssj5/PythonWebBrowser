#!/usr/bin/python3
import gi
gi.require_version('Gtk','3.0')
gi.require_version('WebKit2','4.0')
from gi.repository import Gtk
from gi.repository import WebKit2

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Web browser")
        self.set_default_size(1280, 720)

        header_bar = Gtk.HeaderBar()
        header_bar.set_show_close_button(True)
        header_bar.props.title = ">>>>> || <<<<<"
        self.set_titlebar(header_bar)

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(self.box)

        self.notebook = Gtk.Notebook()
        self.box.pack_start(self.notebook, True, True, 0)

        #first tab/ home page
        tab = Gtk.Box()

        #web view
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        view_box = Gtk.Box()
        self.webview = WebKit2.WebView()
        self.webview.show()
        view_box.pack_start(self.webview, True, True, 0)

        #url bar
        address_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
        #go backward
        self.backward_button = Gtk.Button()
        self.backward_button.add(Gtk.Arrow(Gtk.ArrowType.LEFT, Gtk.ShadowType.NONE))
        self.backward_button.connect("clicked", lambda x: self.webview.go_back())
        #go forward
        self.forward_button = Gtk.Button()
        self.forward_button.add(Gtk.Arrow(Gtk.ArrowType.RIGHT, Gtk.ShadowType.NONE))
        self.forward_button.connect("clicked", lambda x: self.webview.go_forward())
        #reload/load
        self.go_button = Gtk.Button(label="Go")
        self.go_button.connect("clicked",self._load_url)
        #url entry
        self.url_bar = Gtk.Entry()
        self.url_bar.set_text("Enter URL")
        self.url_bar.connect("activate", self._load_url)
        #adding items to address box
        address_box.add(self.backward_button)
        address_box.add(self.forward_button)
        address_box.add(self.go_button)
        address_box.pack_start(self.url_bar, True, True,0)

        #adding boxes
        main_box.add(address_box)
        main_box.pack_start(view_box, True, True, 0)
        tab.pack_start(main_box, True, True, 0)

        self.notebook.append_page(tab, Gtk.Label('Home'))
        print(self.notebook.get_n_pages())

        self.button = Gtk.Button(label='new tab')
        self.button.connect('clicked', self.on_button_clicked)
        header_bar.pack_end(self.button)


    def on_button_clicked(self, widget):
        numpage = self.notebook.get_n_pages() + 1
        #label = Gtk.Label(label='label{}'.format(numpage))
        #creating new tab
        label = Gtk.Label('new tab{}'.format(numpage))
        tab = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)

        #web view
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        view_box = Gtk.Box()
        self.webview = WebKit2.WebView()
        self.webview.show()
        view_box.pack_start(self.webview, True, True, 0)

        #url bar
        address_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
        self.backward_button = Gtk.Button()
        self.backward_button.add(Gtk.Arrow(Gtk.ArrowType.LEFT, Gtk.ShadowType.NONE))
        self.backward_button.connect("clicked", lambda x: self.webview.go_back())

        self.forward_button = Gtk.Button()
        self.forward_button.add(Gtk.Arrow(Gtk.ArrowType.RIGHT, Gtk.ShadowType.NONE))
        self.forward_button.connect("clicked", lambda x: self.webview.go_forward())

        self.go_button = Gtk.Button(label="Go")
        self.go_button.connect("clicked",self._load_url)

        self.url_bar = Gtk.Entry()
        self.url_bar.set_text("Enter URL")
        self.url_bar.connect("activate", self._load_url)

        self.close_button = Gtk.Button(label="close tab")
        self.close_button.connect("clicked",self._close_tab)

        address_box.add(self.backward_button)
        address_box.add(self.forward_button)
        address_box.add(self.go_button)
        address_box.pack_start(self.url_bar, True, True,0)
        address_box.add(self.close_button)

        #adding boxes
        main_box.add(address_box)
        main_box.pack_start(view_box, True, True, 0)
        tab.pack_start(main_box, True, True, 0)

        self.notebook.append_page(tab, label)
        print(self.notebook.get_n_pages())
        self.notebook.show_all()

    def _load_url(self, widget):
        print("loading............")
        url = self.url_bar.get_text()
        if not "://" in url:
            url = "http://"+url
        self.webview.load_uri(url)
        self.url_bar.set_text(url)

    def _close_tab(self, widget):
        page = self.notebook.get_current_page()
        self.notebook.remove_page(page)
        self.notebook.draw((0,0,-1,-1))


window = MainWindow()
window.connect('delete-event', Gtk.main_quit)
window.show_all()
Gtk.main()
