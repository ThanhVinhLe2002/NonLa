from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang import Builder

# Mobile-like window
Window.size = (360, 640)

# Custom tab container
class Tab(BoxLayout, MDTabsBase):
    pass

# Screens
class LoginScreen(MDScreen):
    pass

class MainScreen(MDScreen):
    pass

# App
class NonlaApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.primary_hue = "600"
        self.theme_cls.theme_style = "Light"

        sm = MDScreenManager()
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(MainScreen(name="menu"))
        sm.current = "login"
        return sm

# KV code
KV = '''
<LoginScreen>:
    MDFloatLayout:
        md_bg_color: 1, 0.9686, 0.8196, 1

        MDLabel:
            text: "NONLA"
            font_style: "H3"
            halign: "center"
            pos_hint: {"center_x": 0.5, "center_y": 0.7}
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 1

        MDFillRoundFlatButton:
            text: "Scan Table QR Code"
            pos_hint: {"center_x": 0.5, "center_y": 0.4}
            on_release: root.manager.current = "menu"

<MainScreen>:
    MDScreen:
        md_bg_color: 1, 0.9686, 0.8196, 1

        MDBottomNavigation:
            panel_color: 1, 1, 1, 1

            MDBottomNavigationItem:
                name: "home"
                text: "Home"
                icon: "home"

                BoxLayout:
                    orientation: "vertical"

                    MDBoxLayout:
                        orientation: "vertical"
                        size_hint_y: None
                        height: "136dp"
                        md_bg_color: 1, 0.9686, 0.8196, 1

                        MDTopAppBar:
                            title: "TABLE 1"
                            left_action_items: [["menu", lambda x: None]]
                            right_action_items: [["magnify", lambda x: None], ["account", lambda x: None]]
                            md_bg_color: 1, 0.5647, 0.2039, 1
                            specific_text_color: 0, 0, 0, 1

                        Image:
                            source: "logo.png"
                            size_hint: None, None
                            size: "72dp", "72dp"
                            pos_hint: {"center_x": 0.5}

                    MDTabs:
                        id: tabs
                        expand: True
                        background_color: 1, 0.5647, 0.2039, 1
                        text_color_active: 0, 0, 0, 1

                        Tab:
                            title: "Combo deals"

                            ScrollView:
                                MDBoxLayout:
                                    orientation: "vertical"
                                    padding: "10dp"
                                    spacing: "12dp"
                                    adaptive_height: True
                                    md_bg_color: 1, 0.9686, 0.8196, 1

                                    MDBoxLayout:
                                        orientation: "horizontal"
                                        spacing: "10dp"
                                        size_hint_y: None
                                        height: "100dp"

                                        Image:
                                            source: "combo.png"
                                            size_hint_x: 0.3

                                        MDBoxLayout:
                                            orientation: "vertical"
                                            spacing: "5dp"

                                            MDLabel:
                                                text: "Nonla Special Combo"
                                                bold: True
                                                theme_text_color: "Custom"
                                                text_color: 0.3, 0.2, 0, 1

                                            MDLabel:
                                                text: "Spring Rolls, Grilled Pork, Coffee"
                                                theme_text_color: "Secondary"

                                        MDLabel:
                                            text: "€15"
                                            halign: "right"
                                            size_hint_x: 0.2
                                            theme_text_color: "Primary"

                        Tab:
                            title: "Appetizer"

                            ScrollView:
                                MDBoxLayout:
                                    orientation: "vertical"
                                    padding: "10dp"
                                    spacing: "12dp"
                                    adaptive_height: True
                                    md_bg_color: 1, 0.9686, 0.8196, 1

                                    MDLabel:
                                        text: "Appetizer"
                                        bold: True
                                        font_style: "Subtitle2"
                                        theme_text_color: "Hint"

                                    MDBoxLayout:
                                        orientation: "horizontal"
                                        spacing: "10dp"
                                        size_hint_y: None
                                        height: "100dp"

                                        Image:
                                            source: "spring_rolls.png"
                                            size_hint_x: 0.3

                                        MDBoxLayout:
                                            orientation: "vertical"
                                            spacing: "4dp"

                                            MDLabel:
                                                text: "Spring Rolls"
                                                bold: True
                                                theme_text_color: "Custom"
                                                text_color: 0.3, 0.2, 0, 1

                                            MDLabel:
                                                text: "Fresh rice paper rolls with shrimp, herbs, and vermicelli"
                                                theme_text_color: "Secondary"

                                        MDLabel:
                                            text: "€6"
                                            halign: "right"
                                            size_hint_x: 0.2
                                            theme_text_color: "Primary"

                                    MDBoxLayout:
                                        orientation: "horizontal"
                                        spacing: "10dp"
                                        size_hint_y: None
                                        height: "100dp"

                                        Image:
                                            source: "wontons.png"
                                            size_hint_x: 0.3

                                        MDBoxLayout:
                                            orientation: "vertical"
                                            spacing: "4dp"

                                            MDLabel:
                                                text: "Fried Wontons"
                                                bold: True
                                                theme_text_color: "Custom"
                                                text_color: 0.3, 0.2, 0, 1

                                            MDLabel:
                                                text: "Crispy wontons filled with pork and shrimp - 6pcs"
                                                theme_text_color: "Secondary"

                                        MDLabel:
                                            text: "€7"
                                            halign: "right"
                                            size_hint_x: 0.2
                                            theme_text_color: "Primary"

                                    MDBoxLayout:
                                        orientation: "horizontal"
                                        spacing: "10dp"
                                        size_hint_y: None
                                        height: "100dp"

                                        Image:
                                            source: "papaya.png"
                                            size_hint_x: 0.3

                                        MDBoxLayout:
                                            orientation: "vertical"
                                            spacing: "4dp"

                                            MDLabel:
                                                text: "Green Papaya Salad"
                                                bold: True
                                                theme_text_color: "Custom"
                                                text_color: 0.3, 0.2, 0, 1

                                            MDLabel:
                                                text: "Shredded papaya with shrimp, peanuts, and tangy dressing"
                                                theme_text_color: "Secondary"

                                        MDLabel:
                                            text: "€7"
                                            halign: "right"
                                            size_hint_x: 0.2
                                            theme_text_color: "Primary"

                        Tab:
                            title: "Main dishes"

                            ScrollView:
                                MDBoxLayout:
                                    orientation: "vertical"
                                    padding: "10dp"
                                    spacing: "12dp"
                                    adaptive_height: True
                                    md_bg_color: 1, 0.9686, 0.8196, 1

                                    MDLabel:
                                        text: "Main dishes"
                                        bold: True
                                        font_style: "Subtitle2"
                                        theme_text_color: "Hint"

                                    MDBoxLayout:
                                        orientation: "horizontal"
                                        spacing: "10dp"
                                        size_hint_y: None
                                        height: "100dp"

                                        Image:
                                            source: "bun_bo_hue.png"
                                            size_hint_x: 0.3

                                        MDBoxLayout:
                                            orientation: "vertical"
                                            spacing: "4dp"

                                            MDLabel:
                                                text: "Bun Bo Hue"
                                                bold: True
                                                theme_text_color: "Custom"
                                                text_color: 0.3, 0.2, 0, 1

                                            MDLabel:
                                                text: "Spicy beef noodle soup with lemongrass and thick rice noodles"
                                                theme_text_color: "Secondary"

                                        MDLabel:
                                            text: "€11"
                                            halign: "right"
                                            size_hint_x: 0.2
                                            theme_text_color: "Primary"

                                    MDBoxLayout:
                                        orientation: "horizontal"
                                        spacing: "10dp"
                                        size_hint_y: None
                                        height: "100dp"

                                        Image:
                                            source: "grilled_pork_rice.png"
                                            size_hint_x: 0.3

                                        MDBoxLayout:
                                            orientation: "vertical"
                                            spacing: "4dp"

                                            MDLabel:
                                                text: "Grilled Pork Rice Plate"
                                                bold: True
                                                theme_text_color: "Custom"
                                                text_color: 0.3, 0.2, 0, 1

                                            MDLabel:
                                                text: "Broken rice served with grilled pork, egg, and fish sauce"
                                                theme_text_color: "Secondary"

                                        MDLabel:
                                            text: "€10"
                                            halign: "right"
                                            size_hint_x: 0.2
                                            theme_text_color: "Primary"

                                    MDBoxLayout:
                                        orientation: "horizontal"
                                        spacing: "10dp"
                                        size_hint_y: None
                                        height: "100dp"

                                        Image:
                                            source: "banh_mi.png"
                                            size_hint_x: 0.3

                                        MDBoxLayout:
                                            orientation: "vertical"
                                            spacing: "4dp"

                                            MDLabel:
                                                text: "Banh Mi Sandwich"
                                                bold: True
                                                theme_text_color: "Custom"
                                                text_color: 0.3, 0.2, 0, 1

                                            MDLabel:
                                                text: "Vietnamese baguette filled with grilled pork, pickled vegetables, and pâté"
                                                theme_text_color: "Secondary"

                                        MDLabel:
                                            text: "€7"
                                            halign: "right"
                                            size_hint_x: 0.2
                                            theme_text_color: "Primary"

                        Tab:
                            title: "Dessert"

                            ScrollView:
                                MDBoxLayout:
                                    orientation: "vertical"
                                    padding: "10dp"
                                    spacing: "12dp"
                                    adaptive_height: True
                                    md_bg_color: 1, 0.9686, 0.8196, 1

                                    MDLabel:
                                        text: "Desserts"
                                        bold: True
                                        font_style: "Subtitle2"
                                        theme_text_color: "Hint"

                                    MDBoxLayout:
                                        orientation: "horizontal"
                                        spacing: "10dp"
                                        size_hint_y: None
                                        height: "100dp"

                                        Image:
                                            source: "mango_sticky_rice.png"
                                            size_hint_x: 0.3

                                        MDBoxLayout:
                                            orientation: "vertical"
                                            spacing: "4dp"

                                            MDLabel:
                                                text: "Mango Sticky Rice"
                                                bold: True
                                                theme_text_color: "Custom"
                                                text_color: 0.3, 0.2, 0, 1

                                            MDLabel:
                                                text: "Sweet coconut-infused sticky rice served with fresh mango slices"
                                                theme_text_color: "Secondary"

                                        MDLabel:
                                            text: "€7"
                                            halign: "right"
                                            size_hint_x: 0.2
                                            theme_text_color: "Primary"

                                    MDBoxLayout:
                                        orientation: "horizontal"
                                        spacing: "10dp"
                                        size_hint_y: None
                                        height: "100dp"

                                        Image:
                                            source: "banana_sticky_rice.png"
                                            size_hint_x: 0.3

                                        MDBoxLayout:
                                            orientation: "vertical"
                                            spacing: "4dp"

                                            MDLabel:
                                                text: "Banana Sticky Rice"
                                                bold: True
                                                theme_text_color: "Custom"
                                                text_color: 0.3, 0.2, 0, 1

                                            MDLabel:
                                                text: "Grilled banana with sticky rice and coconut sauce"
                                                theme_text_color: "Secondary"

                                        MDLabel:
                                            text: "€6"
                                            halign: "right"
                                            size_hint_x: 0.2
                                            theme_text_color: "Primary"

                                    MDBoxLayout:
                                        orientation: "horizontal"
                                        spacing: "10dp"
                                        size_hint_y: None
                                        height: "100dp"

                                        Image:
                                            source: "che_ba_mau.png"
                                            size_hint_x: 0.3

                                        MDBoxLayout:
                                            orientation: "vertical"
                                            spacing: "4dp"

                                            MDLabel:
                                                text: "Che Ba Mau"
                                                bold: True
                                                theme_text_color: "Custom"
                                                text_color: 0.3, 0.2, 0, 1

                                            MDLabel:
                                                text: "Three-color sweet dessert with beans, jelly, and coconut milk"
                                                theme_text_color: "Secondary"

                                        MDLabel:
                                            text: "€6"
                                            halign: "right"
                                            size_hint_x: 0.2
                                            theme_text_color: "Primary"

                        Tab:
                            title: "Drinks"

                            ScrollView:
                                MDBoxLayout:
                                    orientation: "vertical"
                                    padding: "10dp"
                                    spacing: "12dp"
                                    adaptive_height: True
                                    md_bg_color: 1, 0.9686, 0.8196, 1

                                    MDLabel:
                                        text: "Drinks"
                                        bold: True
                                        font_style: "Subtitle2"
                                        theme_text_color: "Hint"

                                    MDBoxLayout:
                                        orientation: "horizontal"
                                        spacing: "10dp"
                                        size_hint_y: None
                                        height: "100dp"

                                        Image:
                                            source: "vietnamese_iced_coffee.png"
                                            size_hint_x: 0.3

                                        MDBoxLayout:
                                            orientation: "vertical"
                                            spacing: "4dp"

                                            MDLabel:
                                                text: "Vietnamese Iced Coffee"
                                                bold: True
                                                theme_text_color: "Custom"
                                                text_color: 0.3, 0.2, 0, 1

                                            MDLabel:
                                                text: "Strong coffee with condensed milk"
                                                theme_text_color: "Secondary"

                                        MDLabel:
                                            text: "€5"
                                            halign: "right"
                                            size_hint_x: 0.2
                                            theme_text_color: "Primary"

                                    MDBoxLayout:
                                        orientation: "horizontal"
                                        spacing: "10dp"
                                        size_hint_y: None
                                        height: "100dp"

                                        Image:
                                            source: "fresh_coconut_water.png"
                                            size_hint_x: 0.3

                                        MDBoxLayout:
                                            orientation: "vertical"
                                            spacing: "4dp"

                                            MDLabel:
                                                text: "Fresh Coconut Water"
                                                bold: True
                                                theme_text_color: "Custom"
                                                text_color: 0.3, 0.2, 0, 1

                                            MDLabel:
                                                text: "Served fresh from the coconut"
                                                theme_text_color: "Secondary"

                                        MDLabel:
                                            text: "€5"
                                            halign: "right"
                                            size_hint_x: 0.2
                                            theme_text_color: "Primary"

                                    MDBoxLayout:
                                        orientation: "horizontal"
                                        spacing: "10dp"
                                        size_hint_y: None
                                        height: "100dp"

                                        Image:
                                            source: "passion_fruit_juice.png"
                                            size_hint_x: 0.3

                                        MDBoxLayout:
                                            orientation: "vertical"
                                            spacing: "4dp"

                                            MDLabel:
                                                text: "Passion Fruit Juice"
                                                bold: True
                                                theme_text_color: "Custom"
                                                text_color: 0.3, 0.2, 0, 1

                                            MDLabel:
                                                text: "Refreshing passion fruit juice with honey"
                                                theme_text_color: "Secondary"

                                        MDLabel:
                                            text: "€5"
                                            halign: "right"
                                            size_hint_x: 0.2
                                            theme_text_color: "Primary"

            MDBottomNavigationItem:
                name: "bag"
                text: "Bag"
                icon: "shopping"

            MDBottomNavigationItem:
                name: "orders"
                text: "Orders"
                icon: "clipboard-list"

            MDBottomNavigationItem:
                name: "profile"
                text: "Profile"
                icon: "account"
'''

# Load UI and run
if __name__ == "__main__":
    Builder.load_string(KV)
    NonlaApp().run()
