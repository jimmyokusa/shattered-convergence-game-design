# UFE 2 Engine Implementation Spec: Zenthos

**Implementation Classification:** `Native & Configured`

## 🛠️ Move & Mechanic Mapping

| Move / Mechanic | Type | Implementation Description |
| :--- | :--- | :--- |
| **Normals (5LP, 5HP, 5LK, 5HK, 2LP, 2HK, j.HP)** | `Native` | Configurable entirely in UFE Move Editor. Hitboxes, hurtboxes, frames, and damage values set in visual inspector. |
| **Cinder Wave (236P)** | `Native` | Configured as a standard projectile move in UFE Move Editor (`Move Type: Projectile`). Spawns prefab fireball object. |
| **Inferno Rising (623P)** | `Native` | Configured as anti-air move with invincibility frames (`Invincible Frames: 1-5`) in UFE Move Editor. |
| **Ember Step (214K)** | `Native` | Configured as special dash move (`Move Type: Dash / Special`) with forward velocity. |
| **Perfect Draw (2f Motion Window)** | `Configured` | Configured in UFE Input Manager by setting strict motion sequence timing window (2 frames / 33 ms). `[VERIFY]` |
| **Scorched Earth Shatter (Level 3 Super)** | `Native` | Configured as Super Move spending 3 Gauge bars in UFE Move Editor, spawning full-screen cinematic camera. |

---

## ⚠️ Rollback-Determinism Note

> Zenthos uses purely deterministic native UFE state data. Low rollback risk.
