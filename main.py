#!/usr/bin/env python3
"""
Wind Tunnel Controller - Main Application
A modern Kivy app with professional graphics and beautiful circular gauges.

This is the main entry point - run this file to start the application.
"""

import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.config import Config

# Import our modern custom screens and simulator
from gui.modescreen import ModernModeScreen
from gui.dashboard import ModernDashboardScreen
from logic.simulator import WindTunnelSimulator

# Configure Kivy for better touchscreen and fullscreen experience
Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '800')
Config.set('graphics', 'resizable', True)

# Set minimum Kivy version
kivy.require('2.0.0')

class WindTunnelApp(App):
    """
    Main application class for the Wind Tunnel Controller.
    Now with modern, professional graphics and smooth animations.
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = 'Wind Tunnel Controller - Modern UI'
        
        # Create the data simulator
        self.simulator = WindTunnelSimulator()
        
        print("Modern Wind Tunnel App initialized")
    
    def build(self):
        """
        Build the modern app interface with professional styling.
        This is called automatically by Kivy when the app starts.
        """
        print("Building modern app interface...")
        
        # Create the screen manager to handle switching between screens
        screen_manager = ScreenManager()
        
        # Create the modern mode selection screen
        mode_screen = ModernModeScreen()
        screen_manager.add_widget(mode_screen)
        
        # Create the modern dashboard screen (pass the simulator to it)
        dashboard_screen = ModernDashboardScreen(self.simulator)
        screen_manager.add_widget(dashboard_screen)
        
        # Start with the mode selection screen
        screen_manager.current = 'mode_screen'
        
        # Set up window properties for better experience
        Window.clearcolor = (0.05, 0.05, 0.08, 1)  # Dark background
        
        print("Modern app interface built successfully")
        return screen_manager
    
    def on_start(self):
        """Called when the app starts running"""
        print("=== Modern Wind Tunnel Controller Started ===")
        print("Experience beautiful circular gauges and professional graphics")
        print("Touch the screen to interact • F11 for fullscreen")
        
        # Optional: Start in fullscreen mode (great for Pi and kiosks)
        # Window.fullscreen = True
    
    def on_stop(self):
        """Called when the app is closing"""
        print("=== Modern Wind Tunnel Controller Stopped ===")
        print("Thank you for using our professional control system!")

def main():
    """
    Main function to start the modern application.
    This is what gets called when you run: python main.py
    """
    print("Starting Modern Wind Tunnel Controller...")
    print("Professional graphics • Smooth animations • Modern UI")
    print("=" * 60)
    
    # Create and run the app
    app = WindTunnelApp()
    app.run()

if __name__ == '__main__':
    # This runs when the script is executed directly
    main() 