# -*- coding: UTF-8 -*-
import arcpy
# 判断当前工作空间中是否存在该文件（注意一定要指定工作空间）
# 指定当前的工作空间
arcpy.env.workspace = r".\personal.mdb"
# 判断当前工作空间中是否存在point
arcpy.Exists('point')
# 判断personal.mdb是否中存在一个名称为ds的要素集
arcpy.Exists('ds')
# 判断personal.mdb的ds中是否中存在一个名称为point2的要素类
arcpy.Exists('ds/point2')
# 删除要素类（一般是先判断在删除，如果存在就删除）,比如
if(arcpy.Exists('ds/point1')):
    arcpy.Delete_management("ds/point2.shp")
