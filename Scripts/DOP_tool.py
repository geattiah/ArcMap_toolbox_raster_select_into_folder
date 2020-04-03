#coding= utf-8
"""-----------------------------------------------------------------------------
  Script Name: Select Newest date from overlapping polygons in Layer
  Description: Querey, select and export the overlapping files which have the highest dates
               into a shapefile.
  Created By:  Gifty E. A. Attiah 
  Date:        28th January, 2020.
-----------------------------------------------------------------------------"""

import arcpy
import os
import sys
from arcpy import env

#Get parameters
Shapefile = arcpy.GetParameterAsText(0)
Dissolve = arcpy.GetParameterAsText(1)

#Dissolve based of max date
arcpy.Dissolve_management(Shapefile, Dissolve, dissolve_field="DOP_KURZ", statistics_fields="jear_i MAX", multi_part="MULTI_PART", unsplit_lines="DISSOLVE_LINES")

#Join to original to keep attributes
arcpy.JoinField_management(Dissolve, "DOP_KURZ", Shapefile,"DOP_KURZ", fields="FID;ID;KACH10KM;KACHEL_N;BILDFLUG;A_DATUM;A_DATUM2;E_DATUM;E_DATUM2;HERSTL_D;DGM;DGM_GITT;LB_AUFL;BF_MSTAB;BF_HOEHE;DARSTELL;BF_NR;KAM_SENS;BOD_PIX;SPEKT_K;SPEKT_K1;SPEKT_K2;BEZ_SYS_L;BEZ_SYS_H;DOP_BZFL;LU_R;LU_H;PIX_R;PIX_H;FARB_T;STD_ABW;D_FORMAT;DOP_HG;DOP_HGW;QUELQUAL;KOMPRESS;KOMP_ART;BELAUB;BEMERK;LAND;EIGENTUM;V_REGELW;QUELLE;DOP_GROE;DOP_MSTB;PA_ID;A_ID;KEY_GS;FILE_ID;BF_PLAN;DOP_R;DOP_H;DOP_KURZ;DOP20;DTK5;status;jear_i;comb")

arcpy.Select_analysis(input_shape, AreaOfInterest, where_clause)

arcpy.DefineProjection_management(AreaOfInterest, coor_system="PROJCS['ETRS_1989_UTM_Zone_32N',GEOGCS['GCS_ETRS_1989',DATUM['D_ETRS_1989',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',32500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',9.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]")
arcpy.AddMessage("Area of Interest Projected")
#Find extent of the area of interest
