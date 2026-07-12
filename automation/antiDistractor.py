# A problem I was facing in my daily life is fairly common in the internet age
# I was getting distracted and not focusing on studying or whatever
# I'd open a new browser / browser window and start "distracting" away

# So, let's put an end to that!

import pygetwindow as gw
import time
while True:
    browsers = [] 
    for window in gw.getAllWindows(): # We get all windows that are currently open 
        if window.title != "":  # This filters out completely invisible background windows
                 if "Chrome" in window.title or "Edge" in window.title: # Checking for the two browsers I use, Chrome and Edge
                         browsers.append(window)
                         if len(browsers) > 1: # If there's more than one window open
                                 print("Violation")
                                 for browser in browsers:
                                        try: # In case it fails
                                              browser.close()
                                        except:
                                               pass
                            
    time.sleep(15) # Of course, it needs to keep running.

# Now at the moment this is just a Python file. I packaged it into an .exe file using a library I found after some Googling, but I'm not sure if it's good practice to
# upload .exe files on github. So here's the "source code".
# With the .exe file that I have locally, I can now run it on startup on my laptop.
