#!/usr/bin/env python3
"""
Modern Wind Tunnel Controller Application
Professional Material Design interface with KivyMD for Raspberry Pi touchscreen
Screen Size: 800x480 (7" touchscreen)
"""

import os
import sys

# Set window size for 7" touchscreen BEFORE importing Kivy
os.environ['KIVY_WINDOW_WIDTH'] = '800'
os.environ['KIVY_WINDOW_HEIGHT'] = '480'

from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivy.core.window import Window
from kivy.logger import Logger

# Import our screens
from gui.modescreen import MaterialModeScreen
from gui.dashboard import MaterialDashboardScreen
from logic.simulator import WindTunnelSimulator

class ModernWindTunnelApp(MDApp):
    """
    Modern Wind Tunnel Controller with Material Design
    Optimized for 7" touchscreen (800x480)
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Wind Tunnel Controller - Material Design"
        self.theme_cls.theme_style = "Dark"  # Dark theme for professional look
        self.theme_cls.primary_palette = "Blue"  # Primary color
        self.theme_cls.accent_palette = "Green"  # Accent color
        
        # Set window properties for touchscreen
        Window.size = (800, 480)
        Window.minimum_width = 800
        Window.minimum_height = 480
        
        # Initialize simulator
        self.simulator = WindTunnelSimulator()
        
        print("🚀 Modern Wind Tunnel Controller - Material Design")
        print("📱 Optimized for 7\" touchscreen (800×480)")
        print("🎨 Professional Material Design UI")
        print("=" * 60)
    
    def build(self):
        """Build the application with Material Design components"""
        try:
            print("Building Material Design interface...")
            
            # Create screen manager
            screen_manager = MDScreenManager()
            
            # Create mode selection screen
            mode_screen = MaterialModeScreen(name='mode_screen')
            screen_manager.add_widget(mode_screen)
            
            # Create dashboard screen
            dashboard_screen = MaterialDashboardScreen(
                simulator=self.simulator,
                name='dashboard'
            )
            screen_manager.add_widget(dashboard_screen)
            
            print("✅ Material Design interface built successfully")
            print("🎯 Ready for professional wind tunnel control")
            print("👆 Touch interface optimized for 7\" screen")
            print("=" * 60)
            
            return screen_manager
            
        except Exception as e:
            print(f"❌ Error building interface: {e}")
            Logger.exception("Failed to build interface")
            return None
    
    def on_start(self):
        """Called when application starts"""
        print("🌟 === Material Design Wind Tunnel Controller Started ===")
        print("💫 Experience professional Material Design interface")
        print("📐 Perfect for 800×480 touchscreen • Optimized layouts")
        print("🎨 Dark theme • Touch-friendly controls • Smooth animations")
    
    def on_stop(self):
        """Called when application stops"""
        # Clean shutdown
        if hasattr(self, 'simulator'):
            self.simulator.stop_simulation()
        
        print("🛑 === Material Design Controller Stopped ===")
        print("🙏 Thank you for using our professional control system!")

def main():
    """Main application entry point"""
    try:
        # Create and run the app
        app = ModernWindTunnelApp()
        app.run()
        
    except KeyboardInterrupt:
        print("\n⚠️  Application interrupted by user")
    except Exception as e:
        print(f"💥 Critical error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main() 