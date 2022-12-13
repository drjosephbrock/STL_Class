import numpy as np
import math
from stl import mesh

class My_STL_Class(object):
    def __init__(self,file):
        self.surface = mesh.Mesh.from_file(file)
        self.cg =np.zeros((3))
        print('Input Mesh ranges:')
        xmin = np.min(self.surface.x)
        xmax = np.max(self.surface.x)
        ymin = np.min(self.surface.y)
        ymax = np.max(self.surface.y)
        zmin = np.min(self.surface.z)
        zmax = np.max(self.surface.z)
        self.xrange = xmax - xmin
        self.yrange = ymax - ymin
        self.zrange = zmax - zmin
        print(f'x_min={xmin: .4e} : x_max={xmax: .4e} : range={self.xrange: .4e}')
        print(f'y_min={ymin: .4e} : y_max={ymax: .4e} : range={self.yrange: .4e}')
        print(f'z_min={zmin: .4e} : z_max={zmax: .4e} : range={self.zrange: .4e}')

    def compute_cg_location(self):
        self.cg[0] = np.mean(self.surface.x)
        self.cg[1] = np.mean(self.surface.y)
        self.cg[2] = np.mean(self.surface.z)
        
    def scale_surface(self,scale,center=[0,0,0]):
        self.surface.vectors = self.surface.vectors*scale
        
    def rotate_surface(self, rot_vec, alpha, center=[-99,-99,-99]):
        if center[0] != -99:
            # Define x, y, z from input 'center'
            x = center[0]
            y = center[1]
            z = center[2]
        else:
            # Define x, y, z from object CG
            x = self.cg[0]
            y = self.cg[1]
            z = self.cg[2]

        surf = self.surface
        # Translate to CG
        surf.x -= x
        surf.y -= y
        surf.z -= z
        # rotate
        surf.rotate(rot_vec, math.radians(alpha))
        # translate back
        surf.x += x
        surf.y += y
        surf.z += z
        return surf
    
    def export_stl(self,file='new_surface.stl'):
        self.surface.save(file)