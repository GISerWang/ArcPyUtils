# -*- coding: UTF-8 -*-
import arcpy
arcpy.env.workspace = r"./ItemCRUDTest.mdb"
# 1.通过where_clause查询数据
with arcpy.da.SearchCursor("searchItem/town",['*'],where_clause='Name="陈城镇"') as cursor:
    for row in cursor:
        print row

# 2.查询线数据的点集合
with arcpy.da.SearchCursor("searchItem/lineFeature",['SHAPE@']) as cursor:
    for row in cursor:
        #获得面要素的所有点要素
        for pt in row[0].getPart()[0]:
            print pt

# 3.查询面数据的点集合
with arcpy.da.SearchCursor("searchItem/cityRegion",['SHAPE@']) as cursor:
    for row in cursor:
        #获得面要素的所有点要素
        for pt in row[0].getPart()[0]:
            print pt