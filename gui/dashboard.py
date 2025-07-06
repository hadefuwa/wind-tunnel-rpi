"""
Material Design Dashboard Screen
Professional wind tunnel control interface with KivyMD
Optimized for 800x480 touchscreen
"""

from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.progressbar import MDProgressBar
from kivymd.uix.chip import MDChip
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line, Ellipse, Rectangle, PushMatrix, PopMatrix, Rotate
from kivy.core.text import Label as CoreLabel
from kivy.metrics import dp
from kivy.clock import Clock
from kivy.app import App
import math

class MaterialCircularGauge(Widget):
    """
    Material Design circular gauge widget
    Optimized for touchscreen visibility
    """
    
    def __init__(self, min_val=0, max_val=100, gauge_color=(0.2, 0.6, 1.0, 1), 
                 title="", unit="", **kwargs):
        super().__init__(**kwargs)
        self.min_val = min_val
        self.max_val = max_val
        self.current_val = min_val
        self.target_val = min_val
        self.gauge_color = gauge_color
        self.title = title
        self.unit = unit
        
        # Material Design colors
        self.track_color = (0.3, 0.3, 0.3, 0.3)
        self.bg_color = (0.1, 0.1, 0.1, 0.8)
        
        # Create gauge
        self.bind(size=self.update_gauge, pos=self.update_gauge)
        Clock.schedule_interval(self.animate_gauge, 1/60.0)
        
        # Create labels
        self.create_labels()
        Clock.schedule_once(self.update_gauge, 0.1)
    
    def create_labels(self):
        """Create labels for value display"""
        # Value label - Make it white and larger
        self.value_label = MDLabel(
            text=f"{self.current_val:.1f}",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),  # White text
            font_style="H5",
            size_hint=(None, None),
            height=dp(40),
            width=dp(120),
            halign="center"
        )
        self.add_widget(self.value_label)
        
        # Unit label - Make it light gray and visible
        if self.unit:
            self.unit_label = MDLabel(
                text=self.unit,
                theme_text_color="Custom",
                text_color=(0.8, 0.8, 0.8, 1),  # Light gray text
                font_style="Caption",
                size_hint=(None, None),
                height=dp(20),
                width=dp(80),
                halign="center"
            )
            self.add_widget(self.unit_label)
        
        # Title label - Make it white and visible
        if self.title:
            self.title_label = MDLabel(
                text=self.title,
                theme_text_color="Custom",
                text_color=(1, 1, 1, 1),  # White text
                font_style="Subtitle2",
                size_hint=(None, None),
                height=dp(24),
                width=dp(120),
                halign="center"
            )
            self.add_widget(self.title_label)
    
    def update_gauge(self, *args):
        """Update gauge graphics"""
        self.canvas.clear()
        
        if self.size[0] <= 0 or self.size[1] <= 0:
            return
            
        center_x = self.pos[0] + self.size[0] / 2
        center_y = self.pos[1] + self.size[1] / 2
        radius = min(self.size[0], self.size[1]) * 0.35  # Good size for touchscreen
        
        if radius <= 0:
            return
        
        with self.canvas:
            # Background circle
            Color(*self.bg_color)
            Ellipse(pos=(center_x - radius, center_y - radius), 
                   size=(radius * 2, radius * 2))
            
            # Track circle
            Color(*self.track_color)
            Line(circle=(center_x, center_y, radius * 0.9), width=dp(8))
            
            # Progress arc
            if self.max_val != self.min_val:
                value_percentage = (self.current_val - self.min_val) / (self.max_val - self.min_val)
                value_percentage = max(0, min(1, value_percentage))
                
                # Draw arc
                Color(*self.gauge_color)
                start_angle = 135
                sweep_angle = 270 * value_percentage
                
                # Create arc points
                arc_points = []
                steps = max(int(sweep_angle), 1)
                for i in range(steps + 1):
                    angle = math.radians(start_angle + (sweep_angle * i / steps))
                    x = center_x + (radius * 0.9) * math.cos(angle)
                    y = center_y + (radius * 0.9) * math.sin(angle)
                    arc_points.extend([x, y])
                
                if len(arc_points) > 2:
                    Line(points=arc_points, width=dp(12))
        
        # Update label positions
        self.update_label_positions(center_x, center_y, radius)
    
    def update_label_positions(self, center_x, center_y, radius):
        """Update label positions"""
        if hasattr(self, 'value_label'):
            self.value_label.text = f"{self.current_val:.1f}"
            self.value_label.center_x = center_x
            self.value_label.center_y = center_y
        
        if hasattr(self, 'unit_label'):
            self.unit_label.center_x = center_x
            self.unit_label.center_y = center_y - dp(25)
        
        if hasattr(self, 'title_label'):
            self.title_label.center_x = center_x
            self.title_label.center_y = center_y + radius + dp(15)
    
    def animate_gauge(self, dt):
        """Smooth animation"""
        if abs(self.current_val - self.target_val) > 0.1:
            self.current_val += (self.target_val - self.current_val) * 0.15
            self.update_gauge()
    
    def update_value(self, value):
        """Update target value"""
        self.target_val = max(self.min_val, min(self.max_val, value))

class MaterialSpeedGauge(Widget):
    """
    Material Design speed gauge with colored bands
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_speed = 0
        self.max_speed = 60  # MPH
        self.bind(size=self.update_gauge, pos=self.update_gauge)
        
        # Create speed label - Make it white and visible
        self.speed_label = MDLabel(
            text="0.0 MPH",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),  # White text
            font_style="H4",
            size_hint=(None, None),
            height=dp(48),
            width=dp(150),
            halign="center"
        )
        self.add_widget(self.speed_label)
        
    def update_gauge(self, *args):
        """Draw speed gauge with colored bands"""
        self.canvas.clear()
        
        if self.size[0] <= 0 or self.size[1] <= 0:
            return
            
        center_x = self.pos[0] + self.size[0] / 2
        center_y = self.pos[1] + self.size[1] / 2
        radius = min(self.size[0], self.size[1]) * 0.4
        
        if radius <= 0:
            return
        
        with self.canvas:
            # Background
            Color(0.1, 0.1, 0.1, 0.8)
            Ellipse(pos=(center_x - radius, center_y - radius), 
                   size=(radius * 2, radius * 2))
            
            # Speed bands
            start_angle = 180
            sweep_angle = 180
            line_width = dp(20)
            
            # Blue band (0-20 MPH)
            Color(0.3, 0.6, 1.0, 0.8)
            blue_points = []
            for i in range(int(sweep_angle * 0.33) + 1):
                angle = math.radians(start_angle + i)
                x = center_x + radius * math.cos(angle)
                y = center_y + radius * math.sin(angle)
                blue_points.extend([x, y])
            if len(blue_points) > 2:
                Line(points=blue_points, width=line_width)
            
            # Green band (20-40 MPH)
            Color(0.3, 0.8, 0.3, 0.8)
            green_points = []
            for i in range(int(sweep_angle * 0.33), int(sweep_angle * 0.67) + 1):
                angle = math.radians(start_angle + i)
                x = center_x + radius * math.cos(angle)
                y = center_y + radius * math.sin(angle)
                green_points.extend([x, y])
            if len(green_points) > 2:
                Line(points=green_points, width=line_width)
            
            # Red band (40-60 MPH)
            Color(1.0, 0.4, 0.4, 0.8)
            red_points = []
            for i in range(int(sweep_angle * 0.67), int(sweep_angle) + 1):
                angle = math.radians(start_angle + i)
                x = center_x + radius * math.cos(angle)
                y = center_y + radius * math.sin(angle)
                red_points.extend([x, y])
            if len(red_points) > 2:
                Line(points=red_points, width=line_width)
            
            # Speed indicator
            speed_percentage = min(self.current_speed / self.max_speed, 1.0)
            marker_angle = math.radians(start_angle + sweep_angle * speed_percentage)
            
            # Marker line
            Color(1, 1, 1, 1)
            marker_x = center_x + radius * math.cos(marker_angle)
            marker_y = center_y + radius * math.sin(marker_angle)
            Line(points=[center_x, center_y, marker_x, marker_y], width=dp(4))
            
            # Marker dot
            Color(1, 1, 0, 1)
            Ellipse(pos=(marker_x - dp(6), marker_y - dp(6)), size=(dp(12), dp(12)))
        
        # Update speed label
        if hasattr(self, 'speed_label'):
            self.speed_label.text = f"{self.current_speed:.1f} MPH"
            self.speed_label.center_x = center_x
            self.speed_label.center_y = center_y - radius/4
    
    def update_speed(self, speed):
        """Update displayed speed"""
        self.current_speed = speed
        self.update_gauge()

class MaterialDashboardScreen(MDScreen):
    """
    Material Design dashboard screen
    Optimized for 800x480 touchscreen
    """
    
    def __init__(self, simulator, **kwargs):
        super().__init__(**kwargs)
        self.name = 'dashboard'
        self.simulator = simulator
        
        # Create layout
        self.create_layout()
        
        # Update timer
        self.update_event = None
        print("📊 Material Design dashboard created - 800×480 optimized")
    
    def create_layout(self):
        """Create Material Design dashboard layout"""
        # Main container
        main_layout = MDBoxLayout(
            orientation='vertical',
            spacing=dp(8),
            padding=dp(12)
        )
        
        # Top toolbar
        toolbar = self.create_toolbar()
        toolbar.size_hint_y = None
        toolbar.height = dp(56)
        main_layout.add_widget(toolbar)
        
        # Main content area
        content_layout = MDBoxLayout(
            orientation='horizontal',
            spacing=dp(12),
            size_hint_y=0.85
        )
        
        # Left panel - Speed gauge
        left_panel = self.create_left_panel()
        left_panel.size_hint_x = 0.3
        content_layout.add_widget(left_panel)
        
        # Center panel - Gauges
        center_panel = self.create_center_panel()
        center_panel.size_hint_x = 0.45
        content_layout.add_widget(center_panel)
        
        # Right panel - Controls
        right_panel = self.create_right_panel()
        right_panel.size_hint_x = 0.25
        content_layout.add_widget(right_panel)
        
        main_layout.add_widget(content_layout)
        
        # Bottom controls
        bottom_controls = self.create_bottom_controls()
        bottom_controls.size_hint_y = None
        bottom_controls.height = dp(64)
        main_layout.add_widget(bottom_controls)
        
        self.add_widget(main_layout)
    
    def create_toolbar(self):
        """Create top toolbar"""
        toolbar = MDTopAppBar(
            title="Wind Tunnel Control",
            left_action_items=[["menu", lambda x: None]],
            right_action_items=[
                ["circle", lambda x: None],
                ["information", lambda x: None]
            ],
            elevation=dp(4)
        )
        return toolbar
    
    def create_left_panel(self):
        """Create left panel with speed gauge"""
        card = MDCard(
            elevation=dp(4),
            padding=dp(16),
            radius=[dp(8)]
        )
        
        panel_layout = MDBoxLayout(
            orientation='vertical',
            spacing=dp(12)
        )
        
        # Title - Make it white and visible
        title = MDLabel(
            text="AIRSPEED",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),  # White text
            font_style="H6",
            size_hint_y=None,
            height=dp(32),
            halign="center"
        )
        panel_layout.add_widget(title)
        
        # Speed gauge
        self.speed_gauge = MaterialSpeedGauge()
        panel_layout.add_widget(self.speed_gauge)
        
        # Fan controls
        fan_layout = MDBoxLayout(
            orientation='vertical',
            spacing=dp(8),
            size_hint_y=None,
            height=dp(120)
        )
        
        # Fan speed label - Make it white and visible
        self.fan_speed_label = MDLabel(
            text="50%",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),  # White text
            font_style="H5",
            size_hint_y=None,
            height=dp(32),
            halign="center"
        )
        fan_layout.add_widget(self.fan_speed_label)
        
        # Fan control buttons
        fan_buttons = MDBoxLayout(
            orientation='horizontal',
            spacing=dp(8),
            size_hint_y=None,
            height=dp(40)
        )
        
        fan_minus = MDIconButton(
            icon="minus",
            theme_icon_color="Custom",
            icon_color=(1, 1, 1, 1),
            md_bg_color=(0.9, 0.3, 0.3, 1)
        )
        fan_minus.bind(on_press=self.decrease_fan_speed)
        fan_buttons.add_widget(fan_minus)
        
        fan_plus = MDIconButton(
            icon="plus",
            theme_icon_color="Custom",
            icon_color=(1, 1, 1, 1),
            md_bg_color=(0.2, 0.8, 0.3, 1)
        )
        fan_plus.bind(on_press=self.increase_fan_speed)
        fan_buttons.add_widget(fan_plus)
        
        fan_layout.add_widget(fan_buttons)
        panel_layout.add_widget(fan_layout)
        
        card.add_widget(panel_layout)
        return card
    
    def create_center_panel(self):
        """Create center panel with gauges"""
        card = MDCard(
            elevation=dp(4),
            padding=dp(12),
            radius=[dp(8)]
        )
        
        gauges_grid = MDGridLayout(
            cols=2,
            spacing=dp(8)
        )
        
        # Pressure gauges
        self.static_pressure_gauge = MaterialCircularGauge(
            min_val=1000, max_val=1030,
            gauge_color=(0.2, 0.6, 1.0, 1),
            title="STATIC P",
            unit="hPa"
        )
        gauges_grid.add_widget(self.static_pressure_gauge)
        
        self.dynamic_pressure_gauge = MaterialCircularGauge(
            min_val=1000, max_val=1030,
            gauge_color=(1.0, 0.6, 0.2, 1),
            title="DYNAMIC P",
            unit="hPa"
        )
        gauges_grid.add_widget(self.dynamic_pressure_gauge)
        
        # Angle of Attack
        self.aoa_gauge = MaterialCircularGauge(
            min_val=-20, max_val=20,
            gauge_color=(0.2, 0.8, 0.3, 1),
            title="AOA",
            unit="deg"
        )
        gauges_grid.add_widget(self.aoa_gauge)
        
        # Fan output
        self.fan_output_gauge = MaterialCircularGauge(
            min_val=0, max_val=100,
            gauge_color=(0.2, 0.6, 1.0, 1),
            title="FAN OUT",
            unit="%"
        )
        gauges_grid.add_widget(self.fan_output_gauge)
        
        card.add_widget(gauges_grid)
        return card
    
    def create_right_panel(self):
        """Create right panel with forces and data"""
        panel_layout = MDBoxLayout(
            orientation='vertical',
            spacing=dp(8)
        )
        
        # Forces card
        forces_card = MDCard(
            elevation=dp(4),
            padding=dp(12),
            radius=[dp(8)],
            size_hint_y=0.6
        )
        
        forces_layout = MDBoxLayout(
            orientation='vertical',
            spacing=dp(8)
        )
        
        # Forces title - Make it white and visible
        forces_title = MDLabel(
            text="FORCES",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),  # White text
            font_style="Subtitle1",
            size_hint_y=None,
            height=dp(24),
            halign="center"
        )
        forces_layout.add_widget(forces_title)
        
        # Lift gauge
        self.lift_gauge = MaterialCircularGauge(
            min_val=-2, max_val=8,
            gauge_color=(0.2, 0.8, 0.3, 1),
            title="LIFT",
            unit="N"
        )
        forces_layout.add_widget(self.lift_gauge)
        
        # Drag gauge
        self.drag_gauge = MaterialCircularGauge(
            min_val=0, max_val=3,
            gauge_color=(1.0, 0.3, 0.3, 1),
            title="DRAG",
            unit="N"
        )
        forces_layout.add_widget(self.drag_gauge)
        
        forces_card.add_widget(forces_layout)
        panel_layout.add_widget(forces_card)
        
        # System data card
        data_card = MDCard(
            elevation=dp(4),
            padding=dp(12),
            radius=[dp(8)],
            size_hint_y=0.4
        )
        
        data_layout = MDBoxLayout(
            orientation='vertical',
            spacing=dp(4)
        )
        
        # Data title - Make it white and visible
        data_title = MDLabel(
            text="SYSTEM DATA",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),  # White text
            font_style="Subtitle1",
            size_hint_y=None,
            height=dp(24),
            halign="center"
        )
        data_layout.add_widget(data_title)
        
        # Runtime - Make it light gray and visible
        self.runtime_label = MDLabel(
            text="Runtime: 0.0s",
            theme_text_color="Custom",
            text_color=(0.8, 0.8, 0.8, 1),  # Light gray text
            font_style="Body2",
            size_hint_y=None,
            height=dp(20),
            halign="center"
        )
        data_layout.add_widget(self.runtime_label)
        
        # Status chip
        self.status_chip = MDChip(
            text="READY",
            md_bg_color=(0.2, 0.8, 0.3, 1),
            size_hint_y=None,
            height=dp(32)
        )
        data_layout.add_widget(self.status_chip)
        
        data_card.add_widget(data_layout)
        panel_layout.add_widget(data_card)
        
        return panel_layout
    
    def create_bottom_controls(self):
        """Create bottom control buttons"""
        controls_layout = MDBoxLayout(
            orientation='horizontal',
            spacing=dp(12),
            padding=[dp(12), dp(8)]
        )
        
        # Start/Stop button
        self.start_stop_button = MDRaisedButton(
            text="START",
            icon="play",
            md_bg_color=(0.2, 0.8, 0.3, 1),
            size_hint_x=0.25,
            font_size=dp(16)
        )
        self.start_stop_button.bind(on_press=self.toggle_simulation)
        controls_layout.add_widget(self.start_stop_button)
        
        # Reset button
        reset_button = MDRaisedButton(
            text="RESET",
            icon="refresh",
            md_bg_color=(1.0, 0.6, 0.2, 1),
            size_hint_x=0.25,
            font_size=dp(16)
        )
        reset_button.bind(on_press=self.reset_simulation)
        controls_layout.add_widget(reset_button)
        
        # Spacer
        spacer = Widget()
        controls_layout.add_widget(spacer)
        
        # Back button
        back_button = MDRaisedButton(
            text="BACK",
            icon="arrow-left",
            md_bg_color=(0.4, 0.4, 0.4, 1),
            size_hint_x=0.25,
            font_size=dp(16)
        )
        back_button.bind(on_press=self.go_back)
        controls_layout.add_widget(back_button)
        
        return controls_layout
    
    def increase_fan_speed(self, button):
        """Increase fan speed"""
        self.simulator.adjust_fan_speed(5)
        self.update_fan_display()
    
    def decrease_fan_speed(self, button):
        """Decrease fan speed"""
        self.simulator.adjust_fan_speed(-5)
        self.update_fan_display()
    
    def update_fan_display(self):
        """Update fan speed display"""
        self.fan_speed_label.text = f"{self.simulator.fan_speed}%"
    
    def toggle_simulation(self, button):
        """Toggle simulation start/stop"""
        if self.simulator.is_running:
            self.simulator.stop_simulation()
            self.start_stop_button.text = "START"
            self.start_stop_button.icon = "play"
            self.start_stop_button.md_bg_color = (0.2, 0.8, 0.3, 1)
            self.status_chip.text = "STOPPED"
            self.status_chip.md_bg_color = (0.9, 0.3, 0.3, 1)
        else:
            self.simulator.start_simulation()
            self.start_stop_button.text = "STOP"
            self.start_stop_button.icon = "stop"
            self.start_stop_button.md_bg_color = (0.9, 0.3, 0.3, 1)
            self.status_chip.text = "RUNNING"
            self.status_chip.md_bg_color = (0.2, 0.8, 0.3, 1)
    
    def reset_simulation(self, button):
        """Reset simulation"""
        self.simulator.reset_simulation()
        self.update_fan_display()
        self.status_chip.text = "RESET"
        self.status_chip.md_bg_color = (1.0, 0.6, 0.2, 1)
    
    def go_back(self, button):
        """Go back to mode selection"""
        self.manager.current = 'mode_screen'
    
    def on_enter(self):
        """Called when screen becomes active"""
        self.update_event = Clock.schedule_interval(self.update_data, 0.1)
        
        # Start simulation automatically
        self.simulator.start_simulation()
        self.start_stop_button.text = "STOP"
        self.start_stop_button.icon = "stop"
        self.start_stop_button.md_bg_color = (0.9, 0.3, 0.3, 1)
        self.status_chip.text = "RUNNING"
        self.status_chip.md_bg_color = (0.2, 0.8, 0.3, 1)
        
        print("📊 Material Design dashboard started")
    
    def on_leave(self):
        """Called when leaving screen"""
        if self.update_event:
            self.update_event.cancel()
            self.update_event = None
        print("👋 Dashboard stopped")
    
    def update_data(self, dt):
        """Update all displays with fresh data"""
        data = self.simulator.get_all_data()
        
        # Update speed gauge
        self.speed_gauge.update_speed(data['airspeed_mph'])
        
        # Update pressure gauges
        self.static_pressure_gauge.update_value(data['pressure_static'])
        self.dynamic_pressure_gauge.update_value(data['pressure_dynamic'])
        
        # Update angle of attack
        self.aoa_gauge.update_value(data['angle_of_attack'])
        
        # Update forces
        self.lift_gauge.update_value(data['lift_force'])
        self.drag_gauge.update_value(data['drag_force'])
        
        # Update fan output
        self.fan_output_gauge.update_value(data['fan_output'])
        
        # Update displays
        self.runtime_label.text = f'Runtime: {data["runtime"]:.1f}s'
        self.fan_speed_label.text = f"{self.simulator.fan_speed}%" 