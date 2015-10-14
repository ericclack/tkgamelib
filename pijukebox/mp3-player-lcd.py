import os, time, sys
import Adafruit_CharLCD as LCD

REALLY_HALT = True

lcd = LCD.Adafruit_CharLCDPlate()
lcd.set_backlight(0.5)

def mpc(command):
    output = os.popen("mpc %s" % command)
    s = output.read()
    output.close()
    return s

def lcd_display(m):
    lcd.clear()
    if m.find('Forever More') != -1:
        m = 'Moloko - Endless cheese'
    # Wrap long messages
    if len(m)>16:
        m = m[:16] + "\n" + m[16:]
    lcd.message(m)

def display_current():
    lcd_display(mpc("current"))

def next_song():
    mpc("next")
    display_current()

def prev_song():
    mpc("prev")
    display_current()

def current_album():
    return mpc("current").split()[0]

def next_album():
    start = current_album()
    for go in range(100):
        next_song()
        if current_album() != start:
            return
        
def are_we_shutting_down():
    """Called after pause button pressed"""
    time.sleep(0.5)
    if lcd.is_pressed(LCD.SELECT):        
        lcd_display("Keep pressing to shutdown!")
        time.sleep(2)
        if lcd.is_pressed(LCD.SELECT):
            lcd_display("Shutting down...")
            time.sleep(1)
            if REALLY_HALT: 
                os.system('/sbin/halt')
            lcd_display("")
            sys.exit()

        else:
            display_current()

display_current()

while True:
    if lcd.is_pressed(LCD.RIGHT):
        next_song()
    if lcd.is_pressed(LCD.LEFT):
        prev_song()
    if lcd.is_pressed(LCD.DOWN):
        next_album()
    if lcd.is_pressed(LCD.SELECT):
        mpc("toggle")
        are_we_shutting_down()

    # Don't hog the CPU
    time.sleep(0.05)
