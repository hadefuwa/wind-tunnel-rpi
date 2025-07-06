from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

class ModeScreen(Screen):
    """
    Simple mode selection screen for the wind tunnel app.
    Shows big buttons for Simulation Mode and Exit.
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'mode_screen'
        
        # Create the main layout - everything stacked vertically
        main_layout = BoxLayout(orientation='vertical', spacing=20, padding=40)
        
        # Add the title
        title_label = Label(
            text='Wind Tunnel Controller',
            font_size=48,
            size_hint_y=0.3,
            color=(1, 1, 1, 1)  # White text
        )
        main_layout.add_widget(title_label)
        
        # Add subtitle
        subtitle_label = Label(
            text='Select Mode:',
            font_size=32,
            size_hint_y=0.2,
            color=(0.8, 0.8, 0.8, 1)  # Light gray text
        )
        main_layout.add_widget(subtitle_label)
        
        # Create container for buttons
        button_layout = BoxLayout(orientation='vertical', spacing=20, size_hint_y=0.4)
        
        # Simulation Mode button - big and green
        self.simulation_button = Button(
            text='Simulation Mode',
            font_size=36,
            size_hint_y=0.5,
            background_color=(0.2, 0.8, 0.2, 1),  # Green
            color=(1, 1, 1, 1)  # White text
        )
        self.simulation_button.bind(on_press=self.start_simulation)
        button_layout.add_widget(self.simulation_button)
        
        # Exit button - big and red
        self.exit_button = Button(
            text='Exit',
            font_size=36,
            size_hint_y=0.5,
            background_color=(0.8, 0.2, 0.2, 1),  # Red
            color=(1, 1, 1, 1)  # White text
        )
        self.exit_button.bind(on_press=self.exit_app)
        button_layout.add_widget(self.exit_button)
        
        main_layout.add_widget(button_layout)
        
        # Add info text at bottom
        info_label = Label(
            text='Touch the buttons above to make your selection',
            font_size=20,
            size_hint_y=0.1,
            color=(0.6, 0.6, 0.6, 1)  # Gray text
        )
        main_layout.add_widget(info_label)
        
        # Add everything to the screen
        self.add_widget(main_layout)
        
        print("Mode selection screen created")
    
    def start_simulation(self, button):
        """
        Called when user presses the Simulation Mode button.
        Switches to the dashboard screen.
        """
        print("User selected Simulation Mode")
        
        # Change the button color to show it was pressed
        button.background_color = (0.1, 0.6, 0.1, 1)  # Darker green
        
        # Switch to dashboard screen
        self.manager.current = 'dashboard'
        
        # Reset button color after a short delay
        from kivy.clock import Clock
        Clock.schedule_once(lambda dt: self.reset_button_color(button), 0.2)
    
    def exit_app(self, button):
        """
        Called when user presses the Exit button.
        Closes the application.
        """
        print("User selected Exit")
        
        # Change the button color to show it was pressed
        button.background_color = (0.6, 0.1, 0.1, 1)  # Darker red
        
        # Close the app
        from kivy.app import App
        App.get_running_app().stop()
    
    def reset_button_color(self, button):
        """Reset button color back to normal"""
        if button == self.simulation_button:
            button.background_color = (0.2, 0.8, 0.2, 1)  # Green
        elif button == self.exit_button:
            button.background_color = (0.8, 0.2, 0.2, 1)  # Red 