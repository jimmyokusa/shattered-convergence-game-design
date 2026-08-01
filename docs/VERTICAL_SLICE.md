# 🎯 Vertical Slice Specification — Milestone 0

> **MILESTONE 0 SCOPE BOUNDARY:** This document defines the single, non-negotiable target currently in scope for production. No work outside this document is permitted until Milestone 0 satisfies all Definition of Done criteria.

---

## 1. Goal

Produce **one character** (**Zenthos**), fully playable in a local **mirror match** (Zenthos vs. Zenthos) on **one stage** (*Ashfall Coliseum*), feeling responsive, readable, and satisfying to play at 60 FPS.

---

## 2. Selected Character & Stage

* **Character:** **Zenthos** (Tier 1 Cinder Flame All-Rounder).
* **Stage:** **Ashfall Coliseum** (Static 3D arena mesh, static background, low-poly geometry).

---

## 3. Explicit IN-SCOPE List

Only the following elements may be authored, animated, coded, or configured for Milestone 0:

### 3.1 Character Mechanics & Inputs (Zenthos Only)
* **Locomotion:** Walk forward, walk back, crouch, neutral jump, forward jump, backward jump, dash forward, dash back.
* **Defensive:** Standing block, crouching block, blockstun, hitstun (high/mid/low), air hitstun, knockdown, wakeup.
* **Attacks (Normals):**
  * Standing Light Punch (`5LP`), Standing Heavy Punch (`5HP`).
  * Standing Light Kick (`5LK`), Standing Heavy Kick (`5HK`).
  * Crouching Light Punch (`2LP`), Crouching Heavy Sweep (`2HK`).
  * Jumping Heavy Punch (`j.HP`).
* **Attacks (Specials):**
  * *Cinder Wave* (`236P` — Single-hit fireball projectile).
  * *Inferno Rising* (`623P` — Vertical uppercut).
* **System Mechanics:**
  * Universal Throw (`LP+LK` attempt, connect, whiff, and being thrown).
  * Hitstop (Frame freeze on hit/block).
  * Pushback on hit and block.

### 3.2 Game Engine & Feedback
* **Stage:** Ashfall Coliseum arena floor mesh + static camera.
* **UI & HUD:** Barebones UFE default health bars, super meter, round timer, combo counter text.
* **VFX / SFX:** Generic placeholder hit-sparks (Light/Heavy), generic block flash, placeholder impact sound.
* **Game Loop:** Match start → 99-second round → 2-out-of-3 rounds match win → restart match.

---

## 4. Explicit OUT-OF-SCOPE List (Blunt Refusal List)

The following items are **STRICTLY PROHIBITED** from being worked on during Milestone 0:

* ❌ **No other characters** (Melancholia, Sylas, Brutus, Lyra, Vesper, Ignacia, Nereus are BLOCKED).
* ❌ **No online play / GGPO rollback testing** (Local 2-player controller/keyboard play only).
* ❌ **No story mode, arcade mode, or training mode menus**.
* ❌ **No character select screen** (Direct boot into Zenthos mirror match).
* ❌ **No custom voice acting** or ElevenLabs audio integration.
* ❌ **No character-specific cinematic Super Level 3 animations**.
* ❌ **No 8K stage background renders, dynamic magma shaders, or destruction FX**.
* ❌ **No stage BGM music tracks or ambient audio mix passes**.
* ❌ **No secondary character stances, transformation logic, or puppet entities**.

---

## 5. Definition of Done (Observable Testable Criteria)

Milestone 0 is complete **ONLY** when all of the following empirical criteria pass testing:

1. **Combos & Cancels:** A player can execute a cancel from `5LP` → `5HP` → `236P` (Cinder Wave) reliably on a local controller, and the sequence combo counter increments cleanly.
2. **Hitstop & Impact Weight:** Hitstop duration differs noticeably between Light attacks (3–5 frames freeze) and Heavy attacks (10–12 frames freeze), making heavy hits feel heavy without checking health bars.
3. **Block & Guard Rules:** Crouching block guards against low sweep (`2HK`) but gets hit by jumping overhead (`j.HP`). Standing block guards against jumping overhead (`j.HP`) but gets hit by low sweep (`2HK`).
4. **Collision & Pushback:** Attacking a blocking opponent pushes the attacker backward, preventing infinite corner trapping from normal spam.
5. **Throw Mechanics:** Throw (`LP+LK`) connects cleanly at close range ignoring block, plays throw animation, and knocks down opponent. Throw whiffs with recovery frames if out of range.
6. **Frame Rate Stability:** Locked **60.0 FPS** with zero dropped frames during mirror match projectile clashes on target hardware.

---

## 6. Milestone 0 Animation Budget

* **Total Required Animations for Milestone 0:** **29 Animations**.
*(Derived from Zenthos's `ANIMATION_MANIFEST.md` — covering 20 universal locomotion/hit state clips + 9 in-scope combat clips).*
