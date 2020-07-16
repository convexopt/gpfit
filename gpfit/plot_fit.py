"Fit plotting"
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from gpfit.fit import fit
from gpfit.print_fit import print_MA, print_SMA

# pylint: disable=invalid-name
# pylint: disable=too-many-locals
def plot_fit_1d(udata, wdata, K=1, ftype='MA', plotspace='linear'):
    "Finds and plots a fit (MA or SMA) for 1D data"

    cs, _ = fit(np.log(udata), np.log(wdata), K, ftype)
    uu = np.linspace(min(udata), max(udata), 1000)

    f, ax = plt.subplots()
    if plotspace == 'log':
        ax.loglog(udata, wdata, '+r')
        ax.loglog(uu, np.exp(cs.evaluate(np.log(uu))))
    elif plotspace == 'linear':
        ax.plot(udata, wdata, '+r')
        ax.plot(uu, np.exp(cs.evaluate(np.log(uu))))
    ax.set_xlabel('u')

    return f, ax

if __name__ == "__main__":
    N = 51
    U = np.logspace(0, np.log10(3), N)
    W = (U**2+3) / (U+1)**2
    f, ax = plot_fit_1d(U, W, K=2, ftype='SMA', plotspace="linear")
    f.savefig("test.png")
