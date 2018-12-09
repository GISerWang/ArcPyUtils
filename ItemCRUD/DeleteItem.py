# -*- coding: UTF-8 -*-
import arcpy
# city_region 是一个面要素类
# 指定命名空间
arcpy.env.workspace = r"./ItemCRUDTest.mdb"
# 寻找命名空间下面的某一个要素类，通过where条件查询出我们需要的元素
# 使用delete删除
with arcpy.da.UpdateCursor('deleteItem/city_region',['SHAPE@','Name'],where_clause='Name="龙岩市"') as cursor:
    for row in cursor:
        # 获得面要素的所有点要素
        # for pt in row[0].getPart()[0]:
        #     print pt
        cursor.deleteRow()
# 重新查找改元素，查询不到了
with arcpy.da.UpdateCursor('deleteItem/city_region',['Name'],where_clause='Name="龙岩市"') as cursor:
    for row in cursor:
        print row