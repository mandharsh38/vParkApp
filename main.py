from kivy.lang import Builder
from kivymd.app import MDApp

ScreenHelper = """
Screen:
    NavigationLayout:
    
        ScreenManager:
            id: screen_manager
            
            Screen:
            
                name: "homepage"
                
                BoxLayout:
                    orientation : 'vertical'
                    
                    MDToolbar:
                        title: 'vPark'
                        elevation: 10
                        left_action_items:[["menu",lambda x: root.ids.nav_drawer.toggle_nav_drawer()]]
                        right_action_items:[["face",lambda x: app.AccountPage()]]
                    

                    MDLabel:
                        text: 'Homepage'
                        halign: 'center'

            Screen:
                name: "account-page"
                BoxLayout:
                    orientation : 'vertical'
                    MDToolbar:
                        title: 'My Account'
                        elevation: 10
                        left_action_items:[["home",lambda x: app.HomePage()]]
                    MDLabel:
                        text: 'Account Page'
                        halign: 'center'

            Screen:
                name: "settings-page"
                BoxLayout:
                    orientation : 'vertical'
                    MDToolbar:
                        title: 'Settings'
                        elevation: 10
                        left_action_items:[["home",lambda x: app.HomePage()]]
                    MDLabel:
                        text: 'Settings Page'
                        halign: 'center'

            Screen:
                name: "recents-page"
                BoxLayout:
                    orientation : 'vertical'
                    MDToolbar:
                        title: 'Recent Searches'
                        elevation: 10
                        left_action_items:[["home",lambda x: app.HomePage()]]
                    MDLabel:
                        text: 'Recent Searches'
                        halign: 'center'

            Screen:
                name: "help-page"
                BoxLayout:
                    orientation : 'vertical'
                    MDToolbar:
                        title: 'Help Center'
                        elevation: 10
                        left_action_items:[["home",lambda x: app.HomePage()]]
                    MDLabel:
                        text: 'Help Centre'
                        halign: 'center'

        MDNavigationDrawer:
            id: nav_drawer
            
            BoxLayout:
                
                orientation:'vertical'
                
                Image:
                    source: 'logo-temp.png'
                
                ScrollView:
                    
                    MDList:
            
                        OneLineListItem:
                            text: 'Home'
                    
                    
                        
                            on_release:
                                root.ids.nav_drawer.set_state("close")
                                root.ids.screen_manager.current = "homepage"
                                            
                        OneLineListItem:
                            text: 'Recent Vehicle Searches'
                            
                            
                                
                            on_release: 
                                root.ids.nav_drawer.set_state("close")
                                root.ids.screen_manager.current = 'recents-page'
                                            
                        OneLineListItem:
                            text: 'Settings'
                            
                            
                                
                            on_release: 
                                root.ids.nav_drawer.set_state("close")
                                root.ids.screen_manager.current = 'settings-page'
                                            
                        OneLineListItem:
                            text: 'Help Center'
                            
                            
                                
                            on_release: 
                                root.ids.nav_drawer.set_state("close")
                                root.ids.screen_manager.current = 'help-page'                                    
"""


class vParkApp(MDApp):
    def build(self):
        screen = Builder.load_string(ScreenHelper)
        return screen

    def AccountPage(self):
        self.root.ids.screen_manager.current = 'account-page'

    def HomePage(self):
        self.root.ids.screen_manager.current = 'homepage'


vParkApp().run()
