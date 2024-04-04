from picographics import PicoGraphics, DISPLAY_SCROLL_PACK, PEN_P8
import network
import time
from picoscroll import PicoScroll

# WiFi credentials
ssid = 'JN24'
password = 'D3skt0pK1ng'

# Initialize graphics and PicoScroll
graphics = PicoGraphics(DISPLAY_SCROLL_PACK, pen_type=PEN_P8)
scroll = PicoScroll()

# Connect to WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

# Wait for connection
while not wlan.isconnected():
    pass

# Obtain IP address
ip_address = wlan.ifconfig()[0]

# Calculate text wrap position
wrap = -graphics.measure_text(ip_address, scale=1)

t = scroll.get_width()

# Adjust the speed by changing the sleep time
scroll_speed = 0.5  # Decrease for faster scrolling, increase for slower

while True:
    graphics.set_pen(0)  # Background color
    graphics.clear()
    graphics.set_pen(255)  # Text color
    graphics.text(ip_address, t, 0, scale=1)
    scroll.update(graphics)
    t -= 1
    time.sleep(scroll_speed)  # Control the scroll speed here
    if t <= wrap:
        t = scroll.get_width()
