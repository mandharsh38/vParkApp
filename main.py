from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
import pytesseract
from PIL import Image
from kivymd.uix.dialog import MDDialog
#permissions for camera and storage
#plz comment these two lines to compile on desktop
#only for apk development:
#from android.permissions import request_permissions, Permission
#request_permissions([Permission.CAMERA,Permission.WRITE_EXTERNAL_STORAGE,Permission.READ_EXTERNAL_STORAGE])

# Builder string:
screen_helper = """
<ContentNavigationDrawer>:
    orientation:'vertical'
    Image:
        source:'logo.jpg'
    ScrollView:
        MDList:
            OneLineListItem:
                text: 'Home'                        
                on_release:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "home"
            OneLineListItem:
                text: 'Recent Vehicle Searches'                
                on_release: 
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = 'recent'
            OneLineListItem:
                text: 'Settings'                
                on_release: 
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = 'settings'                                    
            OneLineListItem:
                text: 'Help Center'
                on_release:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = 'help'                    
<HomeScreen>:
    name: "home"
    MDToolbar:
        pos_hint: {"top": 1}
        elevation: 10
        title: "vPark"
        left_action_items: [["menu", lambda x: root.nav_drawer.set_state("open")]]
        right_action_items: [["face", lambda x: app.ShowProfile()]]
    BoxLayout:
        orientation: 'vertical'
        MDLabel:
            text: 'Homepage'
            halign: 'center'
        MDRectangleFlatButton:
            text: 'Start Scanning:'
            pos_hint: {'center_x':.5,'center_y':.3}
            on_release:
                app.ShowCamera()
<ProfileScreen>:
    name: 'profile'
    MDToolbar:
        pos_hint: {"top": 1}
        elevation: 10
        title: "My Profile"
        left_action_items: [["menu", lambda x: root.nav_drawer.set_state("open")]]
        right_action_items: [['home', lambda x: app.ShowHome()]]
    BoxLayout:
        orientation: 'vertical'
        MDLabel:
            text: 'Profile'
            halign: 'center'
<RecentScreen>:
    name: 'recent'
    MDToolbar:
        pos_hint: {"top": 1}
        elevation: 10
        title: "Recent Searches"
        left_action_items: [["menu", lambda x: root.nav_drawer.set_state("open")]]
        right_action_items: [['home', lambda x: app.ShowHome()]]
    BoxLayout:
        orientation: 'vertical'
        MDLabel:
            text: 'Recent Searches'
            halign: 'center'
<HelpScreen>:
    name: 'help'
    MDToolbar:
        pos_hint: {"top": 1}
        elevation: 10
        title: "Help Centre"
        left_action_items: [["menu", lambda x: root.nav_drawer.set_state("open")]]
        right_action_items: [['home', lambda x: app.ShowHome()]]
    BoxLayout:
        orientation: 'vertical'
        MDLabel:
            text: 'Help Centre'
            halign: 'center'
<SettingsScreen>:
    name:'settings'
    MDToolbar:
        pos_hint: {"top": 1}
        elevation: 10
        title: "Settings"
        left_action_items: [["menu", lambda x: root.nav_drawer.set_state("open")]]
        right_action_items: [['home', lambda x: app.ShowHome()]]
    BoxLayout:
        orientation: 'vertical'
        MDLabel:
            text: 'Settings'
            halign: 'center'
NavigationLayout:
    ScreenManager:
        id: screen_manager
        HomeScreen:
            nav_drawer: nav_drawer
        ProfileScreen:
            nav_drawer: nav_drawer
        RecentScreen:
            nav_drawer: nav_drawer
        HelpScreen:
            nav_drawer: nav_drawer
        SettingsScreen:
            nav_drawer: nav_drawer
        Screen:
            name: 'camera'
            FloatLayout:
                Camera:
                    id: cam
                    
                    size_hint: (1,1)
                    pos_hint : {'center_y':0.5,'center_x':0.5}
                MDIconButton:
                    icon: 'camera'
                    text_color: app.theme_cls.primary_color
                    theme_text_color: 'Custom'
                    user_font_size : '40sp'
                    pos_hint : {'center_x':.85,'center_y':.08}
                    on_release:
                        app.OCR()
    MDNavigationDrawer:
        id: nav_drawer
        ContentNavigationDrawer:
            screen_manager: screen_manager
            nav_drawer: nav_drawer
"""


class HomeScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass


class RecentScreen(Screen):
    pass


class HelpScreen(Screen):
    pass


class SettingsScreen(Screen):
    pass


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


# Create the screen manager
sm = ScreenManager()
sm.add_widget(HomeScreen(name='home'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(RecentScreen(name='recent'))
sm.add_widget(HelpScreen(name='help'))

# Main function:
class vParkApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen

    # Functions to change screens:
    def ShowProfile(self):
        self.root.ids.screen_manager.current = 'profile'

    def ShowHome(self):
        self.root.ids.screen_manager.current = 'home'

    def ShowCamera(self):
        self.root.ids.screen_manager.current = 'camera'

    # Function for OCR (bare for now, needs optimisations, work on it after successful apk build)
    def OCR(self):
        # create a camera variable
        camera1 = self.root.ids['cam']
        # capture a shot and export to png
        camera1.export_to_png("IMG.png")
        # open image in PIL(basically storing image in a variable)
        # OCR using pytesseract stored in a variable named 'data'
        data = pytesseract.image_to_string(Image.open('IMG.png'))
        # Back to HomeScreen
        self.ShowHome()
        # Create a dialog to show the 'data' on screen and open the dialog
        self.dialog = MDDialog(text=data,
                               pos_hint={'center_x': 0.5, 'center_y': 0.5},
                               size_hint=(0.7, 1)
                               )
        self.dialog.open()


vParkApp().run()
