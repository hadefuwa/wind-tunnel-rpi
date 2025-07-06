from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.metrics import dp
from kivy.animation import Animation

class ModernButton(Button):
    """
    A modern button with hover effects, shadows, and sleek styling.
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (0, 0, 0, 0)  # Transparent default background
        self.bind(state=self.on_state_change)
        self.create_background()
    
    def create_background(self):
        """Create modern button background with shadow"""
        with self.canvas.before:
            # Shadow
            Color(0, 0, 0, 0.3)
            self.shadow_rect = RoundedRectangle(
                size=(self.width + dp(6), self.height + dp(6)),
                pos=(self.x - dp(3), self.y - dp(3)),
                radius=[dp(15)]
            )
            
            # Main background
            Color(*self.button_color)
            self.bg_rect = RoundedRectangle(
                size=self.size,
                pos=self.pos,
                radius=[dp(12)]
            )
        
        self.bind(size=self.update_bg, pos=self.update_bg)
    
    def update_bg(self, *args):
        """Update background when size/position changes"""
        self.shadow_rect.size = (self.width + dp(6), self.height + dp(6))
        self.shadow_rect.pos = (self.x - dp(3), self.y - dp(3))
        self.bg_rect.size = self.size
        self.bg_rect.pos = self.pos
    
    def on_state_change(self, instance, value):
        """Handle button press animation"""
        if value == 'down':
            # Pressed state - darker color
            with self.canvas.before:
                Color(*[c * 0.8 for c in self.button_color])
                self.bg_rect = RoundedRectangle(
                    size=self.size,
                    pos=self.pos,
                    radius=[dp(12)]
                )
        else:
            # Normal state
            with self.canvas.before:
                Color(*self.button_color)
                self.bg_rect = RoundedRectangle(
                    size=self.size,
                    pos=self.pos,
                    radius=[dp(12)]
                )

class ModernModeScreen(Screen):
    """
    A beautiful, modern mode selection screen with professional styling,
    gradients, and sleek button designs.
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'mode_screen'
        
        # Modern color scheme
        self.bg_color = (0.08, 0.08, 0.12, 1)  # Deep dark blue
        self.accent_color = (0.2, 0.6, 1.0, 1)  # Modern blue
        self.success_color = (0.2, 0.8, 0.3, 1)  # Green
        self.danger_color = (1.0, 0.3, 0.3, 1)  # Red
        
        # Create gradient background
        with self.canvas.before:
            # Background gradient effect
            Color(*self.bg_color)
            self.bg_rect = Rectangle(size=self.size, pos=self.pos)
            
            # Overlay pattern for depth
            Color(0.1, 0.1, 0.15, 0.5)
            self.overlay_rect = Rectangle(size=self.size, pos=self.pos)
        
        self.bind(size=self.update_background, pos=self.update_background)
        
        # Create the main layout
        main_layout = BoxLayout(orientation='vertical', spacing=dp(40), padding=dp(50))
        
        # Header section with modern styling
        header_layout = BoxLayout(orientation='vertical', size_hint_y=0.4, spacing=dp(20))
        
        # Main title
        title_label = Label(
            text='WIND TUNNEL',
            font_size=dp(48),
            color=(1, 1, 1, 1),
            bold=True,
            size_hint_y=0.6
        )
        header_layout.add_widget(title_label)
        
        # Subtitle
        subtitle_label = Label(
            text='CONTROL SYSTEM',
            font_size=dp(32),
            color=self.accent_color,
            size_hint_y=0.4
        )
        header_layout.add_widget(subtitle_label)
        
        main_layout.add_widget(header_layout)
        
        # Status indicator
        status_layout = BoxLayout(orientation='horizontal', size_hint_y=0.1, spacing=dp(10))
        
        status_icon = Label(
            text='●',
            font_size=dp(20),
            color=self.success_color,
            size_hint_x=0.1
        )
        status_layout.add_widget(status_icon)
        
        status_text = Label(
            text='SYSTEM READY - SELECT OPERATION MODE',
            font_size=dp(16),
            color=(0.8, 0.8, 0.8, 1),
            size_hint_x=0.9
        )
        status_layout.add_widget(status_text)
        
        main_layout.add_widget(status_layout)
        
        # Button section
        button_layout = BoxLayout(orientation='vertical', spacing=dp(25), size_hint_y=0.4)
        
        # Simulation Mode button
        self.simulation_button = ModernButton(
            text='⚡ SIMULATION MODE',
            font_size=dp(24),
            color=(1, 1, 1, 1),
            bold=True,
            size_hint_y=0.5
        )
        self.simulation_button.button_color = self.success_color
        self.simulation_button.create_background()
        self.simulation_button.bind(on_press=self.start_simulation)
        button_layout.add_widget(self.simulation_button)
        
        # Exit button
        self.exit_button = ModernButton(
            text='⏻ EXIT SYSTEM',
            font_size=dp(24),
            color=(1, 1, 1, 1),
            bold=True,
            size_hint_y=0.5
        )
        self.exit_button.button_color = self.danger_color
        self.exit_button.create_background()
        self.exit_button.bind(on_press=self.exit_app)
        button_layout.add_widget(self.exit_button)
        
        main_layout.add_widget(button_layout)
        
        # Footer info
        info_layout = BoxLayout(orientation='vertical', size_hint_y=0.1, spacing=dp(5))
        
        info_label = Label(
            text='Touch buttons above to select mode • F11 for fullscreen',
            font_size=dp(14),
            color=(0.5, 0.5, 0.5, 1),
            size_hint_y=0.5
        )
        info_layout.add_widget(info_label)
        
        version_label = Label(
            text='v1.0 | Modern UI | Kivy Framework',
            font_size=dp(12),
            color=(0.4, 0.4, 0.4, 1),
            size_hint_y=0.5
        )
        info_layout.add_widget(version_label)
        
        main_layout.add_widget(info_layout)
        
        # Add everything to the screen
        self.add_widget(main_layout)
        
        print("Modern mode selection screen created with professional styling")
    
    def update_background(self, *args):
        """Update background when size changes"""
        self.bg_rect.size = self.size
        self.bg_rect.pos = self.pos
        self.overlay_rect.size = self.size
        self.overlay_rect.pos = self.pos
    
    def start_simulation(self, button):
        """Start simulation mode with modern transition"""
        print("User selected Simulation Mode")
        
        # Create a smooth transition effect
        anim = Animation(opacity=0.7, duration=0.1)
        anim.bind(on_complete=self.switch_to_dashboard)
        anim.start(button)
    
    def switch_to_dashboard(self, anim, widget):
        """Switch to dashboard after animation"""
        self.manager.current = 'dashboard'
        
        # Reset button opacity
        widget.opacity = 1.0
    
    def exit_app(self, button):
        """Exit the application with confirmation"""
        print("User selected Exit")
        
        # Animate button press
        anim = Animation(opacity=0.7, duration=0.1)
        anim.bind(on_complete=self.close_app)
        anim.start(button)
    
    def close_app(self, anim, widget):
        """Close the application"""
        from kivy.app import App
        App.get_running_app().stop() 