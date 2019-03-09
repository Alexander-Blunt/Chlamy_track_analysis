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
        for i in range(0, num_points-3):
            curv1 = sa.calc_curv(spiral[i,:], spiral[i+1,:], spiral[i+2,:])
            curv1 = ( curv1[0]**2 + curv1[1]**2 + curv1[2]**2 ) **0.5
            curv2 = sa.calc_curv(spiral[i+1,:], spiral[i+2,:], spiral[i+3,:])
            curv2 = ( curv2[0]**2 + curv2[1]**2 + curv2[2]**2 ) **0.5
            success = (curv2 - curv1) < diff

        self.assertTrue(success, 'Curvature must be constant')

if __name__ == '__main__':
    unittest.main()

