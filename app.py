from kivy.app import App
from kivy.uix.button import Button

class myApp():
    def build(self):
        return Button(text = "MyApp")
myApp().run()