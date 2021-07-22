# Preparing Qualisys data for Theia3D processing

1. Install [Theia](https://www.theiamarkerless.ca/) and accompanying engine.
2. In QTM, set Project Options > Miscellaneous > Folder Options for "Theia" to ```C:\Program Files\Theia\Theia3D\Theia3D.exe``` (adapt if Theia is installed at different location).
3. Install Visual3D.
4. Set Project Options > Miscellaneous > Folder Options for "Visual 3d" to ```C:\Program Files\Visual3D\Visual3D.exe``` (adapt if Visual3D is installed at different location).
5. Download data from Qualisys File Library (https://qfl.qualisys.com/#!/project/theiaexample)
   > Note: Example data include two persons. While **John Doe** can be used with Theia to generate .c3d files (use `Markerless Session`), **Jim Doe** does not include videos and can be used to compare marker-based and markerless data (use `Marker-based vs Markerless Comparison Session`). This sesson type expects data to be captured by combined system of video cameras and marker-based cameras where markers are places on the body for the same trial that is used to capture videos. Script is set to work with sports marker set. If other marker set is required, it is necessary to adapt the script and model files accordingly.
6. Extract downloaded .zip file into the projects data folder "Theia Markerless Example\Data"
7. To process the data, you have to first click on **Theia and V3D Processing**
    > Note: For Theia's processing, you can change the following settings using Templates\settings.php: save workspace, filter cutoff frequency and filter type. When saving the workspace, it will create a TheiaFormatData_workspace folder in your session where each subfolder is containing the Theia workspace of a measurement. To open the workspace of a measurement, click on File > Load Workspace and select the subfolder of your choice. If Theia is closed, double-click on the results.p3d included in the subfolder of your choice.

Example tested with:
 - QTM 2021.1 (build 6350)
 - Visual3D 2021.06.2
 - Theia 2021.1.1450
