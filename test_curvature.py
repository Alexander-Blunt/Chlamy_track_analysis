# A test for the calc_curv routine in the spiral_analysis program

import unittest
import numpy as np

import spiral_analysis as sa

class TestCurvature(unittest.TestCase):

    def test_constant(self):
        max_z = 7.0 # maximum value of z to include 2pi
        num_points = 100 # number of points in spiral
        z_inc = max_z / num_points # number to increase z by for each point
        
        # Generate circular spiral
        spiral = np.zeros( (num_points, 3), dtype='float' )
        for i in range(0, num_points):
            spiral[i,0] = i * z_inc
            spiral[i,1] = np.sin(spiral[i,0])
            spiral[i,2] = np.cos(spiral[i,0])

        # Check that curvature is constant throughout the spiral
        diff = 1e-10 # threshold for comparison of floats
        success = True # assume curvature is constant
        # set first curvature to compare the rest of the spiral to
        curv1 = sa.calc_curv(spiral[0,:], spiral[0+1,:], spiral[0+2,:])
        curv1 = ( curv1[0]**2 + curv1[1]**2 + curv1[2]**2 ) **0.5
        for i in range(1, num_points-3):
            curv2 = sa.calc_curv(spiral[i+1,:], spiral[i+2,:], spiral[i+3,:])
            curv2 = ( curv2[0]**2 + curv2[1]**2 + curv2[2]**2 ) **0.5
            if abs(curv2 - curv1) > diff:
                success = False

        self.assertTrue(success, 'Curvature must be constant')

if __name__ == '__main__':
    unittest.main()

