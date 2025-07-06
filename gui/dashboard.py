from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle, Line, Ellipse, PushMatrix, PopMatrix, Rotate
from kivy.uix.widget import Widget
from kivy.graphics.instructions import InstructionGroup
from kivy.graphics.vertex_instructions import Triangle
from kivy.core.text import Label as CoreLabel
from kivy.metrics import dp
import math

class ModernCircularGauge(Widget):
    """
    A beautiful, modern circular gauge with gradients, shadows, and smooth animations.
    This creates a professional-looking gauge that would fit in any modern dashboard.
    """
    
    def __init__(self, min_val=0, max_val=100, gauge_color=(0.2, 0.8, 0.2, 1), 
                 title="", unit="", **kwargs):
        super().__init__(**kwargs)
        self.min_val = min_val
        self.max_val = max_val
        self.current_val = min_val
        self.gauge_color = gauge_color
        self.title = title
        self.unit = unit
        self.target_val = min_val  # For smooth animations
        
        # Colors for modern design
        self.bg_color = (0.1, 0.1, 0.1, 1)  # Dark background
        self.track_color = (0.2, 0.2, 0.2, 1)  # Dark track
        self.glow_color = (*gauge_color[:3], 0.3)  # Glowing effect
        
        # Create the gauge graphics
        self.create_gauge()
        
        # Bind size changes to redraw
        self.bind(size=self.update_gauge, pos=self.update_gauge)
        
        # Schedule smooth animation updates
        Clock.schedule_interval(self.animate_gauge, 1/60.0)  # 60 FPS
    
    def create_gauge(self):
        """Create the beautiful circular gauge with all visual elements"""
        with self.canvas:
            # Clear previous drawings
            self.canvas.clear()
            
            # Background circle with shadow effect
            Color(0.05, 0.05, 0.05, 0.8)  # Shadow
            self.shadow_circle = Ellipse(size=(0, 0), pos=(0, 0))
            
            # Background gradient effect
            Color(*self.bg_color)
            self.bg_circle = Ellipse(size=(0, 0), pos=(0, 0))
            
            # Track (background arc)
            Color(*self.track_color)
            self.track_arc = Line(width=dp(8))
            
            # Glow effect
            Color(*self.glow_color)
            self.glow_arc = Line(width=dp(15))
            
            # Main gauge arc
            Color(*self.gauge_color)
            self.gauge_arc = Line(width=dp(8))
            
            # Center dot
            Color(0.9, 0.9, 0.9, 1)
            self.center_dot = Ellipse(size=(dp(6), dp(6)), pos=(0, 0))
            
            # Value text background
            Color(0.15, 0.15, 0.15, 0.9)
            self.value_bg = Rectangle(size=(0, 0), pos=(0, 0))
        
        # Create text labels
        self.value_label = CoreLabel(text="0", font_size=dp(24), color=(1, 1, 1, 1))
        self.unit_label = CoreLabel(text=self.unit, font_size=dp(12), color=(0.8, 0.8, 0.8, 1))
        self.title_label = CoreLabel(text=self.title, font_size=dp(16), color=(0.9, 0.9, 0.9, 1))
        
        self.update_gauge()
    
    def update_gauge(self, *args):
        """Update the gauge visuals based on current size and position"""
        if self.size[0] <= 0 or self.size[1] <= 0:
            return
            
        # Calculate dimensions
        center_x = self.pos[0] + self.size[0] / 2
        center_y = self.pos[1] + self.size[1] / 2
        radius = min(self.size[0], self.size[1]) / 2 - dp(20)
        
        # Update shadow circle (slightly offset)
        self.shadow_circle.size = (radius * 2 + dp(6), radius * 2 + dp(6))
        self.shadow_circle.pos = (center_x - radius - dp(3), center_y - radius - dp(3))
        
        # Update background circle
        self.bg_circle.size = (radius * 2, radius * 2)
        self.bg_circle.pos = (center_x - radius, center_y - radius)
        
        # Update center dot
        self.center_dot.pos = (center_x - dp(3), center_y - dp(3))
        
        # Calculate arc parameters
        start_angle = 225  # Start at bottom-left
        sweep_angle = 270  # 3/4 circle
        
        # Create track arc (full background)
        track_points = []
        for i in range(int(sweep_angle) + 1):
            angle = math.radians(start_angle + i)
            x = center_x + (radius - dp(10)) * math.cos(angle)
            y = center_y + (radius - dp(10)) * math.sin(angle)
            track_points.extend([x, y])
        
        self.track_arc.points = track_points
        
        # Calculate gauge arc (current value)
        value_percentage = (self.current_val - self.min_val) / (self.max_val - self.min_val)
        value_angle = sweep_angle * value_percentage
        
        # Create glow arc (slightly wider)
        glow_points = []
        for i in range(int(value_angle) + 1):
            angle = math.radians(start_angle + i)
            x = center_x + (radius - dp(10)) * math.cos(angle)
            y = center_y + (radius - dp(10)) * math.sin(angle)
            glow_points.extend([x, y])
        
        self.glow_arc.points = glow_points
        
        # Create main gauge arc
        gauge_points = []
        for i in range(int(value_angle) + 1):
            angle = math.radians(start_angle + i)
            x = center_x + (radius - dp(10)) * math.cos(angle)
            y = center_y + (radius - dp(10)) * math.sin(angle)
            gauge_points.extend([x, y])
        
        self.gauge_arc.points = gauge_points
        
        # Update value background
        self.value_bg.size = (dp(80), dp(60))
        self.value_bg.pos = (center_x - dp(40), center_y - dp(30))
        
        # Update text labels
        self.value_label.text = f"{self.current_val:.1f}"
        self.value_label.refresh()
        self.unit_label.refresh()
        self.title_label.refresh()
    
    def animate_gauge(self, dt):
        """Smooth animation towards target value"""
        if abs(self.current_val - self.target_val) > 0.1:
            # Smooth interpolation
            self.current_val += (self.target_val - self.current_val) * 0.1
            self.update_gauge()
    
    def update_value(self, value):
        """Update the gauge to show a new value with smooth animation"""
        self.target_val = max(self.min_val, min(self.max_val, value))
    
    def set_color(self, color):
        """Change the gauge color"""
        self.gauge_color = color
        self.glow_color = (*color[:3], 0.3)
        self.create_gauge()

class ModernDashboardScreen(Screen):
    """
    A beautiful, modern dashboard with circular gauges, gradients, and professional styling.
    This looks like a high-end industrial control system.
    """
    
    def __init__(self, simulator, **kwargs):
        super().__init__(**kwargs)
        self.name = 'dashboard'
        self.simulator = simulator
        
        # Modern color scheme
        self.bg_color = (0.08, 0.08, 0.12, 1)  # Deep dark blue
        self.accent_color = (0.2, 0.6, 1.0, 1)  # Modern blue
        self.success_color = (0.2, 0.8, 0.3, 1)  # Green
        self.warning_color = (1.0, 0.6, 0.2, 1)  # Orange
        self.danger_color = (1.0, 0.3, 0.3, 1)  # Red
        
        # Create background
        with self.canvas.before:
            Color(*self.bg_color)
            self.bg_rect = Rectangle(size=self.size, pos=self.pos)
        
        self.bind(size=self.update_background, pos=self.update_background)
        
        # Create the main layout
        main_layout = BoxLayout(orientation='vertical', spacing=dp(20), padding=dp(30))
        
        # Header section
        header_layout = BoxLayout(orientation='horizontal', size_hint_y=0.15)
        
        # Title with modern styling
        title_label = Label(
            text='WIND TUNNEL CONTROL SYSTEM',
            font_size=dp(28),
            color=(1, 1, 1, 1),
            bold=True
        )
        header_layout.add_widget(title_label)
        
        # Status indicator
        self.status_label = Label(
            text='* SIMULATION ACTIVE',
            font_size=dp(16),
            color=self.success_color,
            size_hint_x=0.3
        )
        header_layout.add_widget(self.status_label)
        
        main_layout.add_widget(header_layout)
        
        # Gauges section
        gauges_layout = GridLayout(cols=3, spacing=dp(30), size_hint_y=0.6)
        
        # Airspeed gauge
        self.airspeed_gauge = ModernCircularGauge(
            min_val=0, max_val=40, 
            gauge_color=self.success_color,
            title="AIRSPEED",
            unit="m/s"
        )
        gauges_layout.add_widget(self.airspeed_gauge)
        
        # Pressure gauge
        self.pressure_gauge = ModernCircularGauge(
            min_val=1000, max_val=1030,
            gauge_color=self.accent_color,
            title="PRESSURE",
            unit="hPa"
        )
        gauges_layout.add_widget(self.pressure_gauge)
        
        # Flow direction gauge
        self.flow_gauge = ModernCircularGauge(
            min_val=-30, max_val=30,
            gauge_color=self.warning_color,
            title="FLOW DIR",
            unit="deg"
        )
        gauges_layout.add_widget(self.flow_gauge)
        
        main_layout.add_widget(gauges_layout)
        
        # Data display section
        data_layout = BoxLayout(orientation='horizontal', spacing=dp(20), size_hint_y=0.1)
        
        # Create modern data displays
        self.airspeed_display = self.create_data_display("AIRSPEED", "0.0 m/s", self.success_color)
        self.pressure_display = self.create_data_display("PRESSURE", "0.0 hPa", self.accent_color)
        self.flow_display = self.create_data_display("FLOW DIRECTION", "0.0°", self.warning_color)
        
        data_layout.add_widget(self.airspeed_display)
        data_layout.add_widget(self.pressure_display)
        data_layout.add_widget(self.flow_display)
        
        main_layout.add_widget(data_layout)
        
        # Control buttons
        button_layout = BoxLayout(orientation='horizontal', spacing=dp(20), size_hint_y=0.1)
        
        # Modern buttons
        back_button = self.create_modern_button("< BACK", self.go_back, (0.4, 0.4, 0.4, 1))
        reset_button = self.create_modern_button("O RESET", self.reset_simulation, self.accent_color)
        
        button_layout.add_widget(back_button)
        button_layout.add_widget(reset_button)
        
        main_layout.add_widget(button_layout)
        
        # Status bar
        self.status_bar = Label(
            text='System Ready | Data Update: 10 Hz | Runtime: 0.0s',
            font_size=dp(12),
            color=(0.7, 0.7, 0.7, 1),
            size_hint_y=0.05
        )
        main_layout.add_widget(self.status_bar)
        
        # Add everything to the screen
        self.add_widget(main_layout)
        
        # Update timer
        self.update_event = None
        
        print("Modern dashboard created with professional styling")
    
    def create_data_display(self, title, value, color):
        """Create a modern data display widget"""
        layout = BoxLayout(orientation='vertical', spacing=dp(5))
        
        # Title
        title_label = Label(
            text=title,
            font_size=dp(12),
            color=(0.8, 0.8, 0.8, 1),
            size_hint_y=0.4
        )
        layout.add_widget(title_label)
        
        # Value with background
        value_layout = BoxLayout(size_hint_y=0.6)
        value_label = Label(
            text=value,
            font_size=dp(18),
            color=color,
            bold=True
        )
        value_layout.add_widget(value_label)
        layout.add_widget(value_layout)
        
        # Store reference to value label for updates
        setattr(self, f"{title.lower().replace(' ', '_')}_value_label", value_label)
        
        return layout
    
    def create_modern_button(self, text, callback, color):
        """Create a modern button with styling"""
        button = Button(
            text=text,
            font_size=dp(16),
            background_color=color,
            color=(1, 1, 1, 1),
            size_hint_y=1
        )
        button.bind(on_press=callback)
        return button
    
    def update_background(self, *args):
        """Update background rectangle"""
        self.bg_rect.size = self.size
        self.bg_rect.pos = self.pos
    
    def on_enter(self):
        """Called when this screen becomes active"""
        self.update_event = Clock.schedule_interval(self.update_data, 0.1)  # 10 Hz
        self.status_label.text = '* SIMULATION ACTIVE'
        self.status_label.color = self.success_color
        print("Modern dashboard started - updating data every 0.1 seconds")
    
    def on_leave(self):
        """Called when leaving this screen"""
        if self.update_event:
            self.update_event.cancel()
            self.update_event = None
        self.status_label.text = '* SIMULATION PAUSED'
        self.status_label.color = self.warning_color
        print("Modern dashboard stopped")
    
    def update_data(self, dt):
        """Update all displays with fresh simulation data"""
        # Get fresh data
        data = self.simulator.get_all_data()
        
        # Update gauges with smooth animation
        self.airspeed_gauge.update_value(data['airspeed'])
        self.pressure_gauge.update_value(data['pressure'])
        self.flow_gauge.update_value(data['flow_direction'])
        
        # Update data displays
        self.airspeed_value_label.text = f"{data['airspeed']:.1f} m/s"
        self.pressure_value_label.text = f"{data['pressure']:.1f} hPa"
        self.flow_direction_value_label.text = f"{data['flow_direction']:.1f}°"
        
        # Update status bar
        runtime = data['timestamp']
        self.status_bar.text = f'System Active | Data Update: 10 Hz | Runtime: {runtime:.1f}s'
    
    def go_back(self, button):
        """Go back to mode selection"""
        print("User pressed Back button")
        self.manager.current = 'mode_screen'
    
    def reset_simulation(self, button):
        """Reset simulation data"""
        print("User pressed Reset button")
        self.simulator.reset_simulation()
        self.status_bar.text = 'System Reset | Fresh Data Starting' 