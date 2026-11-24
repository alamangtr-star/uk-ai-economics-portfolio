import unittest
import numpy as np
from python_econometrics_demo import synthetic_data, fit_model, leave_one_out


class DemoTests(unittest.TestCase):
    def test_reproducibility(self):
        self.assertTrue(synthetic_data().equals(synthetic_data()))

    def test_equal_weights(self):
        d = synthetic_data().assign(employment=1)
        np.testing.assert_allclose(fit_model(d).params, fit_model(d, False).params)

    def test_known_slope(self):
        d = synthetic_data()
        d['exposure'] = 1 + 2*d.sme_share
        self.assertAlmostEqual(fit_model(d).params['sme_share'], 2)

    def test_invalid_weight(self):
        d = synthetic_data()
        d.loc[0, 'employment'] = 0
        with self.assertRaises(ValueError):
            fit_model(d)

    def test_sensitivity(self):
        d = synthetic_data()
        out = leave_one_out(d)
        self.assertEqual(len(out), len(d))
        self.assertTrue(np.isfinite(out.slope).all())


if __name__ == '__main__':
    unittest.main()
