# -*- coding: UTF-8 -*-
import arcpy
# city 是一个点要素类
# 指定命名空间
arcpy.env.workspace = r"./ItemCRUDTest.mdb"
# 寻找命名空间下面的某一个要素类，通过where条件查询出我们需要的元素
with arcpy.da.UpdateCursor('updateItem/city',['SHAPE@','SHAPE@XY','Name'],where_clause='Name="龙岩市"') as cursor:
    for row in cursor:
        #注意row[0]是arcpy.PointGeometry对象，而不是arcpy.Point对象
        #修改城市的名称（注意只能修改属性数据，不能修改空间数据）
        row[2]='龙岩'
        # 更新数据
        cursor.updateRow(row)
# 重新查找龙岩市
with arcpy.da.UpdateCursor('updateItem/city',['Name'],where_clause='Name="龙岩"') as cursor:
    for row in cursor:
        print row[0]

