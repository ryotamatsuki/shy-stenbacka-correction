# Stage 4A — Partial Reopening and Mathematical Recertification

Date: **2026-09-20**  
Trigger: independent clean-room audit after Stage 13  
Historical Stage-4A record: `audit/STAGE_04A_MATH_RED_TEAM.md`  
Controlling repair ledger: `audit/INDEPENDENT_AUDIT_REPAIR_LEDGER_2026-09-20.md`

## Status

[
oxed{	extbf{GO — C7/C8 MATHEMATICAL RECERTIFICATION PASS}}
]

This is a targeted reopening. It does not erase the original Stage-4A PASS. It records a **certification regression** in two fields of that certificate and supersedes those fields with the repaired statements below.

## 1. Regression found

### C7 — cap-feasibility quantifier

The old Stage-4A certificate described a slope-(+2) global-BR segment as feasible for the whole region (4/9<ho<2/3). That is too strong once the primitive sourcing cap is imposed.

Exact counterexample:
[
(ho,delta,phi)=left(rac35,1,rac1{10}ight).
]
The unconstrained response begins with (R(y)=1+2y), but (R(y)>phi) for every feasible (y), so
[
B_phi(y)equivphi.
]
A source-feasible primitive implementation is
[
H=gamma=1,qquad b=rac35,qquad
phi=rac1{10},qquad a=rac{221}{200},
]
for which (D=1) and the source SOC holds.

The prior Stage-7.5A claim ledger had already used the correct qualifier “whenever the rival-exit piece is feasible.” The regression therefore lies in the Stage-4A/Stage-8/manuscript propagation of C7, not in the Stage-7.5A scope ledger.

### C8 — proof-completeness record

The five-case pure Stage-I correspondence was not falsified. However, the historical Stage-4A clean-room record asserted that branch intersections yield exactly one asymmetric ordered pair without displaying the exclusion logic needed to certify completeness. The old **PASS** therefore overstated the recorded proof completeness.

## 2. Repaired C7 certificate

For
[
rac49<ho<rac23,
]
the **unconstrained** global response (R) contains
[
U(y)=delta+2y
]
on the rival-exit piece.

Define
[
ell=
egin{cases}
0,&1/2leho<2/3,\
y_M,&4/9<ho<1/2,
end{cases}
qquad
J_phi=
{yin[0,phi]:ellle yle y_A, delta+2ylephi}.
]

Then (B_phi(y)=U(y)) on (J_phi). A positive-length feasible increasing segment exists iff

[
phi>delta
quad	ext{for }1/2leho<2/3,
]
and iff
[
phi>M=rac{delta}{4ho-1}
quad	ext{for }4/9<ho<1/2.
]

At equality the feasible exit set degenerates to one point, so there is no positive-length increasing interval.

This suffices to refute the published Proposition 5 as an **unqualified global strategic-substitutes claim**, because admissible source parameters with a positive-slope source-domain best-response segment exist. The paper does not claim that every admissible cap generates such a segment.

C7 state:

[
oxed{	extbf{PROVED — CAP-QUALIFIED}}
]

## 3. Repaired C8 proof certificate

The theorem statement remains unchanged.

Let
[
s=rac{2delta}{9ho-2}.
]

### (ho>2/3)

The capped best response is continuous piecewise affine and globally Lipschitz with constant
[
rac{2}{9ho-4}<1.
]
Thus
[
T(x,y)=(B_phi(y),B_phi(x))
]
is a contraction of ([0,phi]^2). Its fixed point is unique; swap symmetry then forces it to be symmetric.

### (ho=2/3)

[
B_phi(y)=min{phi,max{0,delta-y}}.
]

- (phi<delta/2): unique ((phi,phi)).
- (phi=delta/2): singleton ((delta/2,delta/2)).
- (phi>delta/2): nondegenerate segment (x+y=delta) inside the box.
- if (phigedelta), the segment endpoints are ((0,delta)) and ((delta,0)).

### (4/9<ho<2/3)

The repaired analytic proof establishes
[
y_A<s<delta
]
and the crossing property
[
R(z)>z (z<s),qquad R(s)=s,qquad R(z)<z (z>s).
]

If (phile s), this yields the unique capped fixed point ((phi,phi)), including (phi=s).

If (phi>s), any asymmetric equilibrium can be ordered (x_H>x_L), which forces
[
x_L<s<x_H.
]

- If (x_H<delta), then (x_L=A(x_H)). Uncapped active/active responses cannot be asymmetric because the affine active equations force equality when (ho
e2/3); an uncapped exit response would imply (x_Hgedelta); an uncapped monopoly response, where present, gives (x_H=M>delta); and the zero branch cannot generate the high action. Hence the high action must be capped, (x_H=phi), and (x_L=A(phi)). Direct substitution verifies (B_phi(x_L)=phi).
- If (x_Hgedelta), then (x_L=0) and mutual best response requires (x_H=B_phi(0)=min{phi,R(0)}).

The two cases combine to
[
x_H=min{phi,R(0)},qquad x_L=R(x_H),
]
with no additional cap needed on (x_L). Thus there is exactly one ordered asymmetric pair plus its mirror.

C8 state:

[
oxed{	extbf{PROVED — COMPLETE PURE STAGE-I SOURCE-DUOPOLY CORRESPONDENCE}}
]

No mixed-strategy completeness is implied.

## 4. Independent verification

New independent verifier:

`code/independent_audit_repair_verify.py`

It reconstructs Cournot continuation and payoffs from primitive active-set/KKT conditions rather than importing the production response function.

It checks:

- C7 small-cap disappearance and strict cap thresholds;
- (ho=1/2) and a representative (4/9<ho<1/2) case;
- the original ((3/5,1,2)) positive-slope witness;
- C8 symbolic crossing identities;
- all five C8 regimes and major equality/cap boundaries;
- the all-active multiplicity regression;
- literal Hotelling best-response/equilibrium regressions;
- no-loss strict/tie regressions;
- welfare regressions.

The numerical/exact finite regressions are diagnostics. The complete C8 proof is analytic and recorded in `paper/sections/appendix.tex`.

## 5. C1/C2 proof-record repair

The independent audit also identified non-falsifying proof omissions.

- C1 now records coercivity of the exact potential before invoking strict concavity/KKT uniqueness.
- C2 now records own entry, monotone downstream price, no re-entry, finite rival exits, simultaneous-exit derivative jumps, and one-sided derivative monotonicity.

C1 and C2 theorem statements are unchanged.

## 6. Verdict

The old Stage-4A C7 quantifier and C8 proof-completeness record are superseded by this document.

No source model, equilibrium concept, or C8 equilibrium set is changed.

[
oxed{	extbf{STAGE 4A TARGETED RECERTIFICATION — PASS}}
]
