# Stage 4 Continuation / Solver Ledger

## Cournot

| History class | Method | Outcome | Multiplicity |
|---|---|---|---|
| arbitrary \(i\in[0,\phi]^N\) | sort costs; solve active-set KKT | \`SOLVED_EQUILIBRIUM\` | unique |
| all firms active | closed form | \`SOLVED_EQUILIBRIUM\` | unique |
| one or more zero-output firms | active-set formula | \`SOLVED_EQUILIBRIUM\` | unique |
| exact entry/exit threshold | threshold-cost firm has zero quantity | \`SOLVED_EQUILIBRIUM\` | unique quantities |

Unresolved Cournot continuations: **0**  
Numerical failures: **0**  
Continuation verdict: **PASS**

## Hotelling diagnostic

Let \(d_c=c_B-c_A\).

| Cost-gap class | Price continuation | Outcome | Multiplicity |
|---|---|---|---|
| \(|d_c|<3\tau\) | source interior formula | \`SOLVED_EQUILIBRIUM\` | unique |
| \(|d_c|=3\tau\) | zero-share boundary | \`SOLVED_EQUILIBRIUM\` | unique |
| \(d_c>3\tau\) | \(p_B=s,\ p_A=s-\tau,\ s\in[c_A+3\tau,c_B]\) | \`MULTIPLE_EQUILIBRIA\` | continuum |
| \(d_c<-3\tau\) | mirror image | \`MULTIPLE_EQUILIBRIA\` | continuum |

Unresolved Hotelling price subgames: **0**  
Numerical failures: **0**

The reduced Stage-I payoff is selection-dependent in the multiple-equilibrium regions.

Reduced-game verdict: **not single-valued without a source selection rule**.

## Fail-closed semantics

No invalid interior formula, negative quantity, out-of-range market share, NaN, solver failure, or absent branch is treated as evidence that a deviation is unprofitable.


## Hotelling undominated-price refinement

Deleting only prices (p_j<c_j), each of which is weakly dominated by (p_j=c_j), gives:

| Cost-gap class | Undominated-price continuation | Outcome | Multiplicity |
|---|---|---|---|
| (|d_c|<3\tau) | source interior formula | `SOLVED_EQUILIBRIUM` | unique |
| (|d_c|=3\tau) | zero-share boundary | `SOLVED_EQUILIBRIUM` | unique |
| (d_c>3\tau) | (p_B=c_B, p_A=c_B-\tau) | `SOLVED_EQUILIBRIUM` | unique |
| (d_c<-3\tau) | mirror image | `SOLVED_EQUILIBRIUM` | unique |

Unresolved refined price subgames: **0**  
Numerical failures: **0**

The refined Stage-I payoff is therefore single-valued. Exact symmetric survival/failure conditions are recorded in `audit/STAGE_04_HOTELLING_REAUDIT.md`.

Important: the literal-game multiplicity table above remains valid. The refined table does not rewrite the source strategy space; it reports a one-round weak-dominance refinement.
