# Decision Log

## 2026-09-19 — Source-model fidelity repair

The canonical source audit uses (M(i_j)=i_j^2), not a generalized (eta i_j^2).

---

## 2026-09-19 — Canonical workflow routing

The project follows `research-paper-workflow` v2.2. Repository existence does not imply canonical Stage 9 PASS.

---

## 2026-09-19 — Stage-2 novelty narrowing

The project survives as a source-specific correction/global re-characterization. König (2010) kills any generic novelty claim that more Cournot competition can reduce outsourcing.

---

## 2026-09-19 — Stage-3 architecture selection

Candidate E (unified Cournot + Hotelling global correction) was selected for testing, with Candidate C (complete Cournot correction) pre-authorized as the sole fallback.

---

## 2026-09-19 — Stage-4 Hotelling selection finding

### Finding

For (|c_B-c_A|>3	au), the source Hotelling price subgame has a continuum of pure equilibria.

The low-cost firm's continuation profit differs across those equilibria.

### Consequence

The earlier Stage-1 claim that the displayed corner outsourcing deviation unconditionally destroys Proposition 6 is **superseded**.

The correct finding is equilibrium-selection dependence.

A no-below-cost or weak-dominance refinement could select the high-price corner continuation, but no such refinement is stated in the source and none is added.

### Architecture decision

Candidate E is rejected as the canonical minimal architecture.

---

## 2026-09-19 — Stage-4 Cournot fallback activation

### Finding

The Cournot fallback closes analytically.

Under the source SOC, own reduced payoff is globally strictly concave even across downstream active-set changes.

The corrected symmetric general-(N) equilibrium is

[
i_C^*
=
minleft{
phi,,
rac{HND}{b(N+1)^2-H^2N}
ight}.
]

The equation-(14) sign is negative on the interior branch.

For the source duopoly, the global best response is piecewise and contains a slope-(+2) rival-exit regime whenever (4/9<b/H^2<2/3). The source therefore admits asymmetric Stage-I equilibria; at (b/H^2=2/3) it admits a continuum.

### Decision

Activate **Candidate C — Complete Cournot correction**.

Stage-4 verdict:

[
oxed{	ext{GO TO STAGE 4A}}.
]


---

## 2026-09-19 — Stage-4 construction decision

Stage 4 closes with **GO** for Candidate C — Complete Cournot correction, routed to Stage 4A.

The unified Candidate E is rejected as the minimal canonical architecture because the source Hotelling price subgame has a continuum of valid off-path equilibria for sufficiently asymmetric costs. The Stage-1 Hotelling profitable-deviation result is therefore superseded as an unconditional rejection and retained instead as a continuation-selection diagnostic.

Cournot construction results now frozen for Stage 4A include: global continuation uniqueness, global own-payoff concavity, corrected capped symmetric action, reversed Proposition-3 sign, complete duopoly global BR, and the complete pure duopoly equilibrium correspondence.


---

## 2026-09-19 — Stage-4 Hotelling re-open and final amendment

### Trigger

The previous Stage-4 architecture dropped Hotelling because the literal corner price subgame is multiple when \(|c_B-c_A|>3\tau\).

A re-audit was required because the multiplicity relies on zero-demand high-cost firms choosing prices below marginal cost.

### Mathematical finding

For every \(p_j<c_j\),

\[
p_j=c_j
\]

weakly dominates \(p_j\) under the source Hotelling payoff.

The literal Nash continuum therefore remains a valid source-game diagnosis, but all corner equilibria except the marginal-cost endpoint use weakly dominated prices.

After one-round deletion of these below-cost prices:

- the corner continuation is unique;
- the refined Stage-I payoff is single-valued;
- the source symmetric candidate fails exactly when
  \[
  27\tau/2<H^2n<18\tau
  \]
  and
  \[
  \phi>
  Hn/2-\sqrt{2n(2H^2n-27\tau)}/6.
  \]

The Stage-1 example gives exact gain \(1/90\) under this refinement.

### Architecture decision

The prior Cournot-only routing is superseded.

\[
\boxed{\textbf{RESTORE Candidate E′}}
\]

Candidate E′ = complete Cournot correction + literal/refined Hotelling correction.

Stage-4 verdict remains **GO → Stage 4A**.

No trembling-hand/proper-equilibrium claim is made.


---

## 2026-09-19 — Stage-4A refinement kill test and Stage-4 amendment

The independent Stage-4A attack found that the earlier “undominated-price refinement” label was not defensible.

Although every \(p<c\) is weakly dominated by \(p=c\), the action \(p=c\) itself is weakly dominated by any fixed \(p=c+\varepsilon\). Therefore the corner equilibrium using \(p_{\rm high}=c_{\rm high}\) is not an undominated-strategy equilibrium and cannot be justified by symmetric elimination of all weakly dominated strategies.

The mathematics under the restricted strategy set \(p\ge c\) remains correct. Stage 4 is therefore amended, not abandoned:

- literal source game: corner multiplicity / incomplete backward induction;
- auxiliary no-loss game \(p\ge c\): unique pure corner continuation and exact Proposition-6 failure region;
- architecture: **HYBRID**, with Cournot as main theorem block and Hotelling as secondary source/robustness results.

This amendment is explicit and precedes Stage-4A recertification.


---

## 2026-09-19 — Stage-4A final certification

The amended Stage-4 HYBRID architecture was independently reconstructed and attacked.

### Independent result

- Cournot continuation uniqueness independently follows from a strictly concave exact potential with Hessian \(-b(I+\mathbf1\mathbf1^\top)\).
- Global Cournot own-payoff concavity survives active-set changes.
- The source-duopoly BR, Proposition-5 counterexample, asymmetric equilibria, and \(\rho=2/3\) continuum survive.
- Literal Hotelling corner multiplicity survives.
- The Stage-4A weak-dominance counterexample \(p=c\preceq c+\varepsilon\) is permanently retained.
- Under explicit \(p\ge c\), the pure Hotelling price continuation and exact Proposition-6 failure threshold survive.
- No material continuation remains unresolved.

### Verdict

\[
\boxed{\textbf{GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS}}
\]

Next stage:

\[
\boxed{\textbf{Stage 6 — Novelty Re-Kill}}
\]

Formalization is applicable; target map recorded for the later pre-freeze formal-verification gate.


---

## 2026-09-19 — Stage-6 novelty re-kill

### Parent-class attack

The Stage-4A results were stripped of outsourcing language and searched against standard parent classes.

Strong prior-art threats include:

- König (2010): negative competition–outsourcing effects in a close specification;
- Amir (2000): asymmetric R&D and endogenous exit in symmetric Cournot;
- Amir, Garcia & Knauff (2010): general symmetry-breaking classes;
- Amir, Halmenschlager & Jin (2011): R&D polarization / shake-outs;
- Buehler & Schmutzler (2008): investment asymmetry in successive oligopoly;
- Eckert, Klumpp & Su (2017): multiple asymmetric investment equilibria before Cournot;
- Lamantia, Pezzino & Tramontana (2018): discontinuous/piecewise innovation BRs and multiple equilibria;
- heterogeneous-cost spatial pricing and no-loss-price literature.

### Killed novelty narratives

The project may not claim novelty for generic negative competition effects, endogenous asymmetry, rival exit, piecewise-BR multiplicity, or no-loss Hotelling pricing.

### Surviving novelty

No located parent theorem directly absorbs the exact source correction package.

The key Cournot distinction is that the certified source reduced payoff is globally strictly concave in own sourcing under the paper's SOC, yet the downstream active-set kink makes the global outsourcing BR non-monotone and can produce coexistence of the symmetric equilibrium with an asymmetric pair.

The contribution remains a **new source-specific correction/result in a known model**, not a new general game-theory mechanism.

### Verdict

\[
\boxed{\textbf{STAGE 6 — GO}}
\]

Route:

\[
\boxed{\textbf{Stage 7 — Welfare / Generality / Institutional Validation}}
\]


---

## 2026-09-19 — Stage-7 welfare, generality, and institutional validation

### Welfare

Exact Cournot and Hotelling welfare identities were derived.

The unrestricted planner problems were written explicitly. Restricted sourcing benchmarks are labeled as restricted-instrument or fixed-allocation benchmarks and are not called first best.

The corrected Cournot duopoly is welfare-selection dependent. At the exact three-equilibrium regression

\[
(\rho,\delta,\phi)=(3/5,1,2),
\]

the symmetric equilibrium has welfare \(20/17\), while each asymmetric equilibrium has welfare \(3/2\).

At \(\rho=2/3\), welfare varies across the certified equilibrium continuum.

Therefore no selection-free global welfare claim is authorized.

### Generality

The exact sign, threshold, best-response, and equilibrium-correspondence results remain baseline functional-form results.

A wider decreasing-cost class supports the direction of the rival-exit threshold, but no general equilibrium theorem is promoted.

### Institutional validation

Empirical evidence supports production fragmentation and active monitoring/auditing of outsourced manufacturers. It does not validate the exact quadratic/output-independent monitoring technology.

### Exposition decision

Welfare remains appendix/prose material. Main text remains focused on S1–S3, with S4–S5 secondary.

### Verdict

\[
\boxed{\textbf{STAGE 7 — GO TO STAGE 7.5}}
\]


---

## 2026-09-19 — Stage-7.5 full-theory freeze decision

### Value assessment

The project is not a new general theory of outsourcing, and Stage 6 has already killed that positioning.

It nevertheless merits full-paper investment because the exact published model requires more than an algebraic corrigendum:

- Proposition 3 reverses sign;
- the all-active downstream formula is not globally valid;
- Proposition 5 fails globally;
- the source duopoly pure equilibrium set is qualitatively different from the published interpretation;
- the Hotelling section has a separate off-path continuation defect.

### Mechanism

Outsourcing lowers marginal cost. When a sourcing difference becomes large enough to change downstream participation, the continuation regime changes. That active-set switch changes the global sourcing best-response geometry and can generate equilibrium multiplicity/asymmetry even though own reduced sourcing payoff is globally strictly concave.

### Scope

The exact theorems remain source-model / baseline-functional-form results.

The manuscript should be a compact correction paper / theory note, not an extension-heavy general-theory paper.

### Verdict

\[
\boxed{\textbf{STAGE 7.5 — GO}}
\]

Route:

\[
\boxed{\textbf{Stage 7.5A — Generality / Quantifier Red-Team}}
\]


---

## 2026-09-19 — Stage-7.5A generality / quantifier certification

### Quantifier result

The headline correction package survives independent scope attack after explicit narrowing.

Permanent wording controls:

- general-\(N\) Stage I: unique **symmetric pure action**, not unique equilibrium;
- source duopoly: complete **pure Stage-I** correspondence;
- Hotelling: pure-price equilibrium scope;
- \(N\)-comparative static: admissible integer market sizes satisfying source restrictions;
- no-loss Hotelling: auxiliary \(p\ge c\) game only;
- welfare: selection-dependent in Cournot multiplicity regions.

### Generality kill test

Replacing source monitoring \(x^2\) by the still-convex \(10x^2\) preserves the rival-exit boundary at the exact regression but makes the exit-inducing action strictly worse than no investment.

Thus the active-set intuition has broader interpretive value, but the positive-slope global BR and equilibrium multiplicity remain baseline functional-form theorems.

### Formal verification

Targeted Lean 4 formalization passed.

- Lean 4.19.0;
- mathlib pinned to \`c44e0c8ee63ca166450922a373c7409c5d26b00b\`;
- green run \`35439005968\`;
- no proof placeholders;
- no project-specific axiom;
- no \`sorryAx\` in certified theorem axiom output.

### Verdict

\[
\boxed{\textbf{STAGE 7.5A — PASS}}
\]

Route:

\[
\boxed{\textbf{Stage 8 — Canonical Theory Freeze}}
\]


---

## 2026-09-19 — Stage-8 canonical theory freeze

### Entry gate

All pre-freeze requirements are green:

- Stage 4A: **GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS**;
- Stage 7.5A: **GO — GENERALITY / QUANTIFIER CERTIFICATION PASS**;
- Formal Verification Gate: **FORMAL VERIFICATION PASS**.

### Freeze

The canonical model, exact theorem quantifiers, solution concepts, source-duopoly pure equilibrium correspondence, literal and no-loss Hotelling scopes, welfare benchmark labels, novelty boundary, baseline-only generality boundary, formal-verification provenance, explicit non-claims, and rollback rules are frozen in:

`audit/STAGE_08_CANONICAL_THEORY_FREEZE.md`.

No new extension or theorem widening was introduced at Stage 8.

### Verdict

\[
\boxed{\textbf{CANONICAL STAGE 8 — PASS}}
\]

\[
\boxed{\textbf{THEORY FROZEN}}
\]

Route:

\[
\boxed{\textbf{Stage 9 — Repository / Reproducibility Setup}}
\]


---

## 2026-09-19 — Stage-9 repository / reproducibility setup

### Repository hardening

The existing repository was not treated as an automatic Stage-9 PASS. After the Stage-8 theory freeze it was explicitly converted into a production/reproducibility layout.

Stage 9 added:

- pinned Python runtime and dependency path;
- repository-level `Makefile` verification/build targets;
- complete Python verification CI;
- clean-environment manuscript smoke-build CI;
- modular `paper/sections/` structure;
- `REPRODUCIBILITY.md`;
- theorem-certificate and formal-source indexes;
- permanent counterexample/regression register;
- content-addressed artifact manifest.

### Green evidence

- Python verification: run `35442666402` — **success**;
- Lean formal verification: run `35439005968` — **success**;
- manuscript smoke build: run `35442682700` — **success**.

The Stage-7.5A Lean source/toolchain blobs were unchanged. The Stage-9 manuscript restructuring added no substantive theory.

### Verdict

\[
\boxed{\textbf{CANONICAL STAGE 9 — PASS}}
\]

Route:

\[
\boxed{\textbf{Stage 10 — Section-by-Section Paper Construction}}
\]


---

## 2026-09-19 — Stage-10 manuscript construction

### Construction

The Stage-8 frozen theory was implemented section by section after Stage-9 reproducibility setup.

The manuscript now includes:

- exact source model and strategy domains;
- global nonnegative-quantity Cournot continuation;
- global own-payoff concavity;
- corrected Proposition-3 comparative static;
- complete source-duopoly pure global best response;
- complete pure Stage-I equilibrium correspondence;
- literal Hotelling pure-price continuation;
- explicit auxiliary no-loss Hotelling robustness theorem;
- welfare-selection and benchmark-scope discussion;
- robustness/generality and institutional limits;
- literature/theorem-absorption positioning;
- technical proof appendix.

### Exposition architecture

The Figure/Table Architecture Gate passed.

- Figure 1 is generated from the exact ((\rho,\delta,\phi)=(3/5,1,2)) regression and displays the positive-slope rival-exit branch and three exact pure equilibria.
- Table 1 reports the five certified pure source-duopoly equilibrium regimes.
- welfare and Hotelling threshold results remain equations/prose rather than unnecessary graphics.

### Verification

At substantive head `80f4523222e3f473786f3800ca8be0928de78fe2`:

- Python verification run `35444042815` — **success**;
- manuscript smoke-build run `35444042793` — **success**.

No manuscript placeholder or Stage-9 skeletal marker remains.

### Freeze integrity

No Stage-8 rollback trigger was activated. In particular, there is no unique general-(N) SPNE claim, mixed-equilibrium completeness claim, global strategic-complements claim, generic convex-monitoring theorem, selection-free Cournot welfare claim, or full-model formal-verification claim.

### Verdict

\[
\boxed{\textbf{CANONICAL STAGE 10 — PASS}}
\]

Route:

\[
\boxed{\textbf{Stage 11 — Robustness / Referee Attack Gate}}
\]


---

## 2026-09-20 — Stage-11 robustness / hostile-referee gate

### Attack result

The completed Stage-10 manuscript was attacked independently for:

- known-model-in-disguise / theorem absorption;
- finite/global sourcing deviations and active-set switches;
- (ho=2/3), (ho=1/2), and (phi=s) boundaries;
- literal Hotelling corner-continuation multiplicity;
- the no-loss (1/90) deviation and (x_-) tie boundary;
- welfare selection;
- alternative monitoring curvature;
- theorem-quantifier and benchmark-language inflation;
- citation completeness;
- formal-verification scope inflation and stale formal blobs.

### Finding

No mathematical, novelty, welfare, or formal certificate was invalidated.

One **MINOR** exposition defect was found: Related Literature said “complete pure-strategy re-characterization of a specific published model,” which could overstate the certified completeness scope. It was narrowed to “complete pure Stage-I re-characterization of its Cournot source-duopoly case.”

The first new CI lint attempt also failed because it falsely matched a protective negative sentence about global strategic complementarity. This was a verifier bug, not a manuscript/theory failure, and was corrected.

### Independent verification

Stage-11 verifier:

`code/stage11_hostile_referee_verify.py`

Final verification head:

`89d04eb048257db3f930cd34f96209d34d1e3bc7`

Green runs:

- `35451023487` — Python verification push;
- `35451026809` — Python verification PR;
- `35450876387` — manuscript build containing the prose repair.

### Certification regression

[
\boxed{\textbf{NO CERTIFICATION REGRESSION}}
]

No earlier stage is reopened.

### Verdict

[
\boxed{\textbf{CANONICAL STAGE 11 — PASS}}
]

Route:

[
\boxed{\textbf{Stage 12 — Journal Positioning}}
]


---

## 2026-09-20 — Stage-12 journal positioning

### Current contribution level

The Stage-11-surviving paper is positioned as a compact source-specific industrial-organization correction / theory note. No new generic outsourcing, investment, symmetry-breaking, or spatial-pricing theorem is claimed.

### Live journal comparison

Current official scopes and recent publications were checked for Review of Industrial Organization, Canadian Journal of Economics, Journal of Industry, Competition and Trade, Bulletin of Economic Research, and Economics Bulletin.

The strongest fit is **Review of Industrial Organization** because:

- its scope is directly industrial organization;
- it explicitly accepts theory;
- it explicitly welcomes shorter notes and commentaries;
- its August 2026 issue contains compact formal IO papers and a current make-or-buy theory paper;
- the present 15-page manuscript fits the observed scale without needing a new mechanism.

Canadian Journal of Economics remains an optional stretch because it published the source paper, but its current general-interest scope explicitly screens against very narrow specialist papers.

### Primary target

[
\boxed{\textbf{Review of Industrial Organization}}
]

Default submission ladder:

[
\text{RIO}
\rightarrow
\text{JICT}
\rightarrow
\text{BER}
\rightarrow
\text{Economics Bulletin}.
]

### RIO submission baseline

A current public requirements ledger was created. Key requirements include:

- editable source files at every submission/revision;
- LaTeX permitted;
- no LaTeX subfolders;
- 150–250 word abstract;
- 4–6 keywords and JEL codes;
- Data Availability Statement;
- declarations for competing interests/funding as applicable;
- author-contribution information in the submission interface;
- disclosure of substantive LLM use;
- hybrid publishing, with no APC under subscription publishing.

Portal-only and author-specific facts remain explicitly UNVERIFIED for Stage 14.

### Verdict

[
\boxed{\textbf{PRIMARY JOURNAL SELECTED — GO TO INTEGRATION}}
]

Route:

[
\boxed{\textbf{Stage 13 — Full-Paper Integration for RIO}}
]


---

## 2026-09-20 — Stage-12 v2.3 candidate-universe re-audit

### Trigger

After the original Stage-12 closure, the reusable workflow was strengthened so that journal ranking must be preceded by a contribution-first candidate-universe construction and completeness audit.

Applying that rule exposed a genuine Stage-12 process defect: **International Journal of Industrial Organization** and other obvious/repeated IO venues had not all been explicitly evaluated before RIO was selected.

This is classified as:

\[
\boxed{\textbf{JOURNAL-POSITIONING COMPLETENESS REGRESSION}}
\]

It is not a Stage-6 novelty regression, Stage-8 theory regression, or Stage-11 certification regression.

### Repair

A new candidate-universe ledger was created:

`audit/STAGE_12_CANDIDATE_UNIVERSE_LEDGER.md`.

The expanded serious-candidate set explicitly evaluates IJIO, RIO, JIE, JEMS, CJE, JITE, Journal of Economics, JICT, BER, and Economics Bulletin, while RAND, JET, Economic Theory, JEBO, SEJ, and JEDC receive explicit exclusion reasons.

Key ranking changes relative to the old Stage 12:

- **IJIO** becomes the **best stretch**;
- **RIO** remains **primary** after direct comparison;
- **JITE** becomes realistic fallback 1;
- **Journal of Economics** becomes realistic fallback 2;
- **JICT** moves to fallback 3.

Default route:

\[
\text{RIO}
\rightarrow
\text{JITE}
\rightarrow
\text{Journal of Economics}
\rightarrow
\text{JICT}
\rightarrow
\text{BER}
\rightarrow
\text{Economics Bulletin}.
\]

Optional one-shot stretch:

\[
\text{IJIO}
\rightarrow
\text{RIO}
\rightarrow
\text{JITE}
\rightarrow\cdots
\]

### Verdict

\[
\boxed{\textbf{CANDIDATE-UNIVERSE COMPLETENESS AUDIT — PASS}}
\]

\[
\boxed{\textbf{JOURNAL-POSITIONING COMPLETENESS REGRESSION — REPAIRED}}
\]

\[
\boxed{\textbf{PRIMARY JOURNAL SELECTED — GO TO INTEGRATION}}
\]

Primary remains **Review of Industrial Organization**; best stretch is **International Journal of Industrial Organization**.

No theory, theorem scope, novelty boundary, welfare claim, equilibrium concept, or formal-verification certificate changed.

Route remains:

\[
\boxed{\textbf{Stage 13 — Full-Paper Integration for RIO}}
\]


---

## 2026-09-20 — Stage-13 full-paper integration for RIO

The Stage-12-selected primary route was integrated without changing the frozen economics.

### Manuscript integration

- abstract remains within RIO's 150--250 word public requirement;
- five keywords and JEL codes `L13; L23; L24` added;
- Dai (2026), *A New Strategic Element to the Make-or-Buy Decision*, added and explicitly distinguished from the source-specific correction;
- data/code availability and substantive LLM-use disclosures added;
- Table 1 caption now states its pure Stage-I scope explicitly;
- Stage-10 Figure 1 remains generated from the exact certified regression.

### Package integration

A flat RIO LaTeX package is now generated from the canonical modular manuscript by:

`code/stage13_build_rio_bundle.py`.

`make rio-bundle` regenerates the verified figure, creates `paper/rio_submission/` with no nested source directories, rewrites only path prefixes, and compiles the package.

### Verification

Substantive Stage-13 head:

`72c2f233199bea82e67de9b93987a64fe2dae804`

Green runs:

- `35473538351` — Python verification push;
- `35473541979` — Python verification PR;
- `35473538163` — canonical + flat RIO manuscript build.

The build confirms both layouts and a final 16-page PDF.

Two packaging/lint defects found during Stage 13 were repaired before closure. Neither affected the paper's mathematics or claim scope.

### Verdict

\[
\boxed{\textbf{INTEGRATED MANUSCRIPT READY FOR SUBMISSION QA}}
\]

No rollback is triggered.

Route:

\[
\boxed{\textbf{Stage 14 — Submission QA}}
\]
