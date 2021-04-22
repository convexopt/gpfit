"Runs all tests"
from gpkit.tests.helpers import run_tests
TESTS = []

from gpfit.tests import t_LM
TESTS += t_LM.TESTS

from gpfit.tests import t_lse_implicit
TESTS += t_lse_implicit.TESTS

from gpfit.tests import t_lse_scaled
TESTS += t_lse_scaled.TESTS

from gpfit.tests import t_ba_init
TESTS += t_ba_init.TESTS

from gpfit.tests import t_max_affine
TESTS += t_max_affine.TESTS

from gpfit.tests import t_softmax_affine
TESTS += t_softmax_affine.TESTS

from gpfit.tests import t_implicit_softmax_affine
TESTS += t_implicit_softmax_affine.TESTS

from gpfit.tests import t_print_fit
TESTS += t_print_fit.TESTS

from gpfit.tests import t_ex6_3
TESTS += t_ex6_3.TESTS

from gpfit.tests import t_examples
TESTS += t_examples.TESTS

from gpfit.tests import t_fit
TESTS += t_fit.TESTS


def run(xmloutput=False):
    """Run all gpfit unit tests.

    Arguments
    ---------
    xmloutput: bool
        If true, generate xml output files for continuous integration
    """
    if xmloutput:
        run_tests(TESTS, xmloutput='test_reports')
    else:
        run_tests(TESTS)


if __name__ == '__main__':
    run()
