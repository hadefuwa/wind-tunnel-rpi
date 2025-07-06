import math
import random
import time

class WindTunnelSimulator:
    """
    Simple wind tunnel data simulator that creates realistic but fake data.
    This is beginner-friendly code - everything is clear and readable.
    """
    
    def __init__(self):
        # Keep track of time for realistic data patterns
        self.start_time = time.time()
        
        # Base values for our simulated data
        self.base_airspeed = 25.0  # m/s
        self.base_pressure = 1013.25  # hPa (standard atmospheric pressure)
        self.base_flow_angle = 0.0  # degrees
        
        # These control how much the data changes over time
        self.airspeed_variation = 5.0  # how much airspeed can vary
        self.pressure_variation = 10.0  # how much pressure can vary
        self.flow_angle_variation = 15.0  # how much flow angle can vary
        
        print("Wind tunnel simulator started - generating fake data")
    
    def get_current_time(self):
        """Get how many seconds have passed since we started"""
        return time.time() - self.start_time
    
    def get_airspeed(self):
        """
        Generate realistic airspeed data.
        Uses a sine wave with some random noise to simulate wind variations.
        """
        current_time = self.get_current_time()
        
        # Create a smooth sine wave pattern
        sine_wave = math.sin(current_time * 0.5) * self.airspeed_variation
        
        # Add some random noise to make it more realistic
        random_noise = random.uniform(-2.0, 2.0)
        
        # Calculate final airspeed
        airspeed = self.base_airspeed + sine_wave + random_noise
        
        # Make sure airspeed is never negative
        return max(0.0, airspeed)
    
    def get_pressure(self):
        """
        Generate realistic pressure data.
        Uses a slow ramp up and down pattern with noise.
        """
        current_time = self.get_current_time()
        
        # Create a slow ramp pattern (goes up and down every 30 seconds)
        ramp_wave = math.sin(current_time * 0.1) * self.pressure_variation
        
        # Add some random noise
        random_noise = random.uniform(-1.0, 1.0)
        
        # Calculate final pressure
        pressure = self.base_pressure + ramp_wave + random_noise
        
        return pressure
    
    def get_flow_direction(self):
        """
        Generate realistic flow direction data.
        Creates an angle that sweeps back and forth.
        """
        current_time = self.get_current_time()
        
        # Create a sweeping angle pattern
        sweep_angle = math.sin(current_time * 0.3) * self.flow_angle_variation
        
        # Add some random jitter
        random_jitter = random.uniform(-2.0, 2.0)
        
        # Calculate final flow direction
        flow_direction = self.base_flow_angle + sweep_angle + random_jitter
        
        return flow_direction
    
    def get_all_data(self):
        """
        Get all wind tunnel data at once.
        Returns a dictionary with all current values.
        """
        return {
            'airspeed': self.get_airspeed(),
            'pressure': self.get_pressure(),
            'flow_direction': self.get_flow_direction(),
            'timestamp': self.get_current_time()
        }
    
    def reset_simulation(self):
        """Reset the simulation to start over"""
        self.start_time = time.time()
        print("Simulation reset - starting fresh data") 