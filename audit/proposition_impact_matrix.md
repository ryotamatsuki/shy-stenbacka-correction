# Proposition Impact Matrix

Status: **STAGE-4 CONSTRUCTION COMPLETE — STAGE 4A CERTIFICATION PENDING**

Stage 4 supersedes the earlier Stage-1 classifications where noted.

| Published result | Stage-4 classification | Corrected result / impact | Certificate |
|---|---|---|---|
| Proposition 3 | **INCORRECT** | Eq. (13) is the unconstrained symmetric stationary point, but the feasible symmetric SPNE is (i_C^*=min{phi,ar i_C}). Eq. (14) has the wrong sign: outsourcing is weakly decreasing in (N), strictly decreasing on the interior branch for (N>1). | C3, C4 |
| Corollary 4 | **QUALIFY** | The outsourced **fraction** is weakly increasing in (a) and weakly decreasing in (gamma) and (phi); all are strict on the interior branch. Binding (i=phi) creates flat fraction effects. The outsourced **number** rises one-for-one with (phi) on the cap branch, so a global strict-number claim would be false. | C5 |
| Proposition 5 | **CORRECT LOCALLY, FALSE GLOBALLY ON PART OF SOURCE DOMAIN** | Eq. (15) is the both-active branch and has negative slope. But for (4/9<b/H^2<2/3), the global duopoly BR contains a rival-exit branch with slope (+2). Asymmetric equilibria arise; at (b/H^2=2/3) a continuum can arise. | C6–C8 |
| Proposition 6 | **STAGE-1 “GLOBALLY FALSE” CLASSIFICATION SUPERSEDED** | Eq. (19) is unique only for (|c_B-c_A|le3	au). For larger cost gaps the source price game has a continuum of pure equilibria with different low-cost continuation profits. The source provides no selection rule. Eq. (25) also omits (ilephi). The earlier single corner-deviation rejection is selection-dependent, not selection-free. | H1, H2 |

## Proposition 3 replacement

Let

[
D=a-Hphi-rac{gammaphi^2}{2}>0,
qquad
ar i_C=
rac{HND}{b(N+1)^2-H^2N}.
]

Under the source condition

[
b>left(rac{HN}{N+1}ight)^2,
]

the corrected symmetric Cournot SPNE outsourcing level is

[
oxed{i_C^*=min{phi,ar i_C}}.
]

On the interior branch,

[
rac{partial ar i_C}{partial N}
=
-rac{HDb(N^2-1)}
{left[b(N+1)^2-H^2Night]^2}<0
qquad(N>1).
]

Hence (i_C^*) is weakly decreasing in (N), with strict decrease whenever the cap does not bind.

## Proposition 5 replacement logic

For source duopoly define

[
delta=rac DH,
qquad
ho=rac b{H^2}>rac49.
]

The complete global BR is piecewise affine after exact Cournot continuation.

- On the regular both-active branch its slope is
  [
  -rac{2}{9ho-4}<0.
  ]
- For (4/9<ho<2/3), another optimal branch is the rival-exit threshold
  [
  R(y)=delta+2y,
  ]
  with slope (+2).

Therefore the source condition (8) is insufficient for a global strategic-substitutes theorem.

## Proposition 6 audit correction

For the source full-coverage Hotelling price game:

- (|c_B-c_A|<3	au): unique interior equilibrium;
- (|c_B-c_A|=3	au): unique zero-share boundary equilibrium;
- (|c_B-c_A|>3	au): continuum of corner price equilibria.

The low-cost continuation profit varies across that continuum. No no-below-cost restriction or refinement is stated in the source.

Therefore:

1. the Stage-1 profitable corner deviation is a valid **selection-sensitivity** witness;
2. it is not a selection-free proof that the published symmetric outsourcing candidate cannot be embedded in any SPNE;
3. Hotelling is retained as an audit finding but is not part of the Stage-4A canonical Cournot correction architecture.

## Scope discipline

- C3 uniqueness is uniqueness of the **symmetric** general-(N) equilibrium, not uniqueness of every asymmetric SPNE.
- C8 gives the complete pure Stage-I correspondence only for the source **duopoly**.
- All Stage-4 certificates remain construction-level until Stage 4A independently attacks them.
