# Preparing Qualisys data for OpenSim processing
## Preparation
1. Install OpenSim 4.1 or later from https://simtk.org/frs/index.php?group_id=91 :
   1. Create an account on SimTK, download and install OpenSim. 
   *Note: if you have force data from Type-3 force plates (Kistler) you need to use OpenSim 4.2. Scroll down on SimTK dowload page for beta version.*
2. Install Python 3.7.9 (64-bit) from https://www.python.org/ftp/python/3.7.9/python-3.7.9-amd64.exe.
   1. Select the option to Add Python 3.7 to PATH and click "Install Now" in the first installation step.
   2. Verify Python installation by starting a Windows Command prompt and entering:
      > python --version
      This should return "Python 3.7.9". If not, verify that your Python installation folder is listed in Windows Environment variables -> Path
   3. Install Python packages Start a Windows command prompt and run:
      > pip install numpy
      > pip install pandas
      > pip install scipy
      > pip install matplotlib
      Matplotlib is optional, only required if you want to generate graphs to verify force data processing.
   4. Close Windows Command Prompt.
3. Connect Python with OpenSim
   1. Insert OpenSim into the System Path:
      1. Click the Windows Star icon and type "env". Click "Edit the system environment variables".
      2. Click Envrionment Variables" button at the bottom.
      3. In "System Variables", locate "Path" and click Edit.
      4. Click New and add "c:\\*OpenSim installation folder*\bin", for example: "C:\OpenSim 4.1\bin"
      5. Delete any other OpenSim Path entries.
   2. Run OpenSim setup file from command line:
      1. Open a new Windows Command Prompt
      2. Navigate to the OpenSim installation folder and locate the subfolder sdk\Python:
         >cd C:\OpenSim 4.1\sdk\Python
      3. Run the setup script:
         >python setup.py install
      4. Test the installation by typing:
         >python -c "import opensim"
         If there is no error, the installation was successful.
   Further information and other options can be found here: https://simtk-confluence.stanford.edu/display/OpenSim/Scripting+in+Python#ScriptinginPython-SettingupyourPythonscriptingenvironment (expand the section "Installing Anaconda and the "opensim" Python package")
4. Re-start QTM in case it is open


## Converting files using QTM Project Automation Framework
1. Start QTM and open the project 'OpenSim Example' in QTM
2. Use the Project view in QTM (Ctrl+R) to create a person and session or navigate to example files.
3. Capture or import .qtm files, or use demo files.
4. Make sure Project Options -> C3D Export -> Zero Force Baseline is activated
2. It is recommended to filter marker data prior to exporting it:
   1. Open each measurement
   2. Select all trajectories in the Labelled Trajectories list
   3. Right-click and select Smooth trajectory (Butterworth)
   4. To change the filter frequency, open the Trajectory Editor and change the Cutoff Frequency before applying the filter
3. Click Start Processing to run the Generate .trc and .mot Analysis.
4. Right-click the session folder in the QTM Project view, select "Open folder in explorer" and locate .trc and .mot files.
5. If the files are not generated, run the processing from the command line to get full error outputs (see next section).

## Converting files from command line
As an alternative to starting the conversion from QTM, you can start it from the command line using the file qtm2opensim.py (loacted in Templates folder):
> python qtm2opensim.py --c3d_dir "[c3d file path]" --c3d_file "[c3d file name]"

## Using the exported files in OpenSim
For detailed instructions or if you would like to use a different model, please refer to the OpenSim documentation.
1. Start OpenSim
2. Review data for one of the measurements:
   1. Select File -> Preview Experimental Data and load .trc file (marker data)
   2. Repeat for .mot file (force data)
   3. Extend the ExperimentalData nodes, use Ctrl+click to select .trc and .mot data and select Sync motions
   4. Play files to confirm that marker and force data are aligned as expected.
   5. Note: to change the orientation of the data, you can modify the settings for rotate_data_table in qtm2opensim.py
3. Use data in OpenSim:
   1. Use File -> Open Model and load the example models from OpenSim Example\Templates\OpenSim. Examples for CAST and IOR marker sets are included.
   2. Select Tools -> Scale model:
      1. Enter the subject's mass
      2. Check the box *Marker data for measurements* and select the .trc file for the static trial
      3. Check the box *Adjust Model markers* and sekect the .trc for the static trial
      4. Adjust Scale Factors and Static Pose Weights as desired
      5. Click Run
      6. You can now right-click and close the original model and use the -scaled model instead
   3. Select Tools -> Inverse Kinematics
      1. Load .trc file for dynamic file
      2. Adjust weights as desired
      3. Click Run
   4. Select Tools -> Inverse Dynamics
      1.  Refer to OpenSim documentation for detailed instructions on how to assign forces to the left/right foot: https://simtk-confluence.stanford.edu/display/OpenSim/How+to+Use+the+Inverse+Dynamics+Tool


