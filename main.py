from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import get_color_from_hex
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDButton, MDButtonIcon, MDButtonText
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager

from screens import *
from screens.login import LoginScreen
from screens.menu import MenuScreen

Window.size = (400, 710)


class Example(MDApp):
    def build(self):
        sm = MDScreenManager()
        sm.add_widget(WelcomeScreen())
        sm.add_widget(LoginScreen())
        sm.add_widget(MenuScreen())
        sm.current = "menu"
        return sm


Example().run()



