from pynput import mouse
import serial
import time
import threading

# Ganti port sesuai device kamu
arduino = serial.Serial('/dev/tty.usbmodem1101', 9600)

last_x = 0
last_move_time = time.time()
last_send_time = 0
send_interval = 0.01  # 10ms
stop_sent = False

def on_move(x, y):
    global last_x, last_move_time, stop_sent, last_send_time

    dx = x - last_x
    now = time.time()

    if abs(dx) > 0 and now - last_send_time > send_interval:
        direction = 'L' if dx > 0 else 'R'  # Arah dibalik sesuai preferensi
        arduino.write(f"{direction}\n".encode())
        last_move_time = now
        last_send_time = now
        stop_sent = False

    last_x = x

def check_if_idle():
    global stop_sent
    while True:
        if time.time() - last_move_time > 0.07:
            if not stop_sent:
                arduino.write(b'S\n')
                stop_sent = True
        time.sleep(0.005)

# Thread untuk deteksi idle
idle_thread = threading.Thread(target=check_if_idle)
idle_thread.daemon = True
idle_thread.start()

print("Gerak kiri/kanan aktif. Swipe di trackpad untuk kontrol.")
with mouse.Listener(on_move=on_move) as listener:
    listener.join()
