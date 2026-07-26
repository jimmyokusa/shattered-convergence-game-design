# UFE 2 Engine Implementation Spec: Nereus

**Implementation Classification:** `Native & Configured`

## 🛠️ Move & Mechanic Mapping

| Move / Mechanic | Type | Implementation Description |
| :--- | :--- | :--- |
| **Trident Normals & Tidal Column (22P)** | `Native` | Configured in UFE Move Editor. |
| **Vortex Drag Gravity Pull** | `Configured` | Configured in UFE Move Editor by applying continuous opponent pull force (`Opponent Push/Pull Force`) during active move frames. `[VERIFY]` |

---

## ⚠️ Rollback-Determinism Note

> Low/Moderate rollback risk. Opponent force vectors are tracked in UFE frame state.
