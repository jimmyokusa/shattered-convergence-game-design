"""Generate Speech-to-Speech vocal performance guides for the full roster."""

import os
import sys
from typing import TypedDict

# Generated docs and console output contain emoji; Windows defaults to cp1252,
# which cannot encode them. sys.stdout is typed as the broader TextIO, which
# does not expose reconfigure().
sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[union-attr]


class VoiceLine(TypedDict):
    """A single scripted line with its vocal direction."""

    type: str
    text: str
    performance_tip: str


class VoiceGuide(TypedDict):
    """A character's vocal persona and full set of scripted lines."""

    voice_type: str
    inflection_notes: str
    lines: list[VoiceLine]


ROSTER = ["Zenthos", "Melancholia", "Sylas", "Brutus", "Lyra", "Vesper", "Ignacia", "Nereus"]

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
CHARACTERS_DIR = os.path.join(PROJECT_DIR, "characters")

S2S_GUIDES: dict[str, VoiceGuide] = {
    "Zenthos": {
        "voice_type": "Deep stern Victorian British / Aristocratic Judge accent",
        "inflection_notes": "Authoritative, commanding, menacing yet restrained. Project from the chest.",
        "lines": [
            {
                "type": "intro",
                "text": "[shouts] I am Zenthos! The black flames of my blade... SHALL CONSUME ALL WHO BREACH THE COURT!",
                "performance_tip": "Start steady and regal on 'I am Zenthos', pause 1 sec at 'blade...', then explode into a booming yell on 'SHALL CONSUME ALL'.",
            },
            {
                "type": "victory",
                "text": "The verdict is rendered... [sighs] Your ashes belong to the cinder.",
                "performance_tip": "Deliver with cold finality. Exhale heavily on [sighs].",
            },
            {
                "type": "super3",
                "text": "[shouts] KNEEL BEFORE THE FLAME! Inescapable Frenzy—EXTERMINATE!",
                "performance_tip": "Maximum vocal strain on 'EXTERMINATE'. Push pitch high on the strike impact.",
            },
        ],
    },
    "Melancholia": {
        "voice_type": "Cold aristocratic Eastern European / Gothic Sorceress accent",
        "inflection_notes": "Seductive, sinister, elegant, unfeeling.",
        "lines": [
            {
                "type": "intro",
                "text": "[whispers] Feel the bite of absolute zero... [laughs] HAHAHA! Your blood belongs to the rime!",
                "performance_tip": "Whisper close to mic, transition into a melodramatic gothic laugh.",
            },
            {
                "type": "victory",
                "text": "[scoffs] Heh... Magnificent. Another frozen corpse to adorn my gothic spire.",
                "performance_tip": "Quiet scoff, haughty tone, slow deliberate cadence.",
            },
            {
                "type": "super3",
                "text": "[shouts] Flesh to ice! Blood to rime! Crown of Thorns—PERISH!",
                "performance_tip": "Piercing soprano scream on 'PERISH'.",
            },
        ],
    },
    "Sylas": {
        "voice_type": "Scottish / Celtic highland Druid accent",
        "inflection_notes": "Gritty, ancient, primal, rolling 'r's.",
        "lines": [
            {
                "type": "intro",
                "text": "Och... the ancient roots awaken! [shouts] AND THE FROST WOLF HUNGERS FOR YER SOUL!",
                "performance_tip": "Heavy Scottish 'Och', growl into the wolf transformation call.",
            },
            {
                "type": "victory",
                "text": "[sighs] Grrr... The pack claims this glen! Nature leaves nae trace of the weak!",
                "performance_tip": "Low guttural growl mixed into vocal breath.",
            },
            {
                "type": "super3",
                "text": "[shouts] AWOOOOO! Glacial Awakening! BREAK... SHATTER... RIP THEM TO SHREDS!",
                "performance_tip": "Full dire wolf howl into explosive vocal tearing on 'RIP THEM TO SHREDS'.",
            },
        ],
    },
    "Brutus": {
        "voice_type": "Deep booming Norse / Earth-Titan voice",
        "inflection_notes": "Heavy bass resonance, slow giant tempo.",
        "lines": [
            {
                "type": "intro",
                "text": "Stone stands eternal! [shouts] YOU WILL CRUMBLE AGAINST THE MOUNTAIN!",
                "performance_tip": "Deep chest resonance, heavy reverberating roar.",
            },
            {
                "type": "victory",
                "text": "[sighs] Hmmm... Dust to dust. The earth reclaims all.",
                "performance_tip": "Low rumble groan.",
            },
            {
                "type": "super3",
                "text": "[groans] ARRGH! TECTONIC CRUSH! Fall before the realm!",
                "performance_tip": "Heavy physical strain grunt into a titan shout.",
            },
        ],
    },
    "Lyra": {
        "voice_type": "Energetic Australian / Brit-pop storm punk accent",
        "inflection_notes": "Fast-paced, spunky, playful, high energy.",
        "lines": [
            {
                "type": "intro",
                "text": "Sparking up, mate! [giggles] Let us see if your reflexes can match lightning!",
                "performance_tip": "Rapid Australian cadence with a cheeky chuckle.",
            },
            {
                "type": "victory",
                "text": "[laughs] Haha! Overcharged and outclassed! Better luck next voltage!",
                "performance_tip": "Bouncy triumph laugh.",
            },
            {
                "type": "super3",
                "text": "[shouts] MAX CAPACITY! Conductive Arc—DISCHARGE!",
                "performance_tip": "High pitch electric shout.",
            },
        ],
    },
    "Vesper": {
        "voice_type": "Soft whispered French / Velvet gothic mystery tone",
        "inflection_notes": "Intimate whisper, mysterious, dark elegance.",
        "lines": [
            {
                "type": "intro",
                "text": "[whispers] Solitude and I dance in the dark... step into our shadow.",
                "performance_tip": "Close proximity microphone effect.",
            },
            {
                "type": "victory",
                "text": "[sighs] Two against one was never fair... your shadow belongs to us now.",
                "performance_tip": "Soft breathy sigh.",
            },
            {
                "type": "super3",
                "text": "[whispers] Threads of the Void... Solitude, CONSUME!",
                "performance_tip": "Creepy dual-tone whisper.",
            },
        ],
    },
    "Ignacia": {
        "voice_type": "Passionate Iberian / Spanish fire-warrior accent",
        "inflection_notes": "Fiery, intense, rapid rekka pace.",
        "lines": [
            {
                "type": "intro",
                "text": "[shouts] The Pyre Clan burns bright! TRY TO SURVIVE MY CLAWS!",
                "performance_tip": "Passionate rolling 'r's and aggressive yell.",
            },
            {
                "type": "victory",
                "text": "[gasping] Hah... Too slow! My flames burn away everything in my path!",
                "performance_tip": "Post-combat heavy breathing.",
            },
            {
                "type": "super3",
                "text": "[shouts] PYRO CLAW TRIPLE THREAT! Burn to ash—IGNITION BURST!",
                "performance_tip": "Explosive fire callout.",
            },
        ],
    },
    "Nereus": {
        "voice_type": "Weathered Cornish / Sea-captain mariner accent",
        "inflection_notes": "Grit, ocean salt, deep sea captain rumble.",
        "lines": [
            {
                "type": "intro",
                "text": "[shouts] AHOY! The abyssal tide rises... DROWN IN THE DEPTH OF THE VOID!",
                "performance_tip": "Bellowing sea captain shout.",
            },
            {
                "type": "victory",
                "text": "The ocean claims another soul... Rest in the dark depths.",
                "performance_tip": "Solemn mariner cadence.",
            },
            {
                "type": "super3",
                "text": "[shouts] TIDAL CRUSH! Drag them down to the ocean floor—CATACLYSM!",
                "performance_tip": "Deep storm callout.",
            },
        ],
    },
}


def generate_guides() -> None:
    """Write S2S_PERFORMANCE_GUIDE.md into each character's audio directory."""
    print("--- Generating Speech-to-Speech (S2S) Performance Guides ---")
    for char, data in S2S_GUIDES.items():
        audio_dir = os.path.join(CHARACTERS_DIR, char, "audio")
        os.makedirs(audio_dir, exist_ok=True)

        file_path = os.path.join(audio_dir, "S2S_PERFORMANCE_GUIDE.md")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"# Speech-to-Speech (S2S) Voice Guide: {char}\n\n")
            f.write(f"**Vocal Persona & Accent**: {data['voice_type']}\n")
            f.write(f"**Inflection & Emotion Directives**: {data['inflection_notes']}\n\n")
            f.write("## 🎙️ Dialogue Scripts & Vocal Cues\n\n")
            for line in data["lines"]:
                f.write(f"### Line Type: `{line['type'].upper()}`\n")
                f.write(f"- **Target Speech Text**: `{line['text']}`\n")
                f.write(f"- **S2S Performance Tip**: {line['performance_tip']}\n\n")

        print(f"✅ Generated S2S Performance Guide for [{char}] -> {file_path}")


if __name__ == "__main__":
    generate_guides()
