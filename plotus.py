from matplotlib.backends.backend_gtk3cairo import FigureCanvasGTK3Cairo as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np

# def plot_1D_mesh(data):
#     f = Figure(figsize=(5, 4), dpi=100)
#     a = f.add_subplot(111)
#     t = np.arange(0.0, 3.0, 0.01)
#     s = np.sin(2*np.pi*t)
#     a.plot(t, s)
#     return FigureCanvas(f)

def plot_1D_mesh(data):
    fig = plt.figure()
    barprops = dict(aspect='auto', cmap=plt.cm.binary, interpolation='nearest')
    x = np.array([d[0] for d in data])
    ax = fig.add_axes(
        [0.1, 0.1, 0.8, 0.8],
        title='1D Mesh',
        # xlim=(min(x), max(x)),
        yticks=[],
    )
    ax.imshow(x.reshape((1, -1)), **barprops)
    return FigureCanvas(fig)
