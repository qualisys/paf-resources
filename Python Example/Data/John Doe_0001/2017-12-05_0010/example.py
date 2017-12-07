 

import btk
from lxml import etree
import cPickle as pickle

templateDirectory = "C:\\Users\\nbr\\Documents\\iDrive\\AppTeam\\Projects\\Open PAF Framework\\Python Example\\Templates\\"
workingDirectory = "C:\\Users\\nbr\\Documents\\iDrive\\AppTeam\\Projects\\Open PAF Framework\\Python Example\\Data\\John Doe_0001\\2017-12-05_0010\\"

c3dFile = "Dynamic 1.c3d"
xmlc3dFile = c3dFile.replace(' ','_')

reader = btk.btkAcquisitionFileReader() # build a btk reader object
reader.SetFilename(workingDirectory + c3dFile) # set a filename to the reader
reader.Update()
acq = reader.GetOutput() # acq is the btk aquisition object

captureFq = acq.GetPointFrequency() # give the point frequency
frames = acq.GetPointFrameNumber() # give the number of frames

page = etree.Element('xml')
doc = etree.ElementTree(page)
filename = etree.SubElement(page, xmlc3dFile)
headElt = etree.SubElement(filename, 'Metrics')
out = etree.SubElement(headElt, 'Capture_Frequency')
out.text = str(captureFq)
out = etree.SubElement(headElt, 'Frames')
out.text = str(frames)

with open(workingDirectory + 'output.xml', 'w') as f:
    f.write(etree.tostring(doc, pretty_print=True))


