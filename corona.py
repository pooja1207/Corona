from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen,WipeTransition
screen=ScreenManager(transition=WipeTransition())
class main_screen(App):
    title= "Corona-Virus Status App"
    def build_icon(self):
        return screen
