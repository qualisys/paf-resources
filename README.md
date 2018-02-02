# Resources for Using the Qualisys Project Automation Framework (PAF)

The purpose of the *Project Automation Framework* (PAF) is to streamline the motion capture process from data collection to the final report. This repository contains example projects that illustrate how PAF can be used to implement custom automated data collection in [Qualisys Track Manager (QTM)](http://www.qualisys.com/software/qualisys-track-manager/), and how QTM can be connected to external processing engines like Matlab, Python, and Excel.

Full documentation is available in Project Automation Framework.pdf

As of QTM version 2.17, the examples described in this document can be used without any additional licence. Note that some more advanced analysis types require a licence for the "PAF Framework Developer kit" (Article number 150300).


## Creating a QTM project based on example project

1. In QTM, select File > New Project
2. Tick the box "Use PAF module" and select the example you want to use.
3. If applicable, import project settings from another project where cameras and other hardware have already been set up.


## Examples


### Excel

#### Preparation

1. In QTM, in Project Options > Processing > TSV Export: activate "Include TSV Header", "Export time data for every frame", "Write column header" 
2. Set Project Options > Miscellaneous > Folder Options for "VB Script" to C:\Windows\System32\wscript.exe (adapt if wscript is located elsewhere on your computer).

Example tested with Office 2016


### Python

#### Preparation

1. Install Python, two options:
1.1 Install a Python distribution like Anaconda that includes all common dependencies, see https://www.anaconda.com/download/
1.2 Alternatively:
- Install Python only (see https://www.python.org/ftp/python/2.7.14/python-2.7.14.msi)
- Add numpy and lxml packages (for example using PIP, see https://packaging.python.org/tutorials/installing-packages/)
2. Install BTK, btk-0.3.0_win32.exe (see https://pypi.python.org/pypi/btk)

Example tested with Anaconda (for Python 2.7, 32bit), alternatively Python 2.7.14 (32bit) with numpy and lxml package.


### MATLAB

#### Preparation

1. In QTM, in Project Options > Processing > MATLAB Export: activate "3D Data" export
2. Set Project Options > Miscellaneous > Folder Options for "Matlab" to C:\Program Files\MATLAB\R2017b\bin\matlab.exe (adapt if a different version of Matlab is used).

Example tested with Matlab 2017b.


### Visual3D

#### Preparation

1. Install Visual3D.
2. Set Project Options > Miscellaneous > Folder Options for "Visual 3d" to C:\Program Files\Visual3D v6 x64\Visual3D.exe (adapt if Visual3D is installed at different location).

Example tested with Visual3D 6.01.18.