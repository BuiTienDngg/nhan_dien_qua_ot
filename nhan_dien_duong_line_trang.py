import pyb # Import module for board related functions
import sensor # Import the module for sensor related functions
import image # Import module containing machine vision algorithms
import time # Import module for tracking elapsed time
# Khởi tạo camera
sensor.reset() # Resets the sensor
sensor.set_pixformat(sensor.RGB565) # Sets the sensor to RGB
sensor.set_framesize(sensor.HVGA) # Sets the resolution to 320x240 px
sensor.set_vflip(True) # Flips the image vertically
sensor.set_hmirror(True) # Mirrors the image horizontally
sensor.skip_frames(time = 1000) # Skip some frames to let the image stabilize
threshold = [(64, 100, -128, 127, -128, 127),(54, 100, 120, -31, -30, 22),(82, 93, 127, -99, -71, 29)]
led = pyb.LED(2) # Initiates the red led
while True:
    img = sensor.snapshot() # Takes a snapshot and saves it in memory
    blobs = img.find_blobs([threshold[0],threshold[1],threshold[2] ], area_threshold=5000, merge=True)
    led.off()
    for blob in blobs:
        # Draw a rectangle where the blob was found
        img.draw_rectangle(blob.rect(), color=(0,255,0))
        # Draw a cross in the middle of the blob
        img.draw_cross(blob.cx(), blob.cy(), color=(0,255,0))
        print(blob.cx())
        print(blob.cy())
        led.on()
