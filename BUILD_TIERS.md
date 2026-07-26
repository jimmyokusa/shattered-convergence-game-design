# 🏗️ Build Tiers & Implementation Sequencing

> **CRITICAL PRODUCTION RULE:** No Tier 2 character begins production until every Tier 1 character is playable, and no Tier 3 character begins production until Tier 2 is complete.

Characters are classified into three implementation tiers based on **UFE 2 implementation cost, animation workload, and rollback-determinism risk** — not on lore, popularity, or narrative sequence.

---

## Tier Summary Matrix

| Tier | Character | Archetype | Primary UFE Feature Dependency | Implementation Risk |
| :--- | :--- | :--- | :--- | :--- |
| **Tier 1** | **Zenthos** | Cinder Flame All-Rounder | Native Move Editor, Standard Controls | **Low (Foundation)** |
| **Tier 1** | **Brutus** | Armor Titan / Heavy Grappler | Native Armor Flags, Native Command Throws | **Low (Foundation)** |
| **Tier 1** | **Ignacia** | Rekka Striker / Rushdown | Move Branching, Sequence Inputs | **Low / Moderate** |
| **Tier 2** | **Melancholia** | Gothic Frost Zoner | Resource Meter, Self-Damage Health Cancels | **Moderate** |
| **Tier 2** | **Lyra** | Lightning Speedster / Trapper | Deployable Projectiles / Trap Node Intersections | **Moderate / High** |
| **Tier 2** | **Nereus** | Hydro Zoner / Displacer | Physics Wind Force / Gravitational Pull | **Moderate** |
| **Tier 3** | **Sylas** | Druid / Wolf Shapeshifter | Stance-Switch Engine, Dual Moveset Multiplier | **HIGH (Stance Duplication)** |
| **Tier 3** | **Vesper** | Umbral Puppet Master | Independent Sub-Entity Actor, Puppet Input Sync | **CRITICAL (Rollback Risk)** |

---

## Tier 1 — Foundation Characters

Characters whose mechanics map cleanly to UFE's native feature set (standard normals, projectiles, armor flags, command throws). Built first to establish reusable animation, collision, and hitstop systems.

### 1. Zenthos (Cinder Flame All-Rounder)
* **Justification:** Zenthos is the baseline archetype. His moveset consists of standard strike normals, a forward fireball projectile, an anti-air uppercut, and a forward dash strike. His mechanics establish the core collision, hitstop, and combo systems for the entire game.
* **UFE Dependencies:**
  * Standard Normals & Specials: **Native** (UFE Move Editor).
  * Perfect Draw (2f Motion Window): **Configured** (Requires strict frame window input setup in UFE Input Manager). `[VERIFY]`
* **UFE License Requirement:** UFE Basic / Standard / PRO.

### 2. Brutus (Tectonic Armor Grappler)
* **Justification:** Brutus tests UFE's heavy body collision, armor hit properties, and throw/grapple systems. His moveset uses native engine capabilities with zero custom code required.
* **UFE Dependencies:**
  * Armor Hits (Super Armor): **Native** (UFE Move Editor `Armor Options`). `[VERIFY]`
  * Command Throws (Caldera Press): **Native** (UFE Move Editor `Move Types: Throw`).
* **UFE License Requirement:** UFE Basic / Standard / PRO.

### 3. Ignacia (Pyro Rekka Striker)
* **Justification:** Ignacia validates multi-stage branching combo trees (Rekka slashes) and advance dashes. Her mechanics test sequence inputs without introducing external entities or persistent objects.
* **UFE Dependencies:**
  * Blaze Rekka (Branching Sequence): **Configured** (Configured via UFE Move Link / Chain inputs in Move Editor). `[VERIFY]`
  * Ember Dash: **Native** (Special dash move).
* **UFE License Requirement:** UFE Basic / Standard / PRO.

---

## Tier 2 — Moderate Complexity & Configured Mechanics

Characters requiring resource meter management, health-cost cancels, or persistent spatial trap interactions.

### 4. Melancholia (Gothic Frost Zoner)
* **Justification:** Melancholia introduces custom resource spending and health-cost cancels (Thorn Rush: 10% self-damage for move cancels).
* **UFE Dependencies:**
  * Ice Projectiles & Thrusts: **Native** (UFE Move Editor).
  * Thorn Rush Self-Damage Cancel: **Custom** (Requires C# script hooked to UFE move execution event to deduct HP and grant Grey Health). `[VERIFY]`
* **UFE License Requirement:** UFE Standard / PRO (Source access recommended for clean event hooks).

### 5. Lyra (Lightning Speedster & Trap Controller)
* **Justification:** Lyra deploys persistent Volt Nodes on stage that form electric laser arcs between each other. Persistent world objects create potential state desynchronization under rollback netcode if not tracked deterministically.
* **UFE Dependencies:**
  * High-Speed Movement & Teleports: **Native** / **Configured** (UFE Dash / Teleport moves).
  * Deployable Volt Nodes & Intersecting Beams: **Custom** (Requires C# manager to spawn, track, and sync node positions across network frames).
* **UFE License Requirement:** UFE PRO / Source (Source access required for rollback-safe object tracking).

### 6. Nereus (Abyssal Mariner & Fluid Displacer)
* **Justification:** Nereus features spatial displacement mechanics (Vortex Drag) that continuously pull or push opponent position regardless of hitstate.
* **UFE Dependencies:**
  * Water Projectiles & Geysers: **Native** (UFE Move Editor).
  * Vortex Drag Gravity Pull: **Configured** / **Custom** (Requires applying external velocity vectors to opponent entity during active move frames). `[VERIFY]`
* **UFE License Requirement:** UFE Standard / PRO.

---

## Tier 3 — Advanced Systems & High Rollback Risk

Characters requiring dual full-moveset multipliers or independent secondary actor entities. **High risk of scope creep, budget overflow, and state desynchronization.**

### 7. Sylas (Sylvan Druid / Frost Wolf Shapeshifter)
* **Justification:** Sylas is effectively two full characters in one body. Transforming from Druid (Staff) to Wolf (Bipedal Werewolf) requires swapping animation sets, hitboxes, hurtboxes, and move tables mid-match. This doubles his animation asset budget (~80+ animations).
* **UFE Dependencies:**
  * Dual-Stance System: **Configured** / **Custom** (UFE Stance system or custom character state machine swap). `[VERIFY]`
  * Separate Hitbox/Hurtbox Rigs: **Custom** (C# state swap binding new animator controller & collision profiles).
* **UFE License Requirement:** UFE PRO / Source.

### 8. Vesper (Umbral Void Puppet Master)
* **Justification:** Vesper controls an independent puppet entity (Solitude) simultaneously with her main body. Dual-entity control under rollback netcode requires deterministic synchronization of two complete input streams, state machines, and collision trees.
* **UFE Dependencies:**
  * Independent Sub-Entity Actor (Solitude): **Custom** (Requires custom C# puppet engine hooked into UFE's input and rollback loop). `[VERIFY]`
  * Dual Hitbox/Hurtbox Collision Matrix: **Custom**.
* **UFE License Requirement:** UFE Source (Source code modification required for multi-actor rollback loop).
