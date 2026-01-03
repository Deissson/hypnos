import os
import ctypes
import platform

def shutdown():
    """Shut down the computer."""
    if platform.system() == "Windows":
        os.system("shutdown /s /t 0")
    else:
        print("Unsupported platform for shutdown.")
def restart():
    """Restart the computer."""
    if platform.system() == "Windows":
        os.system("shutdown /r /t 0")
    else:
       print("Unsupported platform for restart.")

def turn_off_display():
    """Turn off the displays."""
    if platform.system() == "Windows":
        # SC_MONITORPOWER = 0xF170
        # 2 = Power off
        # -1 = Turn on (not standard but often used to wake up)
        # 1 = Low power
        HWND_BROADCAST = 0xFFFF
        WM_SYSCOMMAND = 0x0112
        SC_MONITORPOWER = 0xF170
        POWER_OFF = 2
        
        ctypes.windll.user32.PostMessageW(HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, POWER_OFF)
    else:
        print("Unsupported platform for turn_off_display.")