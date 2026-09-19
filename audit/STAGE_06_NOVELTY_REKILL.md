# Stage 6 — Novelty Re-Kill

> **2026-09-20 independent-audit recheck.** The original Stage-6 verdict remains historical provenance. The all-active multiplicity example and C7 cap-feasibility repair were rechecked against the strongest parent-theorem comparisons. The current novelty boundary remains source-specific; the revised mechanism wording below supersedes any implication that downstream exit is necessary for multiplicity.

Status: **GO — GO TO WELFARE / GENERALITY**

Audit date: 2026-09-19  
Canonical workflow: \`research-paper-workflow\` v2.2  
Frozen mathematical input: Stage-4A checkpoint \`e90a7064162c12fc8aba4430388501ff6683af93\`

## 1. Executive re-kill verdict

The project survives Stage 6, but only as a **source-specific correction and global re-characterization of Shy–Stenbacka (2005)**.

The Stage-6 search kills several broader theoretical narratives that would overstate novelty:

- it is not new that more competition can reduce cost-reducing investment / outsourcing;
- it is not new that symmetric Cournot firms can develop asymmetric investment levels;
- it is not new that investment can induce rival exit;
- it is not new that piecewise/discontinuous best responses can generate multiple or asymmetric equilibria;
- it is not new that asymmetric-cost spatial price games require corner/refinement analysis;
- it is not new to impose a no-loss price restriction in a Hotelling-type pricing model.

What survives is narrower and more defensible:

1. the **published Shy–Stenbacka equation (14) / Proposition 3 has the wrong sign in its own source model**;
2. after enforcing the source's own outsourcing cap and globally valid nonnegative-output Cournot continuation, the source duopoly has a piecewise global outsourcing BR that **contradicts the paper's global Proposition-5 strategic-substitutes characterization**;
3. the exact source duopoly admits a fully characterized pure equilibrium correspondence, including coexistence of the symmetric equilibrium with an asymmetric pair and a knife-edge continuum;
4. these source-duopoly results arise **despite globally strictly concave own Stage-I sourcing payoffs under the paper's own SOC**, so they are not directly absorbed by the leading symmetry-breaking results based on payoff nonconcavity / increasing R&D returns / discrete lumpy innovation;
5. the literal Hotelling source game has unaccounted corner continuation multiplicity; under a separately labeled no-loss strategy restriction \(p_j\ge c_j\), the source symmetric sourcing formula fails on an exact cap-aware region. This is retained as a secondary robustness correction, not as a general Hotelling novelty claim.

Canonical verdict:

\[
\boxed{\textbf{GO}}
\]

Route:

\[
\boxed{\textbf{Stage 7 — Welfare / Generality / Institutional Validation}}
\]

---

## 2. Frozen result set entering the novelty re-kill

### Cournot

\[
i_C^*
=
\min\left\{
\phi,\,
\frac{HND}{b(N+1)^2-H^2N}
\right\}.
\]

For \(N>1\), on the interior branch,

\[
\frac{\partial i_C}{\partial N}
=
-\frac{HDb(N^2-1)}
{\left[b(N+1)^2-H^2N\right]^2}
<0.
\]

For source duopoly, with

\[
\delta=D/H,\qquad
\rho=b/H^2>\frac49,
\]

the exact **unconstrained** pure global BR contains a rival-exit branch

\[
U(y)=\delta+2y
\]

for (4/9<\rho<2/3).  After the source cap is imposed, a positive-length
piece survives only for sufficiently large caps; small-cap cases may erase it
entirely.

The complete pure Stage-I duopoly correspondence is:

- \(\rho>2/3\): unique symmetric equilibrium;
- \(\rho=2/3\): knife-edge continuum when the cap permits;
- \(4/9<\rho<2/3\): either a unique capped symmetric equilibrium or, when the cap is large enough, exactly one symmetric equilibrium plus one asymmetric pair.

### Hotelling

Literal source pure-price continuation is unique for \(|c_B-c_A|\le3\tau\) and multiple for larger cost gaps.

Under the auxiliary no-loss strategy restriction \(p_j\ge c_j\), the symmetric source candidate fails exactly when

\[
\frac{27}{2}\tau<H^2n<18\tau
\]

and

\[
\phi>
\frac{Hn}{2}
-
\frac{\sqrt{2n(2H^2n-27\tau)}}{6}.
\]

---

## 3. Proposition-by-proposition Stage-6 classification

| ID | Certified Stage-4A result | Stage-6 novelty status | Canonical treatment |
|---|---|---|---|
| C1 | unique nonnegative-output Cournot continuation | **DIRECTLY ABSORBED as standard Cournot/KKT/potential theory** | proof infrastructure only |
| C2 | global own sourcing payoff concavity across active-set changes | **TECHNICAL SOURCE-SPECIFIC LEMMA; not headline novelty** | retain because it distinguishes the parent class |
| C3 | capped symmetric Cournot action | **SOURCE-SPECIFIC CORRECTION / boundary qualification** | retain, secondary |
| C4 | equation-(14)/Proposition-3 sign reversal | **SURVIVES** | primary correction |
| C5 | cap-aware comparative statics | **SUPPORTING CORRECTION** | retain, not headline novelty |
| C6 | complete source-duopoly global BR | **SURVIVES AS SOURCE-SPECIFIC RE-CHARACTERIZATION** | primary theorem support |
| C7 | Proposition 5 false globally; positive-slope exit branch | **SURVIVES IN EXACT SOURCE MODEL** | primary correction |
| C8 | complete pure source-duopoly equilibrium correspondence | **SURVIVES IN EXACT SOURCE MODEL** | primary correction |
| H1 | literal Hotelling pure-price corner continuum | **GENERIC PRICE-GAME PHENOMENON NOT CLAIMED AS GENERAL NOVELTY; source omission survives** | secondary source correction |
| H2/H2b | dominance facts for below-/at-cost prices | **ELEMENTARY / KILL AS NOVELTY** | methodological clarification only |
| H3-NL | unique pure continuation under \(p\ge c\) | **ROBUSTNESS MACHINERY, NOT NOVELTY** | secondary |
| H4-NL | finite-candidate Stage-I BR | **TECHNICAL SUPPORT** | appendix-level |
| H5-NL | exact cap-aware failure region for Proposition 6 | **SURVIVES AS SOURCE-SPECIFIC CONDITIONAL CORRECTION** | secondary theorem |
| H6-NL | exact \(1/90\) counterexample | **EVIDENCE, NOT INDEPENDENT NOVELTY** | permanent regression |

---

## 4. Strongest prior-art threats

### 4.1 König (2010): generic negative competition effect

Jan König, *Outsourcing motives, competitiveness and taxation*, FU Berlin Discussion Paper 2010/33.

König explicitly adapts the Shy–Stenbacka framework and obtains a negative competition effect under a related marginal-cost-saving outsourcing specification.

**Absorption:**

- “more competition can reduce outsourcing” — **DIRECTLY/PARTIALLY ABSORBED as an economic proposition**;
- “Shy–Stenbacka (2005) equation (14) itself has the wrong sign” — **NOT ABSORBED**;
- source cap / active-set / complete source-duopoly correspondence — **NOT ABSORBED**.

König is therefore mandatory positioning, but not a kill of the correction.

### 4.2 Amir (2000): endogenous asymmetry and exit after cost-reducing R&D

Rabah Amir, “R&D Returns, Market Structure, and Research Joint Ventures,” *Journal of Institutional and Theoretical Economics* 156(4), 583–598.

A symmetric two-stage linear Cournot R&D game can have one firm fully innovate while the other does not, including endogenous exit.

**Absorption:**

- generic claim that symmetric primitives can produce asymmetric investment and exit — **ABSORBED**;
- exact Shy–Stenbacka continuous outsourcing BR and equilibrium thresholds — **NOT ABSORBED**.

The mechanism differs materially: Amir's polar outcomes are associated with the
return structure of R&D.  The corrected source game retains globally strictly
concave own sourcing payoffs and a symmetric equilibrium; moreover, its
multiplicity need not involve a downstream active-set change.

### 4.3 Amir, Garcia & Knauff (2010): general symmetry-breaking parent theorem

Rabah Amir, Filomena Garcia, and Malgorzata Knauff, “Symmetry-breaking in two-player games via strategic substitutes and diagonal nonconcavity: A synthesis,” *Journal of Economic Theory* 145(5), 1968–1986.

Their general classes deliver asymmetric pure equilibria from strategic substitutability together with payoff/diagonal nonconcavity. Their headline class has no symmetric pure equilibrium.

**Mapping attack:**

The source-duopoly sourcing game at Stage 4A instead satisfies:

- globally strictly concave own payoff under the source SOC;
- a symmetric pure equilibrium always remains in the certified correspondence;
- in the multiplicity region, the asymmetric pair coexists with that symmetric equilibrium;
- the all-active witness ((\rho,\delta,\phi)=(3/5,1,3/4)) has the same
  symmetric-plus-asymmetric multiplicity even though both downstream firms remain
  active throughout the feasible sourcing box.

Therefore the Stage-4A game fails the key nonconcavity/no-symmetric-equilibrium
architecture used by this strongest general parent theorem.  Exit remains
important for the positive-slope C7 branch, but the non-absorption of C8 does not
depend on exit being necessary for multiplicity.

**Verdict:** **NOT DIRECTLY ABSORBED**.

The paper must nevertheless cite this literature if it discusses endogenous asymmetry generally.

### 4.4 Amir, Halmenschlager & Jin (2011): industry polarization / shake-outs

“R&D-induced industry polarization and shake-outs,” *International Journal of Industrial Organization* 29(4), 386–398.

The model deliberately relaxes strong decreasing returns in R&D and obtains extreme/asymmetric R&D equilibria, sometimes with endogenous exit.

**Absorption:**

- generic asymmetric R&D / shake-out narrative — **ABSORBED**;
- source result under globally strictly concave own sourcing payoff — **NOT ABSORBED**.

This is an especially useful contrast because their asymmetry relies on a return structure different from the strong own-concavity certified here.

### 4.5 Buehler & Schmutzler (2008): investment asymmetry with vertical integration

“Intimidating competitors — Endogenous vertical integration and downstream investment in successive oligopoly,” *International Journal of Industrial Organization* 26(1), 247–265.

They combine cost-reducing investment with a discrete vertical-integration choice and obtain asymmetric integration/investment outcomes.

Their own discussion notes that without the asymmetric integration structure the firms choose identical investment levels.

**Verdict:** generic investment asymmetry is known; the Shy–Stenbacka source mechanism is **NOT ABSORBED**.

### 4.6 Eckert, Klumpp & Su (2017): multiple investment equilibria in Cournot competition

“An Equilibrium Selection Theory of Monopolization,” *Southern Economic Journal* 83(4), 1012–1037.

Their baseline has homogeneous-product Cournot competition and lumpy process investment. The first-stage action is binary in the baseline, and the authors also consider more than two discrete investment choices. Multiple asymmetric investment equilibria are central to their analysis.

They deliberately maintain downstream interior Cournot quantities in the baseline.

**Absorption:**

- multiple/asymmetric investment equilibria in a two-stage Cournot game — **ABSORBED**;
- a continuous sourcing action whose downstream nonnegativity constraint itself generates the nonmonotone global BR and exact Shy–Stenbacka thresholds — **NOT ABSORBED**.

### 4.7 Lamantia, Pezzino & Tramontana (2018): discontinuous BR and multiple innovation equilibria

“Dynamic analysis of discontinuous best response with innovation,” *Journal of Economic Dynamics and Control* 91, 120–133.

The paper studies fixed-cost innovation in a Cournot duopoly and explicitly characterizes multiple/static equilibria, including symmetric and asymmetric configurations, before adding dynamics.

**Absorption:**

- generic statement “innovation can generate piecewise/discontinuous best responses and multiple asymmetric equilibria” — **ABSORBED**;
- exact continuous outsourcing / rival-exit kink / source Proposition-5 correction — **NOT ABSORBED**.

### 4.8 Spatial-price literature

Jonathan Vogel (2008), *Journal of Political Economy*, and related heterogeneous-cost spatial competition work establish that asymmetric marginal costs and equilibrium refinements in spatial price competition are established topics.

Gill and Thanassoulis (2016) provide a concrete Hotelling-line example using prices weakly above marginal cost.

**Absorption:**

- generic asymmetric-cost Hotelling / no-loss-pricing theme — **ABSORBED**;
- the exact Shy–Stenbacka sourcing-induced cost-gap continuation defect and cap-aware Proposition-6 robustness threshold — **NOT LOCATED / source-specific**.

---

## 5. Application-neutral canonical-form search

The Stage-4A source-duopoly game can be stripped of outsourcing language and written as:

> Two ex ante identical players choose continuous cost-reduction actions from a compact interval. The downstream linear-Cournot game has nonnegative quantities. The induced upstream payoff is continuous, piecewise quadratic, and globally strictly concave in own action. Downstream active-set changes create kinks in the cross-strategic response. For a parameter region, the global upstream BR contains a positive-slope segment and the pure equilibrium set consists of one symmetric equilibrium and one asymmetric pair; at a knife edge there is a continuum.

Searches were run on:

- two-stage Cournot cost-reducing investment;
- endogenous exit / shake-out;
- asymmetric equilibrium with symmetric firms;
- strategic substitutes and symmetry breaking;
- piecewise / discontinuous best responses;
- global concavity and nonmonotone best responses;
- lumpy versus continuous innovation;
- equilibrium multiplicity in investment-then-Cournot games.

The closest families reproduce individual ingredients, but none located in this search gives a theorem that directly specializes to the entire canonical object above.

The key differentiator is **not** “piecewise BR” or “asymmetric equilibrium” separately. It is the exact coexistence structure generated by downstream active-set switching while own upstream payoffs remain globally strictly concave.

This remains a source-specific re-characterization, not a new general theorem about all such games.

---

## 6. Parent-theorem absorption map

| Prior theorem/model | Canonical mapping | Required transformation | Can Stage-4A headline result be derived directly? | Verdict |
|---|---|---|---|---|
| standard linear Cournot KKT / concave potential | Stage-II continuation | identify induced marginal costs | C1 yes; Stage-I results no | **C1 DIRECTLY ABSORBED** |
| König (2010) | continuum sourcing + Cournot | change outsourcing cost technology | generic negative competition sign yes; source Eq14 correction no | **PARTIAL** |
| Amir (2000) | cost reduction → Cournot | replace continuous convex sourcing cost with R&D return structure | generic asymmetry/exit yes; exact source correspondence no | **PARTIAL** |
| Amir–Garcia–Knauff (2010) | symmetric two-player upstream game | would require diagonal/payoff nonconcavity and no symmetric PSNE | no: certified source game is own-concave and retains symmetric equilibrium | **NOT ABSORBED** |
| Amir–Halmenschlager–Jin (2011) | R&D → Cournot → possible exit | replace strong own concavity by mildly decreasing R&D returns | generic polarization yes; exact source theorem no | **PARTIAL** |
| Buehler–Schmutzler (2008) | investment before Cournot | add discrete vertical structure | generic asymmetry yes; source active-set mechanism no | **PARTIAL** |
| Eckert–Klumpp–Su (2017) | investment before Cournot | replace continuous sourcing by lumpy/discrete investment; maintain interior downstream output baseline | generic multiple asymmetric investment equilibria yes | **PARTIAL** |
| Lamantia–Pezzino–Tramontana (2018) | innovation + Cournot + piecewise/discontinuous BR | fixed-cost innovation architecture | generic multiplicity/asymmetry yes | **PARTIAL** |
| heterogeneous-cost spatial price models | induced cost asymmetry → price competition | remove sourcing stage | generic H1 theme yes; H5-NL source threshold no | **PARTIAL** |
| Gill–Thanassoulis (2016) | Hotelling-line pricing with \(p\ge MC\) | different pricing environment | no-loss convention yes; Shy–Stenbacka threshold no | **PARTIAL** |

No \`DIRECTLY ABSORBED\` verdict applies to C4, C7, C8, or H5-NL.

---

## 7. Whole-game absorption verdict

### Cournot

No located single prior model or theorem reproduces all of:

1. the exact Shy–Stenbacka continuous sourcing primitive;
2. source SOC implying global own concavity;
3. downstream nonnegative-output active-set switching;
4. a positive-slope upstream BR segment caused by rival exit;
5. coexistence of the corrected symmetric equilibrium with an asymmetric pair;
6. the exact \(\rho=2/3\) continuum;
7. the equation-(14) sign reversal within the same source model.

Thus:

\[
\boxed{
\text{GENERIC INGREDIENTS ABSORBED;
SOURCE-SPECIFIC CORRECTION PACKAGE NOT ABSORBED}
}
\]

### Hotelling

Generic corner pricing, cost asymmetry, and no-loss restrictions are not novel.

The only surviving novelty unit is the **source-specific diagnosis and threshold**:

- the published interior sourcing calculation lacks a complete off-path price correspondence;
- under an explicitly auxiliary no-loss price strategy domain, the published sourcing candidate fails on the exact cap-aware region.

This should remain secondary.

---

## 8. Updated closest-paper matrix

| Paper | Closest overlap | What it kills | What it does not absorb |
|---|---|---|---|
| König (2010) | outsourcing + Cournot + competition comparative statics | generic negative competition–outsourcing claim | Eq14 correction in source model; global BR/equilibrium correspondence |
| Amir (2000) | symmetric cost-reducing R&D + Cournot + exit | generic endogenous asymmetry/exit | source convex-cost sourcing / global concavity / exact thresholds |
| Amir, Garcia & Knauff (2010) | general two-player symmetry breaking | generic “asymmetric equilibrium is surprising” rhetoric | source game because their core classes rely on nonconcavity and exclude symmetric PSNE |
| Amir, Halmenschlager & Jin (2011) | R&D + Cournot + polarization/exit | generic shake-out mechanism | source globally-concave upstream game |
| Buehler & Schmutzler (2008) | cost investment + Cournot + asymmetry | generic investment asymmetry | source continuous sourcing active-set mechanism |
| Eckert, Klumpp & Su (2017) | investment before Cournot + multiple asymmetric equilibria | generic multiple investment equilibria | continuous sourcing and active-set-generated BR geometry |
| Lamantia, Pezzino & Tramontana (2018) | discontinuous/piecewise BR + multiple equilibria | generic discontinuous-BR/multiplicity narrative | source continuous action / exact Proposition-5 correction |
| Vogel (2008) | heterogeneous marginal costs in spatial competition | broad asymmetric-cost spatial novelty | Shy–Stenbacka sourcing correction |
| Gill & Thanassoulis (2016) | Hotelling-line no-loss price domain | novelty of \(p\ge MC\) modeling convention | source-specific Proposition-6 threshold |

---

## 9. Killed claims

The manuscript must not claim novelty for:

- “competition can reduce outsourcing”;
- “cost-reducing investment may induce rival exit”;
- “symmetric firms may have asymmetric investment equilibria”;
- “piecewise/discontinuous best responses may yield multiple equilibria”;
- “strategic effects can switch sign across regimes” as a generic claim;
- “asymmetric marginal costs matter in Hotelling competition”;
- “prices may reasonably be restricted to be at least marginal cost”;
- “outsourcing decisions are strategic substitutes”;
- continuous/partial outsourcing as an idea.

These are either the source's own ingredients or established in adjacent theory.

---

## 10. Surviving claim set

### Primary

**S1 — source sign correction.**

Within Shy–Stenbacka's published Cournot model, equation (14) has the wrong sign and Proposition 3 reverses once equation (13) is differentiated correctly.

### Primary

**S2 — source global-strategy correction.**

The published Proposition-5 strategic-substitutes conclusion is branch-specific. Solving the source duopoly globally over the primitive sourcing box and valid downstream active sets produces a positive-slope rival-exit segment for an admissible parameter region.

### Primary

**S3 — exact pure equilibrium re-characterization.**

The source duopoly's complete pure Stage-I equilibrium correspondence contains parameter regions with the corrected symmetric equilibrium coexisting with an asymmetric pair, plus a knife-edge continuum.

The novelty is the exact correction of this source model, not the generic existence of asymmetric equilibria.

### Secondary

**S4 — Hotelling literal continuation correction.**

The published interior price calculation is not a complete off-path continuation characterization; the literal source price game becomes multiple for sufficiently asymmetric outsourcing-induced costs.

### Secondary / robustness

**S5 — no-loss Proposition-6 threshold.**

Under explicitly restricted prices \(p_j\ge c_j\), the source symmetric Hotelling outsourcing candidate fails on the exact cap-aware region H-NL3.

---

## 11. Revised contribution statement

Maximum defensible Stage-6 contribution statement:

> We revisit the exact Shy–Stenbacka (2005) model rather than introduce a new outsourcing mechanism. First, the published Cournot comparative static has the opposite sign from that reported. Second, respecting the primitive outsourcing bound and the nonnegative-output Cournot continuation changes the global strategic structure: the source duopoly's outsourcing best response is not everywhere decreasing, and its pure equilibrium correspondence can contain a symmetric equilibrium together with an asymmetric pair. These results occur under the paper's own concavity condition, which makes each firm's reduced sourcing payoff globally strictly concave. Finally, the Hotelling analysis is incomplete off path; as a robustness exercise, imposing an explicit no-loss price restriction yields an exact region in which the published symmetric sourcing candidate is defeated by a global deviation.

Prohibited contribution wording:

> We are the first to show that greater competition can reduce outsourcing.

Prohibited:

> We discover that symmetric Cournot investment games can have asymmetric equilibria.

Prohibited:

> We introduce a new symmetry-breaking mechanism.

Prohibited:

> Our Hotelling result establishes a novel general refinement of spatial price competition.

---

## 12. Strongest remaining novelty threat

The strongest remaining threat is not König alone.

It is the combined parent-class objection:

> “This is just another two-stage cost-reducing-investment Cournot model with endogenous asymmetry / exit, already covered by Amir and related symmetry-breaking literature.”

Stage 6 rejects that absorption only in the **source-specific** sense.

The defense is precise:

- generic asymmetry and exit are conceded as known;
- the leading general symmetry-breaking theorem located relies on payoff/diagonal nonconcavity and yields no symmetric PSNE;
- the certified Shy–Stenbacka reduced sourcing payoff is globally strictly concave in own action under the source SOC;
- the corrected source game retains the symmetric equilibrium and, in another region, adds an asymmetric pair through the downstream active-set kink.

This distinction must be preserved in Stage 7 and the eventual introduction.

If a later literature search finds a general theorem covering exactly this concave-own-payoff / active-set-kink / coexistence pattern and directly specializes to the source game, the novelty claim must be reopened at Stage 6.

---

## 13. Search limitations

- No search can prove absence of prior art.
- Some parent-class comparisons rely on abstracts plus available full-text working-paper versions.
- The strongest full-text parent candidate, Eckert–Klumpp–Su, was checked directly: its baseline uses binary/lumpy investment and assumes downstream quantities remain positive; its extensions use additional discrete investment choices.
- Current exact-title / proposition / correction searches still did not surface a published corrigendum or paper making the exact Shy–Stenbacka corrections recorded here.
- The Stage-6 verdict is therefore a scoped novelty judgment, not a universal priority claim.

---

## 14. Final verdict

At least one source-specific theorem/correction package survives theorem-level absorption.

\[
\boxed{\textbf{GO — GO TO WELFARE / GENERALITY}}
\]

Stage 7 may analyze only the surviving S1–S5 set. All killed generic novelty narratives remain dead.
