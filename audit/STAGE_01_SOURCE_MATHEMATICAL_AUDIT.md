# Stage 1 — Source & Mathematical Audit

Status: **PASS — GO TO NOVELTY GATE**

Audit date: 2026-09-19  
Canonical workflow: `research-paper-workflow` v2.2, main SHA `42574d6c5931275ccff3ef7e8b4acc188077332a`

## 1. Executive audit verdict

The published Shy–Stenbacka (2005) model contains mathematically material defects that survive reconstruction using the paper's own primitives and normalization.

Four findings are Stage-1 certified:

1. **Equation (14) has the wrong sign.** For the paper's own Cournot interior solution, outsourcing per firm decreases with the number of Cournot firms for every (N>1), not increases.
2. **The outsourcing strategy bound is omitted.** Since inputs form (I=[0,phi]), every firm must satisfy (0le i_jlephi). Equations (13) and (25) can exceed (phi) under the paper's stated restrictions.
3. **The Cournot continuation is not globally defined by equation (10).** The paper solves the all-active Cournot branch, but admissible asymmetric outsourcing choices can make the formula imply a negative quantity. A valid SPNE audit therefore requires piecewise active-set continuations.
4. **The Hotelling continuation is not globally defined by equations (19)–(21).** Admissible outsourcing deviations can move the price subgame outside the interior-market-share branch. For a nonempty parameter region satisfying the paper's own second-order condition, such a corner deviation is strictly profitable against the reported symmetric candidate.

These are not cosmetic transcription issues. The first reverses Proposition 3's headline Cournot comparative static. The fourth supplies a source-model counterexample to the unqualified Hotelling equilibrium claim.

Stage 1 does **not** claim novelty. It establishes a verified residual research object for Stage 2.

## 2. Canonical source model

### 2.1 Source identity

Oz Shy and Rune Stenbacka (2005), “Partial outsourcing, monitoring cost, and market structure,” *Canadian Journal of Economics / Revue canadienne d'économique*, 38(4), 1173–1190. DOI: `10.1111/j.0008-4085.2005.00320.x`.

The publisher records first online publication on 27 October 2005 and the article in the November 2005 issue.

### 2.2 Technology and outsourcing

Inputs form a continuum (I=[0,phi]). Hence an outsourcing measure is intrinsically bounded:

[
0le i_jlephi.
]

Input costs are ordered by an index (i). The paper first permits diminishing/rising outsourcing advantage, then imposes constant advantage ((alpha=1)) and normalizes the subcontractor intercept to (S=0).

Under those maintained assumptions, if firm (j) outsources measure (i_j),

[
c_j=H(phi-i_j)+rac{gammaphi^2}{2}
=C_0-Hi_j,
qquad
C_0equiv Hphi+rac{gammaphi^2}{2}.
]

Monitoring cost is **exactly**

[
M(i_j)=i_j^2.
]

No free coefficient multiplying (i_j^2) is part of the published model. Any (eta i_j^2) representation is a later generalization and is not used in this Stage-1 certification.

Define

[
Dequiv a-C_0>0.
]

### 2.3 Timing and equilibrium concept

Both product-market specifications are two-stage games.

1. Stage I: firms choose their production mode / set (equivalently, under constant advantage, measure) of outsourced inputs.
2. Stage II: firms compete in the final-good market—Cournot quantities in Section 3 or Hotelling prices in Section 4.

The paper states that it seeks subgame-perfect equilibrium and focuses on symmetric equilibria.

### 2.4 Cournot branch reconstructed from primitives

Inverse demand is

[
p=a-bQ.
]

On an all-active Cournot branch with arbitrary marginal costs,

[
q_j=
rac{a-Nc_j+sum_{k
e j}c_k}{b(N+1)}.
]

Substituting (c_j=C_0-Hi_j) gives

[
q_j=
rac{D+NH i_j-Hsum_{k
e j} i_k}{b(N+1)}.
]

Because (p-c_j=bq_j) on this regular branch,

[
Pi_j^{mathrm{active}}
=
rac{left[D+NH i_j-HS_{-j}ight]^2}{b(N+1)^2}-i_j^2,
qquad
S_{-j}equivsum_{k
e j}i_k.
]

The paper's restriction

[
b>left(rac{HN}{N+1}ight)^2
]

is equivalent to strict concavity of this active-branch payoff in own outsourcing:

[
b(N+1)^2-N^2H^2>0.
]

The active-branch stationary best response is

[
u_j(S_{-j})
=
rac{NH(D-HS_{-j})}
{b(N+1)^2-N^2H^2}.
]

At symmetry the interior candidate is

[
i_{C,mathrm{int}}
=
rac{HND}
{b(N+1)^2-NH^2},
]

which is equation (13) after algebraic simplification.

### 2.5 Hotelling branch reconstructed from primitives

Use (	au>0) as canonical notation for the paper's differentiation/transport parameter. With firms at 0 and 1, the interior indifferent consumer satisfies

[
hat x=rac12+rac{p_B-p_A}{2	au}.
]

The familiar interior price solution is

[
p_A=rac{2c_A+c_B+3	au}{3},
qquad
p_B=rac{c_A+2c_B+3	au}{3}.
]

At those prices,

[
hat x
=
rac12+rac{c_B-c_A}{6	au}
=
rac12+rac{H(i_A-i_B)}{6	au}.
]

Therefore the interior price branch itself requires

[
|H(i_A-i_B)|le 3	au.
]

Conditional on that branch, firm (A)'s Stage-I payoff is

[
Pi_A^{mathrm{int}}
=
rac{n[3	au+H(i_A-i_B)]^2}{18	au}-i_A^2.
]

Its stationary best response is

[
u_H(i_B)=
rac{Hn(3	au-H i_B)}
{18	au-H^2n},
]

with local concavity condition

[
	au>rac{H^2n}{18}.
]

The symmetric stationary solution is

[
i_{H,mathrm{int}}=rac{Hn}{6}.
]

## 3. Equation-by-equation audit

| Published object | Stage-1 classification | Audit result |
|---|---|---|
| (1) input-cost ordering | **CORRECT** | Defines the input-cost slope used in the sorting result. |
| (2) total production cost | **CORRECT** | Separates variable input cost and fixed monitoring cost. |
| (3) marginal cost | **CORRECT** | Consistent with (2). |
| (4) profit | **CORRECT** | Consistent with (2)–(3). |
| (5) marginal cost under Assumption 2 | **CORRECT** | Gives (c_j=C_0-Hi_j). |
| (6) quadratic monitoring cost | **CORRECT** | Crucially, the coefficient is normalized to one. |
| (7) linear Cournot demand | **CORRECT** | Standard inverse demand. |
| (8) parameter restrictions | **AMBIGUOUS / INSUFFICIENT FOR GLOBAL SPNE** | Gives (D>0) and active-branch outsourcing concavity, but neither (i_jlephi) interiority nor all-active continuation for every feasible deviation. |
| (9) Cournot quantity objective | **CORRECT** | Given a valid Stage-II feasible quantity domain. |
| (10)–(11) Cournot solution | **CORRECT ON ALL-ACTIVE BRANCH ONLY** | Can imply (q_j<0) at feasible asymmetric outsourcing histories. |
| (12) outsourcing FOC | **CORRECT ON REGULAR BRANCH** | Does not itself establish global best response. |
| (13) symmetric outsourcing formula | **CORRECT AS INTERIOR STATIONARY CANDIDATE; INCORRECT AS UNQUALIFIED SPNE** | Can exceed (phi); off-path Stage-II active sets also require treatment. |
| (14) (N)-comparative static | **INCORRECT** | Published positive sign is reversed. |
| (15) Cournot-duopoly BR | **CORRECT LOCALLY / INCOMPLETE GLOBALLY** | Ignores outsourcing boundaries and possible active-set changes. |
| (16) Hotelling utility | **CORRECT** | Standard full-coverage formulation. |
| (17) indifferent consumer | **CORRECT ALGEBRAICALLY** | Interior market share additionally requires (hat xin[0,1]). |
| (18) profits | **CORRECT ON INTERIOR SHARE BRANCH** | Uses (hat x) as a market share. |
| (19)–(20) price/profit solution | **CORRECT ON INTERIOR SHARE BRANCH** | Not the continuation for sufficiently asymmetric costs. |
| (21) Stage-I Hotelling payoff | **CORRECT LOCALLY / INCORRECT AS GLOBAL CONTINUATION** | Extrapolates the interior price branch beyond its domain. |
| (22) local Hotelling BR | **CORRECT LOCALLY** | Requires the interior price branch and outsourcing feasibility. |
| (23) local SOC | **CORRECT LOCALLY** | Does not imply global concavity after the market-share regime changes. |
| (24) BR slope | **CORRECT LOCALLY** | Strict negativity is not a global constrained-BR theorem. |
| (25) symmetric Hotelling solution | **CORRECT AS INTERIOR STATIONARY CANDIDATE; INCORRECT AS UNQUALIFIED SPNE** | May violate (ilephi) and can admit a profitable corner-regime deviation. |
| (26) outsourcing fraction | **CORRECT ONLY CONDITIONAL ON (25)'S INTERIOR VALIDITY** | Not globally established. |

## 4. SOC / feasibility / participation audit

### 4.1 Cournot SOC

The active-branch second derivative is negative under the paper's condition (8):

[
b(N+1)^2-N^2H^2>0.
]

This certifies strict concavity **of that branch only**. It does not certify the active-set domain, the outsourcing upper bound, or all unilateral deviations.

### 4.2 Missing Cournot outsourcing cap — isolated exact witness

Choose

[
phi=1,quad H=1,quad gamma=rac1{10},quad
N=2,quad b=rac12,quad a=rac{51}{20}.
]

Then

[
C_0=rac{21}{20},qquad D=rac32,
]

condition (8) holds, and even the sufficient all-active condition for every feasible outsourcing pair,

[
D>H(N-1)phi,
]

holds strictly. Nevertheless equation (13) gives

[
i_{C,mathrm{int}}=rac65>phi.
]

Thus the missing outsourcing cap is a genuine source-model defect, not an artifact of a Cournot active-set transition.

### 4.3 Cournot off-path active-set failure — exact witness

Choose

[
phi=1,quad H=1,quad gamma=rac1{10},quad
N=2,quad b=rac12,quad a=rac54.
]

The paper's restrictions hold: (D=1/5>0) and the outsourcing-concavity inequality is strict. But at the feasible history ((i_j,i_k)=(0,1)), equation (10) assigns the high-cost firm

[
q_j=-rac{8}{15}<0.
]

The actual Cournot continuation is a corner: the low-cost firm has marginal cost (1/20), the high-cost firm (21/20), and the low-cost monopoly solution has

[
q=rac65,qquad p=rac{13}{20}<rac{21}{20}=c_{mathrm{high}},
]

so the high-cost firm is inactive.

Therefore the regular Cournot formula cannot be used as a global continuation payoff for Stage-I deviations without an additional active-set condition.

### 4.4 Hotelling outsourcing cap — exact witness

Choose

[
H=n=	au=1,qquad phi=rac1{10}.
]

The paper's local SOC (	au>H^2n/18) holds, yet equation (25) gives

[
i_{H,mathrm{int}}=rac16>phi.
]

### 4.5 Hotelling global deviation — exact source-model witness

Choose

[
H=n=1,qquad
	au=rac1{15},qquad
phi=1.
]

The paper's SOC holds because

[
rac1{15}>rac1{18}.
]

Its symmetric candidate is

[
i_0=rac16.
]

Let firm (A) deviate to

[
i_A=rac12.
]

This is feasible. Its cost advantage relative to the rival is

[
H(i_A-i_0)=rac13>3	au=rac15,
]

so the interior price solution is no longer the relevant continuation.

For cost advantage (d=c_B-c_Age3	au), a corner price equilibrium has the low-cost firm serving the market at the limiting price (p_A=c_B-	au), yielding operating profit (n(d-	au)). Hence the deviating Stage-I payoff is

[
Pi_{mathrm{dev}}=rac1{60},
]

while the paper's symmetric candidate yields

[
Pi_{mathrm{sym}}=rac1{180}.
]

Thus

[
Pi_{mathrm{dev}}-Pi_{mathrm{sym}}=rac1{90}>0.
]

More generally, evaluating the corner optimum (i_A=Hn/2) against (i_0=Hn/6) gives

[
Pi_{mathrm{dev}}-Pi_{mathrm{sym}}
=
rac{n(2H^2n-27	au)}{18}.
]

A profitable-deviation region therefore exists when

[
rac{27}{2}	au<H^2n<18	au,
]

subject also to feasibility of the deviation. This interval is nonempty and satisfies the paper's local SOC.

### 4.6 Participation / market coverage

The Cournot model has no separate participation constraint beyond nonnegative output and the outsourcing feasibility set.

The Hotelling specification allocates consumers between the two brands and does not introduce an outside option in the analyzed price game. Stage 1 therefore treats market coverage as a maintained source assumption rather than adding a new participation condition.

## 5. Parameter-interpretation audit

- (H): constant subcontracting cost advantage after the paper's normalization (S=0).
- (gamma): slope of heterogeneous input production costs. Under constant outsourcing advantage it enters the common cost baseline (C_0).
- (phi): both the total measure of required inputs and the **hard upper bound** on outsourcing. This dual role is mathematically material.
- (a,b): Cournot demand intercept and inverse-demand slope. The paper varies (N), not (b), as its main Cournot competition-intensity measure.
- (n): Hotelling market density/size.
- (	au): canonical notation here for the source differentiation/transport parameter.
- Monitoring cost is (i_j^2), not (eta i_j^2). Stage 1 rejects importation of a free monitoring-cost coefficient into the source-model audit.

No parameter-mixing defect is needed to generate the certified failures above.

## 6. Welfare / comparability audit

The article's headline claims are equilibrium and comparative-static claims, not a planner-welfare theorem. Stage 1 therefore records **no welfare correction claim**.

No Cournot-versus-Hotelling welfare comparison is licensed by this audit. The two market structures should not be compared using an invented common welfare benchmark absent an explicit planner problem.

## 7. Correct vs incorrect claim table

| Published result | Classification | Stage-1 conclusion |
|---|---|---|
| Proposition 1 | **CORRECT** | Input sorting follows from the stated relative-cost ordering. |
| Corollary 2 | **CORRECT** | Follows from Proposition 1 under its assumptions. |
| Equation (13) as algebraic interior candidate | **CORRECT** | Re-derived exactly. |
| Equation (13) as unqualified SPNE | **INCORRECT** | Can violate (ilephi); global continuation also needs active-set handling. |
| Equation (14) | **INCORRECT** | Sign is negative for (N>1), not positive. |
| Proposition 3 | **INCORRECT** | Its central Cournot competition conclusion is reversed on the interior branch. |
| Corollary 4 | **AMBIGUOUS / OVERSTATED GLOBALLY** | Interior derivative directions survive; hard bounds can turn strict effects into weak/flat effects. |
| Proposition 5 | **CORRECT LOCALLY / OVERSTATED GLOBALLY** | Local regular-branch BR slope is negative; the global constrained game is not established by (15). |
| Equations (19)–(24) | **CORRECT LOCALLY** | Valid on the interior Hotelling market-share branch. |
| Equation (25) / Proposition 6 as global equilibrium | **INCORRECT** | Missing (ilephi) and defeated by an admissible corner-regime deviation. |
| Abstract/conclusion claim that more Cournot competition increases outsourcing | **INCORRECT** | Same sign defect as Proposition 3; not a mere display-equation typo. |

For the Cournot interior solution,

[
rac{partial i_{C,mathrm{int}}}{partial N}
=
-rac{HDb(N^2-1)}
{left[b(N+1)^2-H^2Night]^2}<0
quad(N>1).
]

The source-model comparative statics behind Corollary 4 are, on the interior branch,

[
rac{partial i}{partial a}>0,qquad
rac{partial i}{partialgamma}<0,qquad
rac{partial i}{partialphi}<0,
]

and the same sign directions hold for the outsourcing fraction (i/phi). Once the upper bound binds, strict comparative statics need not remain strict.

## 8. Surviving economic questions

The audited residual research question is not whether a typo exists. It is:

> What is the complete constrained subgame-perfect equilibrium correspondence of the published Shy–Stenbacka game once outsourcing bounds and product-market corner continuations are respected, and which published comparative-static/strategic-substitutability conclusions survive?

Subquestions for later mathematical stages include:

1. the exact Cournot active-set partition under arbitrary feasible Stage-I histories;
2. the full constrained Cournot best-response correspondence;
3. existence and multiplicity of symmetric/asymmetric outsourcing equilibria;
4. the full Hotelling price-subgame correspondence across interior and corner market shares;
5. exact parameter regions under which the published Hotelling symmetric candidate survives;
6. corrected proposition statements with exact weak/strict inequalities.

These are residual questions, not Stage-1 assumptions.

## 9. Inputs for novelty search

Stage 2 must search for prior disclosure of each defect separately:

- correction/erratum/comment on Shy & Stenbacka (2005);
- papers citing or re-deriving equation (13) or Proposition 3;
- later outsourcing models noting a negative (N)-comparative static;
- later work imposing (ilephi) or otherwise correcting the source feasibility domain;
- citations/comments identifying the Cournot nonnegative-output continuation issue;
- citations/comments identifying the Hotelling interior-share continuation issue or a profitable corner deviation;
- working-paper/prepublication versions that may contain different formulas.

A search that finds no paper with the same correction title is insufficient. Stage 2 must inspect theorem/model content of close descendants and citing papers.

## 10. Verdict and next-stage contract

[
oxed{	extbf{GO TO NOVELTY GATE}}
]

Stage 1 freezes the source representation above.

Stage 2 may search and classify prior art. It **may not** alter the source model, introduce a monitoring-cost coefficient, add assumptions to rescue the paper, or silently replace the published equilibrium with a repaired one.

The complete corrected equilibrium correspondence remains a downstream mathematical task. Any future claim of global Nash/SPNE validity must fail closed unless every economically material Stage-I deviation has a valid Stage-II continuation.

## Reproducibility

Canonical verification script:

- `code/stage01_verify.py`

The script uses exact SymPy arithmetic and checks:

- equation-(14) sign identity;
- Corollary-4 interior derivative signs;
- the isolated Cournot outsourcing-cap witness;
- the Cournot active-set witness;
- the Hotelling outsourcing-cap witness;
- the Hotelling corner-deviation witness and its symbolic gain formula.
