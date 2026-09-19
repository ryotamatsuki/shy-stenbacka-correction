# Stage 4 Continuation / Solver Ledger

## Cournot

| History class | Continuation method | Outcome status | Multiplicity | Notes |
|---|---|---|---|---|
| arbitrary (iin[0,phi]^N) | sort costs; solve active-set KKT | `SOLVED_EQUILIBRIUM` | unique | complete source domain |
| all firms active | closed form | `SOLVED_EQUILIBRIUM` | unique | recovers source regular branch |
| one or more zero-output firms | active-set formula | `SOLVED_EQUILIBRIUM` | unique | source Eq. (10) must not be extrapolated |
| exact entry/exit threshold | zero quantity for threshold-cost firm | `SOLVED_EQUILIBRIUM` | unique quantities | derivative kink handled explicitly |

Unresolved Cournot continuations: **0**  
Numerical failures: **0**  
Continuation verdict: **PASS**

## Hotelling diagnostic

Let (d_c=c_B-c_A).

| Cost-gap class | Price continuation | Outcome status | Multiplicity |
|---|---|---|---|
| (|d_c|<3	au) | source interior price formula | `SOLVED_EQUILIBRIUM` | unique |
| (|d_c|=3	au) | zero-share boundary | `SOLVED_EQUILIBRIUM` | unique |
| (d_c>3	au) | (p_B=s, p_A=s-	au, sin[c_A+3	au,c_B]) | `MULTIPLE_EQUILIBRIA` | continuum |
| (d_c<-3	au) | mirror image | `MULTIPLE_EQUILIBRIA` | continuum |

Unresolved price subgames: **0**  
Numerical failures: **0**

However, Stage-I continuation payoff is selection-dependent in the multiple-equilibrium regions.

Reduced-game verdict: **FAIL AS SINGLE-VALUED OBJECT WITHOUT A SOURCE SELECTION RULE**.

## Fail-closed semantics

No `None`, invalid interior formula, negative quantity, out-of-range market share, or solver failure is treated as evidence that a deviation is unprofitable.
