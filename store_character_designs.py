"""Generate per-character design specs (JSON + Markdown) for the full roster."""

import json
import os
import sys
from typing import TypedDict

# Generated docs and console output contain emoji; Windows defaults to cp1252,
# which cannot encode them. sys.stdout is typed as the broader TextIO, which
# does not expose reconfigure().
sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[union-attr]


class HomeStage(TypedDict):
    """A character's home fighting stage."""

    name: str
    setting: str
    visuals: str
    bgm_style: str


class Design(TypedDict):
    """A character's full design specification."""

    name: str
    epithet: str
    archetype: str
    lore: str
    appearance: str
    unique_mechanic: str
    home_stage: HomeStage


PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
CHARACTERS_DIR = os.path.join(PROJECT_DIR, "characters")

DESIGNS: dict[str, Design] = {
    "Zenthos": {
        "name": "Zenthos",
        "epithet": "Prosecutor of the Cinder Flame",
        "archetype": "Cinder Flame All-Rounder / Strike-Throw",
        "lore": "A dogmatic warrior-monk bound to an involuntary curse: his blade manifests black-and-white ethereal flames. He seeks to purge or control the flame before it consumes his soul.",
        "appearance": "Nordic spellblade wearing black inquisitor robes, white scarf, black leather gauntlets with silver rings. Carries a black flame sword.",
        "unique_mechanic": "Perfect Draw (2-frame motion input window unlocks hard knockdowns, launchers, and ground bounces).",
        "home_stage": {
            "name": "Ashfall Coliseum",
            "setting": "Ancient obsidian arena carved into the crater rim of Mt. Ignis over cascading magma rivers.",
            "visuals": "Obsidian stone platform, warrior-monk statues, glowing braziers, smoke particles.",
            "bgm_style": "Hard Rock / Heavy Metal with blazing electric guitar leads.",
        },
    },
    "Melancholia": {
        "name": "Melancholia",
        "epithet": "Empress of the Sanguine Rime",
        "archetype": "Gothic Frost Sorceress / Cancel-Rushdown",
        "lore": "High ruler of the Eternal Rime. Her frosted silver rapier controls absolute zero temperatures, using living blood as a catalyst to project deadly thorn-ice.",
        "appearance": "Dark gothic frost sorceress in silver and navy silk gown, carrying a frosted silver rapier with crimson crystal accents.",
        "unique_mechanic": "Thorn Rush (Cancels any grounded normal into Thorn Rush for +2 block / +5 hit advantage at the cost of 10% HP, with 50% Grey Health recovery).",
        "home_stage": {
            "name": "Glacial Sanctuary of Frozen Tears",
            "setting": "Gothic cathedral constructed of crystalline eternal ice under an aurora borealis.",
            "visuals": "Vaulted ice arches, frosted ice-stained glass windows, ice-marble floor, falling snow.",
            "bgm_style": "Neoclassical Orchestral Metal with solo violin arpeggios and harpsichord.",
        },
    },
    "Sylas": {
        "name": "Sylas",
        "epithet": "The Sylvan Ice Druid",
        "archetype": "Dual-Stance Transformation Zoner / Rushdown",
        "lore": "A Nordic druid who guards the border between the Sylvan Wilds and the Eternal Rime. Uses nature magic in human form, but transforms into a bipedal Dire Frost Wolf.",
        "appearance": "Druid Form: Nordic leather/fur armor with glowing green vine runes, wolf-pelt cloak, carved oak rime-crystal staff. Wolf Form: Upright bipedal dire wolf with cyan fur and ice armor plates.",
        "unique_mechanic": "Dual-Stance Transformation (Druid Staff long-range keepout <-> Bipedal Frost Wolf fast claw rushdown).",
        "home_stage": {
            "name": "Yggdrasil's Heart (The Ancient Grove)",
            "setting": "Sacred hollow deep within the root canopy of the World Tree.",
            "visuals": "Twisted mossy tree roots, bioluminescent flora, rune stones, floating spirit spores.",
            "bgm_style": "Ethnic Folk-Fusion with Celtic tribal drums, bamboo flutes, and funk bass.",
        },
    },
    "Brutus": {
        "name": "Brutus",
        "epithet": "The Tectonic Titan",
        "archetype": "Heavy Grappler / Armor Titan (1100 HP)",
        "lore": "Forged from living granite and obsidian in magma chambers beneath the Shattered Peaks to anchor the realm back into stone.",
        "appearance": "7'8\" stone juggernaut with obsidian armor plates and glowing magma veins radiating through his stone chest.",
        "unique_mechanic": "Tectonic Armor (Upper-body armor on heavy buttons) & Seismic Slam unblockable command throw.",
        "home_stage": {
            "name": "The Ironclad Foundry & Pit",
            "setting": "Underground steelworks and underground brawl pit beneath active crucibles.",
            "visuals": "Industrial steel cage, iron chains, steam pressure vents, tipped molten metal ladles.",
            "bgm_style": "Industrial Electro-Metal with heavy anvil percussion and chugging bass.",
        },
    },
    "Lyra": {
        "name": "Lyra",
        "epithet": "The Lightning Conduit",
        "archetype": "Dynamic Trapper / Spatial Lockdown (950 HP)",
        "lore": "An atmospheric scholar who harnesses electrical friction generated by the Shattered Convergence using twin galvanic conductors.",
        "appearance": "Agile fighter in insulated navy leather with brass conduit rings and twin electrified batons.",
        "unique_mechanic": "Volt Nodes (Deploys static electricity nodes) & Conductive Arc (Connects shock beams between nodes for +8f block advantage).",
        "home_stage": {
            "name": "Zephyr Spire Overlook",
            "setting": "Open skyward marble balcony of a floating mountain citadel.",
            "visuals": "Ivory balustrades, fluttering wind banners, soaring airships in sunset clouds.",
            "bgm_style": "High-BPM Eurobeat / Pop-Fusion with energetic brass and soaring synth leads.",
        },
    },
    "Vesper": {
        "name": "Vesper",
        "epithet": "The Umbral Weaver",
        "archetype": "Puppet Master / Dual-Entity Offense (900 HP)",
        "lore": "Banishment into the Void Realm severed Vesper's shadow, birthing Solitude—a semi-autonomous husk of dark matter bound to her soul string.",
        "appearance": "Gothic veiled sorceress in raven-black silks with silver thread loops and her shadow puppet Solitude.",
        "unique_mechanic": "Solitude Puppet Commands (Controls independent shadow puppet for pincher sandwich mixups).",
        "home_stage": {
            "name": "Eclipse Citadel Catacombs",
            "setting": "Forgotten umbral temple beneath a gothic city where void rifts bleed through.",
            "visuals": "Obsidian stone altars, floating void crystals, swirling dark shadow tendrils.",
            "bgm_style": "Cyberpunk Darkwave / Synthwave with deep sub-bass and gothic vocal chops.",
        },
    },
    "Ignacia": {
        "name": "Ignacia",
        "epithet": "The Scorching Talon",
        "archetype": "Pure Rushdown / Rekka Striker (890 HP)",
        "lore": "Warlord champion of the Pyre Clan in the Cinder Wastes, wielding wild bladed claw flame arts.",
        "appearance": "Fierce female warrior in feather-patterned crimson armor with ash face paint and bladed fire gauntlets.",
        "unique_mechanic": "Blaze Rekka (Multi-stage advancing slash series branching into overhead, low sweep, or ignition explosion) & Ember Dash.",
        "home_stage": {
            "name": "Brimstone Refinery Rig",
            "setting": "Offshore geothermal energy rig built over a volcanic ocean ridge.",
            "visuals": "Catwalks, high-pressure flame stacks, oil derricks, ocean spray on lower beams.",
            "bgm_style": "Explosive Funk Metal / Breakbeat hybrid with brass stabs and distorted guitar riffs.",
        },
    },
    "Nereus": {
        "name": "Nereus",
        "epithet": "The Abyssal Mariner",
        "archetype": "Spatial Zoner & Fluid Displacer (1000 HP)",
        "lore": "Admiral of the submerged Void Fleet who commands pressurized depth currents and an ancestral Hydro-Trident.",
        "appearance": "Weathered captain clad in deep navy trench coat with coral-encrusted brass armor and aquamarine eyes.",
        "unique_mechanic": "Vortex Drag (Gravitational water current that pulls or pushes opponent) & Tidal Wave projectiles.",
        "home_stage": {
            "name": "The Sunken Trench of Atlantis",
            "setting": "Ancient underwater dome sanctuary situated on the abyssal ocean floor.",
            "visuals": "Greek marble columns, bioluminescent glass dome, sea leviathans gliding in dark ocean.",
            "bgm_style": "Ambient Techno / Progressive House with smooth synth pads and driving 4-on-the-floor rhythm.",
        },
    },
}


def store_designs() -> None:
    """Write CHARACTER_DESIGN.json and CHARACTER_DESIGN.md for every character."""
    print("--- Storing Individual Character & Stage Specifications ---")
    for char, data in DESIGNS.items():
        char_dir = os.path.join(CHARACTERS_DIR, char)
        os.makedirs(char_dir, exist_ok=True)

        # Save JSON spec file
        spec_path = os.path.join(char_dir, "CHARACTER_DESIGN.json")
        with open(spec_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

        # Save Markdown spec file inside character folder
        md_path = os.path.join(char_dir, "CHARACTER_DESIGN.md")
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(f"# Character Specification: {data['name']} — {data['epithet']}\n\n")
            f.write(f"**Archetype**: {data['archetype']}\n\n")
            f.write(f"### 📖 Lore & Faction\n{data['lore']}\n\n")
            f.write(f"### 🎨 Appearance & Aesthetic\n{data['appearance']}\n\n")
            f.write(f"### ⚔️ Unique Signature Mechanic\n{data['unique_mechanic']}\n\n")
            f.write("### 🏟️ Home Fighting Stage\n")
            f.write(f"- **Stage Name**: {data['home_stage']['name']}\n")
            f.write(f"- **Setting**: {data['home_stage']['setting']}\n")
            f.write(f"- **Visuals**: {data['home_stage']['visuals']}\n")
            f.write(f"- **BGM Style**: {data['home_stage']['bgm_style']}\n")

        print(f"✅ Stored design specifications for [{char}] -> {char_dir}")


if __name__ == "__main__":
    store_designs()
