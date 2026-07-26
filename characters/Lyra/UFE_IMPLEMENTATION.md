# UFE 2 Engine Implementation Spec: Lyra

**Implementation Classification:** `Custom (Rollback Risk)`

## 🛠️ Move & Mechanic Mapping

| Move / Mechanic | Type | Implementation Description |
| :--- | :--- | :--- |
| **Arc Blade Normals & Volt Blade (236P)** | `Native` | Configured in UFE Move Editor. |
| **Thunder Step Teleport (623K)** | `Configured` | Configured in UFE Move Editor using Teleport options. |
| **Deployable Volt Nodes & Intersecting Beams** | `Custom` | Requires custom C# Node Manager (`LyraNodeManager.cs`) to track persistent world positions of up to 3 deployed nodes and calculate raycast laser intersections. `[VERIFY]` |

---

## ⚠️ Rollback-Determinism Note

> HIGH ROLLBACK RISK: Persistent world trap nodes must be registered in UFE's rollback object state pool. If node positions are stored in standard Unity MonoBehaviours, network re-simulation will cause desyncs.
