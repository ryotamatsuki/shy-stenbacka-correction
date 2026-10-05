"""Generate the Stage-10 best-response figure from exact rational primitives.

The figure is an exposition object, not proof. Exact assertions preserve the
certified regression (rho, delta, phi) = (3/5, 1, 2).
"""

from fractions import Fraction
from pathlib import Path

RHO = Fraction(3, 5)
DELTA = Fraction(1, 1)
PHI = Fraction(2, 1)

Y_A = DELTA * (2 - 3 * RHO) / (2 * (3 * RHO - 1))
S = 2 * DELTA / (9 * RHO - 2)

def br(y: Fraction) -> Fraction:
    if y >= DELTA:
        return Fraction(0)
    if y <= Y_A:
        return min(PHI, DELTA + 2 * y)
    return min(PHI, 2 * (DELTA - y) / (9 * RHO - 4))

assert Y_A == Fraction(1, 8)
assert S == Fraction(10, 17)
assert br(Fraction(0)) == Fraction(1)
assert br(Fraction(1, 20)) == Fraction(11, 10)
assert br(Fraction(1)) == Fraction(0)
assert br(S) == S

def dec(x: Fraction) -> str:
    return f"{float(x):.8f}".rstrip("0").rstrip(".")

a = Fraction(5, 4)
e = S

tikz = rf"""
\begin{{tikzpicture}}[x=3.0cm,y=3.0cm]
  \draw[->] (0,0) -- (2.08,0) node[right] {{$i_A$}};
  \draw[->] (0,0) -- (0,2.08) node[above] {{$i_B$}};
  \foreach \x/\lab in {{0/0,0.5/0.5,1/1,1.5/1.5,2/2}}
    \draw (\x,0.025) -- (\x,-0.025) node[below] {{\scriptsize \lab}};
  \foreach \y/\lab in {{0.5/0.5,1/1,1.5/1.5,2/2}}
    \draw (0.025,\y) -- (-0.025,\y) node[left] {{\scriptsize \lab}};

  % Firm A: i_A = B(i_B)
  \draw[thick] (1,0) -- ({dec(a)},{dec(Y_A)}) -- (0,1) -- (0,2);
  % Firm B: i_B = B(i_A)
  \draw[thick,dashed] (0,1) -- ({dec(Y_A)},{dec(a)}) -- (1,0) -- (2,0);

  \fill ({dec(e)},{dec(e)}) circle (0.025);
  \fill (1,0) circle (0.025);
  \fill (0,1) circle (0.025);

  \node[above right] at ({dec(e)},{dec(e)}) {{\scriptsize $(10/17,10/17)$}};
  \node[above right] at (1,0) {{\scriptsize $(1,0)$}};
  \node[above right] at (0,1) {{\scriptsize $(0,1)$}};

  \node[anchor=west] at (1.34,1.78) {{\scriptsize solid: $i_A=B(i_B)$}};
  \node[anchor=west] at (1.34,1.62) {{\scriptsize dashed: $i_B=B(i_A)$}};
\end{{tikzpicture}}
""".lstrip()

out = Path("paper/generated/duopoly_best_response.tex")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(tikz, encoding="utf-8")

print("Stage-10 figure regression PASS")
print(f"y_A={Y_A}, s={S}")
print(f"equilibria={(S, S)}, {(Fraction(1), Fraction(0))}, {(Fraction(0), Fraction(1))}")
print(f"wrote {out}")
