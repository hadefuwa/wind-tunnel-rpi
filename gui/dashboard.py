from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle, Line, Ellipse
from kivy.uix.widget import Widget

class SimpleGauge(Widget):
    """
    A simple visual gauge that shows a value with a colored bar.
    This is beginner-friendly - no complex graphics, just a simple bar.
    """
    
    def __init__(self, min_val=0, max_val=100, **kwargs):
        super().__init__(**kwargs)
        self.min_val = min_val
        self.max_val = max_val
        self.current_val = min_val
        self.gauge_color = (0.2, 0.8, 0.2, 1)  # Green by default
        
        # Set up the drawing
        with self.canvas:
            # Background bar (gray)
            Color(0.3, 0.3, 0.3, 1)
            self.bg_rect = Rectangle(pos=self.pos, size=self.size)
            
            # Value bar (colored)
            Color(*self.gauge_color)
            self.value_rect = Rectangle(pos=self.pos, size=(0, self.size[1]))
        
        # Update when widget size changes
        self.bind(pos=self.update_graphics, size=self.update_graphics)
    
    def update_graphics(self, *args):
        """Update the gauge graphics when size or position changes"""
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size
        self.value_rect.pos = self.pos
        self.update_value(self.current_val)
    
    def update_value(self, value):
        """Update the gauge to show a new value"""
        self.current_val = max(self.min_val, min(self.max_val, value))
        
        # Calculate how much of the bar to fill
        percentage = (self.current_val - self.min_val) / (self.max_val - self.min_val)
        bar_width = self.size[0] * percentage
        
        # Update the colored bar
        self.value_rect.size = (bar_width, self.size[1])
    
    def set_color(self, color):
        """Change the gauge color"""
        self.gauge_color = color
        with self.canvas:
            Color(*self.gauge_color)
            self.value_rect = Rectangle(pos=self.pos, size=self.value_rect.size)

class DashboardScreen(Screen):
    """
    Main dashboard screen that shows real-time wind tunnel data.
    Updates every 0.1 seconds (10 Hz) with fresh simulation data.
    """
    
    def __init__(self, simulator, **kwargs):
        super().__init__(**kwargs)
        self.name = 'dashboard'
        self.simulator = simulator
        
        # Create the main layout
        main_layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        
        # Title
        title_label = Label(
            text='Wind Tunnel Dashboard',
            font_size=36,
            size_hint_y=0.1,
            color=(1, 1, 1, 1)
        )
        main_layout.add_widget(title_label)
        
        # Create data display area
        data_layout = GridLayout(cols=1, spacing=20, size_hint_y=0.7)
        
        # Airspeed section
        airspeed_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=0.33)
        
        # Airspeed label and value
        airspeed_info = BoxLayout(orientation='vertical', size_hint_x=0.4)
        airspeed_info.add_widget(Label(text='Airspeed', font_size=24, color=(1, 1, 1, 1)))
        self.airspeed_label = Label(text='0.0 m/s', font_size=32, color=(0.2, 0.8, 0.2, 1))
        airspeed_info.add_widget(self.airspeed_label)
        airspeed_layout.add_widget(airspeed_info)
        
        # Airspeed gauge
        self.airspeed_gauge = SimpleGauge(min_val=0, max_val=40, size_hint_x=0.6)
        self.airspeed_gauge.set_color((0.2, 0.8, 0.2, 1))  # Green
        airspeed_layout.add_widget(self.airspeed_gauge)
        
        data_layout.add_widget(airspeed_layout)
        
        # Pressure section
        pressure_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=0.33)
        
        # Pressure label and value
        pressure_info = BoxLayout(orientation='vertical', size_hint_x=0.4)
        pressure_info.add_widget(Label(text='Pressure', font_size=24, color=(1, 1, 1, 1)))
        self.pressure_label = Label(text='0.0 hPa', font_size=32, color=(0.2, 0.2, 0.8, 1))
        pressure_info.add_widget(self.pressure_label)
        pressure_layout.add_widget(pressure_info)
        
        # Pressure gauge
        self.pressure_gauge = SimpleGauge(min_val=1000, max_val=1030, size_hint_x=0.6)
        self.pressure_gauge.set_color((0.2, 0.2, 0.8, 1))  # Blue
        pressure_layout.add_widget(self.pressure_gauge)
        
        data_layout.add_widget(pressure_layout)
        
        # Flow direction section
        flow_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=0.33)
        
        # Flow direction label and value
        flow_info = BoxLayout(orientation='vertical', size_hint_x=0.4)
        flow_info.add_widget(Label(text='Flow Direction', font_size=24, color=(1, 1, 1, 1)))
        self.flow_label = Label(text='0.0°', font_size=32, color=(0.8, 0.2, 0.8, 1))
        flow_info.add_widget(self.flow_label)
        flow_layout.add_widget(flow_info)
        
        # Flow direction gauge (-30 to +30 degrees)
        self.flow_gauge = SimpleGauge(min_val=-30, max_val=30, size_hint_x=0.6)
        self.flow_gauge.set_color((0.8, 0.2, 0.8, 1))  # Purple
        flow_layout.add_widget(self.flow_gauge)
        
        data_layout.add_widget(flow_layout)
        
        main_layout.add_widget(data_layout)
        
        # Control buttons
        button_layout = BoxLayout(orientation='horizontal', spacing=20, size_hint_y=0.15)
        
        # Back button
        back_button = Button(
            text='Back to Menu',
            font_size=24,
            size_hint_x=0.5,
            background_color=(0.5, 0.5, 0.5, 1),
            color=(1, 1, 1, 1)
        )
        back_button.bind(on_press=self.go_back)
        button_layout.add_widget(back_button)
        
        # Reset button
        reset_button = Button(
            text='Reset Data',
            font_size=24,
            size_hint_x=0.5,
            background_color=(0.8, 0.6, 0.2, 1),
            color=(1, 1, 1, 1)
        )
        reset_button.bind(on_press=self.reset_simulation)
        button_layout.add_widget(reset_button)
        
        main_layout.add_widget(button_layout)
        
        # Status info
        self.status_label = Label(
            text='Simulation running - data updates every 0.1 seconds',
            font_size=16,
            size_hint_y=0.05,
            color=(0.7, 0.7, 0.7, 1)
        )
        main_layout.add_widget(self.status_label)
        
        # Add everything to the screen
        self.add_widget(main_layout)
        
        # Start the data update timer
        self.update_event = None
        
        print("Dashboard screen created")
    
    def on_enter(self):
        """Called when this screen becomes active"""
        # Start updating data when screen becomes active
        self.update_event = Clock.schedule_interval(self.update_data, 0.1)  # 10 Hz
        print("Dashboard started - updating data every 0.1 seconds")
    
    def on_leave(self):
        """Called when leaving this screen"""
        # Stop updating data when screen is not active
        if self.update_event:
            self.update_event.cancel()
            self.update_event = None
        print("Dashboard stopped")
    
    def update_data(self, dt):
        """
        Update all the data displays with fresh simulation data.
        This is called 10 times per second.
        """
        # Get fresh data from the simulator
        data = self.simulator.get_all_data()
        
        # Update airspeed display
        airspeed = data['airspeed']
        self.airspeed_label.text = f'{airspeed:.1f} m/s'
        self.airspeed_gauge.update_value(airspeed)
        
        # Update pressure display
        pressure = data['pressure']
        self.pressure_label.text = f'{pressure:.1f} hPa'
        self.pressure_gauge.update_value(pressure)
        
        # Update flow direction display
        flow_direction = data['flow_direction']
        self.flow_label.text = f'{flow_direction:.1f}°'
        self.flow_gauge.update_value(flow_direction)
        
        # Update status
        runtime = data['timestamp']
        self.status_label.text = f'Simulation running - Runtime: {runtime:.1f} seconds'
    
    def go_back(self, button):
        """Go back to the mode selection screen"""
        print("User pressed Back button")
        self.manager.current = 'mode_screen'
    
    def reset_simulation(self, button):
        """Reset the simulation data"""
        print("User pressed Reset button")
        self.simulator.reset_simulation()
        self.status_label.text = 'Simulation reset - fresh data starting' 