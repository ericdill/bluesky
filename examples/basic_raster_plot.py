import numpy as np
import bluesky.callbacks
import matplotlib.pyplot as plt
from cycler import cycler
import time as ttime
from bluesky import qt_kicker


xct = 10
yct = 15
ict = xct * yct
cb = None

def setup():
    global cb
    cb = bluesky.callbacks.FancyLiveRaster((yct, xct),  'I', clim=[0, 1])
    cb.widget.show()

def run():
    global cb
    cb('start', {})
    cy = ((cycler('x', np.linspace(0, 1, xct, endpoint=True)) *
           cycler('y', np.linspace(0, 1, yct, endpoint=True))) +
          cycler('I', np.linspace(0, 1, ict, endpoint=True)))
    for j, d in enumerate(cy):
        ev = {'data': d, 'seq_num': j + 1}
        cb('event', ev)
        plt.pause(.1)
        # ttime.sleep(0.1)
        qt_kicker.qApp.processEvents()

