# -*- coding: UTF-8 -*-
import arcpy
# arcpy.CreateFishnet_management
# (out_feature_class, 包含由矩形单元组成的渔网的输出要素类。
# origin_coord,       渔网的起始枢轴点。
# y_axis_coord,       Y 轴坐标用于定向渔网。按照原点坐标与 y 轴坐标的连线所定义的角度旋转渔网。
# cell_width,         确定每个单元的宽度。如果要使用行数参数值自动计算宽度，则将该参数留空或将该值设置为零，这样在运行工具时便会计算宽度。
# cell_height,        确定每个单元的高度。如果要使用列数参数值自动计算高度，则将该参数留空或将该值设置为零，这样在运行工具时便会计算高度。
# number_rows,        确定渔网所含的行数。如果要使用单元宽度参数值自动计算行数，则将该参数留空或将该值设置为零，这样在运行工具时便会计算行数。
# number_columns,     确定渔网所含的列数。如果要使用单元高度参数值自动计算列数，则将该参数留空或将该值设置为零，这样在运行工具时便会计算列数。
# {corner_coord},     由 X 坐标和 Y 坐标值设置的渔网的对角。
# {labels},           指定是否在每个渔网单元中心创建包含标注点的点要素类。String:LABELS,NO_LABELS
# {template},         指定渔网的范围。可通过指定坐标或使用模板数据集来输入范围。arcpy.Extent()
# {geometry_type})    确定输出渔网单元是折线要素还是面要素。String:POLYLINE ,POLYGON
# 1. 创建渔网
# 指定输出的坐标系统
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326)
# 设置左下角的坐标(x,y)
originCoordinate = '0 0'
# 渔网不旋转,因此将yAxisCoordinate的X坐标设置和originCoordinate一致
yAxisCoordinate = '0 10'
# 将cell设置为0:自动计算每一个网格的大小
cellSizeWidth = '0'
cellSizeHeight = '0'
# 将整个范围设置为10 * 10 的一个格网
numRows =  '10'
numColumns = '10'
# 设置渔网右上角坐标
oppositeCoorner = '180 90'
# 不生成labels
labels = 'NO_LABELS'
# 格网的范围,通过originCoordinate和oppositeCoorner自动计算,不指定模板
templateExtent = '#'
# 生成Polygon
geometryType = 'POLYGON'
arcpy.CreateFishnet_management('./fishnet.shp', originCoordinate, yAxisCoordinate, cellSizeWidth, cellSizeHeight, numRows, numColumns, oppositeCoorner, labels, templateExtent, geometryType)

