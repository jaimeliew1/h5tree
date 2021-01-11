# h5tree
prints hdf5 file as a tree of groups and data sets.

# Usage
h5tree is executed from the command line. Typical usage is:
```
 h5tree example.h5 
```
A typical output is:
```
           ┌attribute_descriptions (15,)
           ├attribute_names (15,)
 example.h5┤
           ├block0000┐
           │         └data (8192, 15)
           └attribute_units (15,)
```
h5tree can take multiple inputs:
```
 h5tree example1.h5 example2.h5
```
h5tree can be piped:
```
 ls *.h5 | h5tree
```
# Installation
Clone this repository, then pip install:
```
git clone https://github.com/jaimeliew1/h5tree.git
pip install h5tree
```
