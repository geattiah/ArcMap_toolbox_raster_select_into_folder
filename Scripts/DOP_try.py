#coding= utf-8
"""-----------------------------------------------------------------------------
  Script Name: Define projection
  Description: Define projection for all undefined raster files in a folder
  Created By:  Gifty E. A. Attiah
  Date:        30th January, 2020.
-----------------------------------------------------------------------------"""

#Import operating systems
import os, sys, arcpy

#Folder containing raster files to be projected
rFolder = arcpy.GetParameterAsText(0)
#The folder containing the rasters to search from
path = rFolder

for root, dirs, files in os.walk(path):
    arcpy.env.workspace = root
    files = arcpy.ListRasters()
    for Ras in files:
    #Show message to user
    #arcpy.AddMessage("Projecting " + Ras)
        arcpy.DefineProjection_management(Ras, coor_system="PROJCS['ETRS_1989_UTM_Zone_N32',GEOGCS['GCS_ETRS_1989',DATUM['D_ETRS_1989',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',32500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',9.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]")
    #arcpy.AddMessage("Projecting " + Ras)
#Message after all raster files have been defined
        arcpy.AddMessage("Projecting %s complete" % Ras)

