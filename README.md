# Tracey


Tracey is a tool to visualize and inspect data exported by the [devsim](https://www.devsim.org/) TCAD simulator.

Tracey was developed by Noe Nieto as a by-product of the [GSOC 2018 for devsim](https://github.com/misaelnieto/devsim_gsoc_2018).

![Tracey ready to be used](tracey1.png "Tracey window with file open")

## Installation

Tracey's dependencies are pygobject, Gtk+3 and matplotlib.

### Installing dependecies on Fedora (28)

```bash
sudo dnf install python3-matplotlib python3-gobject
```

### Get the code

There is no installation method yet. You have to get a copy of the code and run
it from there.

Clone the repo in your machine.

```bash
git clone git@github.com:misaelnieto/tracey.git
```

Enter the cloned folder

```bash
cd tracey
```

Run the script like this:

```bash
    ./tracey
```

Orby using python directly

```bash
python3 tracey
```


## Usage

Click con the open button and select the data file. Optionally you can especify the path to the file in the command line like this:

```bash
tracey.py path/to/devism_datafile.dat
```

## Status

As of now, tracey can list the regions, nodes, node solutions and edge solutions and the data is only shown as a datagrid.
![Tracey ready to be used](tracey2.png "Tracey window with file open from the command line")


## Further work

- Display the mesh and add 1D, 2D and 3D graphics using matplotlib.
- Export plots to png or svg.



