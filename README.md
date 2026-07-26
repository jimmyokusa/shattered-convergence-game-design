# ⚔️ The Shattered Convergence — Production & Design Repository

---

## 🚨 PROJECT STATUS: DESIGN-COMPLETE / IMPLEMENTATION-ZERO

> **CURRENT SCOPE OF WORK:** This repository contains a fully specified 8-character fighting game design bible, but **zero engine implementation currently exists**. 
>
> All development is strictly focused on **Milestone 0: The Vertical Slice** (Zenthos mirror match on Ashfall Coliseum).
>
> 📖 **Read the Vertical Slice Specification:** [`VERTICAL_SLICE.md`](VERTICAL_SLICE.md)  
> 🛠️ **View the Unity Build Order:** [`BUILD_ORDER.md`](BUILD_ORDER.md)  
> 🏗️ **View Roster Implementation Tiers:** [`BUILD_TIERS.md`](BUILD_TIERS.md)

---

## 📚 Production & Technical Roadmap Files

* [`VERTICAL_SLICE.md`](VERTICAL_SLICE.md) — **Milestone 0 Scope Boundary** (Zenthos Mirror Match, explicit in-scope/out-of-scope lists, Definition of Done).
* [`BUILD_ORDER.md`](BUILD_ORDER.md) — Step-by-step ordered task checklist taking the developer from an empty Unity project to Milestone 0.
* [`BUILD_TIERS.md`](BUILD_TIERS.md) — Implementation classification (Tiers 1–3) based on UFE cost and rollback risk.
* [`ANIMATION_BUDGET.md`](ANIMATION_BUDGET.md) — Project-wide animation clip count aggregate (**341 Animations total; 29 for Milestone 0**).
* [`STAGE_PERFORMANCE_BUDGET.md`](STAGE_PERFORMANCE_BUDGET.md) — Real-time 60 FPS performance limits (85k tris max, 2048x2048 textures, rollback headroom).
* [`GAME_DESIGN.md`](GAME_DESIGN.md) — Primary Game Design Bible (Universal mechanics, provisional frame data, lore, Known Tuning Risks).

---

## 📂 Character Asset Directory Structure

Each character directory under `characters/<Name>/` contains:
* `CHARACTER_DESIGN.md` — Character lore, moveset, and provisional frame data.
* `UFE_IMPLEMENTATION.md` — Technical mapping of moves onto UFE 2 features & rollback risk notes.
* `ANIMATION_MANIFEST.md` — Itemized required animation clip list with total count.
* `VFX_SFX_SPEC.md` — Visual particle texture specs and 3-layer audio profiles.
* `audio/S2S_PERFORMANCE_GUIDE.md` — Speech-to-Speech vocal guides.
* `sprites/` — 3D-optimized T-pose concept sprite.
* `stages/` — Home stage environment concept artwork.

---

## 🎮 Roster Tier Summary

| Tier | Character | Archetype | UFE Implementation Complexity | Rollback Risk |
| :--- | :--- | :--- | :--- | :--- |
| **Tier 1** | **Zenthos** *(Milestone 0)* | Cinder Flame All-Rounder | Native UFE Move Editor | Low (Foundation) |
| **Tier 1** | **Brutus** | Tectonic Armor Grappler | Native Armor & Throws | Low (Foundation) |
| **Tier 1** | **Ignacia** | Flame Rekka Striker | Move Branching Sequences | Low / Moderate |
| **Tier 2** | **Melancholia** | Gothic Frost Zoner | Self-Damage HP Cancels | Moderate |
| **Tier 2** | **Lyra** | Lightning Trapper | Deployable Persistent Nodes | Moderate / High |
| **Tier 2** | **Nereus** | Aquatic Zoner | Spatial Vector Displacement | Moderate |
| **Tier 3** | **Sylas** | Druid / Wolf Shapeshifter | Mid-match Model / Stance Swap | HIGH (Stance Swap) |
| **Tier 3** | **Vesper** | Umbral Puppet Master | Independent Sub-Entity Actor | CRITICAL (Dual Actor) |
