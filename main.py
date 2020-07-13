from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

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
        orientation:'vertical'
        Camera:
            id: camera
            resolution: (3264, 2448)
            play: True
            pos_hint : {'center_y':0.5,'center_x':0.5}
    FloatLayout:
        MDIconButton:
            icon: 'camera'
            text_color: app.theme_cls.primary_color
            theme_text_color: 'Custom'
            user_font_size : '40sp'
            pos_hint : {'center_x':.85,'center_y':.08}
            on_release:
                app.OCR()    
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

    MDNavigationDrawer:
        id: nav_drawer
        ContentNavigationDrawer:
            screen_manager: screen_manager
            nav_drawer: nav_drawer

"""


class HomeScreen(Screen):
    pass


class ProfileScreen(Screen):
    nav_drawer = ObjectProperty()


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


class vParkApp(MDApp):
    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen

    def ShowProfile(self):
        self.root.ids.screen_manager.current = 'profile'

    def ShowHome(self):
        self.root.ids.screen_manager.current = 'home'



    def OCR(self):
        pass
#        cam = self.root.ids['camera']
#        cam.export_to_png("IMG.png")
#        img = Image.open('IMG.png')
#        data = pytesseract.image_to_string(img)
#        self.dialog = MDDialog(text=data,
#                               pos_hint={'center_x': 0.5, 'center_y': 0.5},
#                               size_hint=(0.7, 1)
#                               )
#        self.dialog.open()


vParkApp().run()
