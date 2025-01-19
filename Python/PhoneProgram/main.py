import kivy
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class MyApp(App):
    def build(self):
        main_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        self.solLabel = Label(text="Hello Dima", font_size=55)
        self.solInputText = TextInput(text="message", multiline=False, readonly=False, halign="left", font_size=55)
        self.solButtonSend = Button(text="Send")
        self.solButtonOnOff = Button(text="On/Off")
        
        self.solButtonSend.bind(on_press=self.send_func_butt)
        
        main_layout.add_widget(self.solLabel)
        main_layout.add_widget(self.solInputText)
        
        butt_layout = BoxLayout(orientation="horizontal")
        butt_layout.add_widget(self.solButtonSend)
        butt_layout.add_widget(self.solButtonOnOff)
        main_layout.add_widget(butt_layout)
        
        
        return main_layout
    
    def send_func_butt(self, stl):
        self.solLabel.text = self.solInputText.text
        
        



    


if __name__ == '__main__':
    MyApp().run()