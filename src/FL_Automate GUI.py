import logging
import time
import random
import pyautogui
import pygetwindow as gw
import os

import flappy as flappy
import channels
import transport
import mixer
import midi
import ui
import plugins

"""
gw.getActiveWindow().title
'Rendering to \ue409untitled.mp3'
'FL Studio 21'
'Speichern unter'
"""

def checkForWindow(windowName:str):
    logging.debug('Searching:' + windowName)
    found = False
    while not found:
        topwindow = gw.getActiveWindow().title
        if windowName in topwindow:
            found = True
        time.sleep(0.1)
        

"""Initialize Backend and start Preset Manager application."""
logging.basicConfig(filename='fl_automate.log',
                    level=logging.DEBUG,
                    format='%(asctime)s %(message)s')
# create console handler and set level to info
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("[%(asctime)s]\t[%(levelname)s]\t[%(filename)s]\t\t%(message)s")
handler.setFormatter(formatter)
logging.getLogger().addHandler(handler)

# start application
logging.debug('FL Automate GUI')


basepath = "D:\\SoundDB\\FLStudio\\Toxic Biohazard\\Pads"
outputfolder = basepath

#flappy.enable("PythonMidi 0", "PythonMidi 1")
flappy.enable("PythonMidi 0", "PythonMidi 1", 3.0)
checkForWindow('FL Studio 21')
logging.info('Starting')
while True:
    ui.showWindow(midi.widBrowser)
    browserElementName = ui.getFocusedNodeCaption()
    browserElementType = ui.getFocusedNodeFileType()
    #logging.info(browserElementName)

    if(browserElementType == -100):         #its a folder
        #create folder and so
        outputfolder = os.path.join(outputfolder, browserElementName)
        if not os.path.isdir(outputfolder):
            logging.info('Creating folder:' + str(outputfolder))
            os.makedirs(outputfolder)

        ui.enter() #open folder
    else:                                   #its a preset
        #logging.info('Loading:' + str(browserElementName))
        ui.enter() #load preset to channel 1
        time.sleep(1.0)
        presetname = channels.getChannelName(0)
        if(browserElementName.startswith(presetname)):      #preset is loaded
            pyautogui.hotkey('shift', 'ctrl', 'r')          #open render dialog
            full_path = outputfolder + "\\" + presetname + ".wav"
            logging.info('Rendering:' + str(full_path))
            checkForWindow('Speichern unter')
            time.sleep(1.0)
            pyautogui.write(full_path)                      #enter file path
            pyautogui.press('enter')
            checkForWindow('Rendering to')
            time.sleep(1.0)
            pyautogui.press('enter')                        #render preset
            checkForWindow('FL Studio 21')
    ui.navigateBrowser(midi.FPT_Down,0)
    time.sleep(1.0)