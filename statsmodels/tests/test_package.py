import subprocess
import sys


def test_lazy_imports():
    # Check that when statsmodels.api is imported, matplotlib is _not_ imported
    cmd = ("import statsmodels.api as sm; "
           "import sys; "
           "mods = [x for x in sys.modules if 'matplotlib.pyplot' in x]; "
           "assert not mods, mods")
    cmd = sys.executable + ' -c "' + cmd + '"'
    p = subprocess.Popen(cmd, shell=False, close_fds=True)
    p.wait()
    rc = p.returncode
    assert rc == 0


def test_docstring_optimization_compat():
    # GH#5235 check that importing with stripped docstrings does not raise
    cmd = sys.executable + ' -OO -c "import statsmodels.api as sm"'
    p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    out = p.communicate()
    rc = p.returncode
    assert rc == 0, out
