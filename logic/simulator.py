import math
import random
import time

class WindTunnelSimulator:
    """
    Enhanced wind tunnel simulator with comprehensive data including:
    - Fan speed control
    - Lift/Drag calculations
    - Angle of attack
    - MPH airspeed
    - Fan output percentage
    - Realistic physics simulation
    """
    
    def __init__(self):
        self.start_time = time.time()
        self.is_running = False
        self.fan_speed = 50  # Fan speed percentage (0-100)
        self.angle_of_attack = 0  # Degrees (-20 to +20)
        
        # Base values for simulation
        self.base_pressure = 1013.25  # hPa
        self.base_airspeed = 0  # Will be calculated from fan speed
        
        # Simulation state
        self.current_data = {
            'airspeed_mph': 0,
            'airspeed_ms': 0,
            'pressure_static': self.base_pressure,
            'pressure_dynamic': self.base_pressure,
            'angle_of_attack': 0,
            'lift_force': 0,
            'drag_force': 0,
            'fan_output': 0,
            'timestamp': 0,
            'runtime': 0
        }
        
        print("Enhanced wind tunnel simulator initialized")
        print("Features: Fan control, Lift/Drag, Angle of Attack, MPH display")
    
    def set_fan_speed(self, speed):
        """Set fan speed (0-100%)"""
        self.fan_speed = max(0, min(100, speed))
        print(f"Fan speed set to {self.fan_speed}%")
    
    def adjust_fan_speed(self, delta):
        """Adjust fan speed by delta amount"""
        self.set_fan_speed(self.fan_speed + delta)
    
    def set_angle_of_attack(self, angle):
        """Set angle of attack (-20 to +20 degrees)"""
        self.angle_of_attack = max(-20, min(20, angle))
        print(f"Angle of attack set to {self.angle_of_attack}°")
    
    def start_simulation(self):
        """Start the simulation"""
        self.is_running = True
        self.start_time = time.time()
        print("Simulation started")
    
    def stop_simulation(self):
        """Stop the simulation"""
        self.is_running = False
        print("Simulation stopped")
    
    def reset_simulation(self):
        """Reset simulation to initial state"""
        self.start_time = time.time()
        self.fan_speed = 50
        self.angle_of_attack = 0
        print("Simulation reset to initial state")
    
    def calculate_airspeed(self):
        """Calculate airspeed based on fan speed"""
        if not self.is_running:
            return 0
        
        # Base airspeed calculation: fan speed translates to airspeed
        # 100% fan = ~60 MPH max
        base_speed = (self.fan_speed / 100.0) * 60
        
        # Add some realistic variation
        variation = random.uniform(-2, 2)
        airspeed_mph = max(0, base_speed + variation)
        
        return airspeed_mph
    
    def calculate_pressure(self, airspeed_mph):
        """Calculate static and dynamic pressure"""
        # Convert MPH to m/s for calculations
        airspeed_ms = airspeed_mph * 0.44704
        
        # Dynamic pressure: 0.5 * density * velocity^2
        air_density = 1.225  # kg/m³ at sea level
        dynamic_pressure_pa = 0.5 * air_density * (airspeed_ms ** 2)
        
        # Convert to hPa and add to base pressure
        dynamic_pressure_hpa = dynamic_pressure_pa / 100
        
        # Static pressure decreases slightly with airspeed (Bernoulli's principle)
        static_pressure = self.base_pressure - (dynamic_pressure_hpa * 0.1)
        dynamic_pressure = self.base_pressure + dynamic_pressure_hpa
        
        return static_pressure, dynamic_pressure
    
    def calculate_lift_drag(self, airspeed_mph, angle_of_attack):
        """Calculate lift and drag forces"""
        if airspeed_mph == 0:
            return 0, 0
        
        # Convert to m/s for calculations
        airspeed_ms = airspeed_mph * 0.44704
        
        # Simplified aerodynamic calculations
        # Assume a wing area of 0.1 m²
        wing_area = 0.1  # m²
        air_density = 1.225  # kg/m³
        
        # Lift coefficient based on angle of attack
        # Simplified: Cl = 0.1 * AOA (in degrees) up to stall
        angle_rad = math.radians(angle_of_attack)
        if abs(angle_of_attack) <= 15:
            cl = 0.1 * angle_of_attack  # Linear region
        else:
            cl = 0.1 * 15 * (1 - (abs(angle_of_attack) - 15) / 10)  # Stall region
        
        # Drag coefficient: increases with angle of attack
        cd = 0.02 + 0.01 * (angle_of_attack ** 2) / 100
        
        # Force calculations: F = 0.5 * density * velocity² * area * coefficient
        dynamic_pressure = 0.5 * air_density * (airspeed_ms ** 2)
        
        lift_force = dynamic_pressure * wing_area * cl
        drag_force = dynamic_pressure * wing_area * cd
        
        return lift_force, drag_force
    
    def get_all_data(self):
        """Get all current simulation data"""
        current_time = time.time()
        runtime = current_time - self.start_time
        
        # Calculate all values
        airspeed_mph = self.calculate_airspeed()
        airspeed_ms = airspeed_mph * 0.44704  # Convert to m/s
        
        static_pressure, dynamic_pressure = self.calculate_pressure(airspeed_mph)
        lift_force, drag_force = self.calculate_lift_drag(airspeed_mph, self.angle_of_attack)
        
        # Fan output percentage (with some variation)
        fan_output = self.fan_speed
        if self.is_running:
            fan_output += random.uniform(-2, 2)
            fan_output = max(0, min(100, fan_output))
        
        # Update current data
        self.current_data.update({
            'airspeed_mph': airspeed_mph,
            'airspeed_ms': airspeed_ms,
            'pressure_static': static_pressure,
            'pressure_dynamic': dynamic_pressure,
            'angle_of_attack': self.angle_of_attack,
            'lift_force': lift_force,
            'drag_force': drag_force,
            'fan_output': fan_output,
            'timestamp': current_time,
            'runtime': runtime,
            'is_running': self.is_running
        })
        
        return self.current_data
    
    def get_airspeed_mph(self):
        """Get current airspeed in MPH"""
        return self.get_all_data()['airspeed_mph']
    
    def get_pressure_data(self):
        """Get pressure data"""
        data = self.get_all_data()
        return data['pressure_static'], data['pressure_dynamic']
    
    def get_forces(self):
        """Get lift and drag forces"""
        data = self.get_all_data()
        return data['lift_force'], data['drag_force']
    
    def get_fan_output(self):
        """Get fan output percentage"""
        return self.get_all_data()['fan_output']
    
    def get_status(self):
        """Get simulation status"""
        return "RUNNING" if self.is_running else "STOPPED" 