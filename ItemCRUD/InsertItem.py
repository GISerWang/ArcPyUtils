# -*- coding: UTF-8 -*-
import arcpy
arcpy.env.workspace = r"./ItemCRUDTest.mdb"
# 1.插入点元素（没有Z元素）
# 每次插入一行，都需要两个值，第一个值是name，第二个值是XY坐标
with arcpy.da.InsertCursor("insertItem/point",['name','SHAPE@XY']) as cursor:
    # 构造插入的行
    row=('test1',(110,50))
    # 插入元素
    cursor.insertRow(row)

# 2.插入线元素（没有Z元素）
# 每次插入一行，都需要两个值，第一个值是name，第二个值是线的形状
with arcpy.da.InsertCursor("insertItem/line",['name','SHAPE@']) as cursor:
    arr = arcpy.Array([arcpy.Point(110.12, 50.1285),
                       arcpy.Point(115.3818,55.0808)])
    line=arcpy.Polyline(arr)
    cursor.insertRow(['test2',line])

# 3.插入面元素（没有Z元素）
with arcpy.da.InsertCursor("insertItem/polygon",['name','SHAPE@']) as cursor:
    arr = arcpy.Array([arcpy.Point(110.12, 50.1285),
                       arcpy.Point(115.3818,55.0808),
                       arcpy.Point(117.3818, 55.0808)])
    polygon=arcpy.Polygon(arr)
    cursor.insertRow(['test3',polygon])

# 4.插入具有Z值的要素需要主要的两点
#   创建的要素类需要指定属性has_z='ENABLED'
#   组成Point，需要指定Z元素，比如：arcpy.Point(110.12, 50.1285,10)
#   创建的几何类需要启用Z，比如arcpy.Polygon(arr,sr,True),arcpy.Polyline(arr,sr,True),arcpy.PointGeometry(,sr,True)
#   但是一定不要这样写（会报错）：arcpy.Polygon(arr,has_z=True),arcpy.Polyline(arr,has_z=True),arcpy.PointGeometry(,,has_z=True)