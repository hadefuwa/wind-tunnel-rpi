# 🌪️ Wind Tunnel Controller

<div align="center">


**A professional-grade wind tunnel control system with modern UI and real-time data visualization**

![Python](https://img.shields.io/badge/Python-3.7%2B-blue?style=flat-square&logo=python)
![Kivy](https://img.shields.io/badge/Kivy-2.0%2B-green?style=flat-square&logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20Raspberry%20Pi-lightgrey?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

*Beautiful circular gauges • Professional styling • Touch-optimized interface*

</div>

---
![image](https://github.com/user-attachments/assets/42fe8e17-dc3e-4357-a329-580e6ce6a0b8)

## ✨ Features

### 🎨 **Modern Professional UI**
- **Circular gauges** with smooth animations and glowing effects
- **Dark theme** with professional color schemes  
- **Gradient backgrounds** and shadow effects for depth
- **Touch-friendly** large buttons with visual feedback
- **Real-time animations** at 60 FPS for fluid experience

### 📊 **Real-Time Data Visualization**
- **Airspeed monitoring** (0-40 m/s) with green gauge
- **Pressure tracking** (1000-1030 hPa) with blue gauge  
- **Flow direction** (-30° to +30°) with orange gauge
- **Live updates** every 0.1 seconds (10 Hz)
- **Smooth gauge animations** with realistic data simulation

### 🔧 **Technical Excellence**
- **Offline operation** - no internet required
- **Cross-platform** - Windows, Linux, Raspberry Pi
- **Lightweight** - minimal dependencies (just Kivy + Python)
- **Optimized** for touchscreen displays (7" recommended)
- **Modular architecture** for easy expansion

---

## 🖼️ Screenshots

### Mode Selection Screen
Modern control system interface with professional styling:
- Dark gradient background with blue accents
- Large touch-friendly buttons with icons
- Status indicators and system information
- Smooth button animations with shadow effects

### Dashboard Interface  
Beautiful real-time data visualization:
- Three circular gauges with smooth arcs
- Professional color coding (green/blue/orange)
- Live numeric displays with large fonts
- Modern control buttons with rounded corners
- Status bar with runtime information

---

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/hadefuwa/wind-tunnel-rpi.git
   cd wind-tunnel-rpi
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

### First Launch
1. Application opens to the **Mode Selection** screen
2. Click **"⚡ SIMULATION MODE"** to start
3. View real-time data on the **Dashboard**
4. Use **"⟲ RESET"** to restart simulation
5. Press **"◀ BACK"** to return to main menu

---

## 🍓 Raspberry Pi Deployment

Perfect for industrial applications and kiosk setups:

### Setup Commands
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python and dependencies
sudo apt install python3 python3-pip git -y

# Clone and setup project
git clone https://github.com/hadefuwa/wind-tunnel-rpi.git
cd wind-tunnel-rpi
pip3 install -r requirements.txt

# Run application
python3 main.py
```

### Touchscreen Optimization
For 7-inch touchscreen displays:
```bash
# Enable fullscreen mode (edit main.py)
# Uncomment: Window.fullscreen = True

# Auto-start on boot (optional)
sudo nano /etc/rc.local
# Add: python3 /home/pi/wind-tunnel-rpi/main.py &
```

### Performance Tips
- Use Class 10 SD card or better
- Close unnecessary services for optimal performance
- Consider using Raspberry Pi 4 for best experience

---

## 🛠️ Configuration

### Simulation Parameters
Edit `logic/simulator.py` to customize data ranges:
```python
self.base_airspeed = 25.0      # Base airspeed (m/s)
self.base_pressure = 1013.25   # Base pressure (hPa) 
self.airspeed_variation = 5.0  # Variation range
```

### Update Rate
Modify refresh rate in `gui/dashboard.py`:
```python
# Change update frequency (default: 10 Hz)
self.update_event = Clock.schedule_interval(self.update_data, 0.1)
```

### Display Settings
Adjust window size in `main.py`:
```python
Config.set('graphics', 'width', '1200')   # Window width
Config.set('graphics', 'height', '800')   # Window height
```

---

## 📁 Project Structure

```
wind-tunnel-rpi/
├── main.py                 # Application entry point
├── requirements.txt        # Python dependencies  
├── README.md              # This file
├── App Plan.md            # Development documentation
├── gui/                   # User interface components
│   ├── __init__.py
│   ├── modescreen.py      # Modern mode selection screen
│   └── dashboard.py       # Professional dashboard with gauges
└── logic/                 # Application logic
    ├── __init__.py
    └── simulator.py       # Wind tunnel data simulation
```

---

## 🎯 Use Cases

### **Industrial Applications**
- Wind tunnel testing facilities
- HVAC system monitoring  
- Environmental control systems
- Process monitoring dashboards

### **Educational Projects**
- Engineering demonstrations
- Physics experiments
- Student research projects
- STEM education tools

### **Development & Testing**
- Prototype interface testing
- Data visualization demos
- Touch interface development
- Embedded system projects

---

## 🔧 Technical Details

| Component | Technology | Purpose |
|-----------|------------|---------|
| **GUI Framework** | Kivy 2.0+ | Modern graphics and touch support |
| **Language** | Python 3.7+ | Easy maintenance and cross-platform |
| **Graphics** | OpenGL | Hardware-accelerated rendering |
| **Data Simulation** | Built-in math/random | Realistic wind tunnel behavior |
| **Architecture** | MVC Pattern | Clean separation of concerns |

### System Requirements
- **Memory**: 20-50 MB RAM usage
- **CPU**: Low usage, suitable for Raspberry Pi
- **Display**: 800x600 minimum, 1200x800 recommended
- **Touch**: Multi-touch support for best experience

---

## 🚧 Future Enhancements

### Planned Features
- [ ] **SPI Integration** - Real sensor data input
- [ ] **Data Logging** - Export CSV/JSON data
- [ ] **Historical Charts** - Time-series visualization  
- [ ] **Calibration Mode** - Sensor calibration interface
- [ ] **Multi-language** - Internationalization support
- [ ] **Themes** - Light/dark mode toggle

### Expandability
- **Plugin System** - Easy addition of new sensors
- **API Interface** - REST API for remote monitoring
- **Database Support** - Long-term data storage
- **Network Monitoring** - Remote dashboard access

---

## 🤝 Contributing

We welcome contributions! Here's how to get started:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)  
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Guidelines
- Follow Python PEP 8 style guide
- Add comments for complex logic
- Test on multiple platforms when possible
- Update documentation for new features

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License - Free for commercial and personal use
```

---

## 🙏 Acknowledgments

- **Kivy Community** - Excellent cross-platform framework
- **Python Foundation** - Amazing programming language
- **Raspberry Pi Foundation** - Affordable embedded computing
- **Open Source Community** - Inspiration and collaboration

---

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/hadefuwa/wind-tunnel-rpi/issues)
- **Documentation**: Check the `App Plan.md` file
- **Community**: Star the repo and share your projects!

---

<div align="center">

**Made with ❤️ for the engineering community**

[⭐ Star this repo](https://github.com/hadefuwa/wind-tunnel-rpi) | [🔧 Report Issues](https://github.com/hadefuwa/wind-tunnel-rpi/issues) | [🚀 Request Features](https://github.com/hadefuwa/wind-tunnel-rpi/issues)

</div> 
