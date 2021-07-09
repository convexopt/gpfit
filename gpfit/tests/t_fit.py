#unit tests for gpfit.fit module"
import unittest
from numpy import logspace, log10, log, vstack
from gpfit.fit import fit

class t_fit(unittest.TestCase):

    u = logspace(0, log10(3), 501)
    w = (u**2 + 3)/(u+1)**2
    x = log(u)
    y = log(w)
    K = 3

    def test_rms_error(self):
        cstrt, rms_error = fit(self.x, self.y, self.K, "SMA")
        self.assertTrue(rms_error < 1e-4)
        cstrt, rms_error = fit(self.x, self.y, self.K, "ISMA")
        self.assertTrue(rms_error < 1e-5)
        cstrt, rms_error = fit(self.x, self.y, self.K, "MA")
        self.assertTrue(rms_error < 1e-2)

    def test_incorrect_inputs(self):
        with self.assertRaises(ValueError):
            fit(self.x, vstack((self.y, self.y)), self.K, "MA")


TESTS = [t_fit]

if __name__ == '__main__':
    SUITE = unittest.TestSuite()
    LOADER = unittest.TestLoader()

    for t in TESTS:
        SUITE.addTests(LOADER.loadTestsFromTestCase(t))

    unittest.TextTestRunner(verbosity=2).run(SUITE)