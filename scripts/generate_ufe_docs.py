"""Generate UFE 2 engine implementation specs for the full roster."""

import os
from typing import TypedDict


class UfeSpec(TypedDict):
    """A character's UFE 2 implementation classification and move mapping."""

    classification: str
    # (move or mechanic name, implementation type, description)
    moves: list[tuple[str, str, str]]
    rollback_note: str


# This script lives in scripts/; the repo root is one level up.
REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHAR_DIR = os.path.join(REPO_DIR, "characters")

UFE_SPECS: dict[str, UfeSpec] = {
    "Zenthos": {
        "classification": "Native & Configured",
        "moves": [
            (
                "Normals (5LP, 5HP, 5LK, 5HK, 2LP, 2HK, j.HP)",
                "Native",
                "Configurable entirely in UFE Move Editor. Hitboxes, hurtboxes, frames, and damage values set in visual inspector.",
            ),
            (
                "Cinder Wave (236P)",
                "Native",
                "Configured as a standard projectile move in UFE Move Editor (`Move Type: Projectile`). Spawns prefab fireball object.",
            ),
            (
                "Inferno Rising (623P)",
                "Native",
                "Configured as anti-air move with invincibility frames (`Invincible Frames: 1-5`) in UFE Move Editor.",
            ),
            (
                "Ember Step (214K)",
                "Native",
                "Configured as special dash move (`Move Type: Dash / Special`) with forward velocity.",
            ),
            (
                "Perfect Draw (2f Motion Window)",
                "Configured",
                "Configured in UFE Input Manager by setting strict motion sequence timing window (2 frames / 33 ms). `[VERIFY]`",
            ),
            (
                "Scorched Earth Shatter (Level 3 Super)",
                "Native",
                "Configured as Super Move spending 3 Gauge bars in UFE Move Editor, spawning full-screen cinematic camera.",
            ),
        ],
        "rollback_note": "Zenthos uses purely deterministic native UFE state data. Low rollback risk.",
    },
    "Melancholia": {
        "classification": "Native & Custom",
        "moves": [
            (
                "Rapier Normals & Glacial Thrust (236P)",
                "Native",
                "Configurable in UFE Move Editor.",
            ),
            (
                "Permafrost Barrier (214P)",
                "Native",
                "Configured as counter / shield move (`Move Type: Counter / Parry`) in UFE Editor.",
            ),
            (
                "Thorn Rush Self-Damage Cancel",
                "Custom",
                "Requires custom C# script (`ThornRushCancel.cs`) listening to UFE move execution events to deduct 10% HP from attacker and grant 50% Grey Health. `[VERIFY]`",
            ),
        ],
        "rollback_note": "Custom self-damage scripts must mutate UFE character state variables inside UFE's deterministic game loop to prevent netcode state desyncs.",
    },
    "Sylas": {
        "classification": "Custom (High Complexity)",
        "moves": [
            (
                "Druid Staff Normals & Specials",
                "Native",
                "Configured under Druid Stance move table in UFE Editor.",
            ),
            (
                "Frost Wolf Normals & Specials",
                "Native",
                "Configured under Wolf Stance move table in UFE Editor.",
            ),
            (
                "Dual-Stance Transformation (Shapeshift)",
                "Custom",
                "Requires custom C# Stance Manager (`SylasStanceManager.cs`) to swap Animator Controllers, character collision bounds, hitboxes, and UFE stance tables mid-match. `[VERIFY]`",
            ),
        ],
        "rollback_note": "Mid-match character model and animator controller swapping introduces severe rollback risk if animation state timers get out of sync across frames.",
    },
    "Brutus": {
        "classification": "Native",
        "moves": [
            ("Granite Normals & Tectonic Slam (22P)", "Native", "Configured in UFE Move Editor."),
            (
                "Super Armor Hits (Tectonic Armor)",
                "Native",
                "Configured using UFE Move Editor `Armor Options` (setting armor hits = 1 or 2). `[VERIFY]`",
            ),
            (
                "Caldera Press (63214P Command Grab)",
                "Native",
                "Configured in UFE Move Editor (`Move Type: Throw / Grapple`).",
            ),
        ],
        "rollback_note": "Low rollback risk. All armor counters and throw states are handled natively by UFE.",
    },
    "Lyra": {
        "classification": "Custom (Rollback Risk)",
        "moves": [
            ("Arc Blade Normals & Volt Blade (236P)", "Native", "Configured in UFE Move Editor."),
            (
                "Thunder Step Teleport (623K)",
                "Configured",
                "Configured in UFE Move Editor using Teleport options.",
            ),
            (
                "Deployable Volt Nodes & Intersecting Beams",
                "Custom",
                "Requires custom C# Node Manager (`LyraNodeManager.cs`) to track persistent world positions of up to 3 deployed nodes and calculate raycast laser intersections. `[VERIFY]`",
            ),
        ],
        "rollback_note": "HIGH ROLLBACK RISK: Persistent world trap nodes must be registered in UFE's rollback object state pool. If node positions are stored in standard Unity MonoBehaviours, network re-simulation will cause desyncs.",
    },
    "Vesper": {
        "classification": "Custom (Critical Rollback Risk)",
        "moves": [
            ("Vesper Normals & Thread Attacks", "Native", "Configured in UFE Move Editor."),
            (
                "Solitude Puppet Entity Control",
                "Custom",
                "Requires custom C# Dual-Entity Engine (`PuppetController.cs`). Tracks puppet position, state, and independent move inputs alongside main player inputs. Requires UFE Source Access. `[VERIFY]`",
            ),
        ],
        "rollback_note": "CRITICAL ROLLBACK RISK: Controlling two independent actors simultaneously requires duplicating input simulation loops and state history buffers under GGPO rollback.",
    },
    "Ignacia": {
        "classification": "Native & Configured",
        "moves": [
            (
                "Claw Normals & Blazing Somersault (623K)",
                "Native",
                "Configured in UFE Move Editor.",
            ),
            (
                "Blaze Rekka Multi-Stage Branching (236P)",
                "Configured",
                "Configured using UFE Move Link / Chain inputs (linking 236P -> 236P -> 236P). `[VERIFY]`",
            ),
        ],
        "rollback_note": "Low rollback risk. Rekka branches are native UFE chain links.",
    },
    "Nereus": {
        "classification": "Native & Configured",
        "moves": [
            ("Trident Normals & Tidal Column (22P)", "Native", "Configured in UFE Move Editor."),
            (
                "Vortex Drag Gravity Pull",
                "Configured",
                "Configured in UFE Move Editor by applying continuous opponent pull force (`Opponent Push/Pull Force`) during active move frames. `[VERIFY]`",
            ),
        ],
        "rollback_note": "Low/Moderate rollback risk. Opponent force vectors are tracked in UFE frame state.",
    },
}


def generate_ufe_docs() -> None:
    """Write UFE_IMPLEMENTATION.md into each character's directory."""
    print("--- Generating UFE 2 Implementation Specifications ---")
    for char, data in UFE_SPECS.items():
        char_dir = os.path.join(CHAR_DIR, char)
        os.makedirs(char_dir, exist_ok=True)

        c_path = os.path.join(char_dir, "UFE_IMPLEMENTATION.md")
        with open(c_path, "w", encoding="utf-8") as f:
            f.write(f"# UFE 2 Engine Implementation Spec: {char}\n\n")
            f.write(f"**Implementation Classification:** `{data['classification']}`\n\n")
            f.write("## 🛠️ Move & Mechanic Mapping\n\n")
            f.write("| Move / Mechanic | Type | Implementation Description |\n")
            f.write("| :--- | :--- | :--- |\n")
            for name, mtype, desc in data["moves"]:
                f.write(f"| **{name}** | `{mtype}` | {desc} |\n")

            f.write("\n---\n\n")
            f.write("## ⚠️ Rollback-Determinism Note\n\n")
            f.write(f"> {data['rollback_note']}\n")

        print(f"Generated UFE_IMPLEMENTATION.md for {char}")


if __name__ == "__main__":
    generate_ufe_docs()
