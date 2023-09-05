"""
Created on: Tue Nov 29, 2016
Author:     Suraj Jaiswal
Contact:    suraj.jaiswal29@gmail.com
"""

 #-------------IMPORTING ALL THE NECESSARY MODULES FROM LIBRARY-------------#

# Importing operating system.
import os 
# Importing module to access excel application.
import openpyxl
# Importing module for tree structure to access XML file.
import xml.etree.cElementTree as ET
# Importing module to copy objects.
import copy
# Getting access to the current working directory.
os.getcwd()

 #--------------------------------------------------------------------------#

 #-----------------------ACCESSING EXCEL APPLICATION------------------------#

# Creating object for the workbook "Read_this_Excel.xlsx".
wb = openpyxl.load_workbook('Read_this_Excel.xlsx')
# Creating object for sheet-1 of the workbook in Python.
sheet1 = wb.active

 #--------------------------------------------------------------------------#
 
 #----------------------------ACCESSING XML FILE----------------------------#

# Creating object for the XML file "Tractor_Model.xml".
tree = ET.ElementTree(file = 'Tractor_Model.xml')
# Note: Here, filename can be replaced completely with the file location.
# Creating object for the root of the tree used in the XML file.
root = tree.getroot()

 #--------------------------------------------------------------------------#

 #------------------------------ENGINE MODELING-----------------------------#
 
                   # MODELING MAXIMUM TORQUE OF THE ENGINE

# ".iter" iterates recursively over all the sub-tree below the main tree.                     
for splines in root.iter('Splines'):
    for engineSpline in splines:
        if ((engineSpline.tag == 'Spline_Engine-1')
        or (engineSpline.tag == 'Spline_Engine-2')
        or (engineSpline.tag == 'Spline_Engine-3')):
            if (str(sheet1['D3'].value) == 'Engine-1'):
                # Changing the tag name first and then proceeding.
                engineSpline.tag = 'Spline_Engine-1'
                for child in engineSpline.iter('x'):
                    child.set('x1', '0')
                    child.set('x2', '90')
                    child.set('x3', '100')
                    child.set('x4', '129')
                    child.set('x5', '156')
                    child.set('x6', '160')
                    child.set('x7', '195')
                    child.set('x8', '200')
                    child.set('x9', '220')
                for child in engineSpline.iter('y'):
                    child.set('y1', '200')
                    child.set('y2', '603')
                    child.set('y3', '675')
                    child.set('y4', '763')
                    child.set('y5', '764')
                    child.set('y6', '770')
                    child.set('y7', '600')
                    child.set('y8', '575')
                    child.set('y9', '513')
            elif (str(sheet1['D3'].value) == 'Engine-2'):
                # Changing the tag name first and then proceeding.
                engineSpline.tag = 'Spline_Engine-2'
                for child in engineSpline.iter('x'):
                    child.set('x1', '0')
                    child.set('x2', '90')
                    child.set('x3', '100')
                    child.set('x4', '120')
                    child.set('x5', '150')
                    child.set('x6', '160')
                    child.set('x7', '180')
                    child.set('x8', '200')
                    child.set('x9', '220')
                for child in engineSpline.iter('y'):
                    child.set('y1', '200')
                    child.set('y2', '603')
                    child.set('y3', '675')
                    child.set('y4', '713')
                    child.set('y5', '730')
                    child.set('y6', '750')
                    child.set('y7', '640')
                    child.set('y8', '540')
                    child.set('y9', '460')
            elif (str(sheet1['D3'].value) == 'Engine-3'):
                # Changing the tag name first and then proceeding.
                engineSpline.tag = 'Spline_Engine-3'
                for child in engineSpline.iter('x'):
                    child.set('x1', '0')
                    child.set('x2', '90')
                    child.set('x3', '100')
                    child.set('x4', '120')
                    child.set('x5', '140')
                    child.set('x6', '160')
                    child.set('x7', '165')
                    child.set('x8', '179')
                    child.set('x9', '188')
                for child in engineSpline.iter('y'):
                    child.set('y1', '268')
                    child.set('y2', '628')
                    child.set('y3', '668')
                    child.set('y4', '668')
                    child.set('y5', '669')
                    child.set('y6', '680')
                    child.set('y7', '650')
                    child.set('y8', '587')
                    child.set('y9', '520')
for motor in root.iter('Motor'):
    for engine in motor:
        if ((engine.tag == 'Engine-1')
        or (engine.tag == 'Engine-2')
        or (engine.tag == 'Engine-3')):
            if (str(sheet1['D3'].value) == 'Engine-1'):
                engine.tag = 'Engine-1'
                engine.set('SplName', 'Spline_Engine-1')
            elif (str(sheet1['D3'].value) == 'Engine-2'):
                engine.tag = 'Engine-2'
                engine.set('SplName', 'Spline_Engine-2')
            elif (str(sheet1['D3'].value) == 'Engine-3'):
                engine.tag = 'Engine-3'
                engine.set('SplName', 'Spline_Engine-3')        
for clutch in root.iter('Clutch'):
    clutch.set('Input', engine.tag)
for engine_Input in root.iter('Engine_Input'):
    engine_Input.set('PrimName', engine.tag)

                # MODELING MAXIMUM BRAKING TORQUE FOR THE ENGINE

for motor in root.iter('Motor'):
    for volvo_D6E in motor:
        if ((volvo_D6E.tag == 'Volvo_D6E_LAE3')
        or (volvo_D6E.tag == 'Volvo_D6E_LBE3')
        or (volvo_D6E.tag == 'Volvo_D6E_LCE3')):
            if (str(sheet1['D4'].value) == "5000 Nm"):
                volvo_D6E.set('MbrMax', '0.5e4')
            elif (str(sheet1['D4'].value) == "15000 Nm"):
                volvo_D6E.set('MbrMax', '1.5e4')
            elif (str(sheet1['D4'].value) == "25000 Nm"):
                volvo_D6E.set('MbrMax', '2.5e4')
            elif (str(sheet1['D4'].value) == "35000 Nm"):
                volvo_D6E.set('MbrMax', '3.5e4')
            elif (str(sheet1['D4'].value) == "45000 Nm"):
                volvo_D6E.set('MbrMax', '4.5e4')
            else:
                volvo_D6E.set('MbrMax', '0')

 #--------------------------------------------------------------------------#

 #-----------------------------GEARBOX MODELING-----------------------------#

for gears in root.iter('Gears'):
    # MODELING FORWARD GEARS
    for gearbox in gears.iter('Gearbox'):
        if (str(sheet1['D5'].value) == "6"):
            gearbox.set('ngearf', '6')
            gearbox.set('ifw0', '3.58')
            gearbox.set('ifw1', '2.61')
            gearbox.set('ifw2', '1.89')
            gearbox.set('ifw3', '1.38')
            gearbox.set('ifw4', '1')
            gearbox.set('ifw5', '0.73')
        if (str(sheet1['D5'].value) == "5"):
            gearbox.set('ngearf', '5')
            gearbox.set('ifw0', '3.58')
            gearbox.set('ifw1', '2.61')
            gearbox.set('ifw2', '1.89')
            gearbox.set('ifw3', '1.38')
            gearbox.set('ifw4', '1')
            gearbox.set('ifw5', '')
        if (str(sheet1['D5'].value) == "4"):
            gearbox.set('ngearf', '4')
            gearbox.set('ifw0', '3.58')
            gearbox.set('ifw1', '2.61')
            gearbox.set('ifw2', '1.89')
            gearbox.set('ifw3', '1.38')
            gearbox.set('ifw4', '')
            gearbox.set('ifw5', '')
    # MODELING REVERSE GEARS
    for gearbox in gears.iter('Gearbox'):
        if (str(sheet1['D6'].value) == "3"):
            gearbox.set('ngearr', '3')
            gearbox.set('ibw0', '4')
            gearbox.set('ibw1', '2.05')
            gearbox.set('ibw2', '1.07')
        if (str(sheet1['D6'].value) == "2"):
            gearbox.set('ngearr', '2')
            gearbox.set('ibw0', '4')
            gearbox.set('ibw1', '2.05')
            gearbox.set('ibw2', '')
        if (str(sheet1['D6'].value) == "1"):
            gearbox.set('ngearr', '1')
            gearbox.set('ibw0', '4')
            gearbox.set('ibw1', '')
            gearbox.set('ibw2', '')

 #--------------------------------------------------------------------------#

 #------------------------------TYRE MODELING-------------------------------#           

                         # MODELING OF FRONT TYRES

if (str(sheet1['D10'].value) == '2'):
    for spline_FrontTyres in root.iter('Spline_FrontTyres'):
        spline_FrontTyres.set('NPoints', '3')
        for child in spline_FrontTyres.iter('x'):
            if (str(sheet1['D7'].value) == "600/70R28"):
                child.set('x1', str(-(600/2000)))
                child.set('x3', str(600/2000))
                child.set('x4', '0')
                child.set('x5', '0')
                child.set('x6', '0')
            elif (str(sheet1['D7'].value) == "420/85R28"):
                child.set('x1', str(-(440/2000)))
                child.set('x3', str(440/2000))
                child.set('x4', '0')
                child.set('x5', '0')
                child.set('x6', '0')                
            elif (str(sheet1['D7'].value) == "480/70R28"):
                child.set('x1', str(-(482/2000)))
                child.set('x3', str(482/2000))
                child.set('x4', '0')
                child.set('x5', '0')
                child.set('x6', '0')
            elif (str(sheet1['D7'].value) == "540/65R28"):
                child.set('x1', str(-(540/2000)))
                child.set('x3', str(540/2000))
                child.set('x4', '0')
                child.set('x5', '0')
                child.set('x6', '0')
            elif (str(sheet1['D7'].value) == "600/65R28"):
                child.set('x1', str(-(600/2000)))
                child.set('x3', str(600/2000))
                child.set('x4', '0')
                child.set('x5', '0')
                child.set('x6', '0')
        for child in spline_FrontTyres.iter('y'):
            if (str(sheet1['D7'].value) == "600/70R28"):
                child.set('y1', str(1552/2000))
                child.set('y2', str(1552/2000))
                child.set('y3', str(1552/2000))
                child.set('y4', '0')
                child.set('y5', '0')
                child.set('y6', '0')
            elif (str(sheet1['D7'].value) == "420/85R28"):
                child.set('y1', str(1426/2000))
                child.set('y2', str(1426/2000))
                child.set('y3', str(1426/2000))
                child.set('y4', '0')
                child.set('y5', '0')
                child.set('y6', '0')
            elif (str(sheet1['D7'].value) == "480/70R28"):
                child.set('y1', str(1424/2000))
                child.set('y2', str(1424/2000))
                child.set('y3', str(1424/2000))
                child.set('y4', '0')
                child.set('y5', '0')
                child.set('y6', '0')
            elif (str(sheet1['D7'].value) == "540/65R28"):
                child.set('y1', str(1414/2000))
                child.set('y2', str(1414/2000))
                child.set('y3', str(1414/2000))
                child.set('y4', '0')
                child.set('y5', '0')
                child.set('y6', '0')
            elif (str(sheet1['D7'].value) == "600/65R28"):
                child.set('y1', str(1492/2000))
                child.set('y2', str(1492/2000))
                child.set('y3', str(1492/2000))
                child.set('y4', '0')
                child.set('y5', '0')
                child.set('y6', '0')
    for graphics in root.iter('Graphics'):
        graphics_ExtraFrontTyreL = graphics.find ('Graphics_ExtraFrontTyreL')
        if (graphics_ExtraFrontTyreL == None):
            print("FL-Do nothing")
        else:
            # Removing a particular object.
            graphics.remove(graphics_ExtraFrontTyreL)
        
        graphics_ExtraFrontTyreR = graphics.find ('Graphics_ExtraFrontTyreR')
        if (graphics_ExtraFrontTyreR == None):
            print("FR-Do nothing")
        else:
            # Removing a particular object.
            graphics.remove(graphics_ExtraFrontTyreR)
     
    for dummy_FrontTyreL in root.iter('Dummy_FrontTyreL'):
        dummy_FrontTyreL.set('VisualizationGraphics', 'Graphics_FrontTyreL')
        inertia = dummy_FrontTyreL.find ('Inertia')
        i = inertia.find ('I')
        if (str(sheet1['D7'].value) == "600/70R28"):
            if (str(sheet1['D11'].value) == "150 kg"):
                inertia.set('mass', '150')
                i.set('Ixx', '31.823526')
                i.set('Iyy', '31.823526')
                i.set('Izz', '54.647052')
            elif (str(sheet1['D11'].value) == "175 kg"):
                inertia.set('mass', '175')
                i.set('Ixx', '37.127447')
                i.set('Iyy', '37.127447')
                i.set('Izz', '63.754894')
            elif (str(sheet1['D11'].value) == "200 kg"):
                inertia.set('mass', '200')
                i.set('Ixx', '42.431368')
                i.set('Iyy', '42.431368')
                i.set('Izz', '72.862736')
            elif (str(sheet1['D11'].value) == "225 kg"):
                inertia.set('mass', '225')
                i.set('Ixx', '47.735289')
                i.set('Iyy', '47.735289')
                i.set('Izz', '81.970578')
            elif (str(sheet1['D11'].value) == "250 kg"):
                inertia.set('mass', '250')
                i.set('Ixx', '53.03921')
                i.set('Iyy', '53.03921')
                i.set('Izz', '91.07842')
        elif (str(sheet1['D7'].value) == "420/85R28"):
            if (str(sheet1['D11'].value) == "150 kg"):
                inertia.set('mass', '150')
                i.set('Ixx', '26.2257635')
                i.set('Iyy', '26.2257635')
                i.set('Izz', '47.611527')
            elif (str(sheet1['D11'].value) == "175 kg"):
                inertia.set('mass', '175')
                i.set('Ixx', '30.596724083333335')
                i.set('Iyy', '30.596724083333335')
                i.set('Izz', '55.5467815')
            elif (str(sheet1['D11'].value) == "200 kg"):
                inertia.set('mass', '200')
                i.set('Ixx', '34.967684666666671')
                i.set('Iyy', '34.967684666666671')
                i.set('Izz', '63.482036')
            elif (str(sheet1['D11'].value) == "225 kg"):
                inertia.set('mass', '225')
                i.set('Ixx', '39.33864525')
                i.set('Iyy', '39.33864525')
                i.set('Izz', '71.4172905')
            elif (str(sheet1['D11'].value) == "250 kg"):
                inertia.set('mass', '250')
                i.set('Ixx', '43.709605833333327')
                i.set('Iyy', '43.709605833333327')
                i.set('Izz', '79.352545')
        elif (str(sheet1['D7'].value) == "480/70R28"):
            if (str(sheet1['D11'].value) == "150 kg"):
                inertia.set('mass', '150')
                i.set('Ixx', '26.656376')
                i.set('Iyy', '26.656376')
                i.set('Izz', '47.504652')
            elif (str(sheet1['D11'].value) == "175 kg"):
                inertia.set('mass', '175')
                i.set('Ixx', '31.099105333333334')
                i.set('Iyy', '31.099105333333334')
                i.set('Izz', '55.422094')
            elif (str(sheet1['D11'].value) == "200 kg"):
                inertia.set('mass', '200')
                i.set('Ixx', '35.541834666666666')
                i.set('Iyy', '35.541834666666666')
                i.set('Izz', '63.339536')
            elif (str(sheet1['D11'].value) == "225 kg"):
                inertia.set('mass', '225')
                i.set('Ixx', '39.984564')
                i.set('Iyy', '39.984564')
                i.set('Izz', '71.256978')
            elif (str(sheet1['D11'].value) == "250 kg"):
                inertia.set('mass', '250')
                i.set('Ixx', '44.427293333333331')
                i.set('Iyy', '44.427293333333331')
                i.set('Izz', '79.17442')
        elif (str(sheet1['D7'].value) == "540/65R28"):
            if (str(sheet1['D11'].value) == "150 kg"):
                inertia.set('mass', '150')
                i.set('Ixx', '27.1312635')
                i.set('Iyy', '27.1312635')
                i.set('Izz', '46.972527')
            elif (str(sheet1['D11'].value) == "175 kg"):
                inertia.set('mass', '175')
                i.set('Ixx', '31.65314075')
                i.set('Iyy', '31.65314075')
                i.set('Izz', '54.8012815')
            elif (str(sheet1['D11'].value) == "200 kg"):
                inertia.set('mass', '200')
                i.set('Ixx', '36.175018')
                i.set('Iyy', '36.175018')
                i.set('Izz', '62.630036')
            elif (str(sheet1['D11'].value) == "225 kg"):
                inertia.set('mass', '225')
                i.set('Ixx', '40.69689525')
                i.set('Iyy', '40.69689525')
                i.set('Izz', '70.4587905')
            elif (str(sheet1['D11'].value) == "250 kg"):
                inertia.set('mass', '250')
                i.set('Ixx', '45.2187725')
                i.set('Iyy', '45.2187725')
                i.set('Izz', '78.287545')
        elif (str(sheet1['D7'].value) == "600/65R28"):
            if (str(sheet1['D11'].value) == "150 kg"):
                inertia.set('mass', '150')
                i.set('Ixx', '30.111276')
                i.set('Iyy', '30.111276')
                i.set('Izz', '51.222552')
            elif (str(sheet1['D11'].value) == "175 kg"):
                inertia.set('mass', '175')
                i.set('Ixx', '35.129822')
                i.set('Iyy', '35.129822')
                i.set('Izz', '59.759644')
            elif (str(sheet1['D11'].value) == "200 kg"):
                inertia.set('mass', '200')
                i.set('Ixx', '40.148368')
                i.set('Iyy', '40.148368')
                i.set('Izz', '68.296736')
            elif (str(sheet1['D11'].value) == "225 kg"):
                inertia.set('mass', '225')
                i.set('Ixx', '45.166914')
                i.set('Iyy', '45.166914')
                i.set('Izz', '76.833828')
            elif (str(sheet1['D11'].value) == "250 kg"):
                inertia.set('mass', '250')
                i.set('Ixx', '50.18546')
                i.set('Iyy', '50.18546')
                i.set('Izz', '85.37092')
    
    for dummy_FrontTyreR in root.iter('Dummy_FrontTyreR'):
        dummy_FrontTyreR.set('VisualizationGraphics', 'Graphics_FrontTyreR')
        inertia = dummy_FrontTyreR.find ('Inertia')
        i = inertia.find ('I')
        if (str(sheet1['D7'].value) == "600/70R28"):
            if (str(sheet1['D11'].value) == "150 kg"):
                inertia.set('mass', '150')
                i.set('Ixx', '31.823526')
                i.set('Iyy', '31.823526')
                i.set('Izz', '54.647052')
            elif (str(sheet1['D11'].value) == "175 kg"):
                inertia.set('mass', '175')
                i.set('Ixx', '37.127447')
                i.set('Iyy', '37.127447')
                i.set('Izz', '63.754894')
            elif (str(sheet1['D11'].value) == "200 kg"):
                inertia.set('mass', '200')
                i.set('Ixx', '42.431368')
                i.set('Iyy', '42.431368')
                i.set('Izz', '72.862736')
            elif (str(sheet1['D11'].value) == "225 kg"):
                inertia.set('mass', '225')
                i.set('Ixx', '47.735289')
                i.set('Iyy', '47.735289')
                i.set('Izz', '81.970578')
            elif (str(sheet1['D11'].value) == "250 kg"):
                inertia.set('mass', '250')
                i.set('Ixx', '53.03921')
                i.set('Iyy', '53.03921')
                i.set('Izz', '91.07842')
        elif (str(sheet1['D7'].value) == "420/85R28"):
            if (str(sheet1['D11'].value) == "150 kg"):
                inertia.set('mass', '150')
                i.set('Ixx', '26.2257635')
                i.set('Iyy', '26.2257635')
                i.set('Izz', '47.611527')
            elif (str(sheet1['D11'].value) == "175 kg"):
                inertia.set('mass', '175')
                i.set('Ixx', '30.596724083333335')
                i.set('Iyy', '30.596724083333335')
                i.set('Izz', '55.5467815')
            elif (str(sheet1['D11'].value) == "200 kg"):
                inertia.set('mass', '200')
                i.set('Ixx', '34.967684666666671')
                i.set('Iyy', '34.967684666666671')
                i.set('Izz', '63.482036')
            elif (str(sheet1['D11'].value) == "225 kg"):
                inertia.set('mass', '225')
                i.set('Ixx', '39.33864525')
                i.set('Iyy', '39.33864525')
                i.set('Izz', '71.4172905')
            elif (str(sheet1['D11'].value) == "250 kg"):
                inertia.set('mass', '250')
                i.set('Ixx', '43.709605833333327')
                i.set('Iyy', '43.709605833333327')
                i.set('Izz', '79.352545')
        elif (str(sheet1['D7'].value) == "480/70R28"):
            if (str(sheet1['D11'].value) == "150 kg"):
                inertia.set('mass', '150')
                i.set('Ixx', '26.656376')
                i.set('Iyy', '26.656376')
                i.set('Izz', '47.504652')
            elif (str(sheet1['D11'].value) == "175 kg"):
                inertia.set('mass', '175')
                i.set('Ixx', '31.099105333333334')
                i.set('Iyy', '31.099105333333334')
                i.set('Izz', '55.422094')
            elif (str(sheet1['D11'].value) == "200 kg"):
                inertia.set('mass', '200')
                i.set('Ixx', '35.541834666666666')
                i.set('Iyy', '35.541834666666666')
                i.set('Izz', '63.339536')
            elif (str(sheet1['D11'].value) == "225 kg"):
                inertia.set('mass', '225')
                i.set('Ixx', '39.984564')
                i.set('Iyy', '39.984564')
                i.set('Izz', '71.256978')
            elif (str(sheet1['D11'].value) == "250 kg"):
                inertia.set('mass', '250')
                i.set('Ixx', '44.427293333333331')
                i.set('Iyy', '44.427293333333331')
                i.set('Izz', '79.17442')
        elif (str(sheet1['D7'].value) == "540/65R28"):
            if (str(sheet1['D11'].value) == "150 kg"):
                inertia.set('mass', '150')
                i.set('Ixx', '27.1312635')
                i.set('Iyy', '27.1312635')
                i.set('Izz', '46.972527')
            elif (str(sheet1['D11'].value) == "175 kg"):
                inertia.set('mass', '175')
                i.set('Ixx', '31.65314075')
                i.set('Iyy', '31.65314075')
                i.set('Izz', '54.8012815')
            elif (str(sheet1['D11'].value) == "200 kg"):
                inertia.set('mass', '200')
                i.set('Ixx', '36.175018')
                i.set('Iyy', '36.175018')
                i.set('Izz', '62.630036')
            elif (str(sheet1['D11'].value) == "225 kg"):
                inertia.set('mass', '225')
                i.set('Ixx', '40.69689525')
                i.set('Iyy', '40.69689525')
                i.set('Izz', '70.4587905')
            elif (str(sheet1['D11'].value) == "250 kg"):
                inertia.set('mass', '250')
                i.set('Ixx', '45.2187725')
                i.set('Iyy', '45.2187725')
                i.set('Izz', '78.287545')
        elif (str(sheet1['D7'].value) == "600/65R28"):
            if (str(sheet1['D11'].value) == "150 kg"):
                inertia.set('mass', '150')
                i.set('Ixx', '30.111276')
                i.set('Iyy', '30.111276')
                i.set('Izz', '51.222552')
            elif (str(sheet1['D11'].value) == "175 kg"):
                inertia.set('mass', '175')
                i.set('Ixx', '35.129822')
                i.set('Iyy', '35.129822')
                i.set('Izz', '59.759644')
            elif (str(sheet1['D11'].value) == "200 kg"):
                inertia.set('mass', '200')
                i.set('Ixx', '40.148368')
                i.set('Iyy', '40.148368')
                i.set('Izz', '68.296736')
            elif (str(sheet1['D11'].value) == "225 kg"):
                inertia.set('mass', '225')
                i.set('Ixx', '45.166914')
                i.set('Iyy', '45.166914')
                i.set('Izz', '76.833828')
            elif (str(sheet1['D11'].value) == "250 kg"):
                inertia.set('mass', '250')
                i.set('Ixx', '50.18546')
                i.set('Iyy', '50.18546')
                i.set('Izz', '85.37092')                

elif (str(sheet1['D10'].value) == '4'):
    for spline_FrontTyres in root.iter('Spline_FrontTyres'):
        spline_FrontTyres.set('NPoints', '6')
        for child in spline_FrontTyres.iter('x'):
            if (str(sheet1['D7'].value) == "600/70R28"):
                child.set('x1', str(-(600/2000)))
                child.set('x3', str(600/2000))
                child.set('x4', str((600/2000)+(50/1000)))
                child.set('x5', str((600/2000)+(50/1000)+(600/2000)))
                child.set('x6', str((600/2000)+(50/1000)+(600/1000)))
            elif (str(sheet1['D7'].value) == "420/85R28"):
                child.set('x1', str(-(440/2000)))
                child.set('x3', str(440/2000))
                child.set('x4', str((440/2000)+(50/1000)))
                child.set('x5', str((440/2000)+(50/1000)+(440/2000)))
                child.set('x6', str((440/2000)+(50/1000)+(440/1000)))                
            elif (str(sheet1['D7'].value) == "480/70R28"):
                child.set('x1', str(-(482/2000)))
                child.set('x3', str(482/2000))
                child.set('x4', str((482/2000)+(50/1000)))
                child.set('x5', str((482/2000)+(50/1000)+(482/2000)))
                child.set('x6', str((482/2000)+(50/1000)+(482/1000)))
            elif (str(sheet1['D7'].value) == "540/65R28"):
                child.set('x1', str(-(540/2000)))
                child.set('x3', str(540/2000))
                child.set('x4', str((540/2000)+(50/1000)))
                child.set('x5', str((540/2000)+(50/1000)+(540/2000)))
                child.set('x6', str((540/2000)+(50/1000)+(540/1000)))
            elif (str(sheet1['D7'].value) == "600/65R28"):
                child.set('x1', str(-(600/2000)))
                child.set('x3', str(600/2000))
                child.set('x4', str((600/2000)+(50/1000)))
                child.set('x5', str((600/2000)+(50/1000)+(600/2000)))
                child.set('x6', str((600/2000)+(50/1000)+(600/1000)))
        for child in spline_FrontTyres.iter('y'):
            if (str(sheet1['D7'].value) == "600/70R28"):
                child.set('y1', str(1552/2000))
                child.set('y2', str(1552/2000))
                child.set('y3', str(1552/2000))
                child.set('y4', str(1552/2000))
                child.set('y5', str(1552/2000))
                child.set('y6', str(1552/2000))
            elif (str(sheet1['D7'].value) == "420/85R28"):
                child.set('y1', str(1426/2000))
                child.set('y2', str(1426/2000))
                child.set('y3', str(1426/2000))
                child.set('y4', str(1426/2000))
                child.set('y5', str(1426/2000))
                child.set('y6', str(1426/2000))
            elif (str(sheet1['D7'].value) == "480/70R28"):
                child.set('y1', str(1424/2000))
                child.set('y2', str(1424/2000))
                child.set('y3', str(1424/2000))
                child.set('y4', str(1424/2000))
                child.set('y5', str(1424/2000))
                child.set('y6', str(1424/2000))
            elif (str(sheet1['D7'].value) == "540/65R28"):
                child.set('y1', str(1414/2000))
                child.set('y2', str(1414/2000))
                child.set('y3', str(1414/2000))
                child.set('y4', str(1414/2000))
                child.set('y5', str(1414/2000))
                child.set('y6', str(1414/2000))
            elif (str(sheet1['D7'].value) == "600/65R28"):
                child.set('y1', str(1492/2000))
                child.set('y2', str(1492/2000))
                child.set('y3', str(1492/2000))
                child.set('y4', str(1492/2000))
                child.set('y5', str(1492/2000))
                child.set('y6', str(1492/2000))
    for graphics in root.iter('Graphics'):
        graphics_ExtraFrontTyreL = graphics.find ('Graphics_ExtraFrontTyreL')
        if (graphics_ExtraFrontTyreL != None):
            position = graphics_ExtraFrontTyreL.find ('Position')
            if (str(sheet1['D7'].value) == "600/70R28"):
                position.set('z', str((600/1000)+(50/1000)))
            elif (str(sheet1['D7'].value) == "420/85R28"):
                position.set('z', str((440/1000)+(50/1000)))
            elif (str(sheet1['D7'].value) == "480/70R28"):
                position.set('z', str((482/1000)+(50/1000)))
            elif (str(sheet1['D7'].value) == "540/65R28"):
                position.set('z', str((540/1000)+(50/1000)))
            elif (str(sheet1['D7'].value) == "600/65R28"):
                position.set('z', str((600/1000)+(50/1000)))
        else:
            graphics_FrontTyreL = graphics.find ('Graphics_FrontTyreL')
            # Copying the same attributes to a new object.
            # ".deepcopy" creates a second object.
            graphics_ExtraFrontTyreL = copy.deepcopy(graphics_FrontTyreL)
            # Replacing the tag name with a new name.
            graphics_ExtraFrontTyreL.tag = "Graphics_ExtraFrontTyreL"
            position = graphics_ExtraFrontTyreL.find ('Position')
            if (str(sheet1['D7'].value) == "600/70R28"):
                position.set('z', str((600/1000)+(50/1000)))
            elif (str(sheet1['D7'].value) == "420/85R28"):
                position.set('z', str((440/1000)+(50/1000)))
            elif (str(sheet1['D7'].value) == "480/70R28"):
                position.set('z', str((482/1000)+(50/1000)))
            elif (str(sheet1['D7'].value) == "540/65R28"):
                position.set('z', str((540/1000)+(50/1000)))
            elif (str(sheet1['D7'].value) == "600/65R28"):
                position.set('z', str((600/1000)+(50/1000)))
            graphics.insert(13, graphics_ExtraFrontTyreL)
            # Inserting this element at that particular location of index 13.
            # That means the 14th position.

        graphics_ExtraFrontTyreR = graphics.find ('Graphics_ExtraFrontTyreR')
        if (graphics_ExtraFrontTyreR != None):
            position = graphics_ExtraFrontTyreR.find ('Position')
            if (str(sheet1['D7'].value) == "600/70R28"):
                position.set('z', str((600/1000)+(50/1000)))
            elif (str(sheet1['D7'].value) == "420/85R28"):
                position.set('z', str((440/1000)+(50/1000)))
            elif (str(sheet1['D7'].value) == "480/70R28"):
                position.set('z', str((482/1000)+(50/1000)))
            elif (str(sheet1['D7'].value) == "540/65R28"):
                position.set('z', str((540/1000)+(50/1000)))
            elif (str(sheet1['D7'].value) == "600/65R28"):
                position.set('z', str((600/1000)+(50/1000)))
        else:
            graphics_FrontTyreR = graphics.find ('Graphics_FrontTyreR')
            # Copying the same attributes to a new object.
            # ".deepcopy" creates a second object.
            graphics_ExtraFrontTyreR = copy.deepcopy(graphics_FrontTyreR)
            # Replacing the tag name with a new name.
            graphics_ExtraFrontTyreR.tag = "Graphics_ExtraFrontTyreR"
            position = graphics_ExtraFrontTyreR.find ('Position')
            if (str(sheet1['D7'].value) == "600/70R28"):
                position.set('z', str((600/1000)+(50/1000)))
            elif (str(sheet1['D7'].value) == "420/85R28"):
                position.set('z', str((440/1000)+(50/1000)))
            elif (str(sheet1['D7'].value) == "480/70R28"):
                position.set('z', str((482/1000)+(50/1000)))
            elif (str(sheet1['D7'].value) == "540/65R28"):
                position.set('z', str((540/1000)+(50/1000)))
            elif (str(sheet1['D7'].value) == "600/65R28"):
                position.set('z', str((600/1000)+(50/1000)))
            graphics.insert(14, graphics_ExtraFrontTyreR)
            # Inserting this element at that particular location of index 14.
            # That means the 15th position.

    for dummy_FrontTyreL in root.iter('Dummy_FrontTyreL'):
        dummy_FrontTyreL.set('VisualizationGraphics', 
        'Graphics_FrontTyreL;Graphics_ExtraFrontTyreL')
        inertia = dummy_FrontTyreL.find ('Inertia')
        i = inertia.find ('I')
        if (str(sheet1['D7'].value) == "600/70R28"):
            if (str(sheet1['D11'].value) == "150 kg"):
                inertia.set('mass', '300')
                i.set('Ixx', '90.647052')
                i.set('Iyy', '90.647052')
                i.set('Izz', '109.294104')
            elif (str(sheet1['D11'].value) == "175 kg"):
                inertia.set('mass', '350')
                i.set('Ixx', '105.754894')
                i.set('Iyy', '105.754894')
                i.set('Izz', '127.509788')
            elif (str(sheet1['D11'].value) == "200 kg"):
                inertia.set('mass', '400')
                i.set('Ixx', '120.862736')
                i.set('Iyy', '120.862736')
                i.set('Izz', '145.725472')
            elif (str(sheet1['D11'].value) == "225 kg"):
                inertia.set('mass', '450')
                i.set('Ixx', '135.970578')
                i.set('Iyy', '135.970578')
                i.set('Izz', '163.941156')
            elif (str(sheet1['D11'].value) == "250 kg"):
                inertia.set('mass', '500')
                i.set('Ixx', '151.07842')
                i.set('Iyy', '151.07842')
                i.set('Izz', '182.15684')
        elif (str(sheet1['D7'].value) == "420/85R28"):
            if (str(sheet1['D11'].value) == "150 kg"):
                inertia.set('mass', '300')
                i.set('Ixx', '66.971527')
                i.set('Iyy', '66.971527')
                i.set('Izz', '95.223054')
            elif (str(sheet1['D11'].value) == "175 kg"):
                inertia.set('mass', '350')
                i.set('Ixx', '78.133448166666668')
                i.set('Iyy', '78.133448166666668')
                i.set('Izz', '111.093563')
            elif (str(sheet1['D11'].value) == "200 kg"):
                inertia.set('mass', '400')
                i.set('Ixx', '89.29536933333334')
                i.set('Iyy', '89.29536933333334')
                i.set('Izz', '126.964072')
            elif (str(sheet1['D11'].value) == "225 kg"):
                inertia.set('mass', '450')
                i.set('Ixx', '100.4572905')
                i.set('Iyy', '100.4572905')
                i.set('Izz', '142.834581')
            elif (str(sheet1['D11'].value) == "250 kg"):
                inertia.set('mass', '500')
                i.set('Ixx', '111.61921166666666')
                i.set('Iyy', '111.61921166666666')
                i.set('Izz', '158.70509')
        elif (str(sheet1['D7'].value) == "480/70R28"):
            if (str(sheet1['D11'].value) == "150 kg"):
                inertia.set('mass', '300')
                i.set('Ixx', '70.737052')
                i.set('Iyy', '70.737052')
                i.set('Izz', '95.009304')
            elif (str(sheet1['D11'].value) == "175 kg"):
                inertia.set('mass', '350')
                i.set('Ixx', '82.526560666666668')
                i.set('Iyy', '82.526560666666668')
                i.set('Izz', '110.844188')
            elif (str(sheet1['D11'].value) == "200 kg"):
                inertia.set('mass', '400')
                i.set('Ixx', '94.316069333333346')
                i.set('Iyy', '94.316069333333346')
                i.set('Izz', '126.679072')
            elif (str(sheet1['D11'].value) == "225 kg"):
                inertia.set('mass', '450')
                i.set('Ixx', '106.105578')
                i.set('Iyy', '106.105578')
                i.set('Izz', '142.513956')
            elif (str(sheet1['D11'].value) == "250 kg"):
                inertia.set('mass', '500')
                i.set('Ixx', '117.89508666666666')
                i.set('Iyy', '117.89508666666666')
                i.set('Izz', '158.34884')
        elif (str(sheet1['D7'].value) == "540/65R28"):
            if (str(sheet1['D11'].value) == "150 kg"):
                inertia.set('mass', '300')
                i.set('Ixx', '76.132527')
                i.set('Iyy', '76.132527')
                i.set('Izz', '93.945054')
            elif (str(sheet1['D11'].value) == "175 kg"):
                inertia.set('mass', '350')
                i.set('Ixx', '88.8212815')
                i.set('Iyy', '88.8212815')
                i.set('Izz', '109.602563')
            elif (str(sheet1['D11'].value) == "200 kg"):
                inertia.set('mass', '400')
                i.set('Ixx', '101.510036')
                i.set('Iyy', '101.510036')
                i.set('Izz', '125.260072')
            elif (str(sheet1['D11'].value) == "225 kg"):
                inertia.set('mass', '450')
                i.set('Ixx', '114.1987905')
                i.set('Iyy', '114.1987905')
                i.set('Izz', '140.917581')
            elif (str(sheet1['D11'].value) == "250 kg"):
                inertia.set('mass', '500')
                i.set('Ixx', '126.887545')
                i.set('Iyy', '126.887545')
                i.set('Izz', '156.57509')
        elif (str(sheet1['D7'].value) == "600/65R28"):
            if (str(sheet1['D11'].value) == "150 kg"):
                inertia.set('mass', '300')
                i.set('Ixx', '87.222552')
                i.set('Iyy', '87.222552')
                i.set('Izz', '102.445104')
            elif (str(sheet1['D11'].value) == "175 kg"):
                inertia.set('mass', '350')
                i.set('Ixx', '101.759644')
                i.set('Iyy', '101.759644')
                i.set('Izz', '119.519288')
            elif (str(sheet1['D11'].value) == "200 kg"):
                inertia.set('mass', '400')
                i.set('Ixx', '116.296736')
                i.set('Iyy', '116.296736')
                i.set('Izz', '136.593472')
            elif (str(sheet1['D11'].value) == "225 kg"):
                inertia.set('mass', '450')
                i.set('Ixx', '130.833828')
                i.set('Iyy', '130.833828')
                i.set('Izz', '153.667656')
            elif (str(sheet1['D11'].value) == "250 kg"):
                inertia.set('mass', '500')
                i.set('Ixx', '145.37092')
                i.set('Iyy', '145.37092')
                i.set('Izz', '170.74184')
                
    for dummy_FrontTyreR in root.iter('Dummy_FrontTyreR'):
        dummy_FrontTyreR.set('VisualizationGraphics', 
        'Graphics_FrontTyreR;Graphics_ExtraFrontTyreR')
        inertia = dummy_FrontTyreR.find ('Inertia')
        i = inertia.find ('I')
        if (str(sheet1['D7'].value) == "600/70R28"):
            if (str(sheet1['D11'].value) == "150 kg"):
                inertia.set('mass', '300')
                i.set('Ixx', '90.647052')
                i.set('Iyy', '90.647052')
                i.set('Izz', '109.294104')
            elif (str(sheet1['D11'].value) == "175 kg"):
                inertia.set('mass', '350')
                i.set('Ixx', '105.754894')
                i.set('Iyy', '105.754894')
                i.set('Izz', '127.509788')
            elif (str(sheet1['D11'].value) == "200 kg"):
                inertia.set('mass', '400')
                i.set('Ixx', '120.862736')
                i.set('Iyy', '120.862736')
                i.set('Izz', '145.725472')
            elif (str(sheet1['D11'].value) == "225 kg"):
                inertia.set('mass', '450')
                i.set('Ixx', '135.970578')
                i.set('Iyy', '135.970578')
                i.set('Izz', '163.941156')
            elif (str(sheet1['D11'].value) == "250 kg"):
                inertia.set('mass', '500')
                i.set('Ixx', '151.07842')
                i.set('Iyy', '151.07842')
                i.set('Izz', '182.15684')
        elif (str(sheet1['D7'].value) == "420/85R28"):
            if (str(sheet1['D11'].value) == "150 kg"):
                inertia.set('mass', '300')
                i.set('Ixx', '66.971527')
                i.set('Iyy', '66.971527')
                i.set('Izz', '95.223054')
            elif (str(sheet1['D11'].value) == "175 kg"):
                inertia.set('mass', '350')
                i.set('Ixx', '78.133448166666668')
                i.set('Iyy', '78.133448166666668')
                i.set('Izz', '111.093563')
            elif (str(sheet1['D11'].value) == "200 kg"):
                inertia.set('mass', '400')
                i.set('Ixx', '89.29536933333334')
                i.set('Iyy', '89.29536933333334')
                i.set('Izz', '126.964072')
            elif (str(sheet1['D11'].value) == "225 kg"):
                inertia.set('mass', '450')
                i.set('Ixx', '100.4572905')
                i.set('Iyy', '100.4572905')
                i.set('Izz', '142.834581')
            elif (str(sheet1['D11'].value) == "250 kg"):
                inertia.set('mass', '500')
                i.set('Ixx', '111.61921166666666')
                i.set('Iyy', '111.61921166666666')
                i.set('Izz', '158.70509')
        elif (str(sheet1['D7'].value) == "480/70R28"):
            if (str(sheet1['D11'].value) == "150 kg"):
                inertia.set('mass', '300')
                i.set('Ixx', '70.737052')
                i.set('Iyy', '70.737052')
                i.set('Izz', '95.009304')
            elif (str(sheet1['D11'].value) == "175 kg"):
                inertia.set('mass', '350')
                i.set('Ixx', '82.526560666666668')
                i.set('Iyy', '82.526560666666668')
                i.set('Izz', '110.844188')
            elif (str(sheet1['D11'].value) == "200 kg"):
                inertia.set('mass', '400')
                i.set('Ixx', '94.316069333333346')
                i.set('Iyy', '94.316069333333346')
                i.set('Izz', '126.679072')
            elif (str(sheet1['D11'].value) == "225 kg"):
                inertia.set('mass', '450')
                i.set('Ixx', '106.105578')
                i.set('Iyy', '106.105578')
                i.set('Izz', '142.513956')
            elif (str(sheet1['D11'].value) == "250 kg"):
                inertia.set('mass', '500')
                i.set('Ixx', '117.89508666666666')
                i.set('Iyy', '117.89508666666666')
                i.set('Izz', '158.34884')
        elif (str(sheet1['D7'].value) == "540/65R28"):
            if (str(sheet1['D11'].value) == "150 kg"):
                inertia.set('mass', '300')
                i.set('Ixx', '76.132527')
                i.set('Iyy', '76.132527')
                i.set('Izz', '93.945054')
            elif (str(sheet1['D11'].value) == "175 kg"):
                inertia.set('mass', '350')
                i.set('Ixx', '88.8212815')
                i.set('Iyy', '88.8212815')
                i.set('Izz', '109.602563')
            elif (str(sheet1['D11'].value) == "200 kg"):
                inertia.set('mass', '400')
                i.set('Ixx', '101.510036')
                i.set('Iyy', '101.510036')
                i.set('Izz', '125.260072')
            elif (str(sheet1['D11'].value) == "225 kg"):
                inertia.set('mass', '450')
                i.set('Ixx', '114.1987905')
                i.set('Iyy', '114.1987905')
                i.set('Izz', '140.917581')
            elif (str(sheet1['D11'].value) == "250 kg"):
                inertia.set('mass', '500')
                i.set('Ixx', '126.887545')
                i.set('Iyy', '126.887545')
                i.set('Izz', '156.57509')
        elif (str(sheet1['D7'].value) == "600/65R28"):
            if (str(sheet1['D11'].value) == "150 kg"):
                inertia.set('mass', '300')
                i.set('Ixx', '87.222552')
                i.set('Iyy', '87.222552')
                i.set('Izz', '102.445104')
            elif (str(sheet1['D11'].value) == "175 kg"):
                inertia.set('mass', '350')
                i.set('Ixx', '101.759644')
                i.set('Iyy', '101.759644')
                i.set('Izz', '119.519288')
            elif (str(sheet1['D11'].value) == "200 kg"):
                inertia.set('mass', '400')
                i.set('Ixx', '116.296736')
                i.set('Iyy', '116.296736')
                i.set('Izz', '136.593472')
            elif (str(sheet1['D11'].value) == "225 kg"):
                inertia.set('mass', '450')
                i.set('Ixx', '130.833828')
                i.set('Iyy', '130.833828')
                i.set('Izz', '153.667656')
            elif (str(sheet1['D11'].value) == "250 kg"):
                inertia.set('mass', '500')
                i.set('Ixx', '145.37092')
                i.set('Iyy', '145.37092')
                i.set('Izz', '170.74184')

                         # MODELING OF REAR TYRES

if (str(sheet1['D15'].value) == '2'):
    for spline_RearTyres in root.iter('Spline_RearTyres'):
        spline_RearTyres.set('NPoints', '3')
        for child in spline_RearTyres.iter('x'):
            if (str(sheet1['D12'].value) == "520/85R38"):
                child.set('x1', str(-(536/2000)))
                child.set('x3', str(536/2000))
                child.set('x4', '0')
                child.set('x5', '0')
                child.set('x6', '0')
            elif (str(sheet1['D12'].value) == "580/70R38"):
                child.set('x1', str(-(594/2000)))
                child.set('x3', str(594/2000))
                child.set('x4', '0')
                child.set('x5', '0')
                child.set('x6', '0')                
            elif (str(sheet1['D12'].value) == "650/65R38"):
                child.set('x1', str(-(620/2000)))
                child.set('x3', str(620/2000))
                child.set('x4', '0')
                child.set('x5', '0')
                child.set('x6', '0')
            elif (str(sheet1['D12'].value) == "650/85R38"):
                child.set('x1', str(-(650/2000)))
                child.set('x3', str(650/2000))
                child.set('x4', '0')
                child.set('x5', '0')
                child.set('x6', '0')
            elif (str(sheet1['D12'].value) == "710/70R38"):
                child.set('x1', str(-(710/2000)))
                child.set('x3', str(710/2000))
                child.set('x4', '0')
                child.set('x5', '0')
                child.set('x6', '0')
        for child in spline_RearTyres.iter('y'):
            if (str(sheet1['D12'].value) == "520/85R38"):
                child.set('y1', str(1850/2000))
                child.set('y2', str(1850/2000))
                child.set('y3', str(1850/2000))
                child.set('y4', '0')
                child.set('y5', '0')
                child.set('y6', '0')
            elif (str(sheet1['D12'].value) == "580/70R38"):
                child.set('y1', str(1852/2000))
                child.set('y2', str(1852/2000))
                child.set('y3', str(1852/2000))
                child.set('y4', '0')
                child.set('y5', '0')
                child.set('y6', '0')
            elif (str(sheet1['D12'].value) == "650/65R38"):
                child.set('y1', str(1830/2000))
                child.set('y2', str(1830/2000))
                child.set('y3', str(1830/2000))
                child.set('y4', '0')
                child.set('y5', '0')
                child.set('y6', '0')
            elif (str(sheet1['D12'].value) == "650/85R38"):
                child.set('y1', str(2072/2000))
                child.set('y2', str(2072/2000))
                child.set('y3', str(2072/2000))
                child.set('y4', '0')
                child.set('y5', '0')
                child.set('y6', '0')
            elif (str(sheet1['D12'].value) == "710/70R38"):
                child.set('y1', str(1960/2000))
                child.set('y2', str(1960/2000))
                child.set('y3', str(1960/2000))
                child.set('y4', '0')
                child.set('y5', '0')
                child.set('y6', '0')
    for graphics in root.iter('Graphics'):
        graphics_ExtraRearTyreL = graphics.find ('Graphics_ExtraRearTyreL')
        if (graphics_ExtraRearTyreL == None):
            print("RL-Do nothing")
        else:
            # Removing a particular object.
            graphics.remove(graphics_ExtraRearTyreL)
        
        graphics_ExtraRearTyreR = graphics.find ('Graphics_ExtraRearTyreR')
        if (graphics_ExtraRearTyreR == None):
            print("RR-Do nothing")
        else:
            # Removing a particular object.
            graphics.remove(graphics_ExtraRearTyreR)
     
    for dummy_RearTyreL in root.iter('Dummy_RearTyreL'):
        dummy_RearTyreL.set('VisualizationGraphics', 'Graphics_RearTyreL')
        inertia = dummy_RearTyreL.find ('Inertia')
        i = inertia.find ('I')
        if (str(sheet1['D12'].value) == "520/85R38"):
            if (str(sheet1['D16'].value) == "300 kg"):
                inertia.set('mass', '300')
                i.set('Ixx', '88.821982')
                i.set('Iyy', '88.821982')
                i.set('Izz', '163.279164')
            elif (str(sheet1['D16'].value) == "325 kg"):
                inertia.set('mass', '325')
                i.set('Ixx', '96.223813833333338')
                i.set('Iyy', '96.223813833333338')
                i.set('Izz', '176.885761')
            elif (str(sheet1['D16'].value) == "350 kg"):
                inertia.set('mass', '350')
                i.set('Ixx', '103.62564566666668')
                i.set('Iyy', '103.62564566666668')
                i.set('Izz', '190.492358')
            elif (str(sheet1['D16'].value) == "375 kg"):
                inertia.set('mass', '375')
                i.set('Ixx', '111.0274775')
                i.set('Iyy', '111.0274775')
                i.set('Izz', '204.098955')
            elif (str(sheet1['D16'].value) == "400 kg"):
                inertia.set('mass', '400')
                i.set('Ixx', '118.42930933333335')
                i.set('Iyy', '118.42930933333335')
                i.set('Izz', '217.705552')
        elif (str(sheet1['D12'].value) == "580/70R38"):
            if (str(sheet1['D16'].value) == "300 kg"):
                inertia.set('mass', '300')
                i.set('Ixx', '90.599307')
                i.set('Iyy', '90.599307')
                i.set('Izz', '163.556814')
            elif (str(sheet1['D16'].value) == "325 kg"):
                inertia.set('mass', '325')
                i.set('Ixx', '98.14924925')
                i.set('Iyy', '98.14924925')
                i.set('Izz', '177.1865485')
            elif (str(sheet1['D16'].value) == "350 kg"):
                inertia.set('mass', '350')
                i.set('Ixx', '105.6991915')
                i.set('Iyy', '105.6991915')
                i.set('Izz', '190.816283')
            elif (str(sheet1['D16'].value) == "375 kg"):
                inertia.set('mass', '375')
                i.set('Ixx', '113.24913375')
                i.set('Iyy', '113.24913375')
                i.set('Izz', '204.4460175')
            elif (str(sheet1['D16'].value) == "400 kg"):
                inertia.set('mass', '400')
                i.set('Ixx', '120.799076')
                i.set('Iyy', '120.799076')
                i.set('Izz', '218.075752')
        elif (str(sheet1['D12'].value) == "650/65R38"):
            if (str(sheet1['D16'].value) == "300 kg"):
                inertia.set('mass', '300')
                i.set('Ixx', '89.869582')
                i.set('Iyy', '89.869582')
                i.set('Izz', '160.519164')
            elif (str(sheet1['D16'].value) == "325 kg"):
                inertia.set('mass', '325')
                i.set('Ixx', '97.358713833333326')
                i.set('Iyy', '97.358713833333326')
                i.set('Izz', '173.895761')
            elif (str(sheet1['D16'].value) == "350 kg"):
                inertia.set('mass', '350')
                i.set('Ixx', '104.84784566666667')
                i.set('Iyy', '104.84784566666667')
                i.set('Izz', '187.272358')
            elif (str(sheet1['D16'].value) == "375 kg"):
                inertia.set('mass', '375')
                i.set('Ixx', '112.3369775')
                i.set('Iyy', '112.3369775')
                i.set('Izz', '200.648955')
            elif (str(sheet1['D16'].value) == "400 kg"):
                inertia.set('mass', '400')
                i.set('Ixx', '119.82610933333335')
                i.set('Iyy', '119.82610933333335')
                i.set('Izz', '214.025552')
        elif (str(sheet1['D12'].value) == "650/85R38"):
            if (str(sheet1['D16'].value) == "300 kg"):
                inertia.set('mass', '300')
                i.set('Ixx', '108.527407')
                i.set('Iyy', '108.527407')
                i.set('Izz', '195.929814')
            elif (str(sheet1['D16'].value) == "325 kg"):
                inertia.set('mass', '325')
                i.set('Ixx', '117.57135758333334')
                i.set('Iyy', '117.57135758333334')
                i.set('Izz', '212.2572985')
            elif (str(sheet1['D16'].value) == "350 kg"):
                inertia.set('mass', '350')
                i.set('Ixx', '126.61530816666668')
                i.set('Iyy', '126.61530816666668')
                i.set('Izz', '228.584783')
            elif (str(sheet1['D16'].value) == "375 kg"):
                inertia.set('mass', '375')
                i.set('Ixx', '135.65925875')
                i.set('Iyy', '135.65925875')
                i.set('Izz', '244.9122675')
            elif (str(sheet1['D16'].value) == "400 kg"):
                inertia.set('mass', '400')
                i.set('Ixx', '144.70320933333335')
                i.set('Iyy', '144.70320933333335')
                i.set('Izz', '261.239752')
        elif (str(sheet1['D12'].value) == "710/70R38"):
            if (str(sheet1['D16'].value) == "300 kg"):
                inertia.set('mass', '300')
                i.set('Ixx', '102.100207')
                i.set('Iyy', '102.100207')
                i.set('Izz', '178.995414')
            elif (str(sheet1['D16'].value) == "325 kg"):
                inertia.set('mass', '325')
                i.set('Ixx', '110.60855758333332')
                i.set('Iyy', '110.60855758333332')
                i.set('Izz', '193.9116985')
            elif (str(sheet1['D16'].value) == "350 kg"):
                inertia.set('mass', '350')
                i.set('Ixx', '119.11690816666668')
                i.set('Iyy', '119.11690816666668')
                i.set('Izz', '208.827983')
            elif (str(sheet1['D16'].value) == "375 kg"):
                inertia.set('mass', '375')
                i.set('Ixx', '127.62525875')
                i.set('Iyy', '127.62525875')
                i.set('Izz', '223.7442675')
            elif (str(sheet1['D16'].value) == "400 kg"):
                inertia.set('mass', '400')
                i.set('Ixx', '136.13360933333334')
                i.set('Iyy', '136.13360933333334')
                i.set('Izz', '238.660552')
    
    for dummy_RearTyreR in root.iter('Dummy_RearTyreR'):
        dummy_RearTyreR.set('VisualizationGraphics', 'Graphics_RearTyreR')
        inertia = dummy_RearTyreR.find ('Inertia')
        i = inertia.find ('I')
        if (str(sheet1['D12'].value) == "520/85R38"):
            if (str(sheet1['D16'].value) == "300 kg"):
                inertia.set('mass', '300')
                i.set('Ixx', '88.821982')
                i.set('Iyy', '88.821982')
                i.set('Izz', '163.279164')
            elif (str(sheet1['D16'].value) == "325 kg"):
                inertia.set('mass', '325')
                i.set('Ixx', '96.223813833333338')
                i.set('Iyy', '96.223813833333338')
                i.set('Izz', '176.885761')
            elif (str(sheet1['D16'].value) == "350 kg"):
                inertia.set('mass', '350')
                i.set('Ixx', '103.62564566666668')
                i.set('Iyy', '103.62564566666668')
                i.set('Izz', '190.492358')
            elif (str(sheet1['D16'].value) == "375 kg"):
                inertia.set('mass', '375')
                i.set('Ixx', '111.0274775')
                i.set('Iyy', '111.0274775')
                i.set('Izz', '204.098955')
            elif (str(sheet1['D16'].value) == "400 kg"):
                inertia.set('mass', '400')
                i.set('Ixx', '118.42930933333335')
                i.set('Iyy', '118.42930933333335')
                i.set('Izz', '217.705552')
        elif (str(sheet1['D12'].value) == "580/70R38"):
            if (str(sheet1['D16'].value) == "300 kg"):
                inertia.set('mass', '300')
                i.set('Ixx', '90.599307')
                i.set('Iyy', '90.599307')
                i.set('Izz', '163.556814')
            elif (str(sheet1['D16'].value) == "325 kg"):
                inertia.set('mass', '325')
                i.set('Ixx', '98.14924925')
                i.set('Iyy', '98.14924925')
                i.set('Izz', '177.1865485')
            elif (str(sheet1['D16'].value) == "350 kg"):
                inertia.set('mass', '350')
                i.set('Ixx', '105.6991915')
                i.set('Iyy', '105.6991915')
                i.set('Izz', '190.816283')
            elif (str(sheet1['D16'].value) == "375 kg"):
                inertia.set('mass', '375')
                i.set('Ixx', '113.24913375')
                i.set('Iyy', '113.24913375')
                i.set('Izz', '204.4460175')
            elif (str(sheet1['D16'].value) == "400 kg"):
                inertia.set('mass', '400')
                i.set('Ixx', '120.799076')
                i.set('Iyy', '120.799076')
                i.set('Izz', '218.075752')
        elif (str(sheet1['D12'].value) == "650/65R38"):
            if (str(sheet1['D16'].value) == "300 kg"):
                inertia.set('mass', '300')
                i.set('Ixx', '89.869582')
                i.set('Iyy', '89.869582')
                i.set('Izz', '160.519164')
            elif (str(sheet1['D16'].value) == "325 kg"):
                inertia.set('mass', '325')
                i.set('Ixx', '97.358713833333326')
                i.set('Iyy', '97.358713833333326')
                i.set('Izz', '173.895761')
            elif (str(sheet1['D16'].value) == "350 kg"):
                inertia.set('mass', '350')
                i.set('Ixx', '104.84784566666667')
                i.set('Iyy', '104.84784566666667')
                i.set('Izz', '187.272358')
            elif (str(sheet1['D16'].value) == "375 kg"):
                inertia.set('mass', '375')
                i.set('Ixx', '112.3369775')
                i.set('Iyy', '112.3369775')
                i.set('Izz', '200.648955')
            elif (str(sheet1['D16'].value) == "400 kg"):
                inertia.set('mass', '400')
                i.set('Ixx', '119.82610933333335')
                i.set('Iyy', '119.82610933333335')
                i.set('Izz', '214.025552')
        elif (str(sheet1['D12'].value) == "650/85R38"):
            if (str(sheet1['D16'].value) == "300 kg"):
                inertia.set('mass', '300')
                i.set('Ixx', '108.527407')
                i.set('Iyy', '108.527407')
                i.set('Izz', '195.929814')
            elif (str(sheet1['D16'].value) == "325 kg"):
                inertia.set('mass', '325')
                i.set('Ixx', '117.57135758333334')
                i.set('Iyy', '117.57135758333334')
                i.set('Izz', '212.2572985')
            elif (str(sheet1['D16'].value) == "350 kg"):
                inertia.set('mass', '350')
                i.set('Ixx', '126.61530816666668')
                i.set('Iyy', '126.61530816666668')
                i.set('Izz', '228.584783')
            elif (str(sheet1['D16'].value) == "375 kg"):
                inertia.set('mass', '375')
                i.set('Ixx', '135.65925875')
                i.set('Iyy', '135.65925875')
                i.set('Izz', '244.9122675')
            elif (str(sheet1['D16'].value) == "400 kg"):
                inertia.set('mass', '400')
                i.set('Ixx', '144.70320933333335')
                i.set('Iyy', '144.70320933333335')
                i.set('Izz', '261.239752')
        elif (str(sheet1['D12'].value) == "710/70R38"):
            if (str(sheet1['D16'].value) == "300 kg"):
                inertia.set('mass', '300')
                i.set('Ixx', '102.100207')
                i.set('Iyy', '102.100207')
                i.set('Izz', '178.995414')
            elif (str(sheet1['D16'].value) == "325 kg"):
                inertia.set('mass', '325')
                i.set('Ixx', '110.60855758333332')
                i.set('Iyy', '110.60855758333332')
                i.set('Izz', '193.9116985')
            elif (str(sheet1['D16'].value) == "350 kg"):
                inertia.set('mass', '350')
                i.set('Ixx', '119.11690816666668')
                i.set('Iyy', '119.11690816666668')
                i.set('Izz', '208.827983')
            elif (str(sheet1['D16'].value) == "375 kg"):
                inertia.set('mass', '375')
                i.set('Ixx', '127.62525875')
                i.set('Iyy', '127.62525875')
                i.set('Izz', '223.7442675')
            elif (str(sheet1['D16'].value) == "400 kg"):
                inertia.set('mass', '400')
                i.set('Ixx', '136.13360933333334')
                i.set('Iyy', '136.13360933333334')
                i.set('Izz', '238.660552')
        
elif (str(sheet1['D15'].value) == '4'):
    for spline_RearTyres in root.iter('Spline_RearTyres'):
        spline_RearTyres.set('NPoints', '6')
        for child in spline_RearTyres.iter('x'):
            if (str(sheet1['D12'].value) == "520/85R38"):
                child.set('x1', str(-(536/2000)))
                child.set('x3', str(536/2000))
                child.set('x4', str((536/2000)+(50/1000)))
                child.set('x5', str((536/2000)+(50/1000)+(536/2000)))
                child.set('x6', str((536/2000)+(50/1000)+(536/1000)))
            elif (str(sheet1['D12'].value) == "580/70R38"):
                child.set('x1', str(-(594/2000)))
                child.set('x3', str(594/2000))
                child.set('x4', str((594/2000)+(50/1000)))
                child.set('x5', str((594/2000)+(50/1000)+(594/2000)))
                child.set('x6', str((594/2000)+(50/1000)+(594/1000)))                
            elif (str(sheet1['D12'].value) == "650/65R38"):
                child.set('x1', str(-(620/2000)))
                child.set('x3', str(620/2000))
                child.set('x4', str((620/2000)+(50/1000)))
                child.set('x5', str((620/2000)+(50/1000)+(620/2000)))
                child.set('x6', str((620/2000)+(50/1000)+(620/1000)))
            elif (str(sheet1['D12'].value) == "650/85R38"):
                child.set('x1', str(-(650/2000)))
                child.set('x3', str(650/2000))
                child.set('x4', str((650/2000)+(50/1000)))
                child.set('x5', str((650/2000)+(50/1000)+(650/2000)))
                child.set('x6', str((650/2000)+(50/1000)+(650/1000)))
            elif (str(sheet1['D12'].value) == "710/70R38"):
                child.set('x1', str(-(710/2000)))
                child.set('x3', str(710/2000))
                child.set('x4', str((710/2000)+(50/1000)))
                child.set('x5', str((710/2000)+(50/1000)+(710/2000)))
                child.set('x6', str((710/2000)+(50/1000)+(710/1000)))
        for child in spline_RearTyres.iter('y'):
            if (str(sheet1['D12'].value) == "520/85R38"):
                child.set('y1', str(1850/2000))
                child.set('y2', str(1850/2000))
                child.set('y3', str(1850/2000))
                child.set('y4', str(1850/2000))
                child.set('y5', str(1850/2000))
                child.set('y6', str(1850/2000))
            elif (str(sheet1['D12'].value) == "580/70R38"):
                child.set('y1', str(1852/2000))
                child.set('y2', str(1852/2000))
                child.set('y3', str(1852/2000))
                child.set('y4', str(1852/2000))
                child.set('y5', str(1852/2000))
                child.set('y6', str(1852/2000))
            elif (str(sheet1['D12'].value) == "650/65R38"):
                child.set('y1', str(1830/2000))
                child.set('y2', str(1830/2000))
                child.set('y3', str(1830/2000))
                child.set('y4', str(1830/2000))
                child.set('y5', str(1830/2000))
                child.set('y6', str(1830/2000))
            elif (str(sheet1['D12'].value) == "650/85R38"):
                child.set('y1', str(2072/2000))
                child.set('y2', str(2072/2000))
                child.set('y3', str(2072/2000))
                child.set('y4', str(2072/2000))
                child.set('y5', str(2072/2000))
                child.set('y6', str(2072/2000))
            elif (str(sheet1['D12'].value) == "710/70R38"):
                child.set('y1', str(1960/2000))
                child.set('y2', str(1960/2000))
                child.set('y3', str(1960/2000))
                child.set('y4', str(1960/2000))
                child.set('y5', str(1960/2000))
                child.set('y6', str(1960/2000))
    for graphics in root.iter('Graphics'):
        graphics_ExtraRearTyreL = graphics.find ('Graphics_ExtraRearTyreL')
        if (graphics_ExtraRearTyreL != None):
            position = graphics_ExtraRearTyreL.find ('Position')
            if (str(sheet1['D12'].value) == "520/85R38"):
                position.set('z', str((536/1000)+(50/1000)))
            elif (str(sheet1['D12'].value) == "580/70R38"):
                position.set('z', str((594/1000)+(50/1000)))
            elif (str(sheet1['D12'].value) == "650/65R38"):
                position.set('z', str((620/1000)+(50/1000)))
            elif (str(sheet1['D12'].value) == "650/85R38"):
                position.set('z', str((650/1000)+(50/1000)))
            elif (str(sheet1['D12'].value) == "710/70R38"):
                position.set('z', str((710/1000)+(50/1000)))
        else:
            graphics_RearTyreL = graphics.find ('Graphics_RearTyreL')
            # Copying the same attributes to a new object.
            # ".deepcopy" creates a second object.
            graphics_ExtraRearTyreL = copy.deepcopy(graphics_RearTyreL)
            # Replacing the tag name with a new name.
            graphics_ExtraRearTyreL.tag = "Graphics_ExtraRearTyreL"
            position = graphics_ExtraRearTyreL.find ('Position')
            if (str(sheet1['D12'].value) == "520/85R38"):
                position.set('z', str((536/1000)+(50/1000)))
            elif (str(sheet1['D12'].value) == "580/70R38"):
                position.set('z', str((594/1000)+(50/1000)))
            elif (str(sheet1['D12'].value) == "650/65R38"):
                position.set('z', str((620/1000)+(50/1000)))
            elif (str(sheet1['D12'].value) == "650/85R38"):
                position.set('z', str((650/1000)+(50/1000)))
            elif (str(sheet1['D12'].value) == "710/70R38"):
                position.set('z', str((710/1000)+(50/1000)))
            graphics.insert(15, graphics_ExtraRearTyreL)
            # Inserting this element at that particular location of index 15.
            # That means the 16th position.

        graphics_ExtraRearTyreR = graphics.find ('Graphics_ExtraRearTyreR')
        if (graphics_ExtraRearTyreR != None):
            position = graphics_ExtraRearTyreR.find ('Position')
            if (str(sheet1['D12'].value) == "520/85R38"):
                position.set('z', str((536/1000)+(50/1000)))
            elif (str(sheet1['D12'].value) == "580/70R38"):
                position.set('z', str((594/1000)+(50/1000)))
            elif (str(sheet1['D12'].value) == "650/65R38"):
                position.set('z', str((620/1000)+(50/1000)))
            elif (str(sheet1['D12'].value) == "650/85R38"):
                position.set('z', str((650/1000)+(50/1000)))
            elif (str(sheet1['D12'].value) == "710/70R38"):
                position.set('z', str((710/1000)+(50/1000)))
        else:
            graphics_RearTyreR = graphics.find ('Graphics_RearTyreR')
            # Copying the same attributes to a new object.
            # ".deepcopy" creates a second object.
            graphics_ExtraRearTyreR = copy.deepcopy(graphics_RearTyreR)
            # Replacing the tag name with a new name.
            graphics_ExtraRearTyreR.tag = "Graphics_ExtraRearTyreR"
            position = graphics_ExtraRearTyreR.find ('Position')
            if (str(sheet1['D12'].value) == "520/85R38"):
                position.set('z', str((536/1000)+(50/1000)))
            elif (str(sheet1['D12'].value) == "580/70R38"):
                position.set('z', str((594/1000)+(50/1000)))
            elif (str(sheet1['D12'].value) == "650/65R38"):
                position.set('z', str((620/1000)+(50/1000)))
            elif (str(sheet1['D12'].value) == "650/85R38"):
                position.set('z', str((650/1000)+(50/1000)))
            elif (str(sheet1['D12'].value) == "710/70R38"):
                position.set('z', str((710/1000)+(50/1000)))
            graphics.insert(16, graphics_ExtraRearTyreR)
            # Inserting this element at that particular location of index 16.
            # That means the 17th position.

    for dummy_RearTyreL in root.iter('Dummy_RearTyreL'):
        dummy_RearTyreL.set('VisualizationGraphics', 
        'Graphics_RearTyreL;Graphics_ExtraRearTyreL')
        inertia = dummy_RearTyreL.find ('Inertia')
        i = inertia.find ('I')
        if (str(sheet1['D12'].value) == "520/85R38"):
            if (str(sheet1['D16'].value) == "300 kg"):
                inertia.set('mass', '600')
                i.set('Ixx', '220.738364')
                i.set('Iyy', '220.738364')
                i.set('Izz', '326.558328')
            elif (str(sheet1['D16'].value) == "325 kg"):
                inertia.set('mass', '650')
                i.set('Ixx', '239.13322766666667')
                i.set('Iyy', '239.13322766666667')
                i.set('Izz', '353.771522')
            elif (str(sheet1['D16'].value) == "350 kg"):
                inertia.set('mass', '700')
                i.set('Ixx', '257.52809133333335')
                i.set('Iyy', '257.52809133333335')
                i.set('Izz', '380.984716')
            elif (str(sheet1['D16'].value) == "375 kg"):
                inertia.set('mass', '750')
                i.set('Ixx', '275.922955')
                i.set('Iyy', '275.922955')
                i.set('Izz', '408.19791')
            elif (str(sheet1['D16'].value) == "400 kg"):
                inertia.set('mass', '800')
                i.set('Ixx', '294.31781866666671')
                i.set('Iyy', '294.31781866666671')
                i.set('Izz', '435.411104')
        elif (str(sheet1['D12'].value) == "580/70R38"):
            if (str(sheet1['D16'].value) == "300 kg"):
                inertia.set('mass', '600')
                i.set('Ixx', '234.124014')
                i.set('Iyy', '234.124014')
                i.set('Izz', '327.113628')
            elif (str(sheet1['D16'].value) == "325 kg"):
                inertia.set('mass', '650')
                i.set('Ixx', '253.6343485')
                i.set('Iyy', '253.6343485')
                i.set('Izz', '354.373097')
            elif (str(sheet1['D16'].value) == "350 kg"):
                inertia.set('mass', '700')
                i.set('Ixx', '273.144683')
                i.set('Iyy', '273.144683')
                i.set('Izz', '381.632566')
            elif (str(sheet1['D16'].value) == "375 kg"):
                inertia.set('mass', '750')
                i.set('Ixx', '292.6550175')
                i.set('Iyy', '292.6550175')
                i.set('Izz', '408.892035')
            elif (str(sheet1['D16'].value) == "400 kg"):
                inertia.set('mass', '800')
                i.set('Ixx', '312.165352')
                i.set('Iyy', '312.165352')
                i.set('Izz', '436.151504')
        elif (str(sheet1['D12'].value) == "650/65R38"):
            if (str(sheet1['D16'].value) == "300 kg"):
                inertia.set('mass', '600')
                i.set('Ixx', '237.399164')
                i.set('Iyy', '237.399164')
                i.set('Izz', '321.038328')
            elif (str(sheet1['D16'].value) == "325 kg"):
                inertia.set('mass', '650')
                i.set('Ixx', '257.18242766666668')
                i.set('Iyy', '257.18242766666668')
                i.set('Izz', '347.791522')
            elif (str(sheet1['D16'].value) == "350 kg"):
                inertia.set('mass', '700')
                i.set('Ixx', '276.96569133333338')
                i.set('Iyy', '276.96569133333338')
                i.set('Izz', '374.544716')
            elif (str(sheet1['D16'].value) == "375 kg"):
                inertia.set('mass', '750')
                i.set('Ixx', '296.748955')
                i.set('Iyy', '296.748955')
                i.set('Izz', '401.29791')
            elif (str(sheet1['D16'].value) == "400 kg"):
                inertia.set('mass', '800')
                i.set('Ixx', '316.53221866666672')
                i.set('Iyy', '316.53221866666672')
                i.set('Izz', '428.051104')
        elif (str(sheet1['D12'].value) == "650/85R38"):
            if (str(sheet1['D16'].value) == "300 kg"):
                inertia.set('mass', '600')
                i.set('Ixx', '280.429814')
                i.set('Iyy', '280.429814')
                i.set('Izz', '391.859628')
            elif (str(sheet1['D16'].value) == "325 kg"):
                inertia.set('mass', '650')
                i.set('Ixx', '303.79896516666668')
                i.set('Iyy', '303.79896516666668')
                i.set('Izz', '424.514597')
            elif (str(sheet1['D16'].value) == "350 kg"):
                inertia.set('mass', '700')
                i.set('Ixx', '327.16811633333339')
                i.set('Iyy', '327.16811633333339')
                i.set('Izz', '457.169566')
            elif (str(sheet1['D16'].value) == "375 kg"):
                inertia.set('mass', '750')
                i.set('Ixx', '350.5372675')
                i.set('Iyy', '350.5372675')
                i.set('Izz', '489.824535')
            elif (str(sheet1['D16'].value) == "400 kg"):
                inertia.set('mass', '800')
                i.set('Ixx', '373.9064186666667')
                i.set('Iyy', '373.9064186666667')
                i.set('Izz', '522.479504')
        elif (str(sheet1['D12'].value) == "710/70R38"):
            if (str(sheet1['D16'].value) == "300 kg"):
                inertia.set('mass', '600')
                i.set('Ixx', '279.815414')
                i.set('Iyy', '279.815414')
                i.set('Izz', '357.990828')
            elif (str(sheet1['D16'].value) == "325 kg"):
                inertia.set('mass', '650')
                i.set('Ixx', '303.13336516666664')
                i.set('Iyy', '303.13336516666664')
                i.set('Izz', '387.823397')
            elif (str(sheet1['D16'].value) == "350 kg"):
                inertia.set('mass', '700')
                i.set('Ixx', '326.45131633333335')
                i.set('Iyy', '326.45131633333335')
                i.set('Izz', '417.655966')
            elif (str(sheet1['D16'].value) == "375 kg"):
                inertia.set('mass', '750')
                i.set('Ixx', '349.7692675')
                i.set('Iyy', '349.7692675')
                i.set('Izz', '447.488535')
            elif (str(sheet1['D16'].value) == "400 kg"):
                inertia.set('mass', '800')
                i.set('Ixx', '373.08721866666667')
                i.set('Iyy', '373.08721866666667')
                i.set('Izz', '477.321104')
            
    for dummy_RearTyreR in root.iter('Dummy_RearTyreR'):
        dummy_RearTyreR.set('VisualizationGraphics', 
        'Graphics_RearTyreR;Graphics_ExtraRearTyreR')
        inertia = dummy_RearTyreR.find ('Inertia')
        i = inertia.find ('I')
        if (str(sheet1['D12'].value) == "520/85R38"):
            if (str(sheet1['D16'].value) == "300 kg"):
                inertia.set('mass', '600')
                i.set('Ixx', '220.738364')
                i.set('Iyy', '220.738364')
                i.set('Izz', '326.558328')
            elif (str(sheet1['D16'].value) == "325 kg"):
                inertia.set('mass', '650')
                i.set('Ixx', '239.13322766666667')
                i.set('Iyy', '239.13322766666667')
                i.set('Izz', '353.771522')
            elif (str(sheet1['D16'].value) == "350 kg"):
                inertia.set('mass', '700')
                i.set('Ixx', '257.52809133333335')
                i.set('Iyy', '257.52809133333335')
                i.set('Izz', '380.984716')
            elif (str(sheet1['D16'].value) == "375 kg"):
                inertia.set('mass', '750')
                i.set('Ixx', '275.922955')
                i.set('Iyy', '275.922955')
                i.set('Izz', '408.19791')
            elif (str(sheet1['D16'].value) == "400 kg"):
                inertia.set('mass', '800')
                i.set('Ixx', '294.31781866666671')
                i.set('Iyy', '294.31781866666671')
                i.set('Izz', '435.411104')
        elif (str(sheet1['D12'].value) == "580/70R38"):
            if (str(sheet1['D16'].value) == "300 kg"):
                inertia.set('mass', '600')
                i.set('Ixx', '234.124014')
                i.set('Iyy', '234.124014')
                i.set('Izz', '327.113628')
            elif (str(sheet1['D16'].value) == "325 kg"):
                inertia.set('mass', '650')
                i.set('Ixx', '253.6343485')
                i.set('Iyy', '253.6343485')
                i.set('Izz', '354.373097')
            elif (str(sheet1['D16'].value) == "350 kg"):
                inertia.set('mass', '700')
                i.set('Ixx', '273.144683')
                i.set('Iyy', '273.144683')
                i.set('Izz', '381.632566')
            elif (str(sheet1['D16'].value) == "375 kg"):
                inertia.set('mass', '750')
                i.set('Ixx', '292.6550175')
                i.set('Iyy', '292.6550175')
                i.set('Izz', '408.892035')
            elif (str(sheet1['D16'].value) == "400 kg"):
                inertia.set('mass', '800')
                i.set('Ixx', '312.165352')
                i.set('Iyy', '312.165352')
                i.set('Izz', '436.151504')
        elif (str(sheet1['D12'].value) == "650/65R38"):
            if (str(sheet1['D16'].value) == "300 kg"):
                inertia.set('mass', '600')
                i.set('Ixx', '237.399164')
                i.set('Iyy', '237.399164')
                i.set('Izz', '321.038328')
            elif (str(sheet1['D16'].value) == "325 kg"):
                inertia.set('mass', '650')
                i.set('Ixx', '257.18242766666668')
                i.set('Iyy', '257.18242766666668')
                i.set('Izz', '347.791522')
            elif (str(sheet1['D16'].value) == "350 kg"):
                inertia.set('mass', '700')
                i.set('Ixx', '276.96569133333338')
                i.set('Iyy', '276.96569133333338')
                i.set('Izz', '374.544716')
            elif (str(sheet1['D16'].value) == "375 kg"):
                inertia.set('mass', '750')
                i.set('Ixx', '296.748955')
                i.set('Iyy', '296.748955')
                i.set('Izz', '401.29791')
            elif (str(sheet1['D16'].value) == "400 kg"):
                inertia.set('mass', '800')
                i.set('Ixx', '316.53221866666672')
                i.set('Iyy', '316.53221866666672')
                i.set('Izz', '428.051104')
        elif (str(sheet1['D12'].value) == "650/85R38"):
            if (str(sheet1['D16'].value) == "300 kg"):
                inertia.set('mass', '600')
                i.set('Ixx', '280.429814')
                i.set('Iyy', '280.429814')
                i.set('Izz', '391.859628')
            elif (str(sheet1['D16'].value) == "325 kg"):
                inertia.set('mass', '650')
                i.set('Ixx', '303.79896516666668')
                i.set('Iyy', '303.79896516666668')
                i.set('Izz', '424.514597')
            elif (str(sheet1['D16'].value) == "350 kg"):
                inertia.set('mass', '700')
                i.set('Ixx', '327.16811633333339')
                i.set('Iyy', '327.16811633333339')
                i.set('Izz', '457.169566')
            elif (str(sheet1['D16'].value) == "375 kg"):
                inertia.set('mass', '750')
                i.set('Ixx', '350.5372675')
                i.set('Iyy', '350.5372675')
                i.set('Izz', '489.824535')
            elif (str(sheet1['D16'].value) == "400 kg"):
                inertia.set('mass', '800')
                i.set('Ixx', '373.9064186666667')
                i.set('Iyy', '373.9064186666667')
                i.set('Izz', '522.479504')
        elif (str(sheet1['D12'].value) == "710/70R38"):
            if (str(sheet1['D16'].value) == "300 kg"):
                inertia.set('mass', '600')
                i.set('Ixx', '279.815414')
                i.set('Iyy', '279.815414')
                i.set('Izz', '357.990828')
            elif (str(sheet1['D16'].value) == "325 kg"):
                inertia.set('mass', '650')
                i.set('Ixx', '303.13336516666664')
                i.set('Iyy', '303.13336516666664')
                i.set('Izz', '387.823397')
            elif (str(sheet1['D16'].value) == "350 kg"):
                inertia.set('mass', '700')
                i.set('Ixx', '326.45131633333335')
                i.set('Iyy', '326.45131633333335')
                i.set('Izz', '417.655966')
            elif (str(sheet1['D16'].value) == "375 kg"):
                inertia.set('mass', '750')
                i.set('Ixx', '349.7692675')
                i.set('Iyy', '349.7692675')
                i.set('Izz', '447.488535')
            elif (str(sheet1['D16'].value) == "400 kg"):
                inertia.set('mass', '800')
                i.set('Ixx', '373.08721866666667')
                i.set('Iyy', '373.08721866666667')
                i.set('Izz', '477.321104')

 #--------------------------------------------------------------------------#

 #----------------------------EQUIPMENT MODELING----------------------------#

for assembly in root.iter('Assembly'):
    if (str(sheet1['D17'].value) == "Trailer"):
        assembly.set('FileName', './Trailer.mva')
    else:
        assembly.set('FileName', 'None')

 #--------------------------------------------------------------------------#

 #--------------------------OVER-WRITING XML FILE---------------------------#

# XML file is over-written and saved.
tree.write('Tractor_Model.xml')

 #--------------------------------------------------------------------------#