import socket
from kivymd.app import MDApp
KV="""
Screen:
    MDRaisedButton:
        name:"MDLabel"
        text:"MDLabel"
"""

            

class main(MDApp):
    def Build(self):
        self.theme_cls.primary_palette="Indigo"
        self.theme_cls.theme_style="Dark"
        return Builder.load_string(KV)
if __name__=="__main__":
    Host="127.0.0.1"
    Port=1025
    main().run()