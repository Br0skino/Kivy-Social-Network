import socket
from kivymd.app import MDApp
from kivy.lang import Builder
Host="127.0.0.1"
Port=1025
KV="""
Screen:
    MDLabel:
        name:"MDLabel"
        text:"MDLabel"
    MDRaisedButton:
        text:"Connessione"
        on_press:app.connessione()
    MDLabel:
"""

class main(MDApp):
    def build(self):
        self.title="Hello Kivy"
        self.theme_cls.primary_palette="Indigo"
        self.theme_cls.theme_style="Light"
        return Builder.load_string(KV)
    def connessione(self):
        print("Connessione Inizializzata")
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
            s.connect((Host,Port))
            #s.sendall(b"Ciao")
            data=s.recv(1024)
            return data
main().run()
