from kivy.app import App
from kivy.uix.label import Label

class Lilit(App):
    def build(self):
        return Label(text='Lilit Sistemi Hazir\nSelam Isa!')

if __name__ == '__main__':
    Lilit().run()
