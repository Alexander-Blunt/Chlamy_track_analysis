# A test for the calc_curv routine in the spiral_analysis program

import unittest
import numpy as np

import spiral_analysis as sa

#------------------------------------------------------------------------------
# Program constants
#------------------------------------------------------------------------------
diff = 1e-10 # threshold for comparison of floats

#------------------------------------------------------------------------------
# Generate a spiral for later testing
#------------------------------------------------------------------------------
max_z = 7.0 # maximum value of z to include 2pi
num_points = 100 # number of points in spiral
z_inc = max_z / num_points # number to increase z by for each point

# Generate circular spiral with radius 1
spiral = np.zeros( (num_points, 3), dtype='float' )
for i in range(0, num_points):
    spiral[i,0] = i * z_inc
    spiral[i,1] = np.sin(spiral[i,0])
    spiral[i,2] = np.cos(spiral[i,0])

#------------------------------------------------------------------------------
# Test the curvature function
#------------------------------------------------------------------------------
class TestCurvature(unittest.TestCase):

    #--------------------------------------------------------------------------
    # Check that curvature is constant throughout the spiral
    #--------------------------------------------------------------------------
    def test_constant(self):
        success = True # assume curvature is constant
        # Set first curvature to compare the rest of the spiral to
        curv1 = sa.calc_curv(spiral[0,:], spiral[1,:], spiral[2,:])
        curv1 = ( curv1[0]**2 + curv1[1]**2 + curv1[2]**2 ) **0.5
        for i in range(1, num_points-3):
            curv2 = sa.calc_curv(spiral[i+1,:], spiral[i+2,:], spiral[i+3,:])
            curv2 = ( curv2[0]**2 + curv2[1]**2 + curv2[2]**2 ) **0.5
            if abs(curv2 - curv1) > diff:
                success = False

        self.assertTrue(success, 'Curvature must be constant')

    #--------------------------------------------------------------------------
    # Check curvature gives correct result for a circle
    #--------------------------------------------------------------------------
    def test_value(self):
        success = True # assume curvature is correct

        # Set radius of circle
        rad = 2.0
        circle = spiral
        circle[:,0] = 0.0
        circle[:,1] *= rad
        circle[:,2] *= rad

        for i in range(0, num_points-3):
            curv = sa.calc_curv(circle[i,:], circle[i+1,:], circle[i+2,:])
            curv = ( curv[0]**2 + curv[1]**2 + curv[2]**2 ) **0.5
            if abs(curv - 1/rad) > 1/num_points:
                success = False

        self.assertTrue(success, 'Curvature of a circle should be 1/radius')

    #--------------------------------------------------------------------------
    # Check curvature remains constant on rotation
    #--------------------------------------------------------------------------
    def test_rotation(self):
        angle = 0.3 # arbitrary angle for rotation matrix
        rot = np.array( [ [1, 0, 0],
                          [0, np.cos(angle), -1 * np.sin(angle)],
                          [0, np.sin(angle), np.cos(angle)] ] )

        success = True
        for i in range(0, num_points-3):
            # Calculate initial curvature
            curv1 = sa.calc_curv(spiral[i,:], spiral[i+1,:], spiral[i+2,:])
            curv1 = (curv1[0]**2 + curv1[1]**2 + curv1[2]**2) **0.5

            # Rotate matrix points
            point0 = np.matmul(rot, spiral[i,:])
            point1 = np.matmul(rot, spiral[i+1,:])
            point2 = np.matmul(rot, spiral[i+2,:])

            curv2 = sa.calc_curv(point0, point1, point2)
            curv2 = (curv2[0]**2 + curv2[1]**2 + curv2[2]**2) **0.5

            if abs(curv2-curv1) > diff:
                success = False

        self.assertTrue(success, 'Curvature must be constant on rotation')

    #--------------------------------------------------------------------------
    # Test curvature output function
    #--------------------------------------------------------------------------
    def test_output(self):
        # Set up input track for function
        track = np.zeros( ( num_points, 7 ) )
        for i in range(0, num_points):
            track[i, 0] = i
            track[i, 4:] = spiral[i, :]

        curvature = sa.output_curv(track, 1)
        success = True
        print(curvature)

        for i in range(0, num_points-3):
            # Calculate curvature at i
            curv_i = sa.calc_curv(spiral[i,:], spiral[i+1,:], spiral[i+2,:])
            curv_i = (curv_i[0]**2 + curv_i[1]**2 + curv_i[2]**2) **0.5
            print(curv_i)
            if abs(curvature[i,1]-curv_i) > diff:
                success = False

        self.assertTrue(success, 'Curvature output should equal curvature')

if __name__ == '__main__':
    unittest.main()

