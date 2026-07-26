# 🛠️ Unity & UFE 2 Build Order — Milestone 0 (Zenthos)

This document provides a concrete, ordered, checkbox task list taking the developer from an empty Unity project to the completed **Milestone 0 Vertical Slice** (Zenthos Mirror Match on Ashfall Coliseum).

---

## Phase 1: Engine & Project Initialization
- [ ] **Step 1.1: Unity Project Setup**
  * Create a new Unity 2022.3 LTS 3D project.
  * Set Target Frame Rate to 60 FPS in Quality Settings. Disable V-Sync.
- [ ] **Step 1.2: Import UFE 2 Package**
  * Import Universal Fighting Engine 2 (UFE 2) asset package.
  * Open `UFE 2 -> Global Editor`. Create Global Config asset: `ShatteredConvergence_GlobalConfig.asset`.
- [ ] **Step 1.3: Configure Global Editor**
  * Set Game Mode: 2.5D (3D Models on 2D Plane).
  * Set FPS: 60.
  * Set Stage Dimensions: Width = 14.0m, Height = 6.0m.

---

## Phase 2: Character Rigging & Locomotion (Zenthos)
- [ ] **Step 2.1: Import Character Rig**
  * Import Zenthos 3D model FBX (`zenthos_mesh.fbx`) into Unity. Set Rig Type to `Humanoid`.
  * Create UFE Character Config: `Zenthos_CharacterConfig.asset` in `UFE 2 -> Character Editor`.
- [ ] **Step 2.2: Assign Basic Locomotion Animations**
  * Assign `Idle`, `Walk_Forward`, `Walk_Backward`, `Crouch_In`, `Crouch_Idle`, `Crouch_Out`.
  * Test character spawning in UFE Sandbox Scene (`UFE 2 -> Test Scene`). Verify Zenthos stands on stage.
- [ ] **Step 2.3: Assign Jump & Landing Animations**
  * Assign `Jump_Up`, `Jump_Forward`, `Jump_Backward`, `Landing_Recovery`.
  * Verify jump height (target: 3.5 meters) and jump duration (target: 42 frames).

---

## Phase 3: Collision, Hurtboxes & First Attack
- [ ] **Step 3.1: Configure Character Hurtboxes**
  * Open UFE Character Editor -> `Hitbox Options`.
  * Generate Body Hurtboxes (Head, Torso, Legs, Feet) attached to Humanoid skeleton bones.
- [ ] **Step 3.2: Create First Normal Attack (`5LP` — Standing Light Punch)**
  * Open `UFE 2 -> Move Editor`. Create Move: `Zenthos_5LP.asset`.
  * Assign `Standing_Light_Punch` animation clip.
  * Set Frame Counts: Startup = 4f, Active = 3f, Recovery = 7f. Total = 14f.
  * Add Red Hitbox Cuboid on active frames attached to Right Fist bone.
  * Set Damage: 30, Hitstop: 4 frames, Pushback: 0.5m.
- [ ] **Step 3.3: Verify Hit Reaction & Hitstop**
  * Assign universal hit reaction clips (`Hitstun_High`, `Hitstun_Low`) to Zenthos Character Config.
  * Spawn Zenthos vs. Dummy Zenthos. Press `5LP`. Verify hitstop freezes both characters for 4 frames upon contact.

---

## Phase 4: Defensive Mechanics & Remaining Normals
- [ ] **Step 4.1: Configure Guard & Blocking**
  * Assign `Block_Standing`, `Block_Crouching`, `Blockstun` clips.
  * Set Guard Inputs in UFE Global Editor (Hold Back to Guard).
  * Test blocking `5LP`. Verify blue block-spark and pushback.
- [ ] **Step 4.2: Add Heavy Punch & Sweep Normals**
  * Create `5HP` (Standing Heavy Punch): Startup 9f, Active 4f, Recovery 16f. Hitstop: 10f.
  * Create `2HK` (Crouching Sweep): Startup 10f, Active 3f, Recovery 20f. Set Hit Effect: `Knockdown`.
  * Create `j.HP` (Jumping Heavy Punch): Set Attack Type: `Overhead`.
- [ ] **Step 4.3: Add Light Kick & Heavy Kick Normals**
  * Create `5LK` (Standing Light Kick), `5HK` (Standing Heavy Kick), `2LP` (Crouching Light Punch).

---

## Phase 5: Throws & Special Attacks
- [ ] **Step 5.1: Implement Universal Throw**
  * Create Move: `Zenthos_Throw.asset` in Move Editor. Set Move Type: `Throw`.
  * Assign `Throw_Attempt`, `Throw_Connect`, `Throw_Whiff`, `Being_Thrown` clips.
  * Set Throw Distance = 1.2m. Test close-range throw ignoring guard.
- [ ] **Step 5.2: Implement Cinder Wave Fireball (`236P`)**
  * Create Projectile Prefab: `CinderWave_Projectile.prefab` with low-poly sphere mesh & trail.
  * Create Move: `Zenthos_236P.asset` (`Move Type: Projectile`).
  * Assign `Fireball_Cast` animation clip. Set Startup = 13f, Active = 2f (spawns projectile), Recovery = 24f.
  * Configure Projectile Speed = 12.0 m/s. Test fireball traveling across stage.
- [ ] **Step 5.3: Implement Inferno Rising Anti-Air (`623P`)**
  * Create Move: `Zenthos_623P.asset`. Set Invincible Frames: 1–5.
  * Set Startup = 6f, Active = 6f, Recovery = 28f. Set Hit Effect: `Launch`.

---

## Phase 6: Stage Setup & Tuning Pass
- [ ] **Step 6.1: Import Ashfall Coliseum Stage**
  * Import arena floor 3D mesh (`ashfall_coliseum_floor.fbx`).
  * Create UFE Stage Config: `AshfallColiseum_StageConfig.asset`.
  * Set Left Boundary = -7.0m, Right Boundary = 7.0m.
- [ ] **Step 6.2: Combo & Cancel Tuning Pass**
  * Open UFE Move Editor -> Move Links.
  * Enable chain cancels: `5LP` -> `5HP` -> `236P`.
  * Test combo in engine. Verify combo counter displays 3 hits.
- [ ] **Step 6.3: Milestone 0 Verification Audit**
  * Verify 60.0 FPS performance.
  * Run Definition of Done checklist from `VERTICAL_SLICE.md`.
