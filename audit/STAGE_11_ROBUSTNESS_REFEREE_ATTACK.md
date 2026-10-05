> **Independent-audit reopening notice (2026-09-20).** The historical `NO CERTIFICATION REGRESSION` finding was later falsified for the C7 quantifier/C8 proof record and multiplicity interpretation. The historical record is preserved; the controlling recertification is `audit/STAGE_11_RECERTIFICATION_2026-09-20.md` once closed.

# Stage 11 — Robustness / Referee Attack Gate

Status:

[
\boxed{\textbf{CANONICAL STAGE 11 — PASS}}
]

Date: 2026-09-20  
Workflow: `research-paper-workflow` v2.2  
Pinned workflow commit: `42574d6c5931275ccff3ef7e8b4acc188077332a`  
Stage-10 checkpoint: `753aa97669fa60269564d4fdd598e4ae7b63e081`  
Theory authority: Stage-8 freeze `2fbcf47ff18ea3650d307d90cbdeab78ddb63256`

## 1. Objective

Stage 11 attacks the completed manuscript as a hostile referee.  It is not a repetition of Stage 4A or Stage 7.5A: the target is the manuscript after exposition, literature framing, welfare language, figures/tables, and formal-verification wording have been added.

A Stage-11 mathematical failure that should have been caught earlier is a certification regression and must roll back to the earliest affected stage.  No such regression was found.

## 2. Attack classification

| Attack | Classification | Result |
|---|---|---|
| classic-result / relabeling | no defect | broad mechanism novelty already removed |
| known-model-in-disguise / theorem absorption | no defect | source-specific claims not directly absorbed |
| whole-game novelty | no defect | contribution remains correction/re-characterization |
| ad hoc assumptions / result built into assumptions | no defect | Cournot correction uses source primitives; no-loss game is explicit auxiliary model |
| alternative demand / monitoring / coverage | no defect in stated theorem | broader claims are expressly not made |
| participation / corner / boundary / regime switch | no defect | independent regressions survive |
| welfare mechanicality / selection | no defect | welfare is diagnostic and selection-dependent |
| institutional specificity | no defect | no empirical validation of exact functional form claimed |
| numerical-not-proof | no defect | numerical examples are regression witnesses, not proof substitutes |
| proof / notation / claim consistency | **MINOR, FIXED** | one overbroad literature sentence narrowed |
| theorem quantifier inflation | no defect after repair | Stage-7.5A scopes preserved |
| benchmark terminology drift | no defect | restricted benchmarks not called first best |
| formal-verification scope inflation | no defect | proof-critical-core limitation explicit |
| stale formal theorem / toolchain | no defect | certified blobs unchanged |
| journal-fit / contribution level | non-blocking editorial risk | compact correction-note positioning retained; Stage 12 selects venue |

No attack is classified **FATAL** or **MAJOR BUT FIXABLE** after the recorded prose repair.

## 3. Known-model-in-disguise attack

Canonical artifact:

- `audit/STAGE_11_KNOWN_MODEL_ATTACK.md`

The hostile reductions include:

1. downstream Cournot as a strictly concave exact-potential/KKT problem;
2. Stage-I sourcing as a concave continuous-action game;
3. strategic-substitutes / strategic-complements reductions;
4. potential-game structure within smooth active-set cells;
5. symmetry-breaking parent theorems;
6. cost-reducing R&D / investment / exit models;
7. outsourcing comparative-static prior work;
8. heterogeneous-cost Hotelling / no-loss pricing.

The downstream potential directly absorbs C1 as a standard component.  Existing investment and outsourcing literatures absorb generic narratives of negative competition effects, asymmetry, exit, multiplicity, and piecewise responses.

They do not yield the source-specific exact C7/C8 branch thresholds and complete **pure Stage-I source-duopoly** correspondence as a direct corollary under the same hypotheses.

The manuscript therefore survives only at the already-frozen novelty level:

[
\boxed{
\text{source-specific correction / global re-characterization}
}
]

No novelty regression to Stage 6 is triggered.

## 4. Independent primitive-level Cournot attack

A new independent verifier was created:

- `code/stage11_hostile_referee_verify.py`

It does not import the Stage-4 production verifier.

For the exact regression it uses source-feasible primitives

[
\phi=2,quad H=1,quad \gamma=1/2,quad
C_0=3,quad D=1,quad a=4,quad b=3/5.
]

Thus

[
\rho=\frac35>\frac49
]

satisfies the source SOC.

The verifier reconstructs nonnegative Cournot quantities directly from primitives and attacks the rival-exit best response.

Against (y=0), the exit boundary is (x=1).  The exact one-sided derivative signs are positive from the both-active side and negative from the monopoly side, making the kink the global maximizer under branch concavity.

Against

[
y=\frac1{20},
]

the exit-inducing optimum shifts to

[
x=\frac{11}{10},
]

and the exact direct payoff is

[
\Pi_A\left(\frac{11}{10};\frac1{20}\right)
=
\frac{251}{400},
]

strictly above the payoff from (x=1).

This independently reproduces the positive-slope global-BR logic from primitive downstream payoffs rather than reusing equation ((R)).

**Result: PASS.**

## 5. C8 boundary and alternative-equilibrium attacks

The independent verifier attacks the high-risk boundaries:

- (ho=2/3): mutual response satisfies (x+y=\delta) when the cap permits;
- (phi=s): equality belongs to the unique capped-symmetric regime;
- (ho=1/2): the internal response partition joins continuously;
- exact three-equilibrium regression ((3/5,1,2));
- asymmetric source-feasible continuation histories.

The prior independent grid/branch reconstruction also reproduced the asymmetric pair on both sides of (ho=1/2), including cap-boundary cases.

No omitted pure fixed point or contradiction with the frozen C8 partition was found.

**Result: PASS.**

## 6. Literal Hotelling continuation attack

The Stage-11 verifier independently chooses

[
\tau=1,qquad c_A=0,qquad c_B=4,
]

so (d=4>3\tau).

For

[
z\in[3,4],
qquad
p_B=z,quad p_A=z-1,
]

the low-cost firm optimally prices at the full-market boundary, while every positive-demand deviation by the high-cost firm requires a price below its marginal cost and cannot improve on zero operating profit.

The low-cost continuation profit varies with (z), confirming that the high-cost firm's payoff indifference is strategically material upstream.

The equality case (|d|=3\tau) collapses the interval to the unique boundary point.

**Result: PASS.**

## 7. Auxiliary no-loss attack

The exact source-admissible regression remains:

[
H=n=1,qquad \tau=1/15,qquad \phi=1.
]

The Stage-11 verifier reconstructs the piecewise no-loss payoff independently and obtains

[
V^{NL}_{1/6}(1/6)=\frac1{180},
qquad
V^{NL}_{1/6}(1/2)=\frac1{60},
]

hence

[
\Delta\Pi=\frac1{90}.
]

It also attacks the exact tie boundary with

[
\tau=\frac5{72},
qquad
x_-=\frac5{12},
]

for which the global-deviation gain is exactly zero while

[
\frac{27}{2}\tau<1<18\tau.
]

Thus the manuscript's strict (phi>x_-) failure condition and equality-as-tie wording survive.

**Result: PASS.**

## 8. Function-class / alternative-structure attack

The manuscript does not claim arbitrary-demand, arbitrary-monitoring, incomplete-coverage, or mixed-strategy robustness.

The Stage-11 verifier repeats the decisive convex-monitoring kill test:

[
\delta=1,qquad \rho=3/5,qquad y=0,
]

but monitoring cost

[
M(x)=10x^2.
]

The rival-exit boundary remains (x=1), while

[
\Pi_A(0;0)=\frac5{27}
>
-\frac{25}{3}
=
\Pi_A(1;0).
]

Therefore the exit geometry does not generically imply an increasing global best-response segment.

The manuscript already states C7/C8 as source-functional-form results.

**Result: PASS; no generality rollback.**

## 9. Welfare attack

The exact welfare regression is independently reproduced:

[
W\left(\frac{10}{17},\frac{10}{17}\right)
=
\frac{20}{17}
<
\frac32
=
W(1,0)
=
W(0,1).
]

This confirms that multiplicity is welfare-material.

The manuscript does not infer a selection-free welfare ranking and does not call the restricted Cournot common-sourcing benchmark or fixed-allocation Hotelling benchmark first best.

**Result: PASS.**

## 10. Exposition / claim-inflation finding

Stage 11 found one manuscript sentence in the Related Literature section:

> “complete pure-strategy re-characterization of a specific published model”

That wording could be read as claiming pure-strategy completeness for the entire Shy--Stenbacka model, whereas completeness is certified only for the source-duopoly Cournot **pure Stage-I** correspondence.

Classification:

[
\boxed{\textbf{MINOR — PROSE-ONLY SCOPE INFLATION}}
]

It was repaired to:

> “a complete pure Stage-I re-characterization of its Cournot source-duopoly case.”

Repair commit:

`33b235d1a0ae003359f4e5a4293b8b7ad6801f60`.

The repair narrows prose to the Stage-8 freeze and changes no theorem, model, or proof.  No rollback is required.

## 11. Scope / citation lint

The Stage-11 CI verifier checks for prohibited claim patterns and required scope qualifiers.

It also parses all manuscript `\cite{...}` keys and verifies that every cited key exists in `paper/references.bib`.

The initial Stage-11 CI attempt failed because a naive lint pattern matched the manuscript's protective sentence

> “does not imply that outsourcing is globally a strategic complement.”

This was a verifier false positive, not a mathematical or manuscript defect.  The lint was repaired to require the protective wording rather than ban its substring.

The failed run is retained as audit provenance.

Final scope/citation lint: **PASS**.

## 12. Formal-verification scope attack

The manuscript says that selected algebraic statements are formalized in Lean and explicitly adds that the complete economic game and global equilibrium construction are not formally mechanized.

The current branch retains exactly the certified Stage-7.5A formal blobs:

- `ShyStenbackaFormal/Stage075A.lean`:
  `a634b04eb2ec13a632f10928974f8eab96d1d05c`
- `ShyStenbackaFormal.lean`:
  `e4a44acff03704dbf427b792d9528cf9a0a3c602`
- `lakefile.toml`:
  `6669c6b90caf3c05912556109ead89c33400fe6c`
- `lean-toolchain`:
  `7aca1d8a939cc24c413eddd793671cdce7070b74`
- Lean workflow:
  `886c142e65d35d746cb1803e266aa0d687f7514e`.

Therefore the controlling formal certificate remains the Stage-7.5A green run

`35439005968`.

No paper claim is upgraded from analytic certification to full formal mechanization.

**Result: PASS.**

## 13. Verification evidence

Final Stage-11 verification/code head:

`89d04eb048257db3f930cd34f96209d34d1e3bc7`.

At that head:

- Python verification push run `35451023487`: **success**;
- Python verification PR run `35451026809`: **success**.

The successful log reports:

- `Stage-11 hostile-referee regression PASS`;
- `Cournot finite-deviation / active-set attack: PASS`;
- `Literal Hotelling corner-selection attack: PASS`;
- `Welfare-selection regression: PASS`;
- `Manuscript scope and citation lint: PASS`.

The manuscript itself last changed at repair commit `33b235d1...`.  A later head containing that repair plus the Stage-11 Makefile integration,

`b24e686b0a7a757f2f63d090a214ae604d12c891`,

passed manuscript build run

`35450876387`.

Changes after that green manuscript head concern only the independent Stage-11 verifier and audit documentation, not manuscript content or the paper build target.

## 14. Certification-regression decision

No failure discovered at Stage 11 invalidates a Stage-4A theorem certificate, a Stage-6 novelty certificate, a Stage-7 welfare benchmark, a Stage-7.5A quantifier certificate, or the formal-verification certificate.

The one scope issue was a prose-only overstatement introduced at Stage 10 and was narrowed without changing mathematics.

Therefore:

[
\boxed{\textbf{NO CERTIFICATION REGRESSION}}
]

and no earlier canonical stage is reopened.

## 15. Final attack inventory

### FATAL

None.

### MAJOR BUT FIXABLE

None.

### MINOR

One resolved prose scope inflation in Related Literature.

Venue-specific contribution-level risk remains for Stage 12 journal positioning, but it is not a mathematical or scope defect.

## 16. Canonical verdict and route

All mandatory hostile-referee attacks have been executed.

No material blocker remains.

[
\boxed{\textbf{CANONICAL STAGE 11 — PASS}}
]

[
\boxed{\textbf{ROBUSTNESS / REFEREE ATTACK GATE CLOSED}}
]

Next route:

[
\boxed{\textbf{STAGE 12 — JOURNAL POSITIONING}}
]
