# Stage 4 Continuation / Solver Ledger

## Cournot

| History class | Method | Outcome | Multiplicity |
|---|---|---|---|
| arbitrary \(i\in[0,\phi]^N\) | sorted-cost active-set KKT | \`SOLVED_EQUILIBRIUM\` | unique pure continuation |
| all active | closed form | \`SOLVED_EQUILIBRIUM\` | unique |
| zero-output firms | active-set formula | \`SOLVED_EQUILIBRIUM\` | unique |
| exact entry/exit threshold | threshold-cost firm has zero quantity | \`SOLVED_EQUILIBRIUM\` | unique quantities |

Unresolved material Cournot continuations: **0**.

## Hotelling — literal source game

| Cost gap | Pure price continuation | Status |
|---|---|---|
| \(|d|<3\tau\) | source interior formula | unique |
| \(|d|=3\tau\) | zero-share boundary | unique |
| \(|d|>3\tau\) | exact corner continuum | multiple |

The literal Stage-I continuation payoff is selection-dependent off path.

## Hotelling — auxiliary no-loss game

Impose explicitly

\[
p_j\ge c_j.
\]

| Cost gap | Pure price continuation | Status |
|---|---|---|
| \(|d|<3\tau\) | source interior formula | unique |
| \(|d|=3\tau\) | boundary | unique |
| \(d>3\tau\) | \(p_B=c_B,\ p_A=c_B-\tau\) | unique pure |
| \(d<-3\tau\) | mirror | unique pure |

This is a conditional robustness game, not a source strategy-domain claim and not an all-weak-dominance refinement.

No mixed-equilibrium uniqueness claim is made.

## Fail-closed semantics

No invalid regular formula, negative quantity, out-of-range share, branch failure, NaN, or nonconvergence is treated as evidence against a deviation.
