# PDEs_Simulations
A repository containing a Python code that showcases the power of numerical simulations in solving PDEs, using inviscid Burgers' equation as a particular example.
Download the repository: 

$git clone https://github.com/elimboto/pde_simulations.git 

Run the code:

$ipython burgers.py


Requirements

You need a working installation of https://github.com/hplgit/scitools]python-scitools. Python Scitools works best with Python 2.7.x.

If you are using Debian, or a Debian based platform like Ubuntu-Linux, you can install scitools using sudo:

$sudo apt-get install python-scitools

Be cautious, that if you have another version of Python installed (say Python 3.6.x) and use it as a default Python, this way of installing Scitools may not work because it may create conflicts between the two versions, or likely to get a message "No module named scitools" when you run a code with scitools import. However, Scitools comes with a lot of other packages, system wide installation is not recommended since this may break your system and render parts of it unusable due to changes that Scitools will make.

You can make scitools install by specifying location:

$python setup.py install --prefix=/path/to/install/directory

Then setup the PYTHONPATH to include the path where the package is installed, in the ~/.bashrc (.bash_profile), like,

export PYTHONPATH=/path/to/install/directory:$PYTHONPATH

This will enable Python and other packages to find scitools from wherever folder you have installed it.

If you only have Python 2.7 installed in your system using Anaconda distribution, you can use conda package to install scitools:

$conda install --channel johannr scitools

The best ever and safe way to install scitools is to use virtual environments -- virtualenv.


Using Virtual Python Environments


Create a Python Virtual environment, let's assume you name it "PDEs" and install scitools and any other required packages, mostly numpy.

Create folder for virtualenv:

$mkdir Enviroments

Move inside Environments folder:

$cd Environments

Make virtualenv named PDEs:

$virtualenv PDEs

Activate the virtualenv:

$source PDEs/bin/activate

Install requirements - numpy and scitools:

$pip install numpy

$git clone https://github.com/hplgit/scitools.git

$cd scitools

$python setup.py install

If your system uses Python 2.7.x, you do not need to re-install it inside virtualenv, instead create a virtualenv PDEs on fly by specifying the python version to be used with it. In our case, we want to use python 2.7, so we would run the following command:

$virtualenv -p /usr/bin/python2.7 PDEs

This is especially very important and useful if you have several Python versions installed in your system, to avoid possible problems.

Next, make directory where you will put your code, in our case, we will make a directory under /home/user/ called pde_simulations:

$mkdir  pde_simulations

Create a Python file, for example, named "burgers.py": 

$touch burgers.py

and then open it with your favourite editor/IDE to develop your code in it or cut/copy and paste. Make sure you run the code while inside the virtual environment PDEs.

You can choose between Python Matplotlib, Gnuplot, Pylab, etc., as plotting backends, see https://github.com/hplgit/scitools for customization options.

By default, plotting is done by Easyviz, http://hplgit.github.io/scitools/doc/api/html/easyviz.html, scitools.easyviz module -  a federated interface to various packages for scientific plotting and visualization.

You can then import scitools as

$from scitools.std import *

or minimally in this way, 

$import scitools.std as st

and specify it before any plotting command: st.command.

For sure, there are lot more we can do with Python Scitools such as decorating and adding controls to our plots, making movies and animations in different formats. 
Ability to make movies in different formats depends on the decoders installed in your system. 



