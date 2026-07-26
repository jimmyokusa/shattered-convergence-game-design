# 👥 Development Roster & Subagent Roles

This document defines the specialized roles and subagent configurations for *The Shattered Convergence* production.

---

## Operational Focus: Solo-Developer Engineering & In-Engine Tuning

Because this is a solo-developer project, creative design roles (Game Designer, Concept Artist, Lore Writer) are **DEPRIORITIZED**. The sole production bottleneck is **In-Engine Assembly, Animation Sourcing, and UFE Configuration**.

---

## Subagent Definitions

### 1. `technical_producer` (Primary Lead)
* **Role:** Technical Producer & Pipeline Auditor.
* **Responsibilities:** Enforces [`VERTICAL_SLICE.md`](VERTICAL_SLICE.md) scope boundaries, manages [`BUILD_ORDER.md`](BUILD_ORDER.md) task sequencing, audits UFE rollback risks, and prevents scope creep.
* **Directive:** Rejects all creative feature additions and directs focus to Milestone 0 implementation.

### 2. `ufe_engine_specialist`
* **Role:** Unity & UFE 2 Configuration Engineer.
* **Responsibilities:** Translates character moves into UFE Move Editor config assets, sets up hitboxes/hurtboxes, configures UFE Global Editor settings, and writes custom C# helper scripts for Tier 2/3 mechanics.
* **Directive:** Flags unverified UFE capabilities with `[VERIFY]` and ensures all scripts maintain GGPO rollback determinism.

### 3. `animation_technical_director`
* **Role:** Animation Retargeting & Rigging Specialist.
* **Responsibilities:** Sources and audits 3D animation clips against [`ANIMATION_BUDGET.md`](ANIMATION_BUDGET.md), manages Mixamo/Humanoid retargeting in Unity, and sets up Unity Animator State Machines.
* **Directive:** Enforces minimal animation count targets to protect the developer from asset overload.

---

## Deprioritized Roles (Inactive Until Milestone 0 Complete)
* `game_designer` — INACTIVE (Creative design freeze).
* `game_artist` — INACTIVE (Concept art generation freeze).
* `audio_designer` — INACTIVE (Placeholder audio only during Milestone 0).
