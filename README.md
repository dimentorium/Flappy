# Flappy
First version of an FLStudio Device, that can be used to directly automate FLStudio from a Python IDE (for example VSCode)
Basic idea is quite simple. The device is connected via a virtual midi cable (I used loopmidi https://www.tobias-erichsen.de/software/loopmidi.html) and receives commands from Python via Sysex. Thus you can execute any command that is available either for automating boring tasks, or prototyping functions without a controller.

Installation
You will need
- Loopmidi
- FL API Stubs https://forum.image-line.com/viewtopic.php?p=1844122#p1674575
- The device copied inside the FL Hardware Controller folder
- Python IDE with the flappy.py file in your project
- MIDO installed via PIP https://mido.readthedocs.io/en/latest/installing.html
- RTMidi Version 1.4.9 (I had issues otherwise with loopmidi)

Also information will be posted in the forum
https://forum.image-line.com/viewtopic.php?p=1867789#p1867789
