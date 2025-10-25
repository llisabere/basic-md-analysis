import MDAnalysis as mda
import numpy as np
import matplotlib.pyplot as plt

def init_trj(pdb,xtc):
    """Helps opening a trajectory and output a universe, times and chains arrays"""
    u = mda.Universe(pdb,xtc)
    nframes = u.trajectory.n_frames
    dt = u.trajectory.dt
    units = u.trajectory.units
    protein = u.select_atoms("protein and not resname ACE and not resname NME") #contains only protein information; here is the same as all atoms
    nchains = u.select_atoms('resname ACE and name CH3').n_atoms
    natoms = protein.n_atoms
    natoms_perchain = int(natoms/nchains)
    residues = np.unique(u.residues.resnames)

    print("Trjectory of",nframes,"frames of", u.trajectory.totaltime, units['time'], "with a timestep of", dt, units['time'])
    print("There is", natoms,"total atoms (", nchains,"chains each of",natoms_perchain,"atoms )")
    print("Unique residues ", residues)

    chains = [protein[i*natoms_perchain:(i+1)*natoms_perchain] for i in range(nchains)]
    times = np.arange(0,u.trajectory.totaltime+dt,dt)

    # allresids = protein.residues
    # nres = int(len(allresids)/nchains)
    # chainresids = [allresids[i*nres:(i+1)*nres] for i in range(nchains)]

    return u,times,chains

def plot_timeseries(ax,a,times,name):
    aveR = np.mean(a,axis=0)
    stdR = np.std(a,axis=0)

    for R in a: 
        ax.plot(times, R, alpha=0.2, c='b')
    ax.errorbar(times[::5],aveR[::5],stdR[::5],capsize=3, c='r', label='average')
    ax.set_xlabel("Time [ps]")
    ax.set_ylabel(f"{name} [$\AA$]")
    ax.set_title(f"{name} vs Time")
    # ax[0].grid(True)

def plot_histo(ax,a,nframes,bins=50):
    # flatting out list of as and only looking at the second part of the trajectory
    hlen = int(nframes/2)
    a_flat = [i for j in a for i in j[hlen:]]
    # h,b = np.histogram(a_flat,bins=50)
    # ax[1].barh(b[:-1],h,color='b')
    ax.hist(a_flat, bins=bins, orientation="horizontal")
    ax.set_xlabel('Count')
    # ax[1].grid(True)
    ax.set_title("Distribution")

def save_png(fig,name,dpi=150):
    plt.savefig(name,dpi=dpi,bbox_inches='tight')