
import time
import random

import flappy
import channels
import transport
import mixer
import plugins
import ui
import midi

flappy.enable()

transport.start()
time.sleep(1)
transport.stop()
channels.setChannelName(0, "heiopei")
print(channels.getChannelName(1))
mixer.selectTrack(5)
mixer.soloTrack(5)

# print(channels.getChannelName(1))
# nodecap = ui.getFocusedNodeCaption()
# nodetype = ui.getFocusedNodeFileType()
# ui.selectBrowserMenuItem()
# ui.enter()
# transport.globalTransport(midi.FPT_Enter)


""" print(plugins.getPluginName(4))
paramcount = plugins.getParamCount(4)
for i in range(0, paramcount):
    #print(plugins.getParamName(i, 4), ":", plugins.getParamValue(i, 4))
    plugins.setParamValue(random.random(), i, 4)
    time.sleep(0.01) """