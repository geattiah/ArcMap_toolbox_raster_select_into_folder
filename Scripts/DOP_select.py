#coding= utf-8
"""-----------------------------------------------------------------------------
  Script Name: Spatial selection of raster files
  Description: Select area of interest from the polygon shapefile based on a where clause
               Use this area of interest to select raster files from folders who intersect with it
               and export to a new folder.
  Created By:  Gifty E. A. Attiah
  Date:        28th January, 2020.
-----------------------------------------------------------------------------"""

#Import os
import os, sys, arcpy

#Set parameters in arcgis tool
input_shape = arcpy.GetParameterAsText(0)
# the area of interest to find the rasters for
rasterFolder = arcpy.GetParameterAsText(1) # the folder containing the rasters to search from
outputFolder = arcpy.GetParameterAsText(2) # the folder to copy to

arcpy.DefineProjection_management(input_shape, coor_system="PROJCS['ETRS_1989_UTM_Zone_N32',GEOGCS['GCS_ETRS_1989',DATUM['D_ETRS_1989',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',32500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',9.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]")
arcpy.AddMessage("Area of Interest Projected")

shapeDesc = arcpy.Describe(input_shape) # get the extent of the AOI
shapeExt = shapeDesc.extent #Extent of shapefile

#Set working environment
arcpy.env.workspace = rasterFolder

sr = arcpy.SpatialReference("ETRS 1989 UTM Zone N32")

path = rasterFolder

#Walk through all the folders and sub-folders
for root, dirs, files in os.walk(path):
    arcpy.env.workspace = root
    #List raster files in the folder
    files = arcpy.ListRasters()
    for ThisRas in files:

    #Define extent of rasters
       arcpy.DefineProjection_management(ThisRas, sr)
       arcpy.AddMessage("Raster %s Projected" % ThisRas)
       rasDesc = arcpy.Describe(ThisRas)
       rasExt  = rasDesc.extent

    #Compare the extent of the raster and shapefile to select those that fall within
       if rasExt.disjoint(shapeExt):
        arcpy.AddMessage("Raster %s fall outside" % (ThisRas))
       else:
        arcpy.AddMessage("Raster %s falls within" % (ThisRas))
        outFile = os.path.join(outputFolder,ThisRas)
        arcpy.RasterToOtherFormat_conversion(ThisRas,outputFolder, Raster_Format="JPEG")
        arcpy.AddMessage("%s converted to JPEG " % (ThisRas))


