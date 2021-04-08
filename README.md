# Resources for Using the Qualisys Project Automation Framework (PAF)

The purpose of the ***Project Automation Framework*** (PAF) is to streamline the motion capture process from data collection to the final report. This repository contains example projects that illustrate how PAF can be used to implement custom automated data collection in [Qualisys Track Manager (QTM)](http://www.qualisys.com/software/qualisys-track-manager/), and how QTM can be connected to external processing engines. Several programs can be used for as data processing engines:
- [Excel](https://github.com/qualisys/paf-resources/tree/master/Excel%20Example)
- [Matlab](https://github.com/qualisys/paf-resources/tree/master/Matlab%20Example)
- [OpenSim](https://github.com/qualisys/paf-resources/tree/master/OpenSim%20Example)
- [Python](https://github.com/qualisys/paf-resources/tree/master/Python%20Example)
- [Theia Markerless](https://github.com/qualisys/paf-resources/tree/master/Theia%20Markerless%20Example)
- [Visual3D](https://github.com/qualisys/paf-resources/tree/master/Visual3D%20Example)

Full documentation is available at [Documentation folder](https://github.com/qualisys/paf-resources/blob/master/Documentation/Project%20Automation%20Framework%20Manual.md).

As of QTM version 2.17, the examples described in this document can be used without any additional licence. Note that some more advanced analysis types require a licence for the "PAF Framework Developer kit" (Article number 150300).

## Creating a QTM project based on example project

### Using examples from Github

1. Download .zip or clone example project from repository https://github.com/qualisys/paf-resources/
2. Unzip files (if applicable).
3. If applicable, replace Settings.qtmproj with project settings from another project where cameras and other hardware have already been set up.
4. Open the project in QTM.

### Using examples included with QTM installer

1. In QTM, select File > New Project
2. Tick the box "Use PAF module" and select the example you want to use.
3. If applicable, import project settings from another project where cameras and other hardware have already been set up.

For specific instructions see `README.md` at each example.

