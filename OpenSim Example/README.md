# Preparing Qualisys data for OpenSim processing
## Preparation
1. Install OpenSim 4.1 or later from https://simtk.org/frs/index.php?group_id=91 :
   1. Create an account on SimTK, download and install OpenSim. 
   *Note: if you have force data from Type-3 force plates (Kistler) you need to use OpenSim 4.2. Scroll down on SimTK dowload page for beta version)*
2. Install Python 3.7.x (64-bit) from https://www.python.org/downloads/ or install a Python distribution such as Anaconda (create a Python 3.7 environment).
3. Follow these steps to connect Python with OpenSim: https://simtk-confluence.stanford.edu/display/OpenSim/Scripting+in+Python#ScriptinginPython-Windows

## Converting files using QTM Project Automation Framework
1. Open the project 'OpenSim Example' in QTM
2. Use the Project view in QTM (Ctrl+R) to create a person and session
3. Capture or import .qtm files
4. Make sure Project Options -> C3D Export -> Zero Force Baseline is activated
2. It is recommended to filter marker data prior to exporting it:
   1. Open each measurement
   2. Select all trajectories in the Labelled Trajectories list
   3. Right-click and select Smooth trajectory (Butterworth)
   4. To change the filter frequency, open the Trajectory Editor and change the Cutoff Frequency before applying the filter
3. Click Start Processing to run the Generate .trc and .mot Analysis.

## Converting files from command line
As an alternative to starting the conversion from QTM, you can start it from the command line using the file qtm2opensim.py (loacted in Templates folder):
> python qtm2opensim.py --c3d_dir '[c3d file path]' --c3d_file '[c3d file name]'

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
      1.  Select .mot file for dynamic file, refer to OpenSim documentation for detailed instructions.


