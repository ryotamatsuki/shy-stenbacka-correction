import Mathlib

namespace ShyStenbackaFormal

noncomputable section

/-!
Targeted formalization for the Stage 7.5A proof-critical core.

Scope:
* exact discrete Cournot comparative-static identity/sign;
* exact Cournot-duopoly branch-join identities;
* abstract below-cost/no-loss dominance facts;
* exact Hotelling global-deviation gain identity and source-admissible regression.

This file does not formalize the full economic game, the complete equilibrium
correspondence, mixed equilibria, or the derivation of the economic primitives.
-/

-- C4: corrected Cournot symmetric interior action.
def cournotInterior (H D b N : ℝ) : ℝ :=
  H * N * D / (b * (N + 1)^2 - H^2 * N)

theorem C4_cross_identity
    (H D b N : ℝ) :
    H * (N + 1) * D * (b * (N + 1)^2 - H^2 * N)
      -
    H * N * D * (b * (N + 2)^2 - H^2 * (N + 1))
      =
    -(D * H * b * (N^2 + N - 1)) := by
  ring

theorem C4_step_negative
    (H D b N : ℝ)
    (hH : 0 < H) (hD : 0 < D) (hb : 0 < b)
    (hN : 1 ≤ N)
    (hd0 : 0 < b * (N + 1)^2 - H^2 * N)
    (hd1 : 0 < b * (N + 2)^2 - H^2 * (N + 1)) :
    cournotInterior H D b (N + 1) < cournotInterior H D b N := by
  unfold cournotInterior
  rw [div_lt_div_iff₀ hd1 hd0]
  have hp : 0 < N^2 + N - 1 := by
    nlinarith [sq_nonneg N]
  have hn : 0 < D * H * b * (N^2 + N - 1) := by
    exact mul_pos (mul_pos (mul_pos hD hH) hb) hp
  have hcross := C4_cross_identity H D b N
  nlinarith

-- C6/C7: exact join identities in the normalized source-duopoly BR.
def exitBR (δ y : ℝ) : ℝ := δ + 2 * y
def activeBR (δ ρ y : ℝ) : ℝ := 2 * (δ - y) / (9 * ρ - 4)
def monopolyBR (δ ρ : ℝ) : ℝ := δ / (4 * ρ - 1)
def yA (δ ρ : ℝ) : ℝ := δ * (2 - 3 * ρ) / (2 * (3 * ρ - 1))
def yM (δ ρ : ℝ) : ℝ := δ * (1 - 2 * ρ) / (4 * ρ - 1)

theorem C7_active_exit_join
    (δ ρ : ℝ)
    (hA : 3 * ρ - 1 ≠ 0)
    (hB : 9 * ρ - 4 ≠ 0) :
    activeBR δ ρ (yA δ ρ) = exitBR δ (yA δ ρ) := by
  unfold activeBR exitBR yA
  field_simp [hA, hB]
  ring

theorem C7_monopoly_exit_join
    (δ ρ : ℝ)
    (h : 4 * ρ - 1 ≠ 0) :
    monopolyBR δ ρ = exitBR δ (yM δ ρ) := by
  unfold monopolyBR exitBR yM
  field_simp [h]
  ring

theorem C7_exit_branch_slope_positive :
    (2 : ℝ) > 0 := by norm_num

-- H2/H2b: abstract operating-profit dominance facts.
theorem H2_below_cost_profit_nonpos
    (p c demand : ℝ)
    (hp : p < c)
    (hd : 0 ≤ demand) :
    (p - c) * demand ≤ 0 := by
  exact mul_nonpos_of_nonpos_of_nonneg (le_of_lt (sub_neg.mpr hp)) hd

theorem H2_marginal_cost_profit_zero
    (c demand : ℝ) :
    (c - c) * demand = 0 := by ring

theorem H2b_above_cost_profit_nonneg
    (c ε demand : ℝ)
    (hε : 0 < ε)
    (hd : 0 ≤ demand) :
    ((c + ε) - c) * demand ≥ 0 := by
  have : 0 ≤ ε := le_of_lt hε
  nlinarith [mul_nonneg this hd]

theorem H2b_above_cost_profit_strict
    (c ε demand : ℝ)
    (hε : 0 < ε)
    (hd : 0 < demand) :
    ((c + ε) - c) * demand > 0 := by
  have hmul : 0 < ε * demand := mul_pos hε hd
  nlinarith

-- H5/H6-NL: exact no-loss Hotelling deviation gain.
def hotellingGain (H n τ x : ℝ) : ℝ :=
  -(36 * x^2 - 36 * H * n * x + 5 * H^2 * n^2 + 54 * n * τ) / 36

theorem H5_vertex_gain_identity
    (H n τ : ℝ) :
    hotellingGain H n τ (H * n / 2)
      =
    n * (2 * H^2 * n - 27 * τ) / 18 := by
  unfold hotellingGain
  ring

theorem H5_vertex_gain_positive
    (H n τ : ℝ)
    (hn : 0 < n)
    (hcond : 27 * τ < 2 * H^2 * n) :
    0 < hotellingGain H n τ (H * n / 2) := by
  rw [H5_vertex_gain_identity]
  have hgap : 0 < 2 * H^2 * n - 27 * τ := by
    nlinarith
  exact div_pos (mul_pos hn hgap) (by norm_num)

theorem H6_exact_regression :
    hotellingGain 1 1 (1 / 15 : ℝ) (1 / 2 : ℝ) = 1 / 90 := by
  norm_num [hotellingGain]

-- Stage-7 exact welfare-selection regression values.
theorem W_three_eq_symmetric_value :
    (20 / 17 : ℝ) < 3 / 2 := by norm_num

#print axioms C4_cross_identity
#print axioms C4_step_negative
#print axioms C7_active_exit_join
#print axioms C7_monopoly_exit_join
#print axioms H2_below_cost_profit_nonpos
#print axioms H2b_above_cost_profit_nonneg
#print axioms H5_vertex_gain_identity
#print axioms H5_vertex_gain_positive
#print axioms H6_exact_regression

end

end ShyStenbackaFormal
