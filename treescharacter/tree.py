"""Grow a tree in an Ecosystem object."""

import numpy as np
import math

def vec_from_angle(from_vec, angle):
    from_vec = np.copy(from_vec)
    arc = np.arctan(from_vec[1]/from_vec[0])*180/math.pi
    if from_vec[0]<0:
        big = 180+arc+angle
    elif from_vec[1]<0:
        big = 360+arc+angle
    else:
        big = arc+angle
    big = math.pi*big/180
    return np.array([np.cos(big), np.sin(big)])

class Branch:
    def __init__(self, center, width, direction):
        self.center = np.array(center)
        self.width = width
        self.direction = np.array(direction)/np.linalg.norm(np.array(direction))     ## as unit vector
        self.thresh = .5

class Ecosystem:
    """A must for most trees. Set up your Ecosystem and then use grow() and show() methods to create your tree.\n\nParameters:\n-------------\nsize : array_like\n\tThe shape of the character grid, equalized to account for characters being taller than they are wide. Default is [50,40].\n\nReturns:\n------------\nEcosystem object, with grow() and show() methods.\n"""

    def __init__(self, size=[50,40]):
        self.w = size[0]*2
        self.h = size[1]
        self.plot = 'Nothing has grown!'
        
    def make_wood(self, coor):
        coor = np.copy(coor)
        coor[0] = coor[0]*2
        coor = np.round(coor).astype(int)
        if(coor[1]>=0 and coor[1]<self.h and coor[0]>=0 and coor[0]<self.w):
            self.plot[coor[1], coor[0]] = 1
        
    def show(self, material='$', background='`'):
        """Shows the grown tree. Can be used to experiment with characters without changing the shape of the tree. Must be called after grow() or grow_show()!\n\nParameters:\n-------------\nmaterial : char\n\tThe character used to fill the tree. Must be a single character. Default is '$'.\nbackground : char\n\tThe character used to fill the background of the Ecosystem. Default is '`'.\n\nReturns:\n------------\nNothing. Simply prints tree.\n"""

        if isinstance(self.plot, str):
            print(self.plot)
        else:
            whole = ''
            for row in self.plot:
                line = ''
                for let in row:
                    if let==1:
                        line += material
                    else:
                        line += background
                whole += (line+'\n')
            print(whole)
            
    def grow(self, trunk=3, n_iter=40, density=9, ang_mean=35, ang_range=5):
        """Grows a tree, starting at the bottom center of the grid.\n\nParameters:\n-------------\ntrunk : int\n\tThe starting radius of the trunk. Default is 3.\nn_iter : int\n\tThe number of growth iterations. Default is 40.\ndensity : int\n\tThe rate at which new branches form. Lower numbers are denser. Default is 9, which means new branches form every 9 growth iterations.\nang_mean : int\n\tThe mean angle of branch splits. Default is 35.\nang_range : int\n\tThe range, above and below ang_mean, of angle possibilities. A higher range means a more unpredictable tree. Default is 5.\n\nReturns:\n------------\nNothing. View the grown tree with show().\n"""

        self.plot = np.full(shape=(self.h, self.w), fill_value=0)
        branches = [Branch(center=[self.w/4, self.h], width=trunk, direction=[.001,-7])]
        
        for i in range(n_iter):
            hard_length = len(branches)
            for br in branches:
                if branches.index(br) == hard_length:
                    break
                for r in np.arange(0, br.width/2, .1):
                    ring = np.array([1.,1.])
                    ring -= ring.dot(br.direction) * br.direction
                    ring /= np.linalg.norm(ring)
                    ring *= r

                    self.make_wood(br.center + ring)
                    self.make_wood(br.center - ring)

                if i%density == 0:
                    ang = np.random.randint(ang_mean-ang_range, ang_mean+ang_range)\
                                            * (1 if np.random.random() > br.thresh else -1)
                    if ang<0:
                        br.thresh -= .5
                    else:
                        br.thresh += .5

                    if i>.5*n_iter and br.width > .4:
                        branches.append(Branch(center=br.center,
                                               width=((br.width**2)*.5)**(1/2),
                                               direction=vec_from_angle(br.direction,.5*ang)))
                        br.direction = vec_from_angle(br.direction, -.5*ang)
                        br.width = ((br.width**2)*.5)**(1/2)
                    else:
                        branches.append(Branch(center=br.center, 
                                               width=((br.width**2)*.2)**(1/2),
                                               direction=vec_from_angle(br.direction,ang)))
                        br.direction = vec_from_angle(br.direction, -.15*ang)
                        br.width = ((br.width**2)*.8)**(1/2)
                br.center = br.center + br.direction
                br.width *= .97
                
    def grow_show(self, trunk=3, n_iter=40, density=9, ang_mean=35, ang_range=5, material='$', background='`'):
        """Combines grow() and show() methods, using the same parameters.\n"""

        self.grow(trunk, n_iter, density, ang_mean, ang_range)
        self.show(material, background)