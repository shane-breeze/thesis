import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

def main():
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(4.8, 4.8))
    ax.axis('off')

    #verts = [(0., 0.), (0.2, 1.), (1, 0.8), (0.8, 0.)]
    #codes = [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4]
    #path = Path(verts, codes)
    #patch = patches.PathPatch(path, fc='none', lw=2)
    #ax.add_patch(patch)


    # LHC circle
    lhc_size = 26700 / 0.4
    lhc = patches.Circle((0.5, 0.55), radius=26700/lhc_size, color='black',
                         fc='none', lw=2)
    ax.add_patch(lhc)

    # SPS circle
    sps = patches.Circle((0.5, 0.22), radius=6900/lhc_size, color='black',
                         fc='none', lw=2)
    ax.add_patch(sps)

    # PS circle
    ps = patches.Circle((0.6, 0.1), radius=628/lhc_size, color='black',
                        fc='none', lw=2)
    ax.add_patch(ps)

    fig.savefig("diagram.pdf")

if __name__ == "__main__":
    main()
