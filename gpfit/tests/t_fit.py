#unit tests for gpfit.fit module"
import unittest
from gpfit.fit import fit

class t_fit(unittest.TestCase):
	m = 501
	u = logspace(0,log10(3),501)
	w = (u**2 + 3)/(u+1)**2
	x = log(u)
	y = log(w)
	K = 3

	def test_rms_error(self):
		cstrt, rms_error = fit(x, y, K, "SMA")
		self.assertTrue(self.rms_error < 1e-4)
		cstrt, rms_error = fit(x, y, K, "ISMA")
		self.assertTrue(self.rms_error < 1e-5)
		cstrt, rms_error = fit(x, y, K, "MA")
		self.assertTrue(self.rms_error < 1e-2)

	def test_incorrect_inputs(self):
		err = fit(x, 0, K, "MA")
		self.assertEqual(self.err, 'Dependent data should be a 1D numpy array')
		

TESTS = [t_fit]

if __name__ == '__main__':
    SUITE = unittest.TestSuite()
    LOADER = unittest.TestLoader()

    for t in TESTS:
        SUITE.addTests(LOADER.loadTestsFromTestCase(t))

    unittest.TextTestRunner(verbosity=2).run(SUITE)
 
	
