#!/usr/bin/env python3
"""
Wind Tunnel Controller - Main Application
A simple Kivy app that displays simulated wind tunnel data with modern graphics.

This is the main entry point - run this file to start the application.
"""

import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.config import Config

# Import our custom screens and simulator
from gui.modescreen import ModeScreen
from gui.dashboard import DashboardScreen
from logic.simulator import WindTunnelSimulator

# Configure Kivy for better touchscreen and fullscreen experience
Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '600')
Config.set('graphics', 'resizable', True)

# Set minimum Kivy version
kivy.require('2.0.0')

class WindTunnelApp(App):
    """
    Main application class for the Wind Tunnel Controller.
    This is beginner-friendly - everything is clearly organized and commented.
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = 'Wind Tunnel Controller'
        
        # Create the data simulator
        self.simulator = WindTunnelSimulator()
        
        print("Wind Tunnel App initialized")
    
    def build(self):
        """
        Build the main app interface.
        This is called automatically by Kivy when the app starts.
        """
        print("Building app interface...")
        
        # Create the screen manager to handle switching between screens
        screen_manager = ScreenManager()
        
        # Create the mode selection screen
        mode_screen = ModeScreen()
        screen_manager.add_widget(mode_screen)
        
        # Create the dashboard screen (pass the simulator to it)
        dashboard_screen = DashboardScreen(self.simulator)
        screen_manager.add_widget(dashboard_screen)
        
        # Start with the mode selection screen
        screen_manager.current = 'mode_screen'
        
        # Set up window properties for better touchscreen experience
        Window.clearcolor = (0.1, 0.1, 0.1, 1)  # Dark gray background
        
        print("App interface built successfully")
        return screen_manager
    
    def on_start(self):
        """Called when the app starts running"""
        print("=== Wind Tunnel Controller Started ===")
        print("Touch the screen to interact with the app")
        print("Press F11 to toggle fullscreen (if supported)")
        
        # Optional: Start in fullscreen mode (good for Pi)
        # Window.fullscreen = True
    
    def on_stop(self):
        """Called when the app is closing"""
        print("=== Wind Tunnel Controller Stopped ===")
        print("Thank you for using the Wind Tunnel Controller!")

def main():
    """
    Main function to start the application.
    This is what gets called when you run: python main.py
    """
    print("Starting Wind Tunnel Controller...")
    print("Running in simulation mode with realistic fake data")
    print("=" * 50)
    
    # Create and run the app
    app = WindTunnelApp()
    app.run()

if __name__ == '__main__':
    # This runs when the script is executed directly
    main() 