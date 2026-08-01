# 🏟️ Real-Time Stage Performance Budget

> **ROLLBACK PERFORMANCE DIRECTIVE:** In fighting games utilizing rollback netcode (GGPO / UFE Rollback), the engine frequently re-simulates **2 to 4 execution frames per single displayed frame** during network latency spikes. Stage environments must be aggressively optimized to leave maximum CPU/GPU headroom for deterministic physics and state re-simulations.

---

## 📊 Technical Performance Budget (Target: 60.0 FPS Locked)

| Performance Parameter | Real-Time Limit (Per Stage) | Legacy Concept Spec (Downgraded) |
| :--- | :--- | :--- |
| **Total Geometry (Triangle Count)** | **≤ 85,000 Triangles** (Total Arena + BG) | Uncapped High-Poly Render |
| **Active Draw Calls (Batched)** | **≤ 65 Draw Calls** | Uncapped |
| **Maximum Texture Resolution** | **2048×2048 (Main) / 1024×1024 (BG)** | 8192×8192 (8K) Renders |
| **Total VRAM Texture Budget** | **≤ 256 MB** | Uncapped |
| **Active Dynamic Lights** | **Max 2 Real-time Point Lights** (Rest Baked) | Dynamic Per-Particle Lights |
| **Particle System Active Count** | **≤ 350 Particles Total** | 2,500+ Particles/sec |

---

## 🎨 Asset Downgrade Justification

1. **8K Renders vs. Real-Time Fighting Game Canvas:**
   * 8192×8192 (8K) textures consume **256 MB VRAM per uncompressed texture**. In a 2.5D fighting game where the camera is zoomed out to fit two 14-meter stage boundaries, 8K detail is completely imperceptible to the player and wastes GPU memory bandwidth.
   * All stage environment textures are standardized to **2048×2048** with compressed ASTC/BC3 texture formats.

2. **Rollback CPU/GPU Re-simulation Headroom:**
   * When GGPO/UFE detects a 3-frame network rollback, it executes 3 full game loops (inputs, physics, collision detection, particle ticks) within a single 16.6ms display frame window.
   * If stage background shaders or high-poly meshes consume >8ms of GPU frame time, rollback re-simulation will cause severe frame drops and input stutter.

3. **Background Mesh & Draw Call Batching:**
   * Background scenery (statues, rocks, trees, buildings) must be merged into static batched meshes (`StaticBatchingUtility`) to minimize draw calls.
   * Distant background elements must use low-poly billboard planes with alpha textures rather than full 3D geometry.
