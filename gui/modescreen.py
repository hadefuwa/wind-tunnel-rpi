"""
Material Design Mode Selection Screen
Optimized for 800x480 touchscreen with KivyMD components
"""

from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivymd.uix.toolbar import MDTopAppBar
from kivy.metrics import dp
from kivy.app import App

class MaterialModeScreen(MDScreen):
    """
    Material Design mode selection screen
    Optimized for 7" touchscreen (800x480)
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'mode_screen'
        
        # Create the layout
        self.create_layout()
        
        print("📱 Material Design mode screen created - 800×480 optimized")
    
    def create_layout(self):
        """Create the Material Design layout"""
        # Main container
        main_layout = MDBoxLayout(
            orientation='vertical',
            spacing=dp(16),
            adaptive_height=True,
            padding=dp(24)
        )
        
        # Header card
        header_card = self.create_header_card()
        main_layout.add_widget(header_card)
        
        # Buttons card
        buttons_card = self.create_buttons_card()
        main_layout.add_widget(buttons_card)
        
        # Footer info
        footer = self.create_footer()
        main_layout.add_widget(footer)
        
        self.add_widget(main_layout)
    
    def create_header_card(self):
        """Create header card with title and status"""
        card = MDCard(
            elevation=dp(4),
            size_hint_y=None,
            height=dp(120),
            padding=dp(16),
            radius=[dp(12)]
        )
        
        header_layout = MDBoxLayout(
            orientation='vertical',
            spacing=dp(8),
            adaptive_height=True
        )
        
        # Main title
        title = MDLabel(
            text="WIND TUNNEL CONTROL",
            theme_text_color="Primary",
            font_style="H4",
            size_hint_y=None,
            height=dp(40),
            halign="center"
        )
        header_layout.add_widget(title)
        
        # Subtitle
        subtitle = MDLabel(
            text="Professional Material Design Interface",
            theme_text_color="Secondary",
            font_style="Subtitle1",
            size_hint_y=None,
            height=dp(24),
            halign="center"
        )
        header_layout.add_widget(subtitle)
        
        # Status indicator
        status_layout = MDBoxLayout(
            orientation='horizontal',
            spacing=dp(8),
            adaptive_height=True,
            size_hint_y=None,
            height=dp(32)
        )
        
        # Status icon
        status_icon = MDIconButton(
            icon="circle",
            theme_icon_color="Custom",
            icon_color=(0, 1, 0, 1),  # Green
            size_hint_x=None,
            width=dp(32)
        )
        status_layout.add_widget(status_icon)
        
        # Status text
        status_text = MDLabel(
            text="SYSTEM READY - SELECT OPERATION MODE",
            theme_text_color="Primary",
            font_style="Body1",
            halign="left"
        )
        status_layout.add_widget(status_text)
        
        header_layout.add_widget(status_layout)
        card.add_widget(header_layout)
        
        return card
    
    def create_buttons_card(self):
        """Create buttons card with mode selection"""
        card = MDCard(
            elevation=dp(6),
            size_hint_y=None,
            height=dp(220),
            padding=dp(20),
            radius=[dp(12)]
        )
        
        buttons_layout = MDBoxLayout(
            orientation='vertical',
            spacing=dp(16),
            adaptive_height=True
        )
        
        # Simulation Mode Button
        simulation_button = MDRaisedButton(
            text="SIMULATION MODE",
            icon="flash",
            theme_icon_color="Custom",
            icon_color=(1, 1, 1, 1),
            md_bg_color=(0.2, 0.8, 0.3, 1),  # Green
            size_hint_y=None,
            height=dp(64),
            font_size=dp(18),
            elevation=dp(8)
        )
        simulation_button.bind(on_press=self.start_simulation)
        buttons_layout.add_widget(simulation_button)
        
        # Exit Button
        exit_button = MDRaisedButton(
            text="EXIT APPLICATION",
            icon="close-circle",
            theme_icon_color="Custom",
            icon_color=(1, 1, 1, 1),
            md_bg_color=(0.9, 0.3, 0.3, 1),  # Red
            size_hint_y=None,
            height=dp(64),
            font_size=dp(18),
            elevation=dp(8)
        )
        exit_button.bind(on_press=self.exit_app)
        buttons_layout.add_widget(exit_button)
        
        card.add_widget(buttons_layout)
        return card
    
    def create_footer(self):
        """Create footer with instructions"""
        footer_layout = MDBoxLayout(
            orientation='vertical',
            spacing=dp(4),
            adaptive_height=True,
            size_hint_y=None,
            height=dp(60)
        )
        
        # Instructions
        instructions = MDLabel(
            text="Touch buttons above to select mode • Optimized for 7\" touchscreen",
            theme_text_color="Hint",
            font_style="Caption",
            size_hint_y=None,
            height=dp(20),
            halign="center"
        )
        footer_layout.add_widget(instructions)
        
        # Version info
        version_info = MDLabel(
            text="Material Design UI • 800×480 Resolution • Touch-Friendly Controls",
            theme_text_color="Hint",
            font_style="Caption",
            size_hint_y=None,
            height=dp(20),
            halign="center"
        )
        footer_layout.add_widget(version_info)
        
        return footer_layout
    
    def start_simulation(self, button):
        """Start simulation mode"""
        print("📊 User selected Simulation Mode")
        self.manager.current = 'dashboard'
    
    def exit_app(self, button):
        """Exit the application"""
        print("🚪 User selected Exit")
        App.get_running_app().stop()
    
    def on_enter(self):
        """Called when entering the screen"""
        print("🏠 Material Design mode selection active")
    
    def on_leave(self):
        """Called when leaving the screen"""
        print("👋 Leaving mode selection screen") 