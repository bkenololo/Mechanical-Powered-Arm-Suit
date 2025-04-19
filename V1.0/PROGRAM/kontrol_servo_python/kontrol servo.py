import serial
import time
from pynput import keyboard

# Ganti sesuai port lo
arduino = serial.Serial('/dev/tty.usbmodem1101', 9600)
time.sleep(2)  # Tunggu Arduino siap

moving = False
direction = None
last_send = time.time()

# Waktu antar kirim data ke Arduino (semakin kecil = makin cepat)
send_interval = 0.01  # 10ms

def on_press(key):
    global moving, direction
    try:
        if key == keyboard.Key.space:
            moving = not moving
            print("Start" if moving else "Stop")
        elif key == keyboard.Key.left:
            direction = 'L'
            print("Kiri")
        elif key == keyboard.Key.right:
            direction = 'R'
            print("Kanan")
    except:
        pass

def on_release(key):
    global direction
    if key in [keyboard.Key.left, keyboard.Key.right]:
        direction = None

# Listener keyboard
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

print("Tekan SPACE buat Start/Stop, ← → buat arah")

try:
    while True:
        if moving and direction:
            now = time.time()
            if now - last_send > send_interval:
                arduino.write(direction.encode())
                last_send = now
        time.sleep(0.001)  # super kecil biar nggak boros CPU
except KeyboardInterrupt:
    print("Program dihentikan")
    arduino.close()
 