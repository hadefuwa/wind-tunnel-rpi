# Wind Tunnel Controller

A modern, touch-friendly Python application for displaying wind tunnel data. Built with Kivy for smooth graphics and touchscreen support.

## Features

- **Modern Graphics**: Smooth, professional-looking interface
- **Touch-Friendly**: Large buttons and clear displays
- **Real-time Data**: Updates 10 times per second
- **Simulation Mode**: Realistic fake data for testing
- **Offline**: No internet connection required
- **Cross-Platform**: Works on Windows, Linux, and Raspberry Pi

## Quick Start

### 1. Install Python Requirements

```bash
pip install -r requirements.txt
```

### 2. Run the Application

```bash
python main.py
```

### 3. Use the App

1. **Mode Selection**: Choose "Simulation Mode" to see live data
2. **Dashboard**: View real-time airspeed, pressure, and flow direction
3. **Controls**: Use "Back to Menu" and "Reset Data" buttons

## Project Structure

```
wind_tunnel_app/
├── main.py              # Main application entry point
├── requirements.txt     # Python dependencies
├── README.md           # This file
├── gui/                # User interface screens
│   ├── modescreen.py   # Mode selection screen
│   └── dashboard.py    # Main data dashboard
└── logic/              # Application logic
    └── simulator.py    # Wind tunnel data simulator
```

## Installation on Different Systems

### Windows
```bash
pip install kivy
python main.py
```

### Raspberry Pi
```bash
sudo apt update
sudo apt install python3-pip
pip3 install kivy
python3 main.py
```

### Linux
```bash
pip install kivy
python main.py
```

## Customization

### Changing Update Rate
In `dashboard.py`, line 180:
```python
self.update_event = Clock.schedule_interval(self.update_data, 0.1)  # 10 Hz
```
Change `0.1` to `0.2` for 5 Hz, or `0.05` for 20 Hz.

### Changing Data Ranges
In `simulator.py`, modify the base values:
```python
self.base_airspeed = 25.0  # m/s
self.base_pressure = 1013.25  # hPa
```

### Fullscreen Mode
In `main.py`, uncomment line 70:
```python
Window.fullscreen = True
```

## Troubleshooting

### Common Issues

1. **Import Error**: Make sure Kivy is installed: `pip install kivy`
2. **Screen Too Small**: Resize the window or enable fullscreen
3. **Touch Not Working**: Ensure your system supports touch input

### Performance Tips

- Run in fullscreen mode on Raspberry Pi
- Close other applications to free up memory
- Use a Class 10 SD card on Raspberry Pi

## Technical Details

- **Language**: Python 3
- **GUI Framework**: Kivy 2.0+
- **Data Update Rate**: 10 Hz (configurable)
- **Memory Usage**: ~20-50 MB
- **CPU Usage**: Low (suitable for Raspberry Pi)

## License

This project is open source and available under the MIT License. 