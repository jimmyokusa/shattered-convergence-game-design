import os
import json

ROSTER = [
    "Zenthos",
    "Melancholia",
    "Sylas",
    "Brutus",
    "Lyra",
    "Vesper",
    "Ignacia",
    "Nereus"
]

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
CHARACTERS_DIR = os.path.join(PROJECT_DIR, "characters")

VFX_SFX_SPECS = {
    "Zenthos": {
        "character": "Zenthos",
        "theme": "Cinder Flame & Volcanic Magma",
        "vfx": [
            {
                "name": "Cinder Wave (236P)",
                "type": "Projectile Fireball",
                "texture_atlas": "512x512 8-frame Additive flipbook",
                "particles": "2500 trailing cinder sparks/sec",
                "hdr_bloom": 4.5,
                "rgb_hex": "#FF6E0F",
                "point_light_radius": 4.2
            },
            {
                "name": "Inferno Rising (623P)",
                "type": "Anti-Air Flame Dragon Column",
                "texture_atlas": "1024x1024 vertical flame column atlas",
                "hdr_bloom": 6.0,
                "rgb_hex": "#FF4B00",
                "point_light_radius": 6.5
            },
            {
                "name": "Scorched Earth Shatter (Level 3 Super)",
                "type": "Fullscreen Volcanic Eruption",
                "texture_atlas": "2048x2048 magma crack decal atlas & screen shockwave",
                "hdr_bloom": 9.5,
                "rgb_hex": "#FF2D00",
                "point_light_radius": 12.5
            }
        ],
        "sfx": {
            "cast": "Heavy fire whoosh layered with igniting torch snap (800Hz boost)",
            "hit_impact": "Crisp explosive flame crunch + 60Hz sub-bass thud",
            "block_impact": "Muffled hiss + metallic guard chime",
            "whiff": "Rapid rushing hot wind sweep"
        }
    },
    "Melancholia": {
        "character": "Melancholia",
        "theme": "Sanguine Rime & Gothic Ice Needles",
        "vfx": [
            {
                "name": "Glacial Thrust (236P)",
                "type": "Ice Crystal Needle Lunge",
                "texture_atlas": "Polyhedral ice crystal 3D billboard mesh (180 polys)",
                "particles": "Diamond dust glint burst",
                "hdr_bloom": 5.0,
                "rgb_hex": "#78DCFF",
                "point_light_radius": 3.8
            },
            {
                "name": "Permafrost Barrier (214P)",
                "type": "Deployable Ice Shield",
                "texture_atlas": "Procedural ice wall mesh with refractive frosted glass",
                "hdr_bloom": 3.8,
                "rgb_hex": "#3CB4FF",
                "point_light_radius": 5.0
            },
            {
                "name": "Absolute Zero Execution (Level 3 Super)",
                "type": "Screen-wide Glacier Monolith Burst",
                "texture_atlas": "Massive 3D ice monolith meshes with blizzard vignette",
                "hdr_bloom": 8.8,
                "rgb_hex": "#00D2FF",
                "point_light_radius": 11.0
            }
        ],
        "sfx": {
            "cast": "High-pitch crystal chime + razor-sharp rapier unsheathe",
            "hit_impact": "Glass-shattering piercing crunch + freeze-frame audio stutter",
            "block_impact": "Solid ice impact chime + metallic blade ring",
            "whiff": "Whistling piercing sub-zero wind"
        }
    },
    "Sylas": {
        "character": "Sylas",
        "theme": "Sylvan Druid Frost-Rime & Direwolf Aura",
        "vfx": [
            {
                "name": "Rime Staff Sweep (236P)",
                "type": "Pine-Needle Frost Arc Sweep",
                "texture_atlas": "Arc blade trail with pine-needle micro-sprites",
                "hdr_bloom": 3.5,
                "rgb_hex": "#82D2B4",
                "point_light_radius": 4.0
            },
            {
                "name": "Feral Surge (236P Wolf)",
                "type": "Spectral Wolf Lunge & Dual Claw Slashes",
                "texture_atlas": "Spectral wolf head silhouette mesh + cyan claw slashes",
                "hdr_bloom": 5.2,
                "rgb_hex": "#46E6A0",
                "point_light_radius": 4.5
            },
            {
                "name": "Primal Convergence (Level 3 Super)",
                "type": "Direwolf Avatar & Forest Frost Explosion",
                "texture_atlas": "Ethereal direwolf aura projection + frost shockwave atlas",
                "hdr_bloom": 7.8,
                "rgb_hex": "#28F0C8",
                "point_light_radius": 10.0
            }
        ],
        "sfx": {
            "cast": "Wooden staff whoosh + crystalline frost rustle / Guttural wolf roar",
            "hit_impact": "Heavy wooden thud + ice crackle / Vicious claw rend",
            "block_impact": "Solid wooden block + frost scrape",
            "whiff": "Heavy staff air slice / Beastly lunging swipe"
        }
    },
    "Brutus": {
        "character": "Brutus",
        "theme": "Tectonic Earth & Magma Basalt Eruptions",
        "vfx": [
            {
                "name": "Tectonic Slam (22P)",
                "type": "Lava Ground Crack Eruption",
                "texture_atlas": "Emissive lava ground-crack decals & 3D basalt rocks",
                "hdr_bloom": 6.5,
                "rgb_hex": "#FF3C00",
                "point_light_radius": 5.5
            },
            {
                "name": "Cataclysmic Caldera (Level 3 Super)",
                "type": "Volcanic Magma Chamber Eruption",
                "texture_atlas": "2048x2048 lava chamber atlas + basalt fragment physics",
                "hdr_bloom": 10.0,
                "rgb_hex": "#FF1E00",
                "point_light_radius": 14.0
            }
        ],
        "sfx": {
            "cast": "Heavy fist slamming earth + seismic fault line tearing (40Hz sub-bass)",
            "hit_impact": "Bone-crushing ground slam + erupting magma explosion",
            "block_impact": "Earthshaking block thud + lava splash sizzle",
            "whiff": "Heavy stone impact without hitstop"
        }
    },
    "Lyra": {
        "character": "Lyra",
        "theme": "High-Voltage Electric Arcs & Plasma",
        "vfx": [
            {
                "name": "Volt Blade (236P)",
                "type": "Electric Arc Slashes & Anime Sparks",
                "texture_atlas": "Procedural electrical bolt arcs + cyan/violet hit-sparks",
                "hdr_bloom": 7.0,
                "rgb_hex": "#64B4FF",
                "point_light_radius": 4.0
            },
            {
                "name": "Maelstrom Tempest (Level 3 Super)",
                "type": "Vertical Thunderstorm Pillar",
                "texture_atlas": "Fullscreen vertical lightning column atlas + lens flare",
                "hdr_bloom": 9.5,
                "rgb_hex": "#8CC8FF",
                "point_light_radius": 13.0
            }
        ],
        "sfx": {
            "cast": "Sharp high-voltage spark zaps + plasma buzz (10kHz boost)",
            "hit_impact": "Electric shock crackle + conductive metal slice",
            "block_impact": "Electrical discharge fizzle + shield buzz",
            "whiff": "High-frequency air whip slice"
        }
    },
    "Vesper": {
        "character": "Vesper",
        "theme": "Umbral Void Threads & Dark Shadow Marionette",
        "vfx": [
            {
                "name": "Shadow Puppet Thread (236P)",
                "type": "Void-Purple String Ribbons & Obsidian Needles",
                "texture_atlas": "Glowing void-purple string ribbons + obsidian needles",
                "hdr_bloom": 4.8,
                "rgb_hex": "#B432F0",
                "point_light_radius": 3.2
            },
            {
                "name": "Eclipse Marionette (Level 3 Super)",
                "type": "Shadow Puppet Guillotine Blade Drop",
                "texture_atlas": "Colossal shadow puppet projection + void guillotine blade",
                "hdr_bloom": 8.8,
                "rgb_hex": "#D21EFF",
                "point_light_radius": 9.5
            }
        ],
        "sfx": {
            "cast": "Sinister silk thread snap + dark metallic twang",
            "hit_impact": "Needles stabbing shadow flesh + whispery void slice",
            "block_impact": "String plucking barrier ping",
            "whiff": "Subtle thread slicing air"
        }
    },
    "Ignacia": {
        "character": "Ignacia",
        "theme": "Crimson Pyro Claws & Combustion Back-Blast",
        "vfx": [
            {
                "name": "Pyro Claw Scratch (236P)",
                "type": "Triple Crimson Friction Slash",
                "texture_atlas": "3-lane curved claw slash sprites + friction sparks",
                "hdr_bloom": 5.5,
                "rgb_hex": "#FF1E3C",
                "point_light_radius": 3.6
            },
            {
                "name": "Infernal Cataclysm (Level 3 Super)",
                "type": "Superheated Napalm Flame Pillar",
                "texture_atlas": "Dense crimson napalm flame pillar atlas + ground fire",
                "hdr_bloom": 9.2,
                "rgb_hex": "#FF0A1E",
                "point_light_radius": 11.5
            }
        ],
        "sfx": {
            "cast": "Match-strike friction ignition + claw unsheathe",
            "hit_impact": "Searing triple slash tear + burning flesh sizzle",
            "block_impact": "Metal claw grinding against guard",
            "whiff": "Sharp crimson fire whip swipe"
        }
    },
    "Nereus": {
        "character": "Nereus",
        "theme": "Hydrodynamic Water Vortices & Tsunami Columns",
        "vfx": [
            {
                "name": "Tidal Column (22P)",
                "type": "Pressurized Water Geyser Column",
                "texture_atlas": "Cylinder fluid simulation mesh + water refraction decal",
                "hdr_bloom": 4.0,
                "rgb_hex": "#1EA0FF",
                "point_light_radius": 5.0
            },
            {
                "name": "Abyssal Deluge (Level 3 Super)",
                "type": "Tsunami Wave Crash & Bioluminescent Foam",
                "texture_atlas": "Fullscreen tidal wave mesh + glowing sea-foam overlay",
                "hdr_bloom": 7.5,
                "rgb_hex": "#00F0FF",
                "point_light_radius": 12.5
            }
        ],
        "sfx": {
            "cast": "High-pressure geyser eruption + deep oceanic rush",
            "hit_impact": "Heavy hydraulic water blast thud",
            "block_impact": "Hydrostatic pressure buffeting shield",
            "whiff": "Ocean wave crest splashing"
        }
    }
}

def store_vfx_sfx():
    print("--- Storing 8-Character VFX & SFX Specifications ---")
    for char, data in VFX_SFX_SPECS.items():
        vfx_dir = os.path.join(CHARACTERS_DIR, char, "vfx")
        sfx_dir = os.path.join(CHARACTERS_DIR, char, "sfx")
        os.makedirs(vfx_dir, exist_ok=True)
        os.makedirs(sfx_dir, exist_ok=True)
        
        # Save JSON spec
        spec_path = os.path.join(CHARACTERS_DIR, char, "VFX_SFX_SPEC.json")
        with open(spec_path, "w") as f:
            json.dump(data, f, indent=2)
            
        # Save Markdown spec
        md_path = os.path.join(CHARACTERS_DIR, char, "VFX_SFX_SPEC.md")
        with open(md_path, "w") as f:
            f.write(f"# Visual FX (VFX) & Audio FX (SFX) Specification: {char}\n\n")
            f.write(f"**Elemental Theme**: {data['theme']}\n\n")
            f.write("## 💥 Visual Effects (VFX) Elements\n\n")
            for move in data["vfx"]:
                f.write(f"### {move['name']}\n")
                f.write(f"- **Type**: {move['type']}\n")
                f.write(f"- **Texture Atlas / Mesh**: {move['texture_atlas']}\n")
                f.write(f"- **HDR Bloom Multiplier**: `{move['hdr_bloom']}x`\n")
                f.write(f"- **RGB Color**: `{move['rgb_hex']}`\n")
                f.write(f"- **Point Light Radius**: `{move['point_light_radius']}m`\n\n")
                
            f.write("## 🔊 Sound Effects (SFX) Audio Profile\n\n")
            f.write(f"- **Cast / Startup Sound**: {data['sfx']['cast']}\n")
            f.write(f"- **Hit Impact Sound**: {data['sfx']['hit_impact']}\n")
            f.write(f"- **Block Impact Sound**: {data['sfx']['block_impact']}\n")
            f.write(f"- **Whiff Sound**: {data['sfx']['whiff']}\n")
            
        print(f"✅ Stored VFX & SFX specifications for [{char}] -> {CHARACTERS_DIR}/{char}/")

if __name__ == "__main__":
    store_vfx_sfx()
