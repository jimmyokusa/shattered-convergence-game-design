# UFE 2 Engine Implementation Spec: Sylas

**Implementation Classification:** `Custom (High Complexity)`

## 🛠️ Move & Mechanic Mapping

| Move / Mechanic | Type | Implementation Description |
| :--- | :--- | :--- |
| **Druid Staff Normals & Specials** | `Native` | Configured under Druid Stance move table in UFE Editor. |
| **Frost Wolf Normals & Specials** | `Native` | Configured under Wolf Stance move table in UFE Editor. |
| **Dual-Stance Transformation (Shapeshift)** | `Custom` | Requires custom C# Stance Manager (`SylasStanceManager.cs`) to swap Animator Controllers, character collision bounds, hitboxes, and UFE stance tables mid-match. `[VERIFY]` |

---

## ⚠️ Rollback-Determinism Note

> Mid-match character model and animator controller swapping introduces severe rollback risk if animation state timers get out of sync across frames.
