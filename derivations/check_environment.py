"""Toolchain smoke test only; these assertions are not checks of course answers.

Add separate Python scripts here for results you have first derived by hand.
"""
import mpmath as mp
import sympy as sp

x = sp.symbols("x")
assert sp.diff(x**3, x) == 3 * x**2
assert sp.integrate(x, (x, 0, 1)) == sp.Rational(1, 2)
with mp.workdps(50):
    assert abs(mp.quad(lambda t: t, [0, 1]) - mp.mpf("0.5")) < mp.mpf("1e-45")
print(f"PASS symbolic differentiation/integration (SymPy {sp.__version__})")
print(f"PASS 50-digit numerical integration (mpmath {mp.__version__})")
