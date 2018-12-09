# -*- coding: UTF-8 -*-
import arcpy
# 指定命名空间
arcpy.env.workspace = r"./network.mdb"
# 创建一个坐标系统
sr=arcpy.SpatialReference(3857)
# 如果network许可使用,本脚本申请拿到network需要
if arcpy.CheckExtension("network") == "Available":
    arcpy.CheckOutExtension("network")
# 创建最短路径分析图层
# net/net_ND:命名空间下交通网络的路径
# route生成的交通网络图层的名称
# cost用于交通网络分析阻抗属性值
routeLayer=arcpy.na.MakeRouteLayer('wgnet/wgnet_ND', "route", "cost").getOutput(0)
# 获得最短路径分析图层中的子图层,比如:Barriers,Routes,PolylineBarriers,Stops等
naClasses=arcpy.na.GetNAClassNames(routeLayer)
# 如果命名空间下存在该图层,删除改图层
if(arcpy.Exists('stops_Z')):
    arcpy.Delete_management("stops_Z")
# 创建停留点图层(包含Z坐标)
stopsShp=arcpy.CreateFeatureclass_management(arcpy.env.workspace,"stops_Z","POINT",spatial_reference=sr,has_z='ENABLED')
# 为停靠点图层添加停靠点
with arcpy.da.InsertCursor(stopsShp, ["SHAPE@XY","SHAPE@Z"]) as cursor:
    # has_z 确定有Z坐标
    cursor.insertRow([(13594612,4509644),-20])
    cursor.insertRow([(13594740,4509761),120])
# 为最短路径分析图层添加停靠点
arcpy.na.AddLocations(routeLayer,naClasses["Stops"], stopsShp)
# 分析最短路径
arcpy.na.Solve(routeLayer)
# 获得最短路径
with arcpy.da.SearchCursor(arcpy.mapping.ListLayers(routeLayer, naClasses["Routes"])[0],["SHAPE@"]) as cursor:
    for row in cursor:
        # 最短路径是一条折线,获得折现的所有点,注意polyline是多义线,因此一般取[0]
        ptArr=row[0].getPart()[0]
        for pt in ptArr:
            print pt
