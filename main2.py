import socket
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.label import Label

from kivy.uix.screenmanager import Screen,ScreenManager
Host="127.0.0.1"
Port=1025
KV="""
ScreenManager:
    MainScreen:
    Screen2:
<MainScreen>:
    name:"main"
    MDRaisedButton:
        text:"Unisciti"
        pos_hint:{"center_x":0.5,"center_y":0.2}
        size_hint_x:0.5
        on_press:
            app.root.current="Screen2"
<Screen2>:
    name:"Screen2"

    MDRaisedButton:
        text:"Change MDLabel"
        on_press:root.changetext()
    MDLabel:
        id:MDLabel
        text:"MDLabel"
    MDTextField:
        id:MDTextField
        pos_hint:{"center_x":0.5,"center_y":0.5}
        size_hint_x:0.5
"""
class MainScreen(Screen):
    pass
class Screen2(Screen):

    def changetext(self):
        print("Connessione ricebuta")
        self.ids["MDLabel"].text="KivyMDLabel"
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
            s.bind((Host,Port))
            s.listen()
            conn,addr=s.accept()
            with conn:
                cmd=self.ids["MDTextField"].text
                print(cmd)
                print("Invio Dati")
                cmd=conn.sendall(b"Hello World")#Controlla Non Funziona il server non invia e non riceve,possibile problema per il client
                print(cmd)
                data=conn.recv(1024)
            if not data:
                print("Not Data")
            else:
                
                data=data.decode("utf-8")
                print(data)
                self.ids["MDLabel"].text=data
class ScreenManager(ScreenManager):
    pass

class main(MDApp):
    def build(self):
        self.title="Hello Kivy"
        self.theme_cls.theme_style="Light"
        self.theme_cls.primary_palette="Indigo"
        return Builder.load_string(KV)




main().run()
