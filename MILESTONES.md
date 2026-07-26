# 🗺️ Comprehensive Production Milestone Plan: *The Shattered Convergence*

> **GOVERNING PRODUCTION PRINCIPLE:**
> **Combat game feel cannot be evaluated against missing asset classes.**
> A punch with no sound, no spark, and no hitstop reads as broken even when frame data is frame-perfect. If a solo developer tunes hitstop against a silent, effectless hit, they are tuning against a lie and will re-tune everything later.
> Every milestone exit MUST guarantee that every in-scope element across character, stage, and game shell reaches **at least P1 (Functional Temp)** fidelity. No milestone may exit with an asset class sitting at P0.

---

## 🛠️ Mechanism 1: Asset Class Taxonomy & Discipline Ownership

The production of *The Shattered Convergence* requires 18 distinct asset classes across three major domains: **Character**, **Stage**, and **Game Shell**.

| Domain | # | Asset Class | Contents | Discipline / Producer |
| :--- | :--- | :--- | :--- | :--- |
| **Character** | 1 | **Model & Rig** | 3D Mesh, textures, materials, skeleton, weight painting, Unity Humanoid avatar validation. | **Tool-Assisted / Human-Only** (Tripo3D/Blender + Human Rigging) |
| **Character** | 2 | **Animation** | Full clip manifest per `ANIMATION_MANIFEST.md` (Locomotion, Normals, Specials, Reactions, Throws). | **Human-Only Craft** (Sourcing/Keyframing/Retargeting) |
| **Character** | 3 | **Collision** | Hitboxes (Red), Hurtboxes (Green), Pushboxes (Yellow), Throwboxes (Blue) assigned per animation frame in UFE 2 Move Editor. | **Automatable / Tool-Assisted** (`@ufe-integration-engineer` + Human review) |
| **Character** | 4 | **Frame Data** | Startup, Active, Recovery, Block Advantage, Hitstop, Pushback values authored & tuned in UFE 2. | **Human-Only** (Transcribed to docs by `@frame-data-scribe`) |
| **Character** | 5 | **VFX** | Light/Heavy hit sparks, block sparks, counter-hit flash, special move effects, super flash, motion trails, dust, KO burst. | **Tool-Assisted** (Generic Shaders/Particles + Bespoke VFX Shader Graph) |
| **Character** | 6 | **SFX** | Light/Heavy whiff whooshes, Light/Heavy hit impacts, block chimes, footsteps, landing foley, special move audio, super cast. | **Tool-Assisted** (Royalty-free libraries + synthesized audio layering) |
| **Character** | 7 | **Voice (VO)** | Attack effort grunts, damage hit reactions, KO screams, intro dialogues, victory lines, taunts, character select calls. | **Tool-Assisted** (ElevenLabs / S2S Generator + Human audio chop) |
| **Character** | 8 | **UI Assets** | HUD select portrait, HUD nameplate, select icon, health bar treatment, win screen art, render cuts. | **Tool-Assisted** (2D Concept Generator + Human UI layout) |
| **Character** | 9 | **Camera** | Character intro camera framing, Super Level 3 cinematic camera track, KO slow-mo zoom, round reset camera pan. | **Tool-Assisted** (UFE Camera Editor + Unity Cinemachine) |
| **Character** | 10 | **Metadata** | AI behavior profiles (CPU opponent), movelist UI data, combo trial data definitions. | **Automatable** (`@ufe-integration-engineer` / JSON configs) |
| **Character** | 11 | **Systems Integration** | Character prefab registered in UFE Global Config, loads in match, state resets cleanly across round transitions. | **Automatable** (`@ufe-integration-engineer` / C# Integration) |
| **Stage** | 12 | **Stage Geometry & Rig** | 3D Arena floor mesh, boundary walls (-7m to +7m), prop geometry, static background scenery. | **Tool-Assisted** (Blender / Low-Poly Asset Libraries) |
| **Stage** | 13 | **Stage Lighting & FX** | Main direction light, ambient bounce, magma/frost particle effects, skybox, volumetric fog. | **Tool-Assisted** (Unity Universal Render Pipeline / Lighting Settings) |
| **Stage** | 14 | **Stage Audio & Music** | Stage ambient loops (magma bubbling, wind), dynamic interactive BGM track (Round 1/2 vs Final Round variation). | **Tool-Assisted** (Audio libraries + BGM looping) |
| **Stage** | 15 | **Stage Performance** | Real-time budget validation (Draw calls < 150, Triangles < 100k, locked 60.0 FPS on target hardware). | **Automatable** (`@asset-pipeline-engineer` / Unity Profiler) |
| **Game Shell** | 16 | **Match Flow & Rules** | Round start sequence ("READY / FIGHT"), 99-second round timer, 2-out-of-3 round win logic, KO slow-motion, match reset. | **Automatable** (UFE Native Engine Core) |
| **Game Shell** | 17 | **HUD & UI System** | Health bars, Super Meter gauges, Combo Counter text, Round Win icons, Timer display, Pause menu, Results screen. | **Tool-Assisted** (UFE UI Template + Custom Unity UI Toolkit) |
| **Game Shell** | 18 | **Input & Config** | Controller mapping (Arcade stick, pad, keyboard), deadzones, input leniency buffer, rebinding system. | **Automatable** (UFE Input Manager / Unity Input System) |

---

## 🪜 Mechanism 2: The Fidelity Ladder (P0 / P1 / P2 Criteria)

Every asset class progresses through three distinct fidelity tiers. **P1 is the non-negotiable minimum required to judge game feel.**

| Class | P0 — Absent / Debug | P1 — Functional Temp (Minimum for Game-Feel Evaluation) | P2 — Final (Shippable Quality) |
| :--- | :--- | :--- | :--- |
| **1. Model & Rig** | Capsule / White box / No mesh | Untextured or single-color low-poly mesh; valid Humanoid avatar skeleton; correct height/scale. | Fully textured (2K maps), cel-shaded, custom material shader, weighted mesh, zero bone clipping. |
| **2. Animation** | T-pose T-stance static | Sourced/Mocap/Rough clip; correct frame length; clear key poses for startup, hitframe, and recovery; root motion zeroed out. | Polished hand-keyed/retargeted 60 FPS animation; exaggerated anticipation, follow-through, crisp weight & contact frames. |
| **3. Collision** | No hitboxes / default sphere | Standard cuboid hitboxes/hurtboxes attached to skeleton joints in UFE; color-coded (Red/Green/Yellow/Blue); accurate active frames. | Frame-by-frame tightly fitted collision boxes matching 3D geometry; custom pushbox shapes preventing pass-through. |
| **4. Frame Data** | Default 10f placeholders | Engine-tuned startup, active, recovery, hitstop (3-12f), blockstun, and pushback distance; feels distinct between Light & Heavy. | Tournament-balanced frame advantage, micro-tuned hitstop/blockstop, verified frame-trap and combo routes. |
| **5. VFX** | Silence / No visual output | Generic particle burst (Light=small spark, Heavy=large spark, Block=blue shield, Projectile=colored sphere); correct frame timing & origin joint. | Bespoke shader graph flipbooks matching `VFX_SFX_SPEC.md` (e.g., Zenthos `#FF6E0F` 4.5x HDR cinder sparks, magma cracks). |
| **6. SFX** | Silence | Royalty-free library SFX; distinguishable Light vs Heavy impact, whiff whoosh, block chime, projectile cast; correct frame sync. | Layered custom audio matching `VFX_SFX_SPEC.md` profile (e.g., 60Hz sub-bass thud + crisp flame crunch, 800Hz cast boost). |
| **7. Voice (VO)** | Silence | Generic AI/synth effort grunts (light/heavy attack), hit reactions (light/heavy hit), KO scream, 1 intro line, 1 win line; basic volume mix. | Professional S2S / voice actor performance; full effort table, multi-hit grunts, line variations, distinct character persona. |
| **8. UI Assets** | Missing / Red error texture | Programmer-art gray boxes or standard UFE template graphics; clear text for HP, meter, timer, name; static portrait image. | Bespoke 2D UI matching dark fantasy aesthetic; stylized health bar frame, animated meter, character select render cut. |
| **9. Camera** | Static fixed perspective | Standard UFE tracking camera (smooth pan/zoom keeping both fighters on screen); basic static intro framing. | Dynamic camera work; custom intro pan, dramatic Super Level 3 cinematic tracking cut, low-angle KO impact freeze frame. |
| **10. Metadata** | Empty / Default | Basic CPU AI profile (aggression/blocking probability); standard movelist JSON displaying move names & input motions. | Balanced multi-difficulty AI profiles (Easy/Medium/Hard/Nightmare); combo trials with visual demo inputs. |
| **11. Systems Integration**| Crash on load / Missing asset | Character registers in UFE Global Editor; spawns smoothly; health/meter states clean; survives round reset without state leaks. | Full tournament match persistence; seamless state serializing for rollback netcode; error-free scene transitions. |
| **12. Stage Geometry** | Invisible plane | Low-poly flat floor mesh with boundary walls (-7m to +7m); primitive background geometry representing arena shape. | High-detail 3D environment mesh; textured arena floor, atmospheric background structures, skybox, environmental depth. |
| **13. Stage Lighting** | Ambient white light | Single Directional Light + basic shadow map; clear character visibility; consistent contrast. | Dynamic URP lighting setup; volumetric fog, emissive magma/glow accents, color-graded post-processing profile. |
| **14. Stage Audio** | Silence | Monophonic ambient loop (e.g., wind/rumble); single background music track looping cleanly. | Stereo environmental audio mix; dynamic 2-layer BGM track shifting intensity on final round / low health. |
| **15. Stage Performance**| Uncapped / Stuttering | Verified 60.0 FPS locked performance in 1080p; draw calls < 200; zero frame drops during particle clashes. | Optimized draw calls < 100, triangle count < 80k, rock-solid 60 FPS across all resolution scales up to 4K. |
| **16. Match Flow** | Infinite fight / Manual reset | Standard UFE round manager active; 99s timer ticks; 2-out-of-3 round logic awards wins; KO message; match reset on final KO. | Custom transition overlays ("ROUND 1", "READY/FIGHT", "FINISH!"); victory presentation; seamless instant rematch flow. |
| **17. HUD & UI System**| Missing HUD | UFE default HUD displaying HP bars, Super Meter, Combo Counter, and Round Win indicators. | Custom UI canvas; animated health drain, hit combo counter with scaling font animations, stylized timer. |
| **18. Input & Config** | Hardcoded keys | Direct UFE Input Manager mapping supporting standard Xbox/PS pad + keyboard; basic input leniency buffer (4-6 frames). | Custom input rebinding menu; SOCD cleaner setup for Hitbox/leverless controllers; adjustable input buffer window. |

---

## ⛓️ Mechanism 3: The Serial Dependency Graph & Solo Blocking Path

In a one-person development context, parallel execution across disciplines is impossible. The human developer is **serially blocked** through a single linear production chain per character and stage.

### Primary Character Serial Dependency Chain (11 Sequential Steps)

```
[Step 1: 3D Model & Avatar Rigging] (Tool-Assisted: Tripo3D -> Blender -> Unity Rig Setup)
       │
       ▼
[Step 2: Animation Sourcing & Retargeting] (Human-Only Craft: 29-41 Clips mapped to Skeleton)
       │
       ▼
[Step 3: UFE 2 Move Config & Animation Assignment] (Tool-Assisted: `@ufe-integration-engineer`)
       │
       ▼
[Step 4: Collision Box Authoring] (Human-Only / Tool-Assisted: Hitboxes/Hurtboxes assigned per frame)
       │
       ▼
[Step 5: Engine Frame Data & Pushback Tuning] (Human-Only: Playtesting on Controller)
       │
       ▼
[Step 6: P1 VFX Hookup & Frame Synchronization] (Tool-Assisted: Spawning sparks on active hit frames)
       │
       ▼
[Step 7: P1 SFX Hookup & Audio Sync] (Tool-Assisted: Triggering whiff/hit audio on frame events)
       │
       ▼
[Step 8: P1 Voice / Effort Layering] (Tool-Assisted: S2S / Audio Chop attached to move cast/hit reaction)
       │
       ▼
[Step 9: UI Asset Setup & Portrait Assignment] (Tool-Assisted: 2D render crop -> HUD slot)
       │
       ▼
[Step 10: Camera Framing & Intro Setup] (Tool-Assisted: Cinemachine / UFE Camera Editor)
       │
       ▼
[Step 11: Systems Integration & Round Reset Audit] (Tool-Assisted: `@ufe-integration-engineer`)
```

### Stage & Game Shell Serial Chain

```
[Stage Mesh Geometry] ──► [Stage Lighting & Fog] ──► [Camera Constraints] ──► [Stage Audio & BGM]
                                                                  │
[Game Shell HUD Setup] ──► [Input Rebinding] ──► [Match Loop Logic] ◄───────┘
```

### Solo Bottleneck & Independent Task Slots

- **Primary Solo Bottleneck:** **Steps 2, 4, and 5** (Animation Craft, Collision Box Authoring, and Controller Frame Data Tuning). These three steps consume ~70% of total human production time and **cannot be delegated to AI subagents**.
- **Genuinely Independent Work (Interleaved Tasks):**
  - While waiting on animation retargeting compile cycles or Blender bakes, the human can interleave **UI portrait rendering (Step 9)**, **SFX asset sourcing (Step 7)**, or **Voice sample generation via Python scripts (Step 8)**.
  - Stage geometry and lighting setup can be executed in isolated sessions between character milestones.

---

## 🎯 Mechanism 4: Milestone Definitions (M0 through M7)

---

### Milestone 0 (M0): Vertical Slice — Zenthos Mirror Match
* **Scope Statement:** Build a fully playable, judgeable 2.5D fighting game vertical slice featuring **Zenthos** in a local mirror match (Zenthos vs. Zenthos) on **Ashfall Coliseum** at locked 60 FPS. Establishes core strike/block/throw dynamics, hitstop weight, and projectile clashes at P1 functional temp fidelity across all 18 asset classes.
* **Exit Criteria (Mandatory):**
  1. All in-scope asset classes for Zenthos, Ashfall Coliseum, and Game Shell reach **at least P1 fidelity**. Zero P0 cells permitted.
  2. Player can execute cancel combo `5LP` → `5HP` → `236P` (Cinder Wave) reliably on controller; combo counter increments cleanly.
  3. Hitstop duration differs noticeably between Light (3–5f) and Heavy (10–12f) attacks.
  4. Guard rules function (Low sweep hits crouch-block; Overhead `j.HP` hits stand-block).
  5. Throw (`LP+LK`) connects at close range ignoring guard and whiffs with recovery at distance.
  6. Locked 60.0 FPS with zero dropped frames during projectile clashes on Ashfall Coliseum.
* **Explicit Out-of-Scope Refusal List:**
  - ❌ No other characters (Melancholia, Brutus, Ignacia, Lyra, Nereus, Sylas, Vesper are BLOCKED).
  - ❌ No GGPO rollback netcode or online multiplayer.
  - ❌ No character select menu or story mode (Direct boot into Zenthos mirror match).
  - ❌ No Super Level 3 cinematic animations or 8K stage background shaders.
  - ❌ No custom voice actors or final polished music tracks.

#### M0 Completion Matrix

| Asset Class | Zenthos (P1) | Zenthos (P2) | Ashfall Coliseum | Game Shell |
| :--- | :---: | :---: | :---: | :---: |
| 1. Model & Rig | **P1** | **P1** | — | — |
| 2. Animation | **P1** (29 clips) | **P1** (29 clips) | — | — |
| 3. Collision | **P1** | **P1** | — | — |
| 4. Frame Data | **P1** | **P1** | — | — |
| 5. VFX | **P1** (Temp Sparks) | **P1** (Temp Sparks) | — | — |
| 6. SFX | **P1** (Library SFX) | **P1** (Library SFX) | — | — |
| 7. Voice (VO) | **P1** (TTS / Grunts) | **P1** (TTS / Grunts) | — | — |
| 8. UI Assets | **P1** (Temp Icon) | **P1** (Temp Icon) | — | — |
| 9. Camera | **P1** (Static Tracking)| **P1** (Static Tracking)| — | — |
| 10. Metadata | **P1** (Move JSON) | **P1** (Move JSON) | — | — |
| 11. Systems Integration | **P1** | **P1** | — | — |
| 12. Stage Geometry | — | — | **P1** (Arena Floor) | — |
| 13. Stage Lighting | — | — | **P1** (1 Directional) | — |
| 14. Stage Audio | — | — | **P1** (Single BGM) | — |
| 15. Stage Performance | — | — | **P1** (60 FPS Validated)| — |
| 16. Match Flow | — | — | — | **P1** (99s / 2-out-of-3)|
| 17. HUD & UI System | — | — | — | **P1** (UFE Default HUD)|
| 18. Input & Config | — | — | — | **P1** (Pad / Keys) |

* **New Asset Production Required (Counted):**
  - **Character Assets (Zenthos):** 1 Model & Rig, 29 Animation Clips, 11 Move Collision Sets, 11 Frame Data Configs, 4 Temp VFX (Light spark, Heavy spark, Block flash, Fireball), 4 Temp SFX (Whiff, Impact, Block, Cast), 6 Voice grunts/efforts, 2 UI Images (Portrait, Icon), 1 Camera config, 1 Move metadata set, 1 Integration config. Total = **61 Character Assets**.
  - **Stage Assets (Ashfall Coliseum):** 1 Arena mesh, 1 Lighting profile, 1 BGM loop track, 1 Perf config. Total = **4 Stage Assets**.
  - **Game Shell Assets:** 1 Match loop config, 1 Default HUD setup, 1 Input config. Total = **3 Shell Assets**.
  - **Grand Total M0 New Assets:** **68 Assets**.
* **Fidelity Upgrades Required:** None (First milestone).
* **Primary Risk:** Developer spends weeks tweaking UFE 2 editor parameters without establishing P1 SFX/VFX first, resulting in distorted game-feel judgments and endless re-tuning.

---

### Milestone 1 (M1): Pipeline Proof — Brutus Integration & Matchup Validation
* **Scope Statement:** Prove pipeline generalizability by adding **Brutus** (Tier 1 Armor Grappler) to the game. Validates heavy body collision, armor hit properties, command throws, and asymmetrical matchup dynamics (Zenthos vs. Brutus) on Ashfall Coliseum.
* **Exit Criteria (Mandatory):**
  1. All asset classes for Brutus reach **at least P1 fidelity**. Zero P0 cells permitted.
  2. Brutus vs. Zenthos and Brutus vs. Brutus matches execute flawlessly.
  3. Armor mechanics function in engine (Brutus absorbs 1 hit during `22P` Tectonic Slam without entering hitstun).
  4. Command Throw (*Caldera Press*) connects, overrides guard, and executes multi-hit throw camera sequence.
  5. Asymmetrical pushback and heavy hitstop verified against Zenthos.

#### M1 Completion Matrix

| Asset Class | Zenthos | Brutus | Ashfall Coliseum | Game Shell |
| :--- | :---: | :---: | :---: | :---: |
| 1. Model & Rig | P1 | **P1** | — | — |
| 2. Animation | P1 (29 clips) | **P1** (37 clips) | — | — |
| 3. Collision | P1 | **P1** (Armor/Command Boxes)| — | — |
| 4. Frame Data | P1 | **P1** (Armor/Grab Frames) | — | — |
| 5. VFX | P1 | **P1** (Earth Crack / Armor Flash) | — | — |
| 6. SFX | P1 | **P1** (Sub-Bass Thud / Heavy Slam) | — | — |
| 7. Voice (VO) | P1 | **P1** (Heavy Grunts / Roars) | — | — |
| 8. UI Assets | P1 | **P1** (Brutus Portrait / Icon) | — | — |
| 9. Camera | P1 | **P1** (Command Throw Zoom) | — | — |
| 10. Metadata | P1 | **P1** | — | — |
| 11. Systems Integration | P1 | **P1** | — | — |
| 12-15. Stage Classes | — | — | P1 | — |
| 16-18. Game Shell | — | — | — | P1 |

* **Explicit Out-of-Scope Refusal List:**
  - ❌ No Tier 2/3 characters (Melancholia, Lyra, Nereus, Sylas, Vesper BLOCKED).
  - ❌ No Character Select Screen (Matchup chosen via debug boot parameter).
  - ❌ No rollback netcode testing.
* **New Asset Production Required:** Brutus Model (1), Brutus Animations (37), Brutus Collision (11), Brutus Frame Data (11), Brutus VFX (4), Brutus SFX (4), Brutus Voice (6), Brutus UI (2), Brutus Camera (1), Brutus Metadata (1), Brutus Integration (1). Total = **80 New Assets**.
* **Fidelity Upgrades Required:** None.
* **Primary Risk:** UFE 2 native armor flags or command throw state transitions fail to sync with Zenthos's hitstun states, breaking matchup stability.

---

### Milestone 2 (M2): Core Game Loop & Tier 1 Completion
* **Scope Statement:** Complete Tier 1 by integrating **Ignacia** (Pyro Rekka Striker), alongside a functional 2.5D Game Shell featuring a Character Select Screen, Training Mode with frame data display, Round Reset presentation, and stage BGM.
* **Exit Criteria (Mandatory):**
  1. Ignacia reaches **P1 fidelity** across all asset classes; Tier 1 roster (Zenthos, Brutus, Ignacia) complete.
  2. Player can select any character on a functional Character Select Screen and boot into local matches.
  3. Ignacia's *Blaze Rekka* 3-stage branching sequence input functions cleanly in engine.
  4. Training Mode allows dummy state configuration (Block All, Auto-Block, Crouch, Jump, Reversal).
  5. UI HUD displays character portraits, custom health bars, and combo damage counters.

#### M2 Completion Matrix

| Asset Class | Zenthos | Brutus | Ignacia | Ashfall Coliseum | Game Shell |
| :--- | :---: | :---: | :---: | :---: | :---: |
| 1-11. Character Classes | P1 | P1 | **P1** (39 clips) | — | — |
| 12-15. Stage Classes | — | — | — | P1 | — |
| 16. Match Flow | — | — | — | — | **P1 → P2** (Rematch / Win Flow) |
| 17. HUD & UI System | — | — | — | — | **P1 → P2** (Char Select / Training) |
| 18. Input & Config | — | — | — | — | **P1 → P2** (Rebinding Menu) |

* **Explicit Out-of-Scope Refusal List:**
  - ❌ No Tier 2 or Tier 3 characters.
  - ❌ No online netcode.
  - ❌ No story or arcade cinematic cutscenes.
* **New Asset Production Required:** Ignacia Model (1), Ignacia Animations (39), Ignacia Collision/Frame Data (22), Ignacia VFX/SFX/VO (14), Ignacia UI/Camera (3), Char Select UI (5), Training Mode Engine (2). Total = **86 New Assets**.
* **Fidelity Upgrades Required:** Game Shell HUD & Input System upgraded from P1 to P2.
* **Primary Risk:** Rekka branching input windows in UFE 2 feel dropped or overly restrictive on pad/stick controllers.

---

### Milestone 3 (M3): Tier 2 Roster Expansion — Specialized Zoners & Trappers
* **Scope Statement:** Integrate all three Tier 2 characters (**Melancholia**, **Lyra**, **Nereus**) and introduce a second stage (**Glacial Spire**). Validates complex mechanics including self-damage health cancels, deployable trap nodes, and fluid displacement physics.
* **Exit Criteria (Mandatory):**
  1. Melancholia, Lyra, and Nereus reach **at least P1 fidelity** across all asset classes. Zero P0 cells permitted.
  2. Melancholia's *Thorn Rush* deducts 10% self-damage grey health upon move cancel.
  3. Lyra's *Volt Nodes* deploy on stage and form intersecting damage beam zones.
  4. Nereus's *Vortex Drag* applies smooth physical velocity pull to opponents.
  5. Glacial Spire stage fully playable at 60 FPS.

#### M3 Completion Matrix

| Asset Class | Tier 1 (Zenthos/Brutus/Ignacia) | Melancholia | Lyra | Nereus | Glacial Spire Stage | Game Shell |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| 1-11. Character Classes | P1 | **P1** (40 clips) | **P1** (37 clips) | **P1** (37 clips) | — | — |
| 12-15. Stage Classes | P1 (Ashfall) | — | — | — | **P1** (Spire Arena) | — |
| 16-18. Game Shell | P2 | — | — | — | — | P2 |

* **Explicit Out-of-Scope Refusal List:**
  - ❌ No Tier 3 characters (Sylas and Vesper are BLOCKED).
  - ❌ No online rollback testing.
* **New Asset Production Required:** 3 Character Models (3), 114 Animation Clips (114), 33 Move Collision/Frame Configs (66), 3 sets VFX/SFX/VO (42), 3 UI sets (6), Glacial Spire Stage (4). Total = **235 New Assets**.
* **Fidelity Upgrades Required:** None.
* **Primary Risk:** Lyra's persistent trap nodes or Nereus's displacement vectors cause physics stutter or state errors in UFE 2.

---

### Milestone 4 (M4): Rollback Netcode Integration & Determinism Audit
* **Scope Statement:** Integrate GGPO / UFE Rollback Netcode across the complete 6-character roster (Tiers 1 & 2) over local network and simulated latency (50ms - 150ms with 2% packet loss). Audit state determinism, hitstop syncing, and asset memory allocation.
* **Exit Criteria (Mandatory):**
  1. 6-character roster playable online with zero desynchronization over 100 test matches.
  2. Rollback execution preserves exact frame advantage, hitstop freeze, and pushback values as local play.
  3. Lyra's deployable Volt Nodes and Melancholia's grey health states serialize cleanly across rollback frames without teleporting or state corruption.
  4. Game engine passes UFE Rollback Desync Auto-Test Suite without throwing state divergence exceptions.

#### M4 Completion Matrix

| Asset Class | Tier 1 Roster | Tier 2 Roster | Stages (Ashfall / Glacial) | Netcode & Game Shell |
| :--- | :---: | :---: | :---: | :---: |
| 1-11. Character Classes | P1 (Rollback Audited) | P1 (Rollback Audited) | — | — |
| 12-15. Stage Classes | — | — | P1 (Rollback Validated)| — |
| 16-18. Systems & Netcode| — | — | — | **P1 → P2** (GGPO Rollback Complete)|

* **Explicit Out-of-Scope Refusal List:**
  - ❌ No Tier 3 characters (Sylas & Vesper).
  - ❌ No match-making server backend or online rank systems (P2P direct IP / Steam P2P connection only).
* **New Asset Production Required:** Netcode Sync Scripts (3), Desync Diagnostic Tools (2). Total = **5 System Assets**.
* **Fidelity Upgrades Required:** Netcode & Match Systems upgraded to P2 (Shippable rollback determinism).
* **Primary Risk:** Non-deterministic C# code in UFE 2 custom scripts or particle systems triggers recurring desync bugs under network rollbacks.

---

### Milestone 5 (M5): Tier 3 High-Risk Roster Integration
* **Scope Statement:** Build and integrate the two highest-complexity characters: **Sylas** (Shapeshifter with dual Druid/Wolf movesets) and **Vesper** (Umbral Puppet Master with independent entity Solitude). Integrates both into the validated GGPO rollback loop.
* **Exit Criteria (Mandatory):**
  1. Sylas and Vesper reach **at least P1 fidelity** across all asset classes. Zero P0 cells permitted.
  2. Sylas swaps between Druid (Staff) and Wolf (Feral) stances mid-match; animation clips, hitboxes, and move tables update cleanly without frame lag.
  3. Vesper controls puppet entity *Solitude* simultaneously with main body; dual-entity inputs serialize deterministically under GGPO rollback.
  4. Full 8-character roster functional on Character Select Screen and selectable for online/local matches.

#### M5 Completion Matrix

| Asset Class | Tiers 1 & 2 Roster | Sylas (Tier 3) | Vesper (Tier 3) | Stages | Game Shell & Netcode |
| :--- | :---: | :---: | :---: | :---: | :---: |
| 1-11. Character Classes | P1 | **P1** (71 clips - Dual Stance) | **P1** (41 clips - Puppet Entity) | — | — |
| 12-15. Stage Classes | P1 | — | — | P1 | — |
| 16-18. Shell & Netcode | P2 | — | — | — | P2 |

* **Explicit Out-of-Scope Refusal List:**
  - ❌ No final polish P2 visual assets or bespoke voice acting recordings.
  - ❌ No arcade story cutscenes.
* **New Asset Production Required:** 2 Character Models (3 meshes including Wolf form), 112 Animation Clips (112), 35 Move Collision/Frame sets (70), 2 sets VFX/SFX/VO (28), 2 UI sets (4), Puppet C# Controller Engine (2). Total = **219 New Assets**.
* **Fidelity Upgrades Required:** None.
* **Primary Risk:** Dual-actor state tracking for Vesper's puppet triggers irrecoverable desync loops in GGPO rollback netcode.

---

### Milestone 6 (M6): Content Complete — P2 Polish & Bespoke Asset Upgrade
* **Scope Statement:** Upgrade all 8 characters, 2 stages, and the game shell from P1 (Functional Temp) to **P2 (Final Shippable Quality)**. Integrates bespoke 2K textures, cel-shaders, hand-tuned animations, custom particle shader graphs per `VFX_SFX_SPEC.md`, layered audio profiles, and professional voice acting.
* **Exit Criteria (Mandatory):**
  1. All 18 asset classes across all 8 characters and stages reach **P2 Final Fidelity**. Zero P1 assets remaining.
  2. Character visuals match cel-shaded dark fantasy art direction.
  3. All special moves feature bespoke VFX flipbooks (e.g., Zenthos 4.5x HDR cinder sparks, Melancholia 5.0x ice needles) and 60Hz sub-bass layered audio.
  4. Professional voice acting grunts, hit reactions, intros, and victory lines fully integrated.
  5. Third stage (**Void Convergence Arena**) added at P2 fidelity.

#### M6 Completion Matrix

| Asset Class | Full 8-Character Roster | 3 Stages (Ashfall / Spire / Void) | Game Shell & UI |
| :--- | :---: | :---: | :---: |
| 1. Model & Rig | **P1 → P2** (2K Cel-Shaded) | — | — |
| 2. Animation | **P1 → P2** (Hand-Key Polished)| — | — |
| 3. Collision | **P1 → P2** (Pixel-Fitted) | — | — |
| 4. Frame Data | **P1 → P2** (Tournament Tuned)| — | — |
| 5. VFX | **P1 → P2** (Bespoke Shaders) | — | — |
| 6. SFX | **P1 → P2** (Layered Sub-Bass) | — | — |
| 7. Voice (VO) | **P1 → P2** (Pro Voice Actor) | — | — |
| 8. UI Assets | **P1 → P2** (2D Character Art) | — | — |
| 9. Camera | **P1 → P2** (Cinematic Supers) | — | — |
| 10-11. Metadata/Integration| **P1 → P2** | — | — |
| 12-15. Stage Classes | — | **P1 → P2** (Full Environment) | — |
| 16-18. Shell & Netcode | — | — | **P2** (Shippable Polish) |

* **Explicit Out-of-Scope Refusal List:**
  - ❌ No post-launch DLC characters or additional stages beyond the core 8 characters and 3 stages.
* **New Asset Production Required:** Void Arena Stage (4), Bespoke Voice Acting Package (8 sets), P2 VFX Shader Library (8 sets), P2 Audio Layer Package (8 sets), 2D Victory Character Art (8). Total = **36 New Content Packages**.
* **Fidelity Upgrades Required:** All 341 Animations, 8 Models, 8 VFX sets, 8 SFX sets, 8 Voice sets, 2 Stages upgraded from P1 to P2.
* **Primary Risk:** Asset creation workload (341 P2 polished animations + bespoke shader graphs) overwhelms the solo developer, causing production paralysis.

---

### Milestone 7 (M7): Balance, Optimization & Release Candidate (Ship)
* **Scope Statement:** Execute final frame data balancing pass across all 28 matchup pairs, optimize GPU/CPU memory footprints, complete SOCD input compliance validation, build release installers, and lock the launch candidate.
* **Exit Criteria (Mandatory):**
  1. Game maintains rock-solid 60.0 FPS across all stages and character match combinations on minimum spec hardware.
  2. Zero game-breaking infinite combos, unblockable setups, or desync states detected in automated playtest suite.
  3. Release candidate installer/steam package boots, connects online, and executes error-free.

#### M7 Completion Matrix
* All asset classes sit at **P2 Shippable Quality**.

* **New Asset Production Required:** Zero new assets (Balance & Optimization pass only).
* **Primary Risk:** Last-minute frame data balance changes introduce unintended combo infinites or unblockable setups.

---

## 📊 Summary of Asset Production & Milestone Workload

| Milestone | Target Roster | New Assets (Counted) | Fidelity Upgrades | Primary Bottleneck / Risk |
| :--- | :--- | :---: | :---: | :--- |
| **M0** | Zenthos (Mirror Match) | **68** | None (All P1) | Developer tunes frame data without P1 SFX/VFX feedback. |
| **M1** | Zenthos + Brutus | **80** | None | Armor / Command throw UFE integration issues. |
| **M2** | Tier 1 Complete + Shell | **86** | Shell P1 → P2 | Rekka branching input windows in UFE 2. |
| **M3** | Tier 2 Complete (6 Chars) | **235** | None | Complex traps / physics displacement state lag. |
| **M4** | Netcode (6 Chars) | **5** | Netcode P1 → P2 | Rollback state desynchronization under latency. |
| **M5** | Tier 3 Complete (8 Chars) | **219** | None | Dual-stance / Puppet multi-actor desync. |
| **M6** | Content Complete | **36** | All P1 → P2 | Massive 341-clip animation & audio polish workload. |
| **M7** | Release Candidate | **0** | Final Polish | Last-minute infinite combo / balance breaks. |
| **TOTAL**| **Full Game** | **729 Assets** | — | — |
