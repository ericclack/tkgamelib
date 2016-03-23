import os, time, sys
import Adafruit_CharLCD as LCD

# You'll need to set up your Pi for the Adafruit LCD Plate
# https://learn.adafruit.com/adafruit-16x2-character-lcd-plus-keypad-for-raspberry-pi/usage
# Including I2C Kernel support
# https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c

# Halt or just quit this program?
REALLY_HALT = True
if 'SUDO_UID' in os.environ or 'TERM' in os.environ:
    print "Won't really halt -- running as sudo / from term"
    REALLY_HALT = False

lcd = LCD.Adafruit_CharLCDPlate()

def mpc(command):
    output = os.popen("mpc %s" % command)
    s = output.read()
    output.close()
    return s

def check_for_new_songs():
    mpc("update")
    mpc("clear")
    mpc("ls | mpc add")

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

def pick_random_first_song():
    mpc("random on")    
    mpc("play")
    mpc("random off")

def next_song():
    mpc("next")

def prev_song():
    mpc("prev")

def current_album():
    return mpc("current").split()[0]

def next_album():
    start = current_album()
    for go in range(100):
        next_song()
        if current_album() != start:
            return

def prev_album():
    start = current_album()
    for go in range(100):
        prev_song()
        if current_album() != start:
            break
    start = current_album()
    for go in range(100):
        prev_song()
        if current_album() != start:
            break
    next_song()
                
def shutdown():
    mpc("pause")
    lcd.set_backlight(0)
    lcd_display("")
    time.sleep(1)
    if REALLY_HALT: 
        os.system('/sbin/halt')
        time.sleep(5)
    sys.exit()

def are_we_shutting_down():
    """Call after pause button pressed"""
    time.sleep(0.5)
    if lcd.is_pressed(LCD.SELECT):        
        lcd_display("Keep pressing to shutdown!")
        time.sleep(2)
        if lcd.is_pressed(LCD.SELECT):
            lcd_display("Shutting down...")
            shutdown()
        display_current()

lcd.set_backlight(1)
lcd_display("Checking for new songs...")
check_for_new_songs()
mpc("volume 90")
mpc("repeat on")
pick_random_first_song()
mpc("pause")
lcd_display("Press SELECT to start playing")

last_song = mpc("current")
last_update = int(time.time())

while True:
    if lcd.is_pressed(LCD.RIGHT):
        next_song()
    if lcd.is_pressed(LCD.LEFT):
        prev_song()
    if lcd.is_pressed(LCD.DOWN):
        next_album()
    if lcd.is_pressed(LCD.UP):
        prev_album()
    if lcd.is_pressed(LCD.SELECT):
        mpc("toggle")
        are_we_shutting_down()
        display_current()

    # Don't hog the CPU
    time.sleep(0.05)

    # Tasks to run every second, rather than every
    # iteration, to conserve CPU
    if int(time.time()) > last_update: 
        # New song? Update the display?
        if last_song != mpc("current"):
            display_current()
            last_song = mpc("current")
        last_update = int(time.time())

