# ⚔️ The Shattered Convergence — Official Game Design Repository

Welcome to the dedicated **Game Design Repository** for *The Shattered Convergence* (2.5D Fighting Game).

---

## 📚 Repository Overview & Structure

This repository houses all core game design documents, roster specifications, moveset frame data, stage visual guides, VFX/SFX audio profiles, and Speech-to-Speech vocal guides.

### 📂 Directory Map

```text
shattered-convergence-game-design/
 ├── GAME_DESIGN.md                      # Primary Game Design Document (Universal mechanics, frame data, lore)
 ├── SUBAGENT_ROSTER.md                  # Development team roles & subagent authority rules
 ├── .gemini_rules.md                    # Core Lead Game Designer directive rules
 └── characters/                         # Individual 8-Character Subdirectories
      ├── Zenthos/                       # Cinder Flame Prosecutor
      │    ├── CHARACTER_DESIGN.md       # Lore, moveset, frame data & Ashfall Coliseum home stage
      │    ├── VFX_SFX_SPEC.md           # Cinder fireball & 60Hz sub-bass audio specs
      │    ├── audio/                    # Speech-to-Speech (S2S) voice guide
      │    ├── sprites/                  # 3D-optimized T-pose concept sprite
      │    └── stages/                   # Ashfall Coliseum 8K 3D stage render
      ├── Melancholia/                   # Gothic Frost Sorceress & Glacial Sanctuary
      ├── Sylas/                         # Nordic Ice Druid / Direwolf & Yggdrasil's Heart
      ├── Brutus/                        # Tectonic Titan & Ironclad Foundry
      ├── Lyra/                          # Lightning Conduit & Zephyr Spire
      ├── Vesper/                        # Umbral Weaver & Eclipse Catacombs
      ├── Ignacia/                       # Scorching Talon & Brimstone Refinery
      └── Nereus/                        # Abyssal Mariner & Sunken Trench
```

---

## 🎮 Roster Matrix

| Character | Archetype | Unique Signature Mechanic | Home Fighting Stage |
| :--- | :--- | :--- | :--- |
| **Zenthos** | Cinder Flame All-Rounder | **Perfect Draw** (2f motion window for hard knockdowns) | **Ashfall Coliseum** |
| **Melancholia** | Gothic Frost Zoner | **Thorn Rush** (-10% HP cancel for +2f block advantage) | **Glacial Sanctuary** |
| **Sylas** | Druid / Wolf Shapeshifter | **Dual-Stance Shift** (Staff keepout <-> Wolf rushdown) | **Yggdrasil's Heart** |
| **Brutus** | Heavy Armor Grappler | **Tectonic Armor** (Upper-body armor buttons) | **The Ironclad Foundry** |
| **Lyra** | Lightning Speedster | **Volt Nodes** (Deploys conductive laser traps) | **Zephyr Spire Overlook** |
| **Vesper** | Umbral Puppet Master | **Solitude Puppet** (Dual-entity sandwich mixups) | **Eclipse Catacombs** |
| **Ignacia** | Flame Rekka Striker | **Blaze Rekka** (Branching overhead/low/combustion slashes) | **Brimstone Refinery** |
| **Nereus** | Aquatic Zoner | **Vortex Drag** (Gravitational water currents) | **The Sunken Trench** |

---

## 🔗 Related Repositories
- **3D Asset Pipeline**: [github.com/jimmyokusa/sprite-to-3d](https://github.com/jimmyokusa/sprite-to-3d)
