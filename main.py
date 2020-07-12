from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivymd.theming import ThemeManager
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
import pytesseract
from PIL import Image


KV = '''
<ContentNavigationDrawer>:
    BoxLayout:
        orientation:'vertical'
        Image:
            source: 'logo-temp.png'
        ScrollView:
            MDList:
                OneLineListItem:
                    text: 'Home'                        
                    on_release:
                        root.nav_drawer.set_state("close")
                        root.screen_manager.current = "homepage"
                                                
                OneLineListItem:
                    text: 'Recent Vehicle Searches'                
                    on_release: 
                        root.nav_drawer.set_state("close")
                        root.screen_manager.current = 'recents-page'
                                                
                OneLineListItem:
                    text: 'Settings'                
                    on_release: 
                        root.nav_drawer.set_state("close")
                        root.screen_manager.current = 'settings-page'
                                                
                OneLineListItem:
                    text: 'Help Center'            
                    on_release: 
                        root.nav_drawer.set_state("close")
                        root.screen_manager.current = 'help-page'
Screen:
    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "vPark"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
        right_action_items: [["face", lambda x: app.AccountPage()]]
    
    
    NavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager
            Screen:
                name: "homepage"
                BoxLayout:
                    orientation:'vertical'
                    Camera:
                        id: camera
                        resolution: (3264, 2448)
                        play: True
                        size: self.size
                        size_hint: (1,1)
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
                            
                        
            Screen:
                name: "account-page"
                BoxLayout:
                    orientation : 'vertical'
                    MDLabel:
                        text: 'Account Page'
                        halign: 'center'
    
            Screen:
                name: "settings-page"
                BoxLayout:
                    orientation : 'vertical'
                    MDLabel:
                        text: 'Settings Page'
                        halign: 'center'
    
            Screen:
                name: "recents-page"
                BoxLayout:
                    orientation : 'vertical'
                    MDLabel:
                        text: 'Recent Searches'
                        halign: 'center'
    
            Screen:
                name: "help-page"
                BoxLayout:
                    orientation : 'vertical'
                    MDLabel:
                        text: 'Help Centre'
                        halign: 'center'
    
        MDNavigationDrawer:
            id: nav_drawer
            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
                camera: camera
'''


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
    Camera = ObjectProperty()


class vPark(MDApp):

    def build(self):
        theme_cls = ThemeManager()
        theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)

    def AccountPage(self):
        self.root.ids.screen_manager.current = 'account-page'

    def HomePage(self):
        self.root.ids.screen_manager.current = 'homepage'

    def OCR(self):
        cam = self.root.ids['camera']
        cam.export_to_png("IMG.png")
        img = Image.open('IMG.png')
        data = pytesseract.image_to_string(img)
        self.dialog = MDDialog(text=data,
                               pos_hint={'center_x': 0.5, 'center_y': 0.5},
                               size_hint=(0.7, 1)
                               )
        self.dialog.open()


vPark().run()