# Preparing Qualisys data for Theia3D processing

1. Install [Theia](https://www.theiamarkerless.ca/) and accompanying engine.
2. In QTM, set Project Options > Miscellaneous > Folder Options for "Theia" to ```C:\Program Files\Theia\Theia3D\Theia3D.exe``` (adapt if Theia is installed at different location).
3. Install Visual3D.
4. Set Project Options > Miscellaneous > Folder Options for "Visual 3d" to ```C:\Program Files\Visual3D\Visual3D.exe``` (adapt if Visual3D is installed at different location).
5. Download data from Qualiys File Library (https://qfl.qualisys.com/#!/project/theiaexample)
6. Extract downloaded .zip file into the projects data folder "Theia Markerless Example\Data"
7. To process the data, you have to first click on **Theia and V3D Processing**
    >Note: For Theia's processing, you can change the following settings using Templates\settings.php: save workspace, filter cutoff frequency and filter type. When saving the workspace, it will create a TheiaFormatData_workspace folder in your session where each subfolder is containing the Theia workspace of a measurement. To open the workspace of a measurement, make sure that Theia is closed and double-click on the results.p3d file.

Example tested with:
 - QTM 2020.3 (build 6020)
 - Visual3D 2020.11.2
 - Theia 2020.5.970
