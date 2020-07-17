import tkinter as tk
import os
import time

# declare the window
window = tk.Tk()

# set window title
window.title("Designed by M.Joo")
# set window width and height



# set window background color
window.configure(bg='lightgray')

def Conecttowifi():
    wifi_name = 'WLAN'
    ethernet_name=''   
    disable_ethernet = 'netsh interface set interface "'+ethernet_name+'" disabled'
    enable_wifi = 'netsh interface set interface "'+wifi_name+'" enabled'
    os.popen(disable_ethernet)
    time.sleep(10)
    os.popen(enable_wifi)
    
def ConecttoEthernet():
    wifi_name = 'WLAN'
    ethernet_name=''   
    disable_wifi = 'netsh interface set interface "'+wifi_name+'" disabled'
    enable_ethernet = 'netsh interface set interface "'+ethernet_name+'" enabled'
    os.popen(disable_wifi)
    time.sleep(10)
    os.popen(enable_ethernet)

B1 = tk.Button(window, text ="Connect to Wifi", command = Conecttowifi)
B1.pack()
B2 = tk.Button(window, text ="Connect to Ethenrt", command = ConecttoEthernet)
B2.pack()
B1.pack(side="left", fill="both", )
B2.pack(side="right", fill="both", )
window.configure(width=500, height=300)
window.mainloop()
