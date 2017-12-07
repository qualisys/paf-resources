1. INTRODUCTION
===============
The purpose of the Project Automation Framework (PAF) is to streamline the motion capture process from data collection to final report. The following examples projects illustrate how PAF can be used to customise the data collection in QTM and how QTM can be connected to external processing engines based on Matlab, Python or Excel.

Full documentation is available in Project Automation Framework.pdf

As of QTM version 2.17, the examples described in this document can be used without any additional licence. Note that some more advanced analysis types require a licence for the "PAF Framework Developer kit" (Article number 150300)


2. CREATING A QTM PROJECT BASED ON EXAMPLE PROJECT
==================================================
1. In QTM, select File > New Project
2. Tick the box "Use PAF module" and select the example you want to use.
3. If applicable, import project settings from another project where cameras and other hardware have already been set up.


3. EXCEL EXAMPLE
================
Preparation:
1. In QTM, in Project Options > Processing > TSV Export: activate "Include TSV Header", "Export time data for every frame", "Write column header" 
2. Set Project Options > Miscellaneous > Folder Options for "VB Script" to C:\Windows\System32\wscript.exe (adapt if wscript is located elsewhere on your computer).

Example tested with Office 2016


4. PYTHON EXAMPLE
=================
Preparation:
1. Install Python, two options:
1.1 Install a Python distribution like Anaconda that includes all common dependencies, see https://www.anaconda.com/download/
1.2 Alternatively:
- Install Python only (see https://www.python.org/ftp/python/2.7.14/python-2.7.14.msi)
- Add numpy and lxml packages (for example using PIP, see https://packaging.python.org/tutorials/installing-packages/)
2. Install BTK, btk-0.3.0_win32.exe (see https://pypi.python.org/pypi/btk)

Example tested with Anaconda (for Python 2.7, 32bit), alternatively Python 2.7.14 (32bit) with numpy and lxml package.


5. MATLAB EXAMPLE
=================
Preparation:
1. In QTM, in Project Options > Processing > MATLAB Export: activate "3D Data" export
2. Set Project Options > Miscellaneous > Folder Options for "Matlab" to C:\Program Files\MATLAB\R2017b\bin\matlab.exe (adapt if a different version of Matlab is used).

Example tested with Matlab 2017b.

