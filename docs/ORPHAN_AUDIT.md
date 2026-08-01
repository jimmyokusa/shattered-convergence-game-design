# 🔍 The Orphan Audit: Design & Specification Gaps

> **GOVERNING AUDIT PURPOSE:**
> This document logs every specified asset, visual effect, sound effect, visual treatment, or audio property found across the repository's design documents — specifically each `VFX_SFX_SPEC.md` — that is either unallocated in the milestone sequence, implied but left unspecified, or sitting as an unpopulated cell due to silent source documentation.
> **Rule:** No assets were invented or resolved during this audit. Listed below are empirical design gaps for human developer review and decision.

---

## 1. Specified Assets Appearing in NO Milestone

The following assets are explicitly detailed in `VFX_SFX_SPEC.md` or `CHARACTER_DESIGN.md` but are **Level 3 Supers / Cinematic FX** that are explicitly banned from Milestone 0 (M0) through Milestone 5 (M5) by scope boundaries, and are delayed until Milestone 6 (M6 Content Complete):

| Character | Asset Name | Description in Design Spec | Scheduled Milestone | Notes / Status |
| :--- | :--- | :--- | :---: | :--- |
| **Zenthos** | *Scorched Earth Shatter* (Level 3 Super) | 2048x2048 magma crack decal atlas, screen shockwave, 9.5x HDR bloom, `#FF2D00`. | **M6** | Excluded from M0-M5 scope; P1 functional placeholder allocated in M6. |
| **Brutus** | *Cataclysmic Caldera* (Level 3 Super) | 2048x2048 lava chamber atlas + basalt fragment physics, 10.0x HDR bloom, `#FF1E00`. | **M6** | Excluded from M1-M5 scope. |
| **Ignacia** | *Infernal Cataclysm* (Level 3 Super) | Dense crimson napalm flame pillar atlas + ground fire, 9.2x HDR bloom, `#FF0A1E`. | **M6** | Excluded from M2-M5 scope. |
| **Melancholia** | *Absolute Zero Execution* (Level 3 Super) | Massive 3D ice monolith meshes with blizzard vignette, 8.8x HDR bloom, `#00D2FF`. | **M6** | Excluded from M3-M5 scope. |
| **Lyra** | *Maelstrom Tempest* (Level 3 Super) | Fullscreen vertical lightning column atlas + lens flare, 9.5x HDR bloom, `#8CC8FF`. | **M6** | Excluded from M3-M5 scope. |
| **Nereus** | *Abyssal Deluge* (Level 3 Super) | Fullscreen tidal wave mesh + glowing sea-foam overlay, 7.5x HDR bloom, `#00F0FF`. | **M6** | Excluded from M3-M5 scope. |
| **Sylas** | *Primal Convergence* (Level 3 Super) | Ethereal direwolf aura projection + frost shockwave atlas, 7.8x HDR bloom, `#28F0C8`. | **M6** | Excluded from M5 scope. |
| **Vesper** | *Eclipse Marionette* (Level 3 Super) | Colossal shadow puppet projection + void guillotine blade, 8.8x HDR bloom, `#D21EFF`. | **M6** | Excluded from M5 scope. |

---

## 2. Asset Classes Implied by Design Docs but NEVER Specified

The design documentation describes mechanics and world lore that imply necessary asset classes, but fails to provide explicit asset lists or technical parameters for them:

| Area / Subject | Implied Asset Class | Source Document | Missing Specification Details |
| :--- | :--- | :--- | :--- |
| **Stages 2 & 3** | Stage Geometry & Audio | `BUILD_TIERS.md` / `VERTICAL_SLICE.md` | *Glacial Spire* (Stage 2) and *Void Convergence Arena* (Stage 3) are referenced in build tiers, but have **zero 3D geometry specs, lighting parameters, or audio profiles** authored in the repository. |
| **Grey Health UI** | UI Health Bar Shader | `BUILD_TIERS.md` (Melancholia section) | Melancholia's *Thorn Rush* converts 10% HP to Grey Health, but there is no specification for the **Grey Health UI bar treatment** or recovery flash animation. |
| **Knockdown & Wakeup Foley** | Foley SFX | `ANIMATION_BUDGET.md` / `VERTICAL_SLICE.md` | Ground impact audio (body falling on ash/stone/ice) and wakeup rustle SFX are required for hit reactions but missing from `VFX_SFX_SPEC.md` across all 8 characters. |
| **Universal Throw Impact SFX** | Combat SFX | `VERTICAL_SLICE.md` (Section 3.1) | Universal throw connects require a distinct grab audio snap and ground slam SFX, but character `VFX_SFX_SPEC.md` files only define normal move hit impacts. |
| **Counter-Hit Visual Treatment** | Combat VFX | `MILESTONES.md` (Taxonomy Class 5) | System mechanics reference counter-hit freeze and counter-hit text overlay, but no font or particle specs exist for counter-hit callouts. |

---

## 3. Milestone Cells Left Unpopulated Due to Silent Source Documentation

During milestone matrix construction, the following character cells could not be populated with detailed move-specific parameters because the underlying character design documentation (`CHARACTER_DESIGN.md` / `VFX_SFX_SPEC.md`) is silent on specific animation clip names or precise SFX profiles:

1. **Locomotion Foley Audio Profiles (All 8 Characters):**
   - Source docs define attack hit/block SFX, but are silent on **footstep audio**, **dash burst whooshes**, and **jump takeoff/landing audio profiles** for distinct character weights (e.g., Brutus heavy stone footsteps vs. Lyra high-speed lightning dash).
2. **Hitstun Reaction Audio Variations (All 8 Characters):**
   - `VFX_SFX_SPEC.md` specifies a single `hit_impact` string per character, but does not provide separate audio strings or effort grunts for **Light Hitstun**, **Heavy Hitstun**, and **Air Launch Hitstun**.
3. **CPU AI Profile Parameters (`Metadata` Class 10):**
   - CPU opponent behavior definitions are required for Milestone 0 through Milestone 5, but zero AI behavior parameters (block probability, combo execution preference, reaction delay) exist in `CHARACTER_DESIGN.json` or `CHARACTER_DESIGN.md`.

---

## 🛠️ Summary Recommendation for Developer Action

- [ ] **Action Item 1:** Decide whether to author lightweight `VFX_SFX_SPEC.md` profiles for Stage 2 (*Glacial Spire*) and Stage 3 (*Void Convergence Arena*).
- [ ] **Action Item 2:** Add universal foley entries (footsteps, landing, knockdown ground impact, throw grab) to character audio templates.
- [ ] **Action Item 3:** Confirm whether Level 3 Super cinematically complex assets remain deferred to **Milestone 6 (Content Complete)** as planned.
