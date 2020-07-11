from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivymd.theming import ThemeManager
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivy.uix.camera import Camera
import pytesseract
from PIL import Image

# from kivy.core.window import Window
# Window.size=(400,700)

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
                    padding: 60
                    MDLabel:
                        text: 'homepage'
                        halign: 'center'
                    
                    MDFloatingActionButton:
                        icon: 'camera'
                        elevation_normal:12
                        pos_hint:{"center_x":0.9 }
                        md_bg_color: app.theme_cls.primary_color
                        theme_text_color: 'Custom'
                        text_color: [1,1,1,1]
                        size: (dp(70),dp(70))
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
'''


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class vPark(MDApp):

    def build(self):
        theme_cls = ThemeManager()
        return Builder.load_string(KV)

    def AccountPage(self):
        self.root.ids.screen_manager.current = 'account-page'

    def HomePage(self):
        self.root.ids.screen_manager.current = 'homepage'

    def OCR(self):
        cam = Camera()
        cam.export_to_png("IMG.png")
        #img = cv2.imread('image.png')
        #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.open('IMG.png')
        data = pytesseract.image_to_string(img)
        dia = MDDialog(text=data, size_hint=(0.7, 1), pos_hint={'center_x':0.5,'center_y':0.5})
        dia.open()


vPark().run()
