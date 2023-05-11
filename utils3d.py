# -*- coding: utf-8 -*-
# @Time    : 2023/5/10 21:20
# @Author  : xinyuan tu
# @File    : visulize3d.py
# @Software: PyCharm
import open3d as o3d
import numpy as np

def readMesh(objpath):
    vertex = []
    triangle = []
    with open(objpath,'r') as f:
        lines = f.readlines()
        for line in lines:
            if line[0:2] =="v ":
                line = line.split(" ")
                v = [float(line[1]),float(line[2]),float(line[3])]
                vertex.append(v)
            if line[0]=="f":
                line = line.split(" ")
                f = [int(line[1].split("//")[0]),int(line[2].split("//")[1]),int(line[3].split("//")[1])]
                triangle.append(f)
    vertex = np.array(vertex)
    triangle = np.array(triangle)
    return vertex,triangle

def writeMesh(objpath,vertex,triangle = None):
    with open(objpath,'w') as f:
        for i in range(vertex.shape[0]):
            f_str = "v "+str(vertex[i,0])+" "+str(vertex[i,1])+" "+str(vertex[i,2])+"\n"
            f.write(f_str)
        if triangle is not None:
            triangle = triangle+1
            for i in range(triangle.shape[0]):
                f_str = "f "+str(triangle[i,0])+" "+str(triangle[i,1])+" "+str(triangle[i,2])+"\n"
                f.write(f_str)
    f.close()

def o3dvisulizepoints(vertex):
    point_cloud = o3d.geometry.PointCloud()
    point_cloud.points = o3d.utility.Vector3dVector(vertex)
    o3d.visualization.draw_geometries([point_cloud])
    return point_cloud

def o3dvisulizeLineSet(vertex,triangle):
    line_set = o3d.geometry.LineSet()
    triangle_line = []
    for t in triangle:
        triangle_line.append([t[0],t[1]])
        triangle_line.append([t[0],t[2]])
        triangle_line.append([t[2],t[1]])
    line_set.lines = o3d.utility.Vector2iVector(triangle_line)
    line_set.points = o3d.utility.Vector3dVector(vertex)
    o3d.visualization.draw_geometries([line_set])
    return line_set

def o3dvisulizeMesh(vertex,triangle):
    mesh = o3d.geometry.TriangleMesh()
    mesh.vertices = o3d.utility.Vector3dVector(vertex)
    mesh.triangles = o3d.utility.Vector3iVector(triangle)
    mesh.compute_vertex_normals()
    o3d.visualization.draw_geometries([mesh])
    return mesh