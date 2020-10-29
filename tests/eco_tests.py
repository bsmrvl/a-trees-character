"""Unit tests for methods in the chartree.tree module"""

import unittest 
import numpy as np
import importlib.util
spec = importlib.util.spec_from_file_location("tree", "../chartree/tree.py")
ct = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ct)

class MethodTests(unittest.TestCase):
    """Unit tests for methods in the chartree.tree module"""

    def test_vec_from_angle(self):
        """Ensure vec_from_angle works in all quadrants, and in both directions."""

        inp0 = np.array([1,1])
        angle = 90
        out0 = np.array([-1,1])
        out0 = out0 / np.linalg.norm(out0)    ## Since vec_from_angle returns a unit vector
        self.assertAlmostEqual(out0[0], ct.vec_from_angle(inp0, angle)[0])
        self.assertAlmostEqual(out0[1], ct.vec_from_angle(inp0, angle)[1])

        inp1 = np.array([1,1])
        angle = -90
        out1 = np.array([1,-1])
        out1 = out1 / np.linalg.norm(out1)
        self.assertAlmostEqual(out1[0], ct.vec_from_angle(inp1, angle)[0])
        self.assertAlmostEqual(out1[1], ct.vec_from_angle(inp1, angle)[1])

        inp2 = np.array([-1,-1])
        angle = -45
        out2 = np.array([-1,0])
        out2 = out2 / np.linalg.norm(out2)
        self.assertAlmostEqual(out2[0], ct.vec_from_angle(inp2, angle)[0])
        self.assertAlmostEqual(out2[1], ct.vec_from_angle(inp2, angle)[1])

        inp3 = np.array([-1,1])
        angle = 135
        out3 = np.array([0,-1])
        out3 = out3 / np.linalg.norm(out3)
        self.assertAlmostEqual(out3[0], ct.vec_from_angle(inp3, angle)[0])
        self.assertAlmostEqual(out3[1], ct.vec_from_angle(inp3, angle)[1])

        inp4 = np.array([1,-1])
        angle = -405
        out4 = np.array([0,-1])
        out4 = out4 / np.linalg.norm(out4)
        self.assertAlmostEqual(out4[0], ct.vec_from_angle(inp4, angle)[0])
        self.assertAlmostEqual(out4[1], ct.vec_from_angle(inp4, angle)[1])

        inp5 = np.array([0,1])
        angle = 180
        out5 = np.array([0,-1])
        out5 = out5 / np.linalg.norm(out5)
        self.assertAlmostEqual(out5[0], ct.vec_from_angle(inp5, angle)[0])
        self.assertAlmostEqual(out5[1], ct.vec_from_angle(inp5, angle)[1])

        inp6 = np.array([-1,0])
        angle = 225
        out6 = np.array([1,1])
        out6 = out6 / np.linalg.norm(out6)
        self.assertAlmostEqual(out6[0], ct.vec_from_angle(inp6, angle)[0])
        self.assertAlmostEqual(out6[1], ct.vec_from_angle(inp6, angle)[1])


if __name__ == "__main__":
    unittest.main()