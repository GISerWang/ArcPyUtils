# -*- coding: UTF-8 -*-
import arcpy
# 定义一个坐标系统
sr=arcpy.SpatialReference(4326)
# 1.创建一个要素类（单纯的shp文件）
# ./：代表当前文件夹
# flow.shp:代表shp的名称
# "POLYLINE"：代表折线，还可以有：POLYGON,POINT等
# spatial_reference：表示创建的shp的坐标系
lineShp=arcpy.CreateFeatureclass_management(r"./","flow.shp","POLYLINE",spatial_reference=sr,has_z='DISABLED')
# 给lineShp添加字段
# x是字段的名称
# DOUBLE是字段的类型，类型可以是：DOUBLE，TEXT，FLOAT，DATE 等
arcpy.AddField_management(lineShp,"x","DOUBLE")
# 当字段类型是TEXT时，一般需要指定字段长度field_length
arcpy.AddField_management(lineShp,"name","TEXT",field_length=30)

# 2.创建一个文件地理数据库
# ./：代表当前文件夹
# fGDB.gdb: 文件数据库的名称
fileGDB=arcpy.CreateFileGDB_management(r"./","fGDB.gdb")
# 在fileGDB中创建一个要素数据集，数据集的名称叫做dataset，空间参考是sr
dataset=arcpy.CreateFeatureDataset_management(fileGDB, "dataset",spatial_reference=sr)
# 在文件数据库中创建一个点文件（注意指定坐标系）
fileGDB_Point=arcpy.CreateFeatureclass_management(fileGDB,"point","POINT",spatial_reference=sr,has_z='DISABLED')
# 在文件数据库要素集中创建一个线文件（不需要指定坐标系）
fileGDB_Line=arcpy.CreateFeatureclass_management(dataset,"line","POLYLINE")


# 3.创建个人地理数据库
# ./：代表当前文件夹
# personal.mdb: 个人地理数据库的名称
personalGDB=arcpy.CreatePersonalGDB_management(r"./","personal.mdb")

# 4.创建具有Z值的文件,has_z可以是DISABLED ，ENABLED ，SAME_AS_TEMPLATE
# SAME_AS_TEMPLATE代表仅当模板具有 z 值时，输出要素类才会具有 z 值
# 创建一个有Z值的要素类（单纯的shp文件）
lineShp_Z=arcpy.CreateFeatureclass_management(r"./","flow.shp","POLYLINE",spatial_reference=sr,has_z='ENABLED')
# 在文件数据库中创建一个具有Z值的点文件
fileGDB_Point_Z=arcpy.CreateFeatureclass_management(fileGDB,"point","POINT",spatial_reference=sr,has_z='ENABLED')
# 在文件数据库中创建一个具有Z值的线文件
fileGDB_Line_Z=arcpy.CreateFeatureclass_management(dataset,"line","POLYLINE",has_z='ENABLED')
