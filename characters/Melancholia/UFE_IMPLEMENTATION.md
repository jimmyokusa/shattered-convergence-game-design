# UFE 2 Engine Implementation Spec: Melancholia

**Implementation Classification:** `Native & Custom`

## 🛠️ Move & Mechanic Mapping

| Move / Mechanic | Type | Implementation Description |
| :--- | :--- | :--- |
| **Rapier Normals & Glacial Thrust (236P)** | `Native` | Configurable in UFE Move Editor. |
| **Permafrost Barrier (214P)** | `Native` | Configured as counter / shield move (`Move Type: Counter / Parry`) in UFE Editor. |
| **Thorn Rush Self-Damage Cancel** | `Custom` | Requires custom C# script (`ThornRushCancel.cs`) listening to UFE move execution events to deduct 10% HP from attacker and grant 50% Grey Health. `[VERIFY]` |

---

## ⚠️ Rollback-Determinism Note

> Custom self-damage scripts must mutate UFE character state variables inside UFE's deterministic game loop to prevent netcode state desyncs.
