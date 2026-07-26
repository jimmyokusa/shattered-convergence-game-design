# UFE 2 Engine Implementation Spec: Brutus

**Implementation Classification:** `Native`

## 🛠️ Move & Mechanic Mapping

| Move / Mechanic | Type | Implementation Description |
| :--- | :--- | :--- |
| **Granite Normals & Tectonic Slam (22P)** | `Native` | Configured in UFE Move Editor. |
| **Super Armor Hits (Tectonic Armor)** | `Native` | Configured using UFE Move Editor `Armor Options` (setting armor hits = 1 or 2). `[VERIFY]` |
| **Caldera Press (63214P Command Grab)** | `Native` | Configured in UFE Move Editor (`Move Type: Throw / Grapple`). |

---

## ⚠️ Rollback-Determinism Note

> Low rollback risk. All armor counters and throw states are handled natively by UFE.
