
import time
import random

import flappy
import channels
import transport
import mixer
import plugins
import ui
import midi

flappy.enable("PythonMidi 0", "PythonMidi 1")

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


print(plugins.getPluginName(3))
paramcount = plugins.getParamCount(3)
for i in range(0, paramcount):
    print(plugins.getParamName(i, 3), ":", plugins.getParamValue(i, 3))
    plugins.setParamValue(random.random(), i, 3)
    time.sleep(0.01)