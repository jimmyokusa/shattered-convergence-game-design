# UFE 2 Engine Implementation Spec: Vesper

**Implementation Classification:** `Custom (Critical Rollback Risk)`

## 🛠️ Move & Mechanic Mapping

| Move / Mechanic | Type | Implementation Description |
| :--- | :--- | :--- |
| **Vesper Normals & Thread Attacks** | `Native` | Configured in UFE Move Editor. |
| **Solitude Puppet Entity Control** | `Custom` | Requires custom C# Dual-Entity Engine (`PuppetController.cs`). Tracks puppet position, state, and independent move inputs alongside main player inputs. Requires UFE Source Access. `[VERIFY]` |

---

## ⚠️ Rollback-Determinism Note

> CRITICAL ROLLBACK RISK: Controlling two independent actors simultaneously requires duplicating input simulation loops and state history buffers under GGPO rollback.
