

--------------------------------------------------
Sylas (The Ice Druid)
--------------------------------------------------
Archetype: Stance-Changer / Zoner / Rushdown Hybrid
Signature Feature: Dual-Stance Transformation (Druid Base Form <-> Frost Wolf Stance)

Appearance & Form Overview:
• Druid Form (Base Form):
  A tall Nordic druid spellblade wearing leather and fur armor woven with glowing green vine runes, a wolf-pelt shoulder cloak, and a signature carved oak staff tipped with giant frost rime crystals.
  Gameplay Focus: Nature magic, space control, vine traps, defensive zoning, and staff strikes.

• Frost Wolf Stance (Transformation Form):
  Transforms into a massive upright bipedal Dire Frost Wolf with glowing blue-white icy fur, glowing cyan eyes, sharp icy fangs, and crystalline ice armor plates protruding from his shoulders, spine, and gauntlets.
  Gameplay Focus: Fast rushdown, freezing wave projectiles, low-profile mixups, and frost claw strikes.

Transformation Mechanic:
• Dual-Stance Transformation: Sylas can switch forms using stance commands (236236K or Special Stance Input).
• Engine Implementation: Uses dual sub-models (Sylas_Human and Sylas_FrostWolf) under a single character parent controller in Unity, using a 6-frame icy particle explosion / frost burst VFX shroud during model and hurtbox swaps.
This document assumes you have at least a basic understanding of fighting games.

Universal Info:
Characters block by holding backwards from the opponent, “low” attacks must be blocked while crouching, “overhead” attacks must be blocked while standing and mid attacks can be blocked either way.
A “counter hit” is when an opponent is struck before their move comes out. A “punish counter” is when an opponent is struck after their move comes out, when they are hit during the recovery frames. Counter hits grant two extra frames of hitstun to the attacker, and punish counters grant 4 extra frames.
Up to three bars of super can be gained at once. Overdrive moves cost half a bar of super to perform. Super is gained by blocking attacks, attacking opponents on either hit or block, or using special moves. Level 1 supers cost 1 bar, level 2’s cost 2 bars, and level 3’s cost 3 bars.
All characters can spend half a bar of super to perform an armored move referred to as a Braced Attack (BA). BA has two hits of armor, and lunges forward a decent distance. On block, it’s very safe at -3 with high pushback, but it’s slow to startup at 26 frames, making it easy to counter with a grab or simply block it. On hit, BA sends the opponent flying away, and if they’re in the corner, causes a wallsplat. However, on counter hit or punish counter, it causes a crumple, letting the character combo into whatever they like. However, if you are hit three times while performing a BA (such as with light attacks or multi hit moves), you are crumpled instead.
Currently Debated Mechanic (pretend this doesn’t exist for the time being): Braced Breaker or BB, costs 1 full bar to use, but essentially, can be canceled into from any special cancelable normal, or any special, and causes a crumple on hit, ignoring the usual “1 crumple per combo rule.” Functions as a great combo extender obviously, and a way to dump meter. Uses the regular BA animation, but maybe with an extra flash or something to distinguish it.
All supers break armor.
Level 1 supers can be canceled into through either super cancelable or special cancelable normals.
Level 2 supers can be canceled into through super cancelable normals, special cancelable normals, and grounded Overdrive special moves.
Level 3 supers can be canceled into through super cancelable normals, special cancelable normals, and any grounded specials.
There are different kinds of knockdowns:
Soft Knockdown or just Knockdown: Most common, opponents can either recover in place, quick rise, or recover backwards.
Hard Knockdown: Commonly caused by sweeps or other combo enders. Opponents lose access to both back rise and quick rise, meaning they can only perform a regular get up.
Flip-out: Usually caused by anti air normals. The opponent simply gets hit, and flips backwards before landing on their feet, immediately recovering.
Characters when knocked down, can perform three different ways to get up. These can be used to mess with opponents Oki timing:
If they press nothing, the character will perform a regular getup, rising in place.
If they hold down, they will perform a quick rise, getting up significantly quicker.
If they hold back, they will perform a back rise, which is the slowest wake up option, but in return, causes the character to roll backwards, putting space between them and the opponent.
All level three supers have invincibility until they hit, unless otherwise noted.
Throw’s can be escaped by pressing throw within a short window of being grabbed. Unreactable. Command grabs cannot be escaped.
If a throw and a strike clash on the same frame, the strike will always win.
A “Wall Bounce” causes the opponent to shoot across the screen, hit the wall, and then bounce back towards the attacker, enabling further combos. The amount of time the opponent takes to bounce back to the opponent is always the same, so if a wall bounce causing move is used in the corner, the opponent bounces higher to compensate.
A “Wall splat” causes the opponent to launch across the screen until they hit a wall, at which point they are splatted, lingering on the wall for a moment before falling to the ground. Allows combo extensions as the attacker can strike their opponent whilst they are splatted against the wall.
A “Wall slump” sends the opponent tumbling across the floor with great corner carry. If the opponent strikes the corner whilst tumbling, they are sent into a low splat with more limited follow ups than a wall splat.
Unless otherwise noted, wall bounces, wall splats, wall slumps, and ground bounces all have a limit of once use each per combo. Attempting to use multiple instead just causes a knockdown.
Unblockables are not allowed unless otherwise noted! If an unblockable would occur (I.E, if you have to block an overhead and a low at the same time), simply blocking one hit will be enough to block both.

Design Ethos:
All reversals or moves with invincibility should cost a resource of some kind, usually meter but sometimes character unique resources.
Reversals should always be very unsafe if blocked, and shouldn’t startup faster than 7 frames.
Lows should not be plus on block.
Grounded overhead attacks should be slow to startup and grant low reward without external factors.
Throws should never grant looping Oki (I.E, After a throw, characters should be able to threaten another hit but shouldn’t be able to go for another throw gaplessly).
Combos should generally be quite short, unless the combo is a punish, or a certain condition is met.
Unless otherwise noted, assume crouching kicks always hit low.
Any of these rules can be broken if the move in question has other weaknesses attached or if it’s a defining feature for the character.

If a move is special cancelable, it will have a * next to it.
If it is super cancelable, it will have a ** next to it.

Base Roster:

Zenthos:
Deranged Prosecutor Of The Mad
“Heretics. Let me return you back to light.”
Archetype: Generalist
High Damage
Fantastic Oki
Jack Of All Trades
Great Lows
Dominant Midrange
High Execution
Weak Pressure
No Significant Specialty
Mediocre Mobility
Poor Mix
Appearance: Zenthos is a relatively tall, black haired man with strong limbs and an angular face and a serious expression. His eyes are a deep brown, and he keeps his hair in a short braid. His outfit consists of silver armor, with brown fur boots, although he lacks a helmet. The two most distinct parts of his outfit are his white scarf, which accompanies him always, and his two rings. He has one on each ring finger, both are large, golden, and encrusted with precious stones. His left hand has a brilliant ocean blue sapphire, and his right has a ruby. His sword is long, curved, and wickedly sharp, and he keeps an undecorated sheath for it on his hip (to maintain visual cohesion, this sheath will also switch which hip it’s on when the screen flips). The flame he involuntarily wields glows black and white. His idle stance has him readily holding his sword up in both hands, while his crouching stance has him sheath the blade, although he maintains his grip on the hilt. His forward and back walking animations are very standard, with him holding his sword up aggressively when walking forward and holding it down low in a defensive stance while walking backward.

Light Punch*:
Frame: 4
A short ranged bash with the hilt of Zenthos’ blade. Unremarkable, but can combo into medium Taunting Flames (light travels too slow to connect). +5 on hit and -3 on block.

Light Kick*:
Frame: 5
A quick kick with Zenthos’ back leg with decent range that can combo into light BFSD or light/medium Taunting Flames. Useful as a five frame punish and as Zenthos best light ender. +2 on hit, -4 on block.

Crouching Light Punch:
Frame: 4
Zenthos performs a quick bash with the hilt of his blade while it’s still in its sheath. +5 on hit, -1 on block.

Crouching Light Kick:
Frame: 5
A quick short ranged swipe kick that can chain into crouching light punch and hits low. -3 on block, +4 on hit.

Medium Punch*:
Frame: 7
Zenthos performs a quick, long ranged diagonal swipe with his sword. On hit or block, Zenthos then automatically performs another swipe in the opposite direction, making this a two hit normal. A fantastic standing poke with little whiff recovery, unlike standing heavy punch, but it is less rewarding. +4 on hit, -2 on block.

Medium Kick:
Frame: 9
Zenthos performs a quick thrusting kick with his front leg raised. Has a decently disjointed hitbox at the tip of his foot. Due to his raised leg, Zenthos can dodge over lows while performing this move. A solid but unrewarding poke that’s only +4 on hit, meaning it can’t usually link into anything unless it scores a punish counter. -3 on block, making it always safe. 

Crouching Medium Punch*: 
Frame: 6
A crouching sword thrust. Surprisingly good range for this type of button. Can combo into medium or light Taunting Flames, or any strength of BFSD. +5 on hit, but importantly, is also +1 on block, meaning even after using this move it’s still Zenthos turn. A fantastic normal with use in the midrange, good for poking, whiff punishing, and pressure.

Crouching Medium Kick*:
Frame: 8
A shoto style crouch medium kick with great range that can be special canceled and hits low. A fantastic button that lets Zenthos dominate the midrange. Can combo into any lower strength of Taunting Flames which has pretty low reward unless it’s a Perfect Draw, or BFSD for a riskier but decidedly more rewarding attack. -2 on hit and -6 on block.

Heavy Punch*:
Frame: 10
A high sword swipe with solid range, similar to a shoto stand heavy punch. +4 on hit and is +8 on punish counter, letting him link into crouching medium kick. -2 on block. A dominant counter poke that’s easy to whiff punish, but has fantastic range and is very rewarding on hit.

Heavy Kick**:
Frame: 18
Zenthos takes a big step forward and performs a knee attack with his back leg. A powerful advancing move that’s +1 on block. +6 on hit, meaning on regular hit it can link into crouching medium punch, and on counter hit, into crouching medium kick. Causes a crumple on punish counter, letting Zenthos dash forwards and link back heavy punch or other damaging starters. Has a unique animation if it contacts an armored opponent, where Zenthos will recoil backwards in surprise, leaving him vulnerable and making this move very weak to armored attacks or BA. To compensate, this move can be canceled directly into super on hit, letting Zenthos break the armor of the defender and retaliate with an unscaled super. Also can be comboed into after a Perfect Draw medium Black Flame Sword Draw, granting great oki or a direct link into super. 

Crouching Heavy Punch*:
Frame: 9
A decently disjointed upward angled sword stab, performed at a steep, vertical angle. Covers the space up and above Zenthos quite well, but causes a flip out on aerial hits, so somewhat lacks reward. -8 on block, +1 on hit.

Crouching Heavy Kick:
Frame: 11
Zenthos performs a one legged sweep with his back leg. Hits low. Grants a hard knockdown on hit, unless you go into the target combo. Very unsafe on block at -11, with a unique animation where Zenthos recoils in surprise. Has a target combo with forward heavy punch.
Forward Heavy Punch (TC):
Zenthos spins as he stands upright and goes into a slamming backfist with his forward hand, similar to Kazuya’s hellsweep from Tekken. Extremely unsafe at -15, and is always a true blockstring out of sweep. Launches on hit, but is not special cancelable, limiting it’s follow ups to either medium or heavy Black Flame Sword Draw, medium Pecking Order, or Zealotry.

Forward Medium Punch:
Frame: 22
Zenthos leaps into the air slightly and performs a powerful, 2 handed plunge downwards with his sword. Hits overhead, and is +3 on hit and -3 on block. Due to the leap into the air he takes, Zenthos can actually hop over some low attacks while using this move. 

Back Heavy Punch*:
Frame: 12
Zenthos performs a large 2 handed upward slash with his blade. An acceptable anti air for far away jumps, covers a lot of horizontal space in front of him but has very little vertical range directly above him. One of Zenthos’ most important combo starters, as it can be special canceled, and launches on hit. Can be canceled into light Taunting Flames, then finished with medium Pecking Order, but if Zenthos uses a Perfect Draw light Taunting Flames, he can get a much better combo using crouching heavy kick target combo into heavy Black Flame Sword Draw, which can then obviously be continued further if that’s a perfect draw. -10 on block, but can be special canceled to make it safer.

Forward Heavy Punch:
Frame: 14
Zenthos takes a large step forward and performs a big, two handed, diagonal slash with his sword. Has very good range due to the large advancing step, and does a decent chunk of damage. +4 on hit, -3 on block with large pushback. Comes with a target combo which is fairly easy to hit-confirm.
Forward Heavy Punch (TC):
Zenthos performs a meaty elbow with his forward arm. -10 on block, so it’s very important to hit-confirm the combo. +4 on hit. Has another, final follow up.
Forward Heavy Kick (TC):
Zenthos performs a full bodied ram with his back shoulder, slamming against the opponent and sending them flying. Zenthos can dash forward after the combo to get pretty decent Oki. The target combo does great damage, but it can’t be used as a frame trap as the whole thing is always a true blockstring. This final hit is -15 on block.

Forward Heavy Kick:
Frame: 20
Zenthos plunges his sword into the ground and vaults forward, using his sword as leverage to perform a diagonal two footed stomp downwards. Causes a hard knockdown on hit, and a ground bounce on punish counter, granting follow up combos. Is +2 on block, making it a good approach tool in neutral, but its high end lag makes it quite easy to punish if it whiffs.

Forward Throw:
Frame: 5
Zenthos grabs the opponent by the left arm, turns them around, then delivers a stern strike with the hilt of his blade to the enemies shoulder, aiming to break their arm and sending them slamming into the ground before he steps away. Great oki, but with no throw loop.

Back Throw:
Frame: 5
Zenthos folds along the opponent to get behind them, then slides his blade along their throat, crumpling them to the ground, where he kicks them away. Very good oki for a back throw.

Unique Mechanic:
Perfect Draw:
Some (not all) of Zenthos’ special moves have a mechanic referred to as Perfect Draw. If while doing a motion input the player presses both the last directional input and the button within two frames of each other, the move will gain new effects. However, only one Perfect Draw can be performed per move type per combo (I.E, if Zenthos uses Perfect Draw medium BFSD, he could use Perfect Draw Taunting Flames in the same combo, but he could not use any other Perfect Draw version of BFSD (additionally, despite overdrive moves occasionally functioning the same as Perfect Draws, they do not count, meaning both an overdrive move and a Perfect Draw move can be used in the same combo). If he attempts to use two same move Perfect Draws in the same combo, the normal version of the move is used instead.

Black Flame Sword Draw:
(Dragon Punch + Punch)
Zenthos quickly sheathes his sword, then unleashes a strong slash with direction dependent on the strength of the button. All versions are punishable on block, although to varying extents. A powerful combo ender with a unique twist: if the punch button and down forward are pressed at the same time (with a 2 frame window), Zenthos’ blade flashes black in its scabbard, and when he draws it, it is enwreathed in black flame. This is henceforth referred to as a Perfect Draw. Perfect Draw grants new effects to all strengths except the overdrive version which are generally extremely beneficial. 
Light: Zenthos performs a horizontal swing aimed at chest height. A decent combo ender for light strings that leaves the opponent standing, and a great tool to just buffer into from normals, but is -6 on block. Thankfully, it has very solid range, and rather high pushback, making it usually safe if spaced well. This also gives the move utility in neutral, where it can be used as a risky but rewarding poke with more range than any of his buttons. Will not frametrap from lights, but will from mediums and heavies. On hit it can be canceled into Death Seed for a high damage combo. The pushback on hit means that it generally leaves you out of range for a strike throw mix, and it leaves Zenthos +3 and the opponent standing. A Perfect Draw instead grants Zenthos a hard knockdown, letting him further pressure his opponent by dashing forward.
Medium: Zenthos performs an upward arcing slash. A great anti air and combo ender that causes a knockdown on hit, but is -12 on block. With a Perfect Draw, this move instead launches the opponent upward, granting a combo into either light Pecking Order, which does decent damage but leaves Zenthos rather far away, or uniquely, standing Heavy Kick. This link does rather poor damage, but allows Zenthos to double dash forward, leaving him +6 point blank, or he can cancel the heavy kick into super for high damage. Combos out of medium buttons. Has upper body invincibility to jumping attacks, making it extremely reliable as an anti air.
Heavy: Zenthos performs a strong, two handed downward slash that sends the opponent slamming into the floor, granting a hard knockdown. Zenthos can dash forward twice after this knockdown for corner carry and oki that leaves him +2 point blank. Generally Zenthos’ highest damage combo ender, and is easy to connect after juggles due to the wide, vertical hitbox. With a Perfect Draw, the opponent instead bounces off the ground, allowing one more, further ender. This can be finished with another heavy BFSD, Zealotry, Of One Mind, Explosive Madness, or medium Pecking Order, which uniquely of the options, grants a safe jump, though at the cost of less damage then his other enders. Combos out of heavy normals, and is -15 on block.
Overdrive: This move emulates the Perfect Draw features of the other variations of this move. Pressing Light + Medium punch emulates the Perfect Draw version of Light Black Flame Sword Draw. Pressing Medium + Heavy punch emulates the Perfect Draw version of Medium BFSD. Pressing Light + Heavy punch emulates the Perfect Draw version of Heavy BFSD. This move lets beginners access the flashy combos granted by Perfect Draw, but at a cost, or for higher level players, grants combo extensions by allowing players to use an Overdrive move then a Perfect Draw before finishing with their preferred combo ender.

Taunting Flames:
(Quarter Circle Forward + Punch)
Zenthos covers his face, seething black flame pouring from his mouth and eyes, before tearing his hand away and unleashing a seething ball of black flame from his face. A strong projectile Zenthos can also use as a combo tool. Gains unique attributes if the punch button and forward are pressed at the same time (with a 2 frame window), henceforth referred to as a Perfect Draw. 
Light: A very traditional projectile. Mediocre startup, Zenthos spits out a large oval shaped globule of dripping black flame that moves forward. Only one projectile can exist at a time. Clashes with other projectiles, you know the story. A very simple projectile Zenthos can use to approach or force others to approach with. On Perfect Draw, Zenthos’ face flashes black, and the projectile's properties change. It becomes a two hit projectile that will beat other single hit projectiles, and has significantly better combo potential.
Medium: Identical to the light version except the projectile travels faster, letting it link from more moves at the cost of being slightly less safe on block.
Heavy: A different style of move. Instead of being a fireball, this move functions more like Yoga Flame. Zenthos tears his hand away and spews a short range torrent of fire from his face. 3 hits total, and safe on block despite being -4 due to its high pushback, making it a good move to buffer into, though it won’t frame trap or combo from anything other than heavy buttons. Also a great Meaty option on wake-up, due to its long active time, so it can be used to grant Zenthos exorbitant amounts of plus frames. On Perfect Draw, the end lag of this move is reduced significantly, so much so that it lets Zenthos get a combo on hit, leaving him +7, and making the move +1 on block.
Overdrive: This move emulates the Perfect Draw features of the other variations of this move. Pressing Light + Medium punch emulates the Perfect Draw version of Light Taunting Flames. Pressing Medium + Heavy punch emulates the Perfect Draw version of Medium Taunting Flames. Pressing Light + Heavy punch emulates the Perfect Draw version of Heavy Taunting Flames. This move lets beginners access the flashy combos granted by Perfect Draw, but at a cost. Additionally, allows Zenthos to win in fireball wars, as the projectiles retain overdrive properties, destroying other non overdrive projectiles.

Pecking Order:
(Quarter Circle Backwards + Kick)
Zenthos pulls himself back, then slides forward, blade stretched forward. Can low profile certain attacks, and hits low. Grants varying frame advantage/disatvantage depending on distance traveled. If it hits in its last few moments, Zenthos can be up to +2 point blank, but if misspaced, he’s likely to be punished. All versions except overdrive cause a hard knockdown on hit, trading the damage of BFSD for significantly better oki.
Light: Generally just a fireball punisher. Has fireball immunity starting from frame 7 until it hits. Cannot link out of light normals, only medium ones, and knocks the opponent down on hit. Travels the shortest distance, but has the quickest startup, and is rather easy to make safe, although the spacing to make it plus is rather specific.
Medium: Can link from medium normals. Causes a hard knockdown on hit. The easiest version to space for plus frames, as it’ll usually be plus from about midscreen. Causes a hard knockdown against airborne opponents, and can be used to set up a safe jump after Perfect Draw heavy BFSD.
Heavy: Slowest startup, but travels the furthest. On hit, causes a wall slump, which, in the corner, allows Zenthos to connect crouching heavy kick target combo, creating powerful juggles. Can only be linked into through heavy normals. 
Overdrive: Zenthos’ invincible reversal. Slightly less damage than most reversals, but in return, side switches on hit. Doesn’t hit low like the other strengths, and grants quite bad oki, generally leaving Zenthos only barely plus, despite the side switch. Incredibly unsafe on block.

Super 1:
Zealotry:
(Double Quarter Circle Forward + Punch)
“Return to light!”
“PERISH, HERETIC!”
Zenthos yells, sheaths his sword, then draws it and performs a wide arcing overhead slash with his sword. A few moments later, an enormous blade of black flame cuts across the screen in an arching echo of the slash. The Blackflame blade is large enough that it hits full screen, and if the opponent is hit by the first slash with the blade, they will combo into the next hit. Has invincibility until the first sword slash hits, and works as a good combo ender, can also be used to punish very laggy fireballs at full screen (both the initial sword slash and the black flame blade destroy projectiles on contact). This move also has a Perfect Draw: If punch and the final forward input are pressed on the same frame, Zenthos will say a different voiceline, and there will be two slashes of black flame, with the second one happening a few moments after the first. This vastly increases the super's damage, in addition to making it much safer (it’s still very unsafe, but much less so, especially at mid or fullscreen).

Super 2:
Of One Mind:
(Double Quarter Circle Backward + Punch)
“I… shall not… FALL!!”
Zenthos grips his head in both hands and unleashes a loud yell, creating a large rippling shockwave of black flame that does 3 hits and hits from close range to about midscreen. Has invincibility until it hits, and activates an install. While in this install, Zenthos’ eyes constantly leak black flame, and his hair (which is normally kept in a neat braid) is let loose, flowing down his shoulders and chest wildly. Once he leaves the install, he returns to normal. In this install, he gains 2 new moves. This super does relatively low damage, especially for a level 2. If Zenthos is hit during this move's recovery, he does not gain the install. He has a total of 3 uses for either move, after he uses either move a total of 3 times, he exits the install. Extremely unsafe on block.
Inescapable Frenzy:
(Half Circle Forward + Any Punch)
A command grab with only one level of strength. Zenthos lunges forward with both hands and grabs the opponent by the head. Reactable, but quick-ish startup, making it useful for catching opponents off guard. Very good range for a grab, as Zenthos rears back during the startup of the move (significantly retracting his hurtbox and allowing him to dodge attacks and shimmy throws) before taking a large step forward. On hit, he closes his eyes, and gets close to the opponents face, before opening his eyes and mouth and screaming, pouring a fountain of black flame onto the opponents face. Does high damage, and leaves the opponent extremely close while causing a hard knockdown. This move greatly enhances Zenthos’ pressure, like any command grab. If the grab whiffs, Zenthos enters a long whiff animation that leaves him very vulnerable.
Explosive Madness:
(Half Circle Forward + Any Kick)
An extremely high damage combo ender and reversal, equivalent to a mini super. Zenthos performs a short ranged punch which triggers a hit grab on contact with the opponent. On hit, Zenthos grabs the opponent by the throat, then begins glowing, black flame building up. A moment later, the screen flashes black, and he explodes, launching the opponent and Zenthos in opposite directions, leaving them fullscreen, unless it lands in the corner. If this move lands in the corner, the opponent is wallsplatted, but Zenthos is still launched away. This means the only follow up Zenthos can land here is Zealotry, although he can use medium Pecking Order to get good Oki. This move also has invincibility until it hits. Is incredibly unsafe if blocked, however, and it’s slow startup limits its use in combos, as it will only combo from heavy normals, or after juggles. Unlike other specials, this move cannot be canceled into level 3 super.

Super 3:
Death Seed:
“Another, reclaimed!”
Zenthos preps his sword in its sheath, then performs a shoulder ram forwards. On contact with the opponent, engages a cinematic where Zenthos elbows the opponent across the jaw, sending them spinning, then dashes through his opponent, before sheathing his blade. Once he sheathes it, the opponent flinches, and the screen is cast in silhouette as black flame pours from a cut across them and Zenthos stands up. Grants no meaningful Oki, but does cause a hard knockdown. Has a unique animation if blocked where Zenthos bounces back and cries out “You dare-!”

Critical Art:
Blind Man’s Greed:
“REPENT WITH YOUR DEATH!”
Zenthos drops his blade as he clutches his face, screeching at the opponent as black flame pours from his eyes. He then lunges forward, both hands outstretched, and engages a cinematic on hit wherein he clutches the opponent by the face and unleashes a fountain of flame upon them. As he does so, he reaches one hand up behind himself, which he coats in black flame, stretches his fingers, and then plunges that hand through the opponent as it cuts to a side profile silhouette, black flame exploding out the back of them. Zenthos then picks his sword back up. If blocked or whiffed, Zenthos katana will magically reappear in his hands through the power of convenience. If he whiffs this move, Zenthos lets out a loud, animalistic grunt.

Win Quotes:
(vs. Zenthos) “What trickery is this!? Some madman’s conjuring!? Show yourself!”
(vs. Kalle) “Accept your natural place: crushed beneath my boot!”
(vs. Vile) "The heresy of the gods can be found everywhere. How does it feel to be toyed with?”
(vs. Melancholia) “Let it be known, madwoman: the only reason the black god has not claimed your shattered mind is your broken form.”
(vs. Ngann) “You were my hero, sir. It is an honor to duel with you.”
(vs. Beast) “You are not mad, but rather, sick… perhaps I shall cleanse you of this plague too.”
(vs. Gauss) “Go now, specter. The fires of madness have long since claimed you. ”
(vs. Salazar) “I shall be keeping that gun. It will make a fine addition to the prosecutors toolset.”
(vs. Laecaera) “The pursuit of all knowledge inevitably leads one to him. Beware, girl.”
(vs. Alphard) “Your magic is practice for my tools and little else!”

Kalle:
The Chosen Child
“Shall we dance?”
Archetype: Generalist/Zoner
Setplay
Ranged Buttons
Zoning
Corner Carry
Strong Lights
No Grounded Overhead
Low Damage
No Plus On Block Normals
Slow Specials
Requires Setup

Light Punch*:
Frame: 5
Kalle does an open palm jab with his forward hand. Unlike most jabs, this cannot chain into itself or any other lights. +5 on hit, -3 on block. Has a target combo with light kick.
Light Kick (TC):
Kalle transitions from the jab to a forward advancing shin kick with his back leg. +1 on hit and -6 on block. Forms a true blockstring from the starter. Has a target combo with heavy punch.
Heavy Punch (TCC)*:
Kalle rips his spear upward, launching the opponent. Forms a true blockstring from the starter. Can be used as an easy hit confirm, and also grants Kalle unusually good light confirms. -12 on block. The launch can be used to either continue combos (notably, at midscreen, Kalle can cancel into light Pyre and then into overdrive Ignition for high damage, or in the corner, he can use medium Sermon and then link into light Black Seed), or he can use it to set up some of his bombs. A very versatile combo tool that’s a staple of a lot of Kalle’s common routes.

Crouching Light Punch*:
Frame: 4
Kalle does a crouching swat with his forward hand. +5 on hit and -2 on block, but chains into itself and crouching light kick. Notably can link into standing light punch for a full combo extension. Kalle also has a useful frame trap after three lights in the form of light Sermon, which will catch opponents trying to take back their turn at the cost of being unsafe on block.

Light Kick:
Frame: 5
Kalle does a stepping shin kick with good range for a five frame move. Limited combo utility when compared to standing light punch, but a useful whiff punish or punish tool for unsafe moves. -3 on block and +2 on hit.

Crouching Light Kick:
Frame: 5
Kalle does a low crouch kick. Kalle’s fastest low, and a useful meaty tool. -2 on block and +3 on hit. 

Medium Punch*:
Frame: 7
Kalle performs a hooked bash with the hilt of his spear. Short ranged, and is +5 on hit and -1 on block. Notably, this move has an outrageous amount of active frames, which means that if spaced to hit at the very last moment, it can actually be up to +9 on hit and +3 on block (notably, certain combo enders allow Kalle to dash up and perform an auto timed meaty medium punch for plus frames). Has a target combo with medium kick. Extremely low pushback on both hit and block.
Medium Kick (TC)*:
Kalle performs spinning back kick. Frametraps from the starter, making it a useful tool for opponents trying to mash on Kalle’s standing medium punch. Causes a knockdown on hit and is -10 on block. Can be utilized to set up one of Kalle’s bombs safely, or can combo into Black Seed or Sermon.

Crouching Medium Punch*:
Frame: 6
Kalle does a quick waist high sweep with the hilt of his spear. +5 on hit and -1 on block. A decent combo tool and good counter poke in neutral that combos into most of Kalle’s useful tools (notably standing light punch).

Medium Kick*:
Frame: 9
An important but standard poke and buffer option, Kalle pulls his front leg back, then thrusts it forward, moving himself forward slightly. Has a slightly disjointed hurtbox, low whiff recovery, and is safe on block at -3. +1 on hit, and can be canceled into a variety of useful options, making it good combo for filler or just a solid buffer option.

Crouching Medium Kick*:
Frame: 8
Kalle does a low sliding kick with both legs whilst supporting himself with his spear. A vital neutral tool for catching out back walks or for whiff punishing. Combos into medium Sermon. +2 on hit and -5 on block.

Heavy Punch:
Frame: 13
Kalle performs a forward spear thrust at head height with very good range, better than his medium kick. +4 on hit and -3 on block with low pushback. Has a target combo with forward heavy kick that can be hit confirmed quite reliably. Kalle’s longest ranged poke.
Forward Heavy Kick (TC):
Kalle uses the momentum from his forward stab, and plants the tip of his spear into the ground, then uses it to vault forward, like a pole vaulter, with both feet outstretched to perform a stomp. Causes a knockdown on hit, but is -12 on block, making it very punishable. The knockdown can be used to either set up one of Kalle’s bombs or to push advantage.

Crouching Heavy Punch:
Frame: 9
A respectable anti air and little else. Kalle does an upward wave above his head with his spear. Does decent damage and causes a flip out versus aerial opponents. +1 on hit and -7 on block.

Heavy Kick*:
Frame: 12
A terrifying neutral tool, heavy kick has Kalle bury the hilt of his spear in the ground, and use it as leverage to swing around it and perform a swinging one legged kick. On hit, is +3 and combos into any strength of Sermon, Black Seed, Pyre, and has enough hitstun to be possible (albeit difficult) to hit confirm. On block it’s -4, but can be spaced to be safe. The real draw is that on punish counter, this move causes a crumple, letting Kalle set up one of his bombs for devastating combos. To compensate, this move does apply heavy scaling to follow up combos. On punish counter, if canceled into Formless Chaos, leaves Kalle +10, and if canceled into Burn Rack, leaves Kalle +8.

Crouching Heavy Kick:
Frame: 9
The whiff punish button, Kalle’s sweep boasts great range and relatively quick startup at the cost of being -11 on block. Causes a hard knockdown on hit. Kalle plants the hilt of his spear in the ground and utilizes it to perform a low swinging kick. Significantly better range than most characters sweeps. This move does have one major unique advantage: on hit, Kalle can dash up and perform an immediate standing medium punch to automatically time it and make it +9 on hit and +3 on block, giving him an immediate strike throw setup on block and combo on hit.

Forward Heavy Punch:
Frame: 8
Kalle drags his spear across the ground, then rips it upward. Launches the opponent on hit, and functions as an excellent combo extender or starter, especially after a detonation from Ignition. Also has a decent hitbox for beating jump attacks, but has very little forward movement. Causes a high launch on hit that can consistently be finished with any strength of Black Seed, or in the corner, medium Sermon into light Black Seed for slightly higher damage (alternatively, he can skip the Black Seed finisher to set up Burn Rack). -10 on block. Causes an aerial tailspin on punish counter, which lets Kalle set up Formless Chaos, then launch them with this move again before going into a full combo.

Forward Throw:
Frame: 5
Kalle grabs the opponent by the head, then unsheathes his violin and performs a batter swing with it to the opponents gut, sending them flying away. Rather good Oki for a throw, but sends the opponent far away, which lets Kalle set up his bombs. In the corner, if Kalle performs a forward dash then does a meaty standing medium punch, it will hit on the last active frame, although this will whiff if the opponent does a delayed wakeup, which still leaves Kalle plus.

Back Throw:
Frame: 5
Kalle grabs the opponent by the head and places his palm on their face, blasting them with black flame before throwing them behind him. Hits 5 times with a rapid barrage of black flame, and grants rather poor oki, not letting Kalle use any set play tools without leaving himself vulnerable.

Ignition:
(Dragon Punch + Kick)
Kalle forms a small detonator of Blackflame in his back hand, holds it in an upright grip, and gently presses down on the top of it with his thumb, which makes a distinct clicking noise. This move is a utility move that has no hitbox, and leaves Kalle vulnerable while performing it (although, if hit while performing this move, he will only receive a counter hit, not a punish counter). However, once used it immediately detonates any of the three bombs Kalle can plant using Formless Chaos, Burn Rack, or Black Seed. This can start or extend combos, pressure, block strings, or it can simply catch opponents unawares in neutral. If Kalle uses a version of this move without the corresponding bomb being planted, he will still perform the animation but instead of a click the detonator will make a sizzling noise. Kalle can use this to try and fake pressure (such as by pretending to detonate a bomb only to move forward and throw), but this is obviously a risky play that leaves him vulnerable.
Light: Detonates Formless Chaos. This explosion has a wide aoe centered around the fireball that staggers grounded opponents, generally leaving Kalle around +7 and launches aerial ones, extending combos.
Medium: Detonates Burn Rack. Instantly causes the landmine to detonate in a large explosion that staggers opponents, while launching aerial ones. On block, this lets Kalle continue pressure.
Heavy: Detonates Black Seed. This causes the flame within the opponent, wherever they are, to implode, causing them to instantly stagger, generally leaving Kalle massively plus and letting him get devastating combos, or extend pressure. Also relaunches airborne opponents for better combos (making jumping against Kalle potentially very scary). On block, this leaves Kalle very plus.
Overdrive: Overdrive Ignition can be canceled into from any other non overdrive special move, letting Kalle instantly detonate placed bombs or place out a new bomb while activating a different one, making it a powerful but expensive tool. The combination of buttons used determines which bomb detonates, light + medium detonates Formless Chaos, medium + heavy detonates Burn Rack, and light * heavy detonates Black Seed.

Formless Chaos:
(Quarter Circle Forward + Punch)
Kalle reaches one hand to his face, pulling together a clump of gelatinous, napalm-like Blackflame, then throws it forward. This fireball moves forward in a straight line, but after a certain point, will boomerang back towards Kalle. Notably, this fireball does not have a hitbox. It cannot interact with the opponent or Kalle in any way. This also means it doesn’t clash with other fireballs, and will instead harmlessly pass through them. However, once it’s out, Kalle can use Ignition to manually detonate it, which causes the fireball (wherever it is) to implode, creating an explosion with a wide area of effect, although it doesn’t hit high enough to catch most jumping opponents unless they are close to the ground. Only one fireball can exist at a time, whenever Kalle uses this move any previous fireballs that may still be lingering are immediately deleted before the new one is summoned. After traveling forward a certain distance (which is affected by the strength of move used), the fireball will slow to a stop in midair, before heading back in the direction it came from, like a boomerang. This is signified by a “whoosh” noise that plays once the fireball starts heading back, as if the wind is pushing it backwards, letting both players know that the fireball is coming and they should be ready. If the fireball touches a wall before activating it’s retreat, then it will stick to the wall for a few moments before heading back, playing the same identifiable noise. If the fireball heads past its origin point (where Kalle first summoned it), it will despawn after a few moments, fizzling out with a brief animation if it's onscreen. Overall, this move is a fantastic zoning tool and great for controlling neutral, as well as being a potent combo extender, but due to its slow startup and the fact it leaves Kalle vulnerable while performing it, it must be used carefully and in combination with his other midrange and zoning tools (I.E, his normals and Pyre).
Light: The fireball moves quite slowly and advances the least far before returning, going to just barely half screen. This lets Kalle advance alongside it to set up for pressure, or combine it with combos for extensions.
Medium: The fireball moves at a decent speed, similar to most other characters fireballs, and goes about 3/4ths screen before returning. Useful for combos or fireball wars.
Heavy: The fireball moves quickly and goes fullscreen before returning.
Overdrive: The speed and travel distance of the medium version, but the explosion can destroy overdrive projectiles and also causes an aerial tail spin on hit, granting combos from anywhere on screen, such as using Pyre at distance and Black Seed up close.

Burn Rack:
(Quarter Circle Backward + Kick)
Kalle lifts his spear up, upon which a mass of black fire begins swirling, then throws it to the ground, where the black blob will then stick as a landmine. This landmine has a hurtbox, and will be destroyed if it is hit by 2 attacks, although due to being low to the ground, lows almost always must be used against it (this makes crouching light kicks a strong option for destroying the mine). This landmine can be detonated using Ignition, which will cause it to create a large explosion which staggers grounded opponents and launches aerial ones. The strength of move used changes the resulting angle and distance the landmine is placed at. Has relatively quick startup, meaning it can technically be used in neutral, but this does leave Kalle vulnerable, meaning it’s best used after a knockdown. The mine will persist even if it leaves the screen.
Light: Kalle throws the mine right in front of his feet.
Medium: Kalle throws the mine at a midscreen distance.
Heavy: Kalle throws the mine far away.
Overdrive: Kalle throws 2 mines, one at the light distance and one at the medium. When Ignition is used, the mines will explode on a delay, with the first exploding immediately and the second exploding about 2 seconds later, leading to brutal damage and fantastic pressure, especially in the corner. Notably, if Kalle uses Ignition and then forward throws the opponent after, the second explosion will actually hit the opponent, launching them and letting Kalle get a combo after a regular throw, a very rare thing, although with heavy damage scaling applied.

Black Seed:
(Dragon Punch + Punch) 
Swirling black flame surrounds the tip of Kalle’s spear as he performs an upward angled two handed diagonal stab, with the range and damage increasing with the strength of move used. Does less damage than most characters combo enders, but in return plants a black flame bomb onto the opponent that can be detonated using Ignition, meaning it’s extremely rewarding to land. However, if Kalle is ever hit, this bomb will automatically disappear. Oki is dependent on the strength of move used. All versions have immunity to jumping attacks, making them great anti airs. Startup and damage increase with each strength. All versions cause a knockdown and are very unsafe if blocked or whiffed. If Kalle uses overdrive Ignition after any strength of this move, he cannot combo after the light or medium version, as it will not launch high enough. However, if he uses it after the heavy version, he just barely has enough time to land light Black Seed.
Light: Lightning quick startup makes this a fantastic anti air. It doesn’t move forward much and it does less damage than other strengths, but it knocks down opponents and plants a bomb on them.
Medium: Decent startup and good damage, travels forward a decent distance. Knocks down opponents.
Heavy: Kalle takes a step forward before performing the attack, making it a little trickier to anti air with, but a better combo tool and great for anti airing far away jumps.
Overdrive: Kalle’s reversal. Has the same step forward as the heavy version and same startup as the medium version. Possesses full invincibility until it hits. Also places the aforementioned bomb onto the opponent, making it very rewarding to land, despite its lower than average damage for a reversal.

Sermon:
(Quarter Circle Backward + Punch)
Kalle leans forward slightly and speaks a word, unleashing a short ranged blast of black fire from his mouth. Kalle moves forward a decent bit whilst performing this move. Mostly has use as a semi safe buffer or combo filler, but can also be used to feint a fireball in neutral. Notably, this gives him a semi safe way to buffer into overdrive Ignition for a large combo,
Light: “Singe” Kalle unleashes a short blast of fire, with decent range. Combos from light normals and leaves the opponent standing on hit. Is -5 on block, but can be spaced to be safe a lot of the time, especially when used from medium normals. Frametraps off of light and medium normals and forms a true block string from heavy ones. +3 on hit, meaning on counter hit Kalle can pick up a combo, making it a rewarding frametrap tool, although a somewhat lackluster combo ender as it leaves the opponent out of throw range. Applies heavy damage scaling if used as a combo starter however.
Medium: “Burn”  Kalle performs a step forward and does the aforementioned blast. Frame traps from medium and heavy normals, but unlike the light version, is very unsafe at -6 on block, making it usually punishable. To compensate, it’s a better combo ender, causing a knockdown, and on counter hit or punish counter, it launches opponents into an aerial tail spin, letting Kalle dash up and perform Black Seed for a snappy and damaging combo (or he can use Ignition to get a better extension). He can also use Pyre for a better knockdown and higher damage, but sacrifices a bomb placement to do so.
Heavy: “Scorch” Kalle leans back, then truly puts his back into it and lunges forward before unleashing a 2 hit blast of black fire. Unlike the other versions, this strength is +2 on block with very low pushback, granting Kalle a strike throw mixup. To compensate, it’s much slower, and doesn’t frame trap from any normals, meaning opponents can always interrupt it. Is also a better combo tool, but with fewer applications, as it only naturally combos from standing heavy kick. In return, causes an aerial tail spin on hit, leading to damaging combos.
Overdrive: “Just stop!” Combines the speed of the light version with the +2 block advantage of the heavy version, making it a fantastic tool for frame trapping or pushing advantage on block. To compensate, it is less rewarding on hit, causing a knockdown, but it’s still a very powerful tool. Additionally, on hit, can be hit confirmed into Revenant Flames for high damage and corner carry.

Pyre:
(Quarter Circle Forward + Kick)
Kalle quickly retrieves his violin from his back and performs a harsh note on it, summoning a large pillar of fire that crashes downward somewhere on screen. All of these pillars have use as combo tools or anti airs, but their main use is for zoning, which allows Kalle to set up Formless Chaos or other bombs. They’re also fantastic against enemy zoners, as they won’t clash with other projectiles and can catch opponents who are attempting to play slow. Do note that if Kalle is hit before the pillar appears, they will not be summoned. They do have slow startup, but due to attacking specific areas, they have no travel speed and hit instantly. On hit, all versions cause a knockdown, and on hit against an aerial opponent, spike them into the ground, granting an even more advantageous knockdown. Because these pillars technically launch the opponent, canceling into overdrive Ignition from them causes an aerial launch, which can be extremely powerful in certain situations, even at range where Kalle can combo into either another Pyre or any of his supers. All versions do the same damage except overdrive. Technically Kalle’s highest damage combo ender, but doesn’t place a bomb, meaning Kalle must weigh between the choice of Pyre for damage and oki or Black Seed for setups and potentially higher damage down the line. All versions except overdrive are -2 on block.
Light: Hits relatively close to Kalle, with only a small dead zone in front of him. Useful in combos, such as after the light punch, light kick, heavy kick target combo for good oki and damage or an Ignition trigger for long combos. Also the only version that will combo from raw normals, linking from any medium or stronger normals. Will not frametrap from any normals.
Medium: Hits at about midscreen. A useful zoning tool. Can be comboed into via standing heavy kick at max range, but Kalle usually has better options.
Heavy: Hits from fullscreen, fantastic for countering an opponents zoning or their set up mechanics, and also useful after a wall splat, letting Kalle get a combo finisher after from anywhere on screen.
Overdrive: Summons a long pillar of fire right in front of Kalle that then travels forward to about mid screen, dragging any opponents hit by it along with it (although opponents who are blocking aren’t pushed back nearly as far), leading to fantastic corner carry. Useful as it has less endlag than other versions, and a fantastic combo extender in the corner where Kalle can link into forward heavy punch after it. Combos from medium normals. Will not frametrap from any normals, but is massively plus on block, especially in the corner.


Super 1:
Wrath Of Choengoreni:
(Double Quarter Circle Forward + Punch)
“I…”
“-can’t control it!”
“-back off!”
Kalle sheaths his spear, tucks both hands to his head, then rips them away, unleashing a large, spiraling beam of black flame that travels fullscreen really quickly, clashing with and destroying non super projectiles. Does decent damage, and causes a knockdown. An excellent tool for beating opponents in projectile wars, and it also boasts full invincibility until it hits, although it’s extremely unsafe if blocked. Uniquely, if Kalle holds up during the screen freeze, an alternate version of the move is used, with a different voice line. This version has Kalle aim upward at a diagonal angle, covering most jump angles that aren’t directly above him, and unleashing the powerful beam. On hit, this version does less damage than the base version, but sends the opponent flying away and causes a wall splat, letting Kalle pick up combos into forward heavy punch after if he's close to the corner or heavy Pyre anywhere on screen. However, this anti air version has no invincibility whatsoever, meaning it must be done preemptively.

Super 2:
Revenant Flames:
(Double Quarter Circle Back + Kick)
“(Shrill whistle)”
Kalle raises his fingers to his mouth and lets out a loud shrill whistle, summoning a massive steed composed of Blackflame with glowing eyes. Kalle leaps atop it and charges across the screen extremely quickly, the horse surging forward with unnatural speed, presenting a continuous, lingering hitbox. This move has full invincibility until it ends, and dashes across the screen incredibly quickly, making it a great whiff punish or fireball counter in neutral. On hit, Kalle keeps charging, pushing the opponent about half screen away, making it excellent for cornering them. It also causes a hard knockdown, finishing with a small scene of Kalle jumping off his horse, which will dissolve into nothingness moments later. If let to play out his animation, Kalle will actually nuzzle the horse first before it disappears, although this animation will be interrupted if anything is inputted. Leaves Kalle right next to the opponent, letting him activate his set play tools. Alternatively, if he does a double dash forward and then does a standing medium punch, it will automatically time it to hit on the last active frame, leaving him +3 on block and +9 on hit.

Super 3:
Embrace Chaos:
(Double Quarter Circle Forward + Kick)
“Enough of this.”
Kalle sheaths his spear and pulls out his violin as the screen freezes. Once the screen unfreezes, he plays a single, sharp note, causing a massive pillar of fire to descend upon the opponent wherever they are on screen. On hit, this engages a cinematic where Kalle continues playing a frantic, crazed folk tune on his violin as the opponent staggers around, getting beamed three separate times with black flame pillars. Kalle finishes and takes a bow as the opponent falls to their knees and is struck by another pillar. If this move kills, the freezeframe shows the silhouette from behind Kalle of him bowing and the opponent writhing in pain beneath the pillar of fire. If it doesn’t kill, Kalle and the opponent both recover at about half screen, and the move causes a hard knockdown, letting Kalle set up some set play tools. To compensate for hitting anywhere on screen, this super is ludicrously slow, with almost triple the startup of most level 3 supers, which greatly limits its combo potential, as the only specials it will only combo from are heavy Sermon, any strength of Pyre, and any strength of Black Seed, as the others don’t give enough hitstun. It will also only combo from heavy normals.

Critical Art:
I, Choengoreni:
“Let us dance in hell together.”
Kalle performs the same harsh violin strum as before, and has the same pillar of fire and slow startup as the base version. On hit, engages a cinematic wherein Kalle and the opponent are transported to a dark void. Kalle begins playing a soft, gentle tune as the opponent looks around in confusion. Black flame begins growing around the borders of the void, slowly creeping its way inward as the opponents confusion turns to fear. Kalle finishes his song, and the flame lunges towards the opponent lifting them upward as it scorches beneath them, eventually forming an enormous fountain of fire. Kalle bows as the opponent erupts into flames, their body fragmenting in the sudden heat as a cackling face of fire appears above them. If this kills the opponent, the freeze frame has their body ripped apart with both Kalle bowing and the cackling face in frame. Has a unique win animation where Kalle falls to his hands and knees on the ground, shaking with exertion, and the opponent clutches their face and dies kneeling. Grants the same Oki as the base version if the opponent survives.

Win Quotes:
(vs. Zenthos) “Piss off. Last time I ask.”
(vs. Kalle) “Man, black flame is a strange thing, eh?”
(vs. Vile) “Look at you, so much sorrow, so much age. Have you never sung?”
(vs. Melancholia) “I kinda get it, that was pretty fun, but you take it too far.”
(vs. Ngann) “Screw the king, you should be in this for the people, not the royalty.”
(vs. Beast) “Not too fond of fire, eh? I’m with you there…”
(vs. Gauss) “… suppose that’s his doing, eh? Guess I know what I’m in for…”
(vs. Salazar) “Loving the moves, loving the style, you got something man. Wanna hit the taverns?”
(vs. Laecaera) “You wanna learn about this? Trust me, this is not a path you want to walk… at least, I hope it isn’t. ”
(vs. Alphard) “All those stars and rocks sure are pretty, but pretty never won a fight.”

Ngann:
Shining Font Of Mankind’s Will
“For the King, I would give my second life.”
Archetype: Rushdown
Rushdown
Mix
Incredible Movement
Oki
Versatile
Weak To Zoning
Mediocre Midrange
Mediocre Damage
Requires Charge
Super Reliant

Light Punch*:
Frame: 4
Ngann does a quick short punch with his forward hand. A useful combo tool that chains into itself and other lights and can combo into a variety of specials (notably Unyielding for damage or Crusader’s Charge for corner carry and oki). -2 on block and +4 on hit. 

Crouching Light Punch:
Frame: 4
Unlike the standing version, this crouching jab isn’t special cancelable, but it boasts better frame data to compensate, being +5 on hit and -1 on block.

Light Kick*:
Frame: 5
Ngann does a short knee with his back leg. +3 on hit, and a pivotal combo tool for Ngann after moves like standing medium punch, which lets Ngann combo into a variety of specials. Doesn’t chain from or into other lights or itself however.

Crouching Light Kick:
Frame: 5
Ngann does a short crouching slide kick with his back leg. Ngann’s fastest low, helpful for catching opponents trying to walk back, but unlike most characters, it cannot chain into itself or any other light normal. To compensate for this, it has a target combo with down medium kick.
Down Medium Kick (TC):
Ngann transitions from the crouching slide kick to a low thrust kick with both legs, supporting himself with one hand. Causes a knockdown on hit, letting Ngann continue pressuring the opponent. Frametraps from crouching light kick, but is -8 on block to compensate.

Medium Punch:
Frame: 10
Ngann does a forward palm with his forward hand while stepping forward. Fantastic range, while being very rewarding on both hit and block, as this move is actually +2 on block, which is extremely rare for a normal that moves him this far forward. Combined with Ngann’s fast walk speed, standing medium punch is a workhorse button that Ngann relies on heavily in neutral. +5 on hit.

Crouching Medium Punch*:
Frame: 7
Ngann does a crouching knife hand swipe that’s +5 on hit and -1 on block. A helpful neutral tool with very good range that can be used as a special cancelable poke or combo extender.

Medium Kick:
Frame: 9
Ngann does a forward snap kick with his back leg that has low whiff recovery, making it quite safe to throw out. Nothing exceptional, simply a very decent poke that’s +5 on hit and -4 on block, but with enough pushback to almost always be safe.

Crouching Medium Kick*:
Frame: 8
A low hitting buffer tool Ngann can throw out in neutral to catch back walks, although he somewhat lacks safe options to cancel into besides Flash-Step for a potential mix up or Unyielding. Ngann does a low sliding kick with one leg. Quite easy to whiff punish, but has good range. +3 on hit and -5 on block.

Heavy Punch*:
Frame: 9
In a reversal of the usual roles, Ngann’s crouching heavy punch is an important combo tool, whilst his standing heavy punch is an excellent anti air. Ngann does an upward angled backfist that causes a flipout versus aerial opponents, with a decent hitbox for beating jump attacks. Whiffs against crouching opponents, but is technically Ngann’s highest damage special cancel, and a fantastic punish counter starter, as it causes a crumple on punish counter. +4 on hit and +2 on block.

Crouching Heavy Punch*:
Frame: 9
Ngann does an elbow drop with his forward arm, with rather short range. A vital combo tool that doesn’t see much use in neutral. +5 on hit and -3 on block. As a crouching normal, this move allows Ngann to build charge for either Adamance or Crusader’s Charge while using it.

Heavy Kick:
Frame: 12
A spinning kick Ngann does while pivoting on his forward heel, kicking with his other leg outstretched. A fantastic disjointed poke that’s especially good as a whiff punish, as on punish counter it sends the opponent into an aerial tailspin, letting Ngann use Flash-Step to get close and finish with Golden Sun for high damage. Alternatively, if he has charge, he can use Crusader’s Charge for lower damage but better oki, or the overdrive version for further combos. 

Crouching Heavy Kick:
Frame: 10
A somewhat below average sweep that had Ngann do a forward swipe kick with his front leg. Low whiff recovery and long range make it good for whiff punishing, but it’s -11 on block. Causes a hard knockdown on hit.

Down Back Light Kick*:
Frame: 8
Ngann does a forward moving knee strike, taking a short step forward. The main use of this command normal is to move Ngann around the screen while maintaining charge for both Adamance and Crusader’s Charge. Can also be used as a combo extender, although it offers less damage than alternatives in return for easier charge building. Has low whiff recovery, but is rather unsafe on block, being -5 and only +2 on hit.

Forward Medium Punch:
Frame: 20
Ngann pauses and solidifies his stance, then delivers a stern, overhead chop downwards with his back arm. Hits twice, and is +3 on hit and -2 on block, while striking overhead.

Forward Heavy Punch:
Frame: 15 (30)
Ngann does a forward moving palm strike with both hands. A slow but powerful counter poke with a very disjointed hitbox, but somewhat short range. On block it is -4, but with really high pushback. Can be charged by holding down the button, which greatly slows its startup, but makes it +4 on block. Can be used as an interceptor for forward advancing moves thanks to its disjoint, and is very rewarding on hit, leaving Ngann +6. Also useful as a meaty tool thanks to its high number of active frames, which can leave the uncharged version 0 on block and the charged version a massive +8 if it hits on the very last frame. The charged version causes a spin state on hit, letting Ngann combo into lots of options. Especially useful in combos using Willpower Overdrive, where after certain afterimage attacks, Ngann has time to land the charged strength, opening up his combo routes significantly.

Forward Throw:
Frame: 5
Ngann knocks aside his opponent’s guard, then teleports far above them, offscreen, and slams down with a hammerfist onto them, knocking them into the floor, where Ngann then backs off. Grants generally poor Oki, but let’s Ngann get pressure in the corner.

Back Throw:
Frame: 5
Ngann knocks aside his opponent’s hands, teleports behind them, and hits them with a powerful punch to their spine, knocking them away. Grants poor Oki, and leaves Ngann midscreen.

Flash-Step:
(Quarter Circle Back + Kick)
A command dash that forms the crux of Ngann’s gameplan, leading to combos, mixups, and just generally granting him fantastic mobility. Ngann shimmers slightly, dimming and fading, almost blurring into the background, not enough that he becomes invisible but just enough to become slightly translucent, and appears to teleport forward, leaving a trail and an afterimage in his wake due to the speed of his dash. If Ngann is close enough, this dash can even cross through opponents to hit opponents from the other side, as Ngann will automatically turn around before performing any of the follow ups. Has several follow ups, and additionally, the strength of move used changes the properties.
Light: Ngann performs a short dash forward, with lightning quick startup and low end lag, but low travel distance. Will never cross up the opponent. Can be snuck in for pressure resets versus opponents who aren’t paying attention.
Medium: Ngann does a pretty decent dash, a little shorter than his forward dash. Can cross up the opponent if Ngann is close enough to touch the opponent by the end of the dash, he will automatically go a little further to cross them up.
Heavy: Ngann does a dash with slightly more range than his forward dash, albeit only slightly.  Has the same cross up feature as the medium version.
Overdrive: A lightning quick dash with the same distance as the medium version but the speed of the light version. Similar to the light version, cannot cross up. Has complete projectile immunity until it finishes.
Follow Ups:
Falling Ladder (Forward + Punch): A ground pound that works as a slow but functional overhead, which means it can always be interrupted, and will never form a frametrap or blockstring. In return, it’s unusually rewarding for an overhead, being +4 on hit, letting Ngann link after it, while only being -3 on hit. Ngann leaps forward in a tucked in roll and slams his fist into the ground. This little hop lets him jump over low attacks or throws and counter them, although because it counts as an aerial attack it can be anti aired. On punish counter, this causes a ground bounce, but Ngann’s follow ups are very limited, essentially only Adamance or light Unyielding, 
Golden Sun (Back + Punch): Ngann extends the dash slightly, clenching his fist, and at the end of it, unclenches his fist, unleashing a large, orb shaped aoe of light around it that acts as a decently disjointed move, great for checking opponents buttons and acting as a stop sign in neutral. Causes a knockdown on hit with quite high damage, which Ngann can chase, but is -12 on block with low pushback, making it unsafe at almost all ranges. Also a strong ender that will frametrap and combo from normals if light Flash-Step is canceled into (except from light normals, which can be interupted). On punish counter, causes a wall splat, leading to high damage. 
Flip (Forward + Kick): Ngann does a flip forward, which functions similarly to a forward jump and can be canceled into any jump normal, or can be used to bait out attacks. Can also hop over the opponent, which lets Ngann get a cross up jumping normal for a full combo. The flip travels at a lower angle than his forward jump, and goes farther, which can make it tricky to anti air.
Crushed Beneath (Forward + Kick): Ngann performs a forward moving low sweep, doing a circular low kick with his forward leg. Slow, but can low profile and can catch opponents who are moving backwards. Also a decent combo ender that trades the damage from Golden Sun for a better knockdown. -4 on block, but can be spaced to be safe. Causes a hard knockdown on hit.

Crusader’s Charge:
(Charge Back > Forward + Punch)
Ngann pulls back, flashing brightly and shimmering as though the camera can’t keep up with his speed and is flashing frames, and performs a dashing straight punch which he fully leans into. Has use as a combo extender, ender, and general neutral tool for harassing in the midrange. In general, this is (usually) Ngann’s best combo ender, granting fantastic oki, and some of the highest corner carry in the game, meaning whenever he can he wants to use this move to push the opponent to the corner.
Light: An extremely strong neutral tool, light Crusader’s Charge starts up lightning quick, and covers a rather large distance, equivalent to a solid poke. To compensate, it is -10 on block with almost no pushback. Links from light normals, and causes a knockdown on hit with rather good oki, as Ngann can double dash forward to be right in front of the opponent and plus. On punish counter, this move causes a wall bounce, making it a very rewarding whiff punish, especially considering its quick startup. The main downside to this move is the fact it requires charge, which means Ngann doesn't always have access to it.
Medium: Combos from medium normals, with fantastic corner carry. Ngann surges forward and performs a powerful straight punch with great oki. Mostly used as a combo ender. Causes a knockdown on hit and is -10 on block.
Heavy: Ngann quickly surges forward, leaving cracks in the ground, and once he reaches the opponent, he crosses behind them before delivering a stern straight fist. Sends the opponent flying away on hit, causing a knockdown with rather poor oki unless it corners them, and is safe on block at -3, although its low pushback leaves Ngann vulnerable to a strike throw mixup. Ngann can travel up to half screen while performing this move, but will instantly stop once he reaches the opponent to perform the aforementioned cross up. If Ngann doesn’t reach the opponent, he will simply stop, meaning this can be used after some knockdowns to get oki. To make up for its safety on block, it doesn’t combo from any normals without a counter hit, and is only able to be used as a combo finisher after a juggle.
Overdrive: Ngann performs the standard dash forward, but this one causes a wall bounce, allowing follow up combos. Combos from medium normals, and is one of Ngann’s most pivotal combo extenders (especially when combined with super 2).

Adamance:
(Charge Down > Up + Punch)
An uppercut that functions as a reversal, good combo ender and an excellent anti air, only somewhat held back by its charge requirement, meaning if Ngann is looking to anti air with a special, he can’t move, and his lack of a projectile means he struggles to force opponents to jump at him.
Light: A short, quick, leaping uppercut. Causes a knockdown on hit, but in combos is held back by very poor forward movement. Due to its upper body invincibility and quick startup, it’s a fantastic anti air. Very unsafe on block.
Medium: Similar to the light version but with worse startup, and higher damage. It also moves forward more, making it better in combos but worse for anti airing close jumps. Causes a knockdown on hit, incredibly unsafe on block.
Heavy: Really slow startup, only comboing from heavy normals, and moves very far forward, making it guaranteed to connect from grounded combos, but struggled with anti airing due to the above described features. Does the highest damage of any of Ngann’s combo enders. Causes a knockdown on hit, incredibly unsafe on block.
Overdrive: Ngann does a spinning, multi hit uppercut. Fully invincible until it hits. Quite good forward movement, but is absolute death on block like most reversals. Grants no oki on hit, fully resetting to neutral.

Unyielding:
(Dragon Punch + Punch)
Ngann pulls both arms to his side briefly, charges for a moment, and then unleashes a flurry of punches faster than the eye can track, forming a wall of impacts directly in front of him. A powerful move that is used to set up frametraps and also as a combo extender, although it has rather short range and somewhat high pushback on block. All versions also destroy non overdrive or super projectiles on hit, which will instantly cancel the move, letting Ngann close in on opponents attempting to zone him. While performing all versions, Ngann can mash punch buttons to change the properties of the move.
Light: Ngann’s flurry of punches also have him sliding forward, making this version difficult to space. Combos from medium normals, and frametraps from heavy ones. -5 on block, so while it’s difficult to space, Ngann isn’t usually punished too much for using it. Causes a knockdown on hit, unless Ngann mashes, which will instead leave the opponent standing and Ngann +4, letting him combo after it, although the pushback is so high that only a single jab will connect, meaning Ngann must be airtight with his charging for moves like Crusader’s Charge and Adamance.
Medium: Ngann charges extra long, and lunges forward before performing the punch rush. High damage, combos from heavy normals. Launches the opponent on hit, but sends them too far for any combo unless Ngann is in the corner, in which case he can combo into heavy Adamance for high damage. If mashed, the opponent is instead left in place and Ngann is left +5 point blank, letting him chain a few jabs before finishing.
Heavy: Combos from punish counter heavies, and will never frametrap, but can be used as a tricky reset option, as it’s +2 on block with low pushback. On hit, Ngann finishes the flurry punch with a slap to the head that leaves Ngann +7. The mashed version causes Ngann to finish with an uppercut that sends the opponent into an aerial tail spin while also doing higher damage.
Overdrive: Combos from heavy normals, and is just about safe on block at -3. On hit, Ngann is left +4 and point blank. If mashed, causes a hard knockdown with great oki. Most notably gives Ngann a safe way to activate Willpower Overdrive, as doing it on block leaves him +5 and doing it on hit leaves him +9.

Super 1:
Royal Treatment:
(Charge Back > Forward > Back > Forward + Punch)
“Fall!”
Ngann charges his back fist with golden energy, then charges forward and does a single, explosive golden straight punch. Has no invincibility, and boasts about the same startup and travel distance as light Crusader’s Charge. On hit, sends the opponent flying away with high damage. On punish counter, however, causes a crumple, meaning that this is technically Ngann’s optimal punish starter, letting him combo into whatever he wants while applying no scaling whatsoever. -8 on block, but can be spaced to be safe, or better yet, set up a spacing trap.

Super 2:
Willpower Overdrive:
(Double Quarter Circle Backward + Kick)
“For the king…”
Ngann raises both arms crossed above his head, then slams both down by his sides before returning to his idle pose, glowing brighter than before. This activates an install which causes an afterimage of Ngann to begin following behind him, with about a 2 second delay between Ngann’s actions and itself. This afterimage cannot be damaged or hurt in any way, but any attacks it performs also have a hitbox, although they do about 50% less damage than Ngann himself. This afterimage also ignores the typical “1 wall bounce/splat/slump etc. per combo” rule, meaning he can perform multiple combo extensions using it. After around 7 seconds, this afterimage will disappear and Ngann will stop glowing. This super opens up countless opportunities for Ngann, including but not limited to:
Comboing off of forward medium punch by setting up an attack with a lingering hitbox beforehand (such as Unyielding).
Making all versions of Crusader’s Charge frametrap, as the afterimage will strike with a delay.
Allowing two wall bounces in a combo, as overdrive Crusader’s Charge has the exact right timing so that the afterimage will strike once the opponent comes flying back, causing another wall bounce.
Allows any higher strength of Adamance to combo into a lower strength (heavy -> medium, medium -> light) as the afterimage will hit the opponent at the top of the attack, keeping them airborne just long enough to land another attack.
Set up ambiguous left right mixups using either Flash-Step, Flip, or heavy Crusader’s Charge.
Essentially infinite plus frames.
Overall, this is just one of the best supers in the game, and a vital tool Ngann relies on heavily.

Super 3:
Hand Of The King:
(Double Quarter Circle Forward + Kick)
“This is your end!”
Ngann performs a lunging knee forward. On contact with the enemy, triggers a cinematic where the camera pans around the opponent, showing Ngann continuously dashing through them, the opponents body getting knocked around in different directions. Finally, the camera pans to behind the opponent, where Ngann performs one final dashing punch through them, after which the opponent crumples to the ground as Ngann turns around to face them. The freeze frame on kill with this super shows multiple afterimages of Ngann dashing through the opponent, the camera unable to keep up with his speed. Leaves the opponent midscreen and causes a hard knockdown, letting Ngann easily pursue the enemy due to his great movement.

Critical Art:
Heaven’s Touch:
“You have fought well.”
Ngann performs a lunging knee forward. On contact with the enemy, triggers a cinematic where Ngann begins running circles around the opponent, the camera following him as he begins glowing brighter and brighter, leaving continuous afterimages behind him. The opponent begins turning in confusion, unable to track Ngann due to his mounting speed, and with one final closeup of Ngann, now shimmering with raw, uncontrollable power, he dashes into the opponent, slamming his fist into their gut. The camera replays this moment from 3 different angles, and finally, the opponent erupts with golden magic, a massive explosion detonating outward. The freezeframe on kill shows an overhead shot of this massive explosion, with only the vague silhouette of Ngann and the opponent inside. Grants the same oki as the base version.

Win Quotes:
(vs. Zenthos) “What is this crusade you speak of? Surely the king has not sanctioned this…”
(vs. Kalle) “Child, please, abandon this power. I have seen it destroy much stronger than you.”
(vs. Vile) “This war ends the only way it could have.”
(vs. Melancholia) “Your devotion to battle sickens me. This fight is a means to an end, not a goal to achieve.”
(vs. Ngann) “For the king!”
(vs. Beast) “Forgive me, Lord Beast. But you have served your purpose.”
(vs. Gauss) “Gauss, my friend, how did you escape?! Where… oh no.”
(vs. Salazar) “You do not fully devote yourself to your cause. It is no wonder you lost.”
(vs. Laecaera) “You are improving. Next time I meet Gauss, I will ask him if I may train you formally. ”
(vs. Alphard) “You may have been granted amnesty, but some of us have long memories, and more importantly, dead friends.”

Vile:
Icy Lord of All
“All is mine.”
Archetype: Zoner
Powerful Zoning
Great Pokes
Setplay
Dominant Anti Airs
Monstrous Midrange
NO Reversal (Except Level 3)
Lingering Hurtboxes
No Plus On Block Normals
Slow Movement
Low Damage Without Setplay

Light Punch*:
Frame: 4
Vile does a short jab in front of himself with his forward arm. Has rather poor range. -3 on block and +4 on hit.

Crouching Light Punch:
Frame: 4
Vile does a short, low jab with his forward hand. +4 on hit and -1 on block.

Light Kick:
Frame: 6
Generates 5 chill on hit
Vile does a short claw swipe that hits mid. Excellent range for a light. +3 on hit and -3 on block. Like all of Vile’s kick normals, if light kick whiffs it leaves a massive, lingering hurtbox for a few frames, which makes it relatively easy to punish if whiffed. Comes with a target combo with light kick.
Light Kick (TC):
Generates 5 chill on hit
Vile performs another claw swipe with his other hand. Forms a true block string with light kick. -3 on block, leaves the opponent standing and +2 on hit. Has a target combo with light kick.
Light Kick (TCC):
Generates 5 chill on hit
Vile performs a final, slashing claw swipe. Has a good amount of forward movement and leaves the opponent standing on hit and leaves Vile point blank and +1. Is -6 on block. This full target combo is also a decent way for Vile to build chill, as the full string builds 15.

Crouching Light Kick*:
Frame: 5
Generates 5 chill on hit
Vile performs a short, crouching claw swipe. A great button with fantastic range considering its quick startup, and shockingly low end lag. A great buffer tool in neutral Vile can usually just throw out risk free. Unfortunately, to compensate for all these strengths it doesn’t hit low, and none of Vile’s lights have enough hitstun to naturally link into it. +2 on hit and -4 on block.

Medium Punch*:
Frame: 7 (12)
Vile does a short, stomach level jab with his forward hand, then performs a step forward and a straight punch with his back hand. Both hits benefit from counter hit and punish counter frame advantage. Only the second hit is special cancelable. +4 on hit, -2 on block. While the second hit has decent range, the fact that the first hit must be performed makes it a pretty slow poke considering it’s mediocre range. Has two separate follow ups that Vile can choose from. Vile’s main mix tool after setting up Frozen Fear.
Forward Heavy Punch (TC):
Vile clutches both hands together and delivers a stern overhead to the opponent. Slow startup, like most overheads, making it possible (albeit difficult) to react to. Does not frametrap or naturally combo off of standing medium punch, and can be interrupted with any 4 frame normal. Cannot be blocked low. +2 on hit, but with very very large pushback, leaving Vile completely outside throw range. -6 on block, with low pushback, making it easy to punish. An unsafe, low damage, interruptible overhead sounds worthless, but it’s high pushback actually is a massive upside: if Vile sets up Frozen Fear behind the opponent, the large pushback of this move will knock the opponent into the ice block, bouncing them back and allowing Vile to combo into crouching heavy punch or other extenders for high damage.
Down Heavy Kick (TC):
Vile quickly throws a shadows behind the opponents legs, then yanks it back. Hits low, +3 on hit with high pushback. -9 on block. Frame traps and combos off of standing medium punch. Can knock opponents into Frozen Fear the same as the forward heavy punch extension. Is unreactable, and much faster than the other extension.

Crouching Medium Punch*:
Frame: 8
Vile does a stomach angled swipe with his forward hand. Has rather good range to make up for its poor startup. A very good poke that combos into medium/overdrive Arisen, +2 on hit and -5 on block.

Medium Kick*:
Frame: 9
Generates 10 chill on hit
Vile does a forward swipe with his hand, and along with it swings a large, sharpened tendril of shadow, greatly increasing its range. An incredible button, plain and simple. Absolutely incredible range for a 9 frame button, better than most characters' heavy normals. Low whiff recovery for a kick button, special cancelable, massive range, relatively quick startup, all of this comes with one massive downside: this move can be ducked under, and if it is, Vile is left punishable. This is a pretty big deal, but the move is still incredible. +2 on hit and -3 on block. Combos into medium/overdrive Arisen, but is otherwise kinda lacking in terms of combo potential.

Crouching Medium Kick:
Frame: 10
Generates 10 chill on hit
Vile throws forth a low, horizontal slash made from a shadow tendril. Fantastic range to compensate for it’s poor startup, equivalent to most characters sweeps, with a large, disjointed hitbox. Has a lingering hurtbox while recovering, making it easier to whiff punish. Hits low, and is a fantastic poke for keeping opponents out and making them scared to approach Vile. +1 on hit and -3 on block.

Heavy Punch*:
Frame: 10 (15)
Vile performs a short ranged two hit strike with his fists, performing a right hook with his forward hand into an uppercut with his back hand. Both hits can be special canceled. The first hit keeps opponents grounded, whilst the second hit launches them, allowing Vile to choose whether to go for a grounded or launched combo. Vile moves slightly forward while performing the move. -6 on block. The second hit combos into the slash of Shadow-Shape, which launches high enough for vile to combo into Halt, which carries the opponent along, giving Vile time to set up Frozen Fear or distance to zone his opponent.

Crouching Heavy Punch*:
Frame: 9
Vile does a crouching, upward angled elbow with his back arm. Has two hits, the second of which can be special canceled. Launches on hit, and is Vile’s main way to start juggle combos, leading to powerful juggles into medium Arisen that can be finished with Rime’s Greeting. -10 on block. On punish counter, this move launches extremely high, letting Vile use heavy Arisen instead for significantly better juggles and higher damage. After the opponent connects with Frozen Fear and bounces back towards Vile, crouching heavy punch is usually the best way to extend combos.

Heavy Kick*:
Frame: 13
Generates 10 chill on hit
Vile performs a forward advancing claw swipe, with better range than standing medium kick, however this cannot be ducked under. To compensate for its great range, it’s very slow, and has a large lingering hurtbox if whiffed. +2 on hit and -5 on block. Has a target combo with heavy punch. This target combo is extremely easy to hit confirm.
Heavy Kick (TC)**:
Generates 10 chill on hit 
Vile leaps forward, performing a 2-hit spinning slash with his back arm. Always guaranteed to connect from the starter due to the massive leap forward Vile takes. Easy to hit confirm, this move can be canceled into supers, and grants enough time to build up charge for Inevitable. It also causes a knockdown on hit if it isn’t canceled, although it sacrifices its ability to perform special cancels in return. -12 on block.

Crouching Heavy Kick:
Frame: 13
Generates 10 chill on hit
Vile sends a shadow tendril out forward at a low angle, then casually pulls it back once it reaches the ground. The shadow then slides across the ground back towards him. Only the slide back has a hitbox. Causes a hard knockdown and is unsafe on block at -7, although it can be spaced to be safe. Hits low. Better range than most sweeps, and much safer on block, but with higher startup. High whiff recovery.

Back Medium Kick:
Frame: 12
Generates 10 chill on hit
Vile performs a diagonally upward angled slash with his arm, with a huge claw of darkness accompanying it and extending its range greatly directly above and diagonal to Vile. One of Vile’s most reliable anti airs, with a huge, disjointed hitbox that causes a knockdown on aerial contact. Cannot hit grounded opponents, and is unsafe if whiffed. If Vile knocks someone out of the sky and into Frozen Fear, the opponent will bounce back towards him, allowing him to extend the combo with crouching heavy punch or other moves.

Forward Heavy Kick:
Frame: 24
Generates 10 chill on hit
Vile does a huge step forward, and pulls back a huge claw of shadow from behind himself, forms it into a fist, and slams it down in a hammer strike. Hits overhead, and has great range. -9 on block but has great range and can be spaced to be safe a lot of the time. Causes a knockdown on hit, sending the opponent flying away to let Vile set up his zoning (or bounce them into Frozen Fear). On counter hit or punish counter, causes a ground bounce with limited follow ups. High whiff recovery with a large, lingering hurtbox.

Down Back Heavy Kick:
Frame: 12
Generates 10 chill on hit
Vile performs a long, swinging, claw uppercut, dragging his dark claw across the ground behind him, before ripping it upward in front of him, with an enormous hitbox that stretches in front of him, hitting about half screen away before finishing with an aerial hit. +6 on hit and -6 on block, but due to high pushback is essentially always unpunishable if spaced well, only being truly punishable if used close to the opponent. On counter hit or punish counter, launches the opponent with limited follow ups like Rime’s Greeting. Its enormous range makes it a fantastic poke, and its upward slash allows it to be used as a slow but reliable anti air, which causes a knockdown against airborne opponents. Also a decent combo ender from some routes. Is rather vulnerable to armored moves due to only being 1 hit and having pretty decent end lag, with a large, lingering hurtbox if whiffed.

Forward Throw:
Frame: 5
Vile reaches out with his forward arm, and grabs the opponent by the neck. Shadows then lunge out from behind his shoulders and strike the opponent, punching them out of Vile’s hand and sending them flying away. Sends the opponent a great distance away, and uniquely, if the opponent hits an ice block created by Frozen Fear after being launched, they will be hit, locking them in place and allowing Vile to combo, albeit with heavy scaling applied.

Back Throw:
Frame: 5
Vile grabs the opponent by the neck, and delivers a stern punch to their face before throwing them behind him. Has the same properties as forward throw regarding Frozen Fear.

Unique Mechanic:
Chill:
Some of Vile’s specials and all kick normals fill a bar called Chill. The bar has 125 points and drains at a rate of 2 points a second, and is also consumed by some of Vile’s moves.

Arisen: 
(Quarter Circle Forward + Punch)
All strengths generate 10 chill on use
Vile’s base zoning tool and an excellent tool for controlling neutral. Vile performs a low underhand swipe, raising up an amalgamation of bones that takes the form of a stumbling whirlwind of bones, constantly forming into a skeleton and falling apart only to reform as it marches forward, clawing at the opponent. An excellent projectile that covers an enormous amount of space and slowly travels forward, its only weakness being rather high recovery, and that it clashes with ground based projectiles. Staggers opponents on hit, and can be used as a semi safe block string ender.
Light: A feint Vile can use to trick opponents into committing to a jump or other option, and then punish. Vile performs the claw swipe, but the skeleton only briefly pokes up from above the ground before immediately dissolving, and has no hitbox whatsoever. Vile recovers from this feint extremely quickly, but it has only slightly slower startup than the medium version, so it does leave him somewhat vulnerable.
Medium: The basic version of the projectile. Functions basically identically to how it’s described above. Combos off of any cancelable normal. Also a great juggle extender after crouching heavy punch, where it can be used to relaunch the opponent and allow Vile to connect Rime’s Greeting. Leaves the opponent standing, but generally leaves Vile out of range for any combo or mixup.
Heavy: Vile performs a double claw swipe, taking a step back as he does so, raising two separate whirlwinds, with the second traveling slightly behind the first. Has really slow startup and even slower recovery, meaning it cannot be used safely as a block string ender, as it can always be interrupted, and has extremely limited combo application, though it can be connected after punish counter crouching heavy punch. Obviously being able to summon two projectiles at once is incredibly strong, letting Vile destroy non overdrive projectiles and still push through. Due to the step back Vile takes while performing it, can also be somewhat difficult to jump in on, although Vile does leave a lingering hurtbox shortly after the step.
Overdrive: Vile raises his arm like a pillar, and raises an actual skeleton which charges forward, destroying all non overdrive projectiles in its way. It has identical startup to the medium version, meaning they both combo from the same moves. The skeleton moves extremely quickly, running towards the opponent, and once it reaches them, it performs a flurry of three claw swipes, which causes a knockdown on hit or grants plus frames on block. A plus on block block string ender, great combo tool, extremely fast moving projectile, just a great move overall.

Rime’s Greeting:
(Charge Back > Forward + Kick)
Vile lunges forward, performing a slide across the ground with his feet sliding across ice and with a spear of ice held low, similar to sub zero’s slide from mortal kombat. A good burst movement tool and Vile’s primary combo ender.
Light: A feint/backdash Vile can cancel into. Vile readies the same spear, but instead dashes backwards, sliding across a path of ice he creates for himself. The length of the backslide can be extended by holding the button down, Vile will continue sliding until the button is released. Has rather lengthy recovery, but quick startup.
Medium: Vile sends out a clone formed of ice that performs the lunging slide for him and travels about midscreen. A pretty bad projectile with slow startup and end lag, but a great combo ender that causes a knockdown on hit, sending the opponent away from Vile and letting him zone effectively. Massively unsafe on block. Technically, this move launches, but Vile recovers too slowly to land another hit afterward. The only way Vile can continue a combo after this move is if the opponent lands on a projectile, such as Arisen or Frozen Fear, which grants a continued juggle.
Heavy: Vile performs the lunge himself. A decent burst movement tool that sacrifices positioning for slightly higher damage, and can also combo into Vile’s level 3 super unlike the medium version. -20 on block, knocks down on hit. Also used to get close to the opponent after a hard knockdown and set up Frozen Fear.
Overdrive: Functions similarly to the heavy function, but causes a hard knockdown, allowing Vile to set up Frozen Fear.

Shadow-Shape:
(Quarter Circle Forward + Kick)
Vile does a slash through the air with his forward hand, leaving a lingering cut of shadows in the air which he can then manipulate further. This slash of shadows can dispel enemy projectiles, and also boasts a hitbox, making it good for combos, although its -6 on block with low pushback, and only +2 on hit (although it can frametrap and combo into some of the follow ups). This initial slash only has one strength, but by pressing any of the following kick buttons after the slash, Vile will perform a follow up. If Vile presses nothing, he will only do the initial slash.
Normal: Vile performs the basic slash, as listed above. Can destroy basic projectiles.
Overdrive: The overdrive version is safer on block at -3, and launches on hit, letting it combo into any of the follow ups. Can destroy any non super projectiles. Also grants all follow ups overdrive properties, allowing them to clash with overdrive projectiles.
Follow Ups:
Bore (Forward + Light Kick): Vile drags his hand through the shadow, forming a sharp spear, then pulls it back before throwing it like a javelin forward. A decently fast traveling projectile that compliments Vile’s other zoning tools and pokes nicely, and also both frametraps and combos from the starter. Quite a lot of endlag, making it unsafe on block up close. Causes a knockdown on hit.
Pierce (Forward + Medium Kick): Vile places one hand into the shadows, then places the other into it and stretches it back, almost like he’s readying a bow, stretching out the shadow like elastic. He then releases his grip, sending the shadow flying forward like an arrow. Incredibly quick travel speed makes this function like a jumpscare in neutral, although it has slow startup to compensate.
Halt (Forward + Heavy Kick): Vile plunges both hands into the shadow slash, then stretches it open, forming a wide grid of black shadows, almost waffle like. Vile then pushes it forward, which sends it traveling forward slowly. Moves much more slowly than Vile’s other projectiles, and acts as a nice supplement for his zoning. To compensate, has much greater startup and endlag than the other follow ups. Very plus on block, and leaves the opponent standing on hit, letting Vile potentially combo them. Hits three times, carrying airborne opponents along with it for great corner carry.

Shadowstep (Forward):
(Forward + 3 Kicks)
Vile steps into the background as shadows engulf him. He then reappears about half screen ahead his original position, stepping back into the stage before returning to his idle stance. If an opponent is in the way of this teleport, Vile will cross up the opponent, which can be useful for getting behind them in order to sandwich them between Vile and Frozen Fear. Unfortunately, it has very slow startup that leaves Vile very vulnerable. To make up for this, its endlag is very low, letting Vile instantly get back to work once he’s finished teleporting.

Shadowstep (Backward):
(Back + 3 Kicks)
Vile steps into the background as shadows engulf him. He then reappears about half screen behind his original position, stepping back into the stage before returning to his idle stance. Used as a tool for getting away from an opponent, helpful for setting up Vile’s zoning or returning to midrange. Unfortunately, it has very slow startup that leaves Vile very vulnerable. To make up for this, its endlag is very low, letting Vile instantly get back to work once he’s finished teleporting.

Frozen Fear:
(Quarter Circle Backward + Kick)
Consumes 50 Chill
Vile claps, then pulls his hands apart vertically, pulling up a large block of ice slightly taller than he from the ground in front of him. This move has very slow startup, meaning it can only be safely used at fullscreen or after a knockdown. The strength of the button used dictates where the ice block is placed. The ice block has 3 hits of projectile durability, and hits 3 times, and is destroyed if all hits are consumed, or if it comes in contact with a super or overdrive projectile. The ice block is also destroyed automatically after being up for more than 4 seconds. Vile can manipulate the ice block using his punch normals or special moves, which can dictate the properties of the block of ice. He can always do this, no matter how much or little durability the ice block has. On hit, the ice block does its 3 hits of damage, and then bounces back the opponent in the direction they came from. By setting up the block of ice behind an opponent and pushing them into it by striking them, Vile can set up dangerous mixups utilizing the blockstun created by pushing the opponent into the 3 hits of the ice block. On hit, these mixups push the opponent back towards Vile, letting him link into combo starters like crouching heavy punch. Up to 2 blocks of ice (altered or otherwise) can exist at a time. Frozen Fear is Vile’s win con, after building up enough Chill it allows him to switch the gameplan from zoning to mixups and deliver staggering damage to the opponent, or strengthen his zoning further by manipulating it with normals and specials. If Vile attempts to use this move without 50 Chill, nothing happens.
Light: “Close.” Places the ice block directly in front of Vile.
Medium: “Near.” Places the ice block about a character length ahead of Vile.
Heavy: “Far.” Places the ice block two character lengths in front of Vile.
Overdrive: “Air.” Places the ice block at about the same distance as the medium version, but it goes much higher, reaching up above Vile. Useful for blocking out aerial approaches.
Interactions:
Light Punch: Vile’s first jab causes the block of ice to shake slightly, but if hit twice by a jab, the ice block shatters, laying shards of ice across the ground in front of him. These shards stay on the ground for a few seconds, then spear upwards, dealing damage and launching opponents. Functions as a trap Vile can use to pressure those trying to approach him, or he can set them up underneath an opponent who is waking up from a knockdown.
Medium Punch: The first strike causes the ice block to form spikes on the other side of it, and the second blow causes it to slide forward, turning it into a projectile. On hit, this projectile knocks down opponents. It has two hits of projectile durability, and shatters when it hits or is blocked. It moves much slower than Vile’s other projectiles, letting him set up for more zoning.
Heavy Punch: Vile’s first strike shatters the ice block into 2 balls, which hovers in air, and the second uppercut launches them upward, sending them up at a vertical angle before they quickly descend in an arc. A good move for pressuring the opponent and also locks down the air, preventing opponents from jumping at Vile. Knocks down airborne opponents and staggers grounded ones. The two balls hit at different intervals, allowing Vile to apply staggered pressure to the opponent.
Arisen: Functions the same for all strengths of Arisen except the light version, which will not interact with the ice block. Once the projectile does any of the following: makes contact with the ice block / makes contact with the enemy (whether or not they’re blocking) / makes contact with another projectile, the block of ice will sprout bones and skulls inside itself. This block of ice begins sliding backwards in the opposite direction from which the original Arisen projectile came, striking opponents from behind or acting as a shield. This block of ice travels at the same speed as medium Arisen, regardless of the strength used. While the block of ice collides with enemy projectiles, it ignores projectiles Vile creates. This is fantastic when combined with juggles off of crouching heavy punch, as when the skeleton charges back it relaunches the opponent, allowing Vile to connect 2 Rime’s Greeting (once when the projectile first connects and once on the rebound) instead of the usual 1. The ice block will continue to slide through Vile until it gets offscreen, at which point it despawns.
Rime’s Greeting: If Vile dashes into the block of ice using any strength of Rime’s Greeting other than light, he will push the block forward, disabling its collision as it rushes forward ahead of him. Because the block of ice has no hitbox while it’s moving like this, Vile can use this to easily maneuver the block of ice to get it behind his opponent, activating his setplay.
Shadow-Shape: If Vile strikes the block of ice with the initial slash, it creates a bubbling black shadow within the ice that rapidly begins growing and expanding, frothing within the frozen cube. After about 5 seconds, the block will then detonate into a massive explosion of whirling shadows and ice shards that hits multiple times and causes a hard knockdown while doing both high damage on hit and high chip damage on block. Additionally, if Vile does any of the follow ups (Bore, Pierce, or Halt), instead of performing the follow ups, he will push the ice block forward, briefly disabling its collision and pausing the detonation timer. The strength of follow up used determines how far the ice block slides (keep in mind that due to its collision being disabled, it can slide behind opponents), with Bore sending it the least far, Pierce sending it a decent distance and Halt sending it hurtling away.

Super 1:
Blizzard Born:
(Double Quarter Circle Forward + Punch)
“Experience oblivion!”
Vile floats upward into the air, crosses his arms, then unfolds them, unleashing a large circular blizzard around him that hits multiple times, locking opponents in place, before he finishes with a single, large blast of ice. A rather high damage combo ender that sends the opponent flying away, letting Vile set up his zoning. Has a large, disjointed hitbox all around Vile, and is only -12 on block with great range, meaning even if blocked it can usually be safe. Also possesses rather quick startup and upper body invincibility to jumping attacks, making it a fantastic, damaging anti air. Unfortunately, it boasts no invincibility, leaving Vile’s defenses very lacking.

Super 2:
Inevitable:
(Charge Back > Forward > Back > Forward + Punch)
“The end nears!”
Vile’s body becomes a whirling mass of shadows before he lunges forward in a shoulder tackle. Has a massive hitbox above and around Vile, basically guaranteeing a hit if the opponent is near and not blocking, especially if they’re in midair, and boasts upper body invincibility to air attacks. On hit, the opponent shoots into the air, borne upward by a whirling maelstrom of ice and shadow, before Vile leaps above them and performs a double handed slam to their stomach, sending them flying against the wall. If Vile is anywhere near the corner, this causes a wall splat, letting him pick up combos after it, although at midscreen it simply leaves Vile fullscreen, letting him set up zoning. Also does high damage, but doesn’t have any invincibility. Massively unsafe on block.

Super 3:
Brighter:
(Double Quarter Circle Forward + Kick)
“Now freeze!”
Vile forms a large spear of ice in both hands, then does a lunging slide forward, similar to Rime’s Greeting. This is Vile’s only invincible reversal, and as it requires all of his super, it’s obviously a last ditch resort to try and either close out a round or a desperate attempt to get the opponent off of you. On hit, Vile engages a cinematic where he places his hand on the enemies face, grabbing them by the head, and dashes forward, dragging them across the ground as he skates forward on a path of ice. After going a brief distance, Vile picks the opponent up, slams their head into the floor, and then walks off, then charges up a large ice blast around their head, finishing with a panning shot showing a large explosion of ice and shadow, which is also the freeze frame if this super kills. Vile then kicks the opponent away, granting terrible oki, but letting him zone effectively.

Critical Art:
A World In Ice:
“Suffer, as I have!”
Vile does the same lunging spear attack as the base version. On hit, engages a cinematic where Vile raises his hand in a pillar motion, rising up on a large spire of ice above the opponent as a blizzard surrounds both. The camera pans to the opponent, and shows them trying to move as their limbs slow and then shows their legs frozen to the ground. The camera pans back upward to Vile as he throws down his arm, sending forth a rain of shadow spears that impale the opponent before Vile himself descends upon them, spear gripped and pointed downward. He impales his opponent, causing them to fall to the ground, and then kicks them away, with the same knockdown as the base version.

Win Quotes:
(vs. Zenthos) “You have become what you desire to cleanse. What a cruel mirror fate displays to me.”
(vs. Kalle) “I fear not the flame within you, child. My master shall quell it, eventually.”
(vs. Vile) “… What has become of me…?”
(vs. Melancholia) “Hmph. Still not enough. Continue your training.”
(vs. Ngann) “The kings loyal lapdog lies broken at my feet. Soon, this war will end.”
(vs. Beast) “Enough of your petty rivalry. Alatar serves me, and now, so shall you.”
(vs. Gauss) “Alatar’s greatest failure, manifest. As usual, I must clean up his mess.”
(vs. Salazar) “Sniveling sycophant. I suppose this was inevitable.”
(vs. Laecaera) “Gauss is gone child. Now you shall go to meet him.”
(vs. Alphard) “You always were weak.”

Melancholia:
Relentless Crimson Valkyrie
“How many times can you guess right?”
Archetype: Rushdown
Fast
Insane Pressure
High Low Mix
Great Oki
Corner Carry
Meter Hungry
Very Poor Range
Poor Defence
Self Destructive
Poor Neutral

Light Punch*:
Frame: 4
A quick forward jab melancholia performs with her front hand. Longer ranged than crouching light punch, but otherwise unremarkable, being -3 on block and +4 on hit.

Crouching Light Punch:
Frame: 4
A quick ducking elbow. Has short range, but is +5 on hit, letting Melancholia link into medium punch target combo for fantastic corner carry and respectable damage. -1 on block. 

Light Kick*:
Frame: 5
Melancholia performs a forward step kick. Uniquely for a light, Melancholia actually advances forward a decent amount while performing this move. Mostly used as a whiff punish or -5 punish, as Melancholia’s longest ranged light and has greater range than both of her medium punches. Low damage to compensate. +1 on hit, and -4 on block.

Crouching Light Kick:
Frame: 5
Melancholia does a low thrust kick. Unremarkable, but hits low, and can chain into crouching light punch. -2 on block and +3 on hit.

Medium Punch*:
Frame: 5
An incredibly fast elbow thrust melancholia performs with her front arm. To make up for its very fast startup, it has very short range. +3 on hit, -3 on block. Has a target combo with heavy punch.
Heavy Punch (TC)*:
Melancholia pulls her elbow back in and then swings her fist horizontally. Launches the opponent on hit, and frametraps from standing medium punch. -10 on block. This launcher can combo into a variety of follow ups, making this target combo Melancholia's main combo extender. Notably, combos into medium Sinful Briars for damage, and both damaging Into The Fray follow ups, with the heavy follow up usually being superior unless Melancholia wishes to cancel the medium follow up into a super. The only notable thing is that in the corner, Melancholia can connect Back Heavy Kick after heavy Sinful Briars, granting her great damage, and making her corner presence rather threatening.

Crouching Medium Punch*:
Frame: 6
A rather stubby crouching chop swipe Melancholia performs with her forward hand. +3 on hit, -3 on block. Has use as a six frame punish, and occasionally as a poke.

Medium Kick:
Frame: 8
A quickish thrust kick melancholia steps forward while performing. One of Melancholia’s only buttons that actually has decent range, due to the large thrusting kick in addition to the step forward she takes. Useful as a poke, and grants powerful combos when combined with Thorn Rush. +3 on hit, and -3 on block.

Crouching Medium Kick:
Frame: 7
A strong crouching medium kick Melancholia performs by balancing herself with one arm and throwing one leg out thrusting style. Has shorter range than most crouching medium kicks, to make up for its faster startup. +5 on hit, -4 on block. Is not special cancelable, but can be cancelled into Thorn Rush, giving Melancholia a powerful low starter if she’s willing to burn some of her hp.

Heavy Punch*:
Frame: 7
Melancholia does a sideways backfist. While held back by its poor range, its fast startup combined with ample combo routes it can go into make it a great combo tool. +5 on hit, -1 on block. Has a target combo with back heavy punch.
Back Heavy Punch* (TC):
Melancholia leans back slightly then delivers a swift headbutt. Frametraps off of the starter and can punish people attempting to mash on Melancholia, and has the same frame data and combo routes as standing heavy punch. Naturally combos from the starter, tacking on more damage to Melancholia’s confirms.

Crouching Heavy Punch*:
Frame: 9
Melancholia does an upwards angled open palm strike with her front fist. A decent panic anti air that causes a flip out against aerial opponents, and better combo tool. Short ranged, but can combo into overdrive Sinful Briars, starting melancholia’s devastating jumping medium punch combos. 0 on hit, -4 on block.

Heavy Kick*:
Frame: 15
Melancholia performs a short hop and a forward advancing hop kick. Melancholia is technically considered airborne during this attack, meaning this move can only be special canceled into aerial specials, and cannot be canceled into Thorn Rush. Can hop over low attacks. +3 on hit, -4 on block with high pushback. Canceling into Shards of Agony from this move leaves the opponent standing, which can grant a combo at certain spacings, and Sanguine Slash (Air) grants a knockdown. The only notable cancel is overdrive Shards of Agony, which causes a ground bounce, allowing further combos. Has enough hitstun that it can be hit confirmed with some practice. A fantastic counter poke in the midrange, shutting down low attacks from opponents who are reliant on them.

Crouching Heavy Kick:
Frame: 11
Melancholia has what is colloquially referred to as the “Rich White Girl” sweep, where she places one hand on the ground to steady herself, then performs a long ranged thrusting kick with both legs aimed at the opponents feet. Causes a hard knockdown on hit, but is -11 on block. Crouching heavy kick is the only grounded normal Melancholia cannot cancel into Thorn Rush. However, it’s also one of Melancholia’s only buttons that has decent range, meaning she does rely on it as a counter poke or whiff punish in the neutral.

Forward Heavy Punch:
Frame: 24
Melancholia grins hideously, and performs a downward swinging headbutt. Hits overhead, and when combined with Thorn Rush, grants Melancholia true high low mix. To compensate, it has very short range like most of Melancholia’s normals, and slightly slower startup than most overheads. +3 on hit and -2 on block. Causes a crumple on punish counter, making it Melancholia’s optimal punish starter as well as a mix tool.

Back Heavy Kick:
Frame: 9
Melancholia performs a forward shunting knee while pulling back her arms. A unique normal that can be jump canceled, making it Melancholia’s best meterless way to access her high damage jumping medium punch combos. Has rather short range (even more so than most of Melancholia’s buttons), but launches the opponent on hit, granting full combos into jumping medium punch, and is -8 on block. Can also be used as a much riskier but extremely rewarding anti air, granting a full combo on hit, but with a very stubby hitbox that often trades or flat out loses to jumping attacks.

Jumping Medium Punch*:
Frame: 6
Melancholia performs a sideways knife hand swipe with her front hand. A great combo extender and air to air that can be canceled into either of Melancholia’s airborne specials. Has a target combo with jumping medium punch.
Jumping Medium Punch*:
Melancholia swings her back elbow upward, stalling her momentum on hit and sending the opponent up. A simple combo extender that tacks on a bit more damage to Melancholia’s combos before she cancels into one of her airborne specials.

Forward Throw:
Frame: 5
Melancholia grabs the opponent by the shoulder and headbutts them, then punches them in the chest, sending them away. Grants pretty good oki at both midscreen and in the corner, although Melancholia has no throw loop. Cannot be canceled into Thorn Rush.

Back Throw:
Frame: 5
Melancholia grabs the opponent by the shoulders and knees them in the gut, before turning around and throwing them behind her. Grants rather poor oki. Cannot be canceled into Thorn Rush.

Thorn Rush: 
(Quarter Circle Backward + Any Punch)
Melancholia’s defining move. Melancholia cancels whatever she’s doing, and instantly bursts forward with a cross arm slash, hands coated in spiky thorns. Melancholia can cancel literally any grounded move into Thorn Rush on either hit or block, including Thorn Rush itself, and it will always combo, even from lights! There are only 3 exceptions: Crouching Heavy Kick, and both her level 1 and 3 supers. This move gives her ridiculous pressure, and ensures that if you give her an inch, she’ll take a mile. All of this comes at a cost: any use of Thorn Rush quickly drains 1/10th of Melancholia’s hp, marked by the section of her health bar that is being used turning red and quickly disappearing. The massive lunge forward Melancholia takes almost guarantees this move will connect at any range when canceled into. On block, Melancholia is left +2, and on hit, Melancholia is left +5, letting her link into medium punch. On hit against a mid air opponent, this move causes a flip out, leaving Melancholia right in the opponents face for an instantaneous mixup. Melancholia cannot use this move if she has less than 1/10 of her hp. Unless otherwise noted, this move will always form a true blockstring when canceled into. Applies heavy scaling if used in combos, usually making it not worth using. 
Break In Case of Emergency (Only implement if Melancholia is too underpowered):
Overdrive Thorn Rush:
(Quarter Circle Backward + Any 2 Punches)
Identical to Thorn Rush, but costs no health.

Shards Of Agony:
(Quarter Circle Forward + Punch)
Air Only, Can Only Be Used After A Forward Jump
Melancholia stalls briefly in midair, slices her front forearm open with her nails, then throws out her hand, throwing out at a wide spread of red thorns with the angle dependent on the strength of the button. An airborne projectile that travels at varying angles depending on its strength, not dissimilar to Akuma’s air fireball. However, the projectiles do travel much faster, generally leaving Melancholia less plus on both hit and block. It also stalls Melancholia in midair, then after the attack, she immediately begins descending, letting her alter her jump trajectory and bait out committal anti airs. Also has use as a combo ender or extender. An insanely versatile and powerful move that lets Melancholia approach and pressure in ways unique to her. However, she is left vulnerable while falling, and the move does have greater landing recovery than most aerial attacks.
Light: Melancholia throws her hand out straight, firing off a horizontal traveling blast of thorns that lock down the space in the air. On hit against an opponent, launches them into a juggle state, which Melancholia can usually finish with medium Sanguine Slash if she lands in time. Cannot hit most grounded opponents. A good air to air, but generally a bad combo tool due to the flat angle it travels at.
Medium: Travels at an extremely steep angle, almost straight down. Travels slower than other versions. Is usually the most plus in block, but has limited use in combos due to its harsh angle.
Heavy: Melancholia sends out the thorns at a sharp diagonal angle. Less plus on block then the medium version, but covers much more horizontal space and is generally the best combo extender. Juggles opponents after the jump medium punch target combo, allowing a finish with medium or heavy Sanguine Slash.
Overdrive: A completely different move to other strengths, Melancholia leans back her forward arm, wraps the entire thing in an enormous stake of thorns, and then quickly descends at a sloping, steep angle while slamming it into the floor. Stalls longer than other strengths, and functions as a dive kick of sorts rather than a projectile. Massively plus on block, and on hit against either an aerial or grounded opponent, causes a ground bounce, allowing follow up combos into either Sanguine Slash, sweep, or Thorn Stake. A great combo extender and approach tool. 

Sanguine Slash:
(Quarter Circle Forward + Kick)
Melancholia performs a leaping spin kick, extending it with a blade of thorns that coats her leg. Due to Melancholia’s incredibly stubby buttons, this special fills the role of poking in the midrange for her, and also acts as a suitable combo extender/ender.
Light: A fairly straightforward poke, Melancholia performs a short hop forward and does a spin kick massively extended by a blade of thorns coating her leg. Has rather good range, but the notable drawback of having extra whiff recovery if it misses or hits an armored move, meaning opponents who jump it or absorb it with a BA likely score a full punish. However, do note that on both hit and block, Melancholia can cancel into Thorn Rush, letting her get a combo if she’s close enough. If a hit lands near the tip of the move however, Thorn Rush will unfortunately whiff. This still leaves her safe on hit, but she is left punishable on block. Combos from light normals, and is +2 on hit and -5 on block. On Punish Counter, causes a crumple state, letting Melancholia dash up and get whatever she wants. While the blade of thorns is completely disjointed, Melancholia does have a large, protruded hurtbox in front of her before the move comes out, and above her for the entire duration, meaning it’s vulnerable to quicker attacks on startup and is easy to hit with jump ins.
Medium: Similar to the light strength, but aimed at an upward diagonal angle. Functions as a good anti air for far away jumps, with high range, and causes a knockdown on hit against a grounded or airborne opponent. Whiffs on standing opponents unless rather close to them, and whiffs against all crouching opponents. In the corner, if Melancholia uses her medium punch heavy punch target combo, then uses this move, she can finish the juggle with heavy Sanguine Slash. Combos from light buttons, but again, is very range reliant and doesn’t work on crouching opponents.
Heavy: Melancholia does an upward double leg swing. Hits directly above and a little diagonal to Melancholia, and also has the quickest startup of any version. Hits twice, meaning it does quite good damage, but also unfortunately means that if it whiffs, Melancholia is stuck in a very long, drawn out animation, making her easy to punish. A great anti air and combo finisher that causes a knockdown, but cannot hit grounded opponents. In the corner, Melancholia can combo into back heavy kick after this attack, granting her quite good damage, although this requires her to be right next to the corner.
Overdrive: One of Melancholia’s most pivotal combo extenders. Melancholia dashes forward and performs a grounded uppercut coated in thorns with her back hand. On hit against a grounded opponent, launches them into a spinning juggle state, similar to some punish counter moves. Melancholia can then finish with Sinful Briars, or she can jump up and extend the combo with the jumping medium punch target combo into her move of choice. On hit against an aerial opponent, launches them away, with very poor follow up potential beyond medium Sinful Briars in the corner. A great combo extender, although expensive, that grants Melancholia great damage and ridiculous corner carry (it’s also one of the only ways to combo into Apotheosis). Unfortunately, the only way to combo into it is through heavy normals. -8 on block.

Sanguine Slash (Air):
(Quarter Circle Forward + Kick)
Air Only
Melancholia performs a quick, spinning kick covered in thorns with her back leg while in midair. Only has 2 strengths, a normal and an overdrive. Mostly a combo extender/ender, but has the niche utility of being able to cross up against opponents, causing a knockdown against grounded foes. Once Melancholia uses this move, it causes her to stall and travel a further horizontal distance as she descended (like a helicopter). This combined with Shards Of Agony lets her choose her jump arc, either cutting it short with the former or extending it with this move.
 Any Strength: Functions as described above. Leaves Melancholia generally plus on block and grants a knockdown on grounded hit. Knocks down airborne opponents, making it a pretty good combo ender off of jumping medium punch.
Overdrive: Causes a wall bounce on airborne hit, letting Melancholia jump up again to use the jumping medium punch target combo to extend her combo further. Functions the same as the regular version against grounded opponents.

Sinful Briars:
(Quarter Circle Backward + Punch)
A spike projectile Melancholia can use to pressure opponents, or as a combo extender.
Light: Melancholia stomps the floor and  sends forth a creeping trail of red thorns across the floor. After a short while, it erupts upward. This spike hits relatively high, but not high enough to hit a jumping opponent. Overall an extremely mediocre projectile that doesn’t go very far, but at least it has quite low recovery time.
Medium: Similar to the light strength, but it travels further and faster, but with the drawback of longer recovery.
Heavy: Travels fullscreen very quickly, at the cost of more recovery. Has some use in corner juggles.
Overdrive: The thorn instantly bursts from beneath the opponent, at the cost of much longer startup than any other version, but with less recovery. Again, similar to the heavy version has some use in juggles.

Into The Fray:
(Any Two Kicks)
Melancholia surges forward into a sprint, with thorns growing from her boots as she runs forward. A great way for Melancholia to close distance, its only problem being how committal it is. Can also be used to extend or start combos when combined with Thorn Rush. Has several follow ups that can be performed while in the run by pressing corresponding kick buttons or by inputting grab. If no follow up is chosen, Melancholia will continue to sprint until she reaches the opponent, upon which she will immediately perform the light kick follow up.
Light: Melancholia immediately skids to a stop. Has use in certain combo links, but is mostly used just to stop melancholias momentum. She is left punishable for the entire recovery duration, however.
Medium: Melancholia halts her momentum and performs a forward step kick, similar to her standing medium kick. Has combo potential when combined with Thorn Rush. This move is -4 on block, but assuming Melancholia actually spaces it and hits with the tip of her foot, it’s usually completely safe. +3 on hit. Can be canceled into any super.
Heavy: Melancholia absolutely dives towards the opponent, leaping at them with her arms crossed and coated in thorns. After she hits the ground, she rolls forward and recovers. Technically, this move can hop over lows due to how melancholia jumps into the air, but this is almost never practical, because the move is death on block, -15, and the early hit cannot be canceled into Thorn Rush because melancholia is considered airborne. On hit, knocks the opponent down, and on contact after the medium punch heavy punch target combo, grants a safe jump in the corner, although at midscreen the opponent can back rise to leave Melancholia too far away to get Oki. Grants fantastic corner carry. Has projectile invulnerability on startup, letting Melancholia bypass projectiles the opponent throws at her, although this must be done on prediction.
Grab: Melancholia leaps forward with her front hand outstretched. On contact with the opponent, Melancholia grabs them by the front of their face, and slams them into the ground, before stepping backward and recovering. A command grab that cannot be blocked, this move has a long startup animation that makes it quite easy to react to, but adds on to the mental stack opponents must face while fighting Melancholia. Grants fantastic Oki and does slightly more damage than a regular throw. On whiff, Melancholia stumbles forward and is left very vulnerable.

Super 1:
Thorn Stake:
(Double Quarter Circle Forward + Punch)
“WRONG-!”
“CHOICE!”
“Uh oh.”
Melancholia leans way back, forms a massive stake of thorns around her back arm, then lunges forward and slams it into the ground in front of her, knocking opponents away. Has invincibility until it hits. Melancholia will only say the second part of the voice line if the move hits, if it misses or is blocked, she’ll say the third voice line instead. A decent combo ender, but mostly has use as a reversal, shoring up Melancholia’s poor defense. Is massively unsafe on block, and has slower startup than most invincible reversals. Cannot be canceled into Thorn Rush.

Super 1:
Thorn Stake (Air):
(Double Quarter Circle Forward + Punch)
“(Manic laughter)”
Air Only
Melancholia massively stalls her momentum in midair, wraps her forward arm in a massive stake of thorns, then plunges forward and slams into the ground at a sloped angle. Has no invincibility, but its air stall lets it beat a lot of anti airs. Can be used as a high damage combo ender, but also a neutral tool, as it’s massively plus on block and causes a knockdown on hit. On punish counter against either a grounded or airborne opponent, causes an aerial tail spin, letting Melancholia perform her jumping medium punch combos. Can also be used out of all jump types, allowing Melancholia to predict if the opponent will throw her, neutral jump, and then perform this move to quickly slam down and punish their throw attempt.

Super 2:
Blood-Borne Valkyrie:
(Double Quarter Circle Backward + Punch)
“My offerings overflow!”
Melancholia rises into the air and grows large red wings of thorns from her back. After using this super, Melancholia has an install for the next 7 seconds (referred to as “Valkyrie form”) where she can use Thorn Rush without consuming HP. This grants her brutal combos and even more brutal pressure until it wears off. Once it wears off, the wings dissipate. 
Apotheosis:
(Double Quarter Circle Backward + Punch)
“SUFFERING GREETS YOU.”
A unique, secret super only available while in Valkyrie form. Costs no super meter, and functions the same as a level 2 super, meaning it can be canceled into from overdrive specials, although it won’t combo from almost any. Can be used both while grounded and in midair, and will completely freeze Melancholia in midair until the animation finishes. Has invincibility until it hits, but has incredibly slow startup, making it a very bad reversal unless the opponent commits to something stupidly slow.
Melancholia bundles up into a ball, hovering in midair with her wings wrapped around her. After the super freeze, she throws out all her limbs, unleashing a massive torrent of crazed, energetic thorns that explode outward in every direction, hitting fullscreen (although they do take time to travel) and destroying all projectiles, even other supers. These thorns do ludicrous damage, more than a critical art, up to 50% of an opponent's health if it hits raw, though when used in a combo they do less damage. After using this move, Melancholia’s Hp is set to 1, and she is instantly stunned, falling to the ground with a unique animation before recovering and entering her stunned animation. This move is an all or nothing gambit that’s extremely difficult to combo into due to its high startup. It can usually only be used after a whiffed reversal or a stun. If Melancholia whiffs it, or if the damage isn’t enough to kill there’s no doubt, she dies. But if it lands, its extraordinary damage is usually enough to close out a round. Has a unique animation if Melancholia wins a round with this move. 

Super 3:
Glory, Glory:
“My turn!”
Melancholia stretches out both arms in an embracing gesture, then lunges forward. On hit against the opponent, Melancholia pins their arms to their side and delivers a headbutt to their skull knocking them to the floor. Melancholia then straddles atop them, and begins delivering a flurry of blows to their skull, socking them again and again with punches. The camera actually cuts mostly to blood splattering from the opponents mouth at a side angle as this happens. Melancholia delivers one final punch to the face, then stands back up, laughing hysterically the whole while. Guaranteed to connect from Thorn Rush, even after a juggle where it would usually cause a flip out.

Critical Art:
Laudate:
“I’LL RIP YOU APART.”
Melancholia performs the same embrace gesture as before, but this time she doesn’t smile. On hit Melancholia grabs the opponent by the throat and begins screeching at the opponent: “You arrogant prudish gnat, you dare to face me?? Like this??? I should rip the veins from your body, tear the heart from your chest and wipe that stupid look off your dumb looking-“ As she monologues, the camera closes in on the opponents neck as they struggle to break melancholia’s grip, their skin visibly turning red. After Melancholia says “looking”, the opponents entire body erupts with red thorns, ripping through their skin, and Melancholia drops them in surprise. She remarks “Oh. Forgot I could do that” and returns to midscreen.

Win Quotes:
(vs. Zenthos) “Look, I get the irony of me saying this, but you could tone it down a few notches. I’m just saying.”
(vs. Kalle) “Holy hell that’s hot! Jeez kid, no offense but seems a bit much for someone like you!”
(vs. Vile) “I know you’re going easy on me. Come on, get up!”
(vs. Melancholia) “Is this another test? Some kinda proof of loyalty? Eh, whatever.”
(vs. Ngann) “Wow, that was fun. Surely, Vile won’t notice if I let you get back up, right?”
(vs. Beast) “Blood too sickly to manipulate and I still win. Alatar overhyped you, honestly.”
(vs. Gauss) “Is this because I broke your leg that one time- where did he go?”
(vs. Salazar) “Go annoy Alatar. You’re boring me”
(vs. Laecaera) “And the king is sending children to war! Can’t say I’m surprised…”
(vs. Alphard) “Last time I took your arms, this time… maybe a leg?”

Beast:
The Rotting King
“We shall not take your trespass lightly…”
Archetype: Brawler
Huge Normals
Explosive Damage
Incredible Pressure
Armored Moves
Corner Carry
Unrewarding Lows
Few Cancelable Normals
Slow Movement
Sluggish Frame Data
High Commitment Moves

Light Punch:
Frame: 5
Beast reaches out his front arm and performs a quick chop. Cannot chain into itself, +4 on hit, -1 on block. Excellent range for a jab. Cannot be special canceled. Has a target combo with medium punch.
Medium Punch (TC):
Beast performs a second chop with his forward arm. Does pretty decent damage. Has better range than light punch, making it almost guaranteed to connect after the starter. +2 on hit and -5 on block. Has a target combo with heavy punch. Frame traps off of the starter.
Heavy Punch (TCC):Beast performs a final, high horizontal swing at the opponent with his sword. Causes a knockdown on hit. -8 on block. A really easy move to hitconfirm and let Beast score a knockdown. Frame traps off of the starter.

Crouching Light Punch:
Frame: 4
A short ranged low punch Beast performs with his forward arm. +5 on hit and -1 on block. Chains into crouching light kick. Beast’s fastest normal.

Light Kick*:
Frame: 6
Beast performs a forward shin stomp before stepping back. Has extremely good range, easily able to whiff punish or counter moves. +1 on hit and -3 on block. A great neutral tool, despite its poor startup.

Crouching Light Kick*:
Frame: 5
Beast performs a low stubby slide kick with his forward leg. A fast, special cancelable, low hitting kick, with significantly better range than is typical of this type of normal. Can chain into itself or crouching light punch. Let’s Beast catch backwalk, finish light strings, the whole shebang. A great poke and light string extender. +2 on hit, -4 on block.

Medium Punch:
Frame: 6
Beast performs a hooked elbow with his forward arm. Beast’s main pressure tool, as it’s +2 on block and +6 on hit. Grants a full combo into standing heavy punch if Beast trades with a 4 frame normal while using this move. To compensate for all these strengths, this move has rather high pushback and very stubby range, shorter than his light kick.

Crouching Medium Punch*:
Frame: 7
Beast performs a large, hooked punch with his forward arm. Beast’s only special cancelable medium. A great special cancelable counter poke with very good range, one of Beast’s most abusable buttons in the midrange. +3 on hit and -1 on block, but if it hits in its later frames it can be plus, making it a decent meaty tool.

Medium Kick:
Frame: 13
Beast performs a swinging roundhouse kick with his back leg, with enormous range. -5 on block, and +2 on hit. An absolutely incredible poke and whiff punish that, on punish counter, launches the opponent into an aerial tail spin, letting him connect charged medium Blighted March. A terrifying button that makes whiffing a move in front of Beast a terrible error. Low whiff recovery also makes it hard to punish.

Crouching Medium Kick:
Frame: 8
Beast performs a low, crouching slide kick with absolutely fantastic range. +4 on hit and -2 on block. On punish counter or counter hit, causes a hard knockdown, meaning Beast can’t really get a combo off this move, but does let him better pressure opponents by closing distance. An extremely strong poke.

Heavy Punch*:
Frame: 10
Beast performs a massive lunging backfist swipe with his forward hand. Enormous range, and hits mid while being Beast’s only special cancelable heavy. A dominant counter poke and a great combo extender as it can combo into heavy Earthstep. +3 on hit and -3 on block.

Crouching Heavy Punch:
Frame: 12
Beast performs a massive, upward arcing swing with his sword. Launches on hit, allowing a combo into medium Ferocity, light Blighted March or Rotting Quake at midscreen or Rotting Earth in the corner, which then leads to further extensions. A dominant anti air that grants a combo extension, instilling fear in opponents who try to jump out of Beast’s pressure. Also one of Beast’s best combo extenders after a wall bounce. -6 on block.

Heavy Kick:
Frame: 16 (30)
Beast pulls his forward leg way back, then unleashes a massive stepping thrust kick. Massive range, and safe on block at -3, this button is a dominant poke that covers half of the screen with a huge hitbox. However, Beast can also charge this move by holding down heavy kick. This slows down the startup from 16 frames to 30, but in return, grants the move one hit of armor, letting Beast absorb an opponent's attack and retaliate. When uncharged, this move is +3 on hit, and causes a hard knockdown on counter hit or punish counter. When charged, the move becomes +5 on block (although with such large pushback Beast can struggle to take advantage of it), causes a hard knockdown on hit, and causes a wall bounce on either counter hit or punish counter (with heavy scaling applied). If the charged version of this move whiffs, Beast enters a unique animation where he stumbles forward, leaving him insanely vulnerable. Having on demand armor is excellent for going against opponents who rely on burst movement attacks in neutral.

Crouching Heavy Kick:
Frame: 11 (22)
Beast performs a wild swing with his back leg, striking low. Causes a hard knockdown on hit and is -15 on block. Can be charged. When charged, doubles the startup but grants the move one hit of armor and makes it safer on block, going from -15 to -7. On hit when charged, causes a hard knockdown, but on punish counter or counter hit, causes a tumble state with great corner carry that becomes a wall slump if they hit the wall.

Forward Medium Kick:
Frame: 14
Beast performs a forward stepping knee with his back leg. A forward advancing normal Beast can use to close distance while placing a hitbox in front of himself. +1 on hit, -4 on block. However, at the end of this move, a late hitbox appears, right at the very tip of Beast’s knee with slightly larger range than the early hitbox. This latter hitbox is +5 on hit and +1 block, meaning if Beast spaces the move well enough (or uses it as a meaty) he is rewarded with plus frames. It also has very little pushback on both hit and block, usually leaving Beast close enough for a throw attempt on block or a link into lights on hit.

Forward Heavy Punch:
Frame: 24
Beast does a large, two-handed, overhead slam with his sword. Hits overhead and causes a knockdown on hit. -8 on block, but has such large range it can often be spaced to be safe. Massive range for an overhead, and a great poke despite its unsafety. On punish counter, causes a wall slump. Also a fantastic anti air that covers a huge area above and in front of Beast, with a large disjointed hitbox.

Down Heavy Kick (Air Only):
Frame: 12
Beast performs a heavy double footed stomp. This move is an incredible jump normal that can hit cross up, is massively plus on block, reaches extremely far down, and also causes a hard knockdown on hit against either a grounded or airborne opponent. On punish counter against either a grounded or airborne opponent, causes a ground bounce, allowing follow up combos. Additionally, sharply stops Beast’s air momentum, letting him mix up his jump timing.

Forward Throw:
Frame: 5
Beast knocks his opponents arms aside, then slams them with a hammerfist to the head, knocking them directly into the floor. Leaves Beast relatively close, but not close enough for another throw. The opponent gets up very quickly. Allows Beast to get more pressure on the opponent with his large normals, but he has no throw loop.

Back Throw:
Frame: 5
Beast grabs the opponent by their front leg, and slams them over his head into the ground, where they then get up. Leaves Beast midscreen with poor Oki.

Air Throw:
Frame: 5
Beast reaches out his free hand in midair, aiming to grab the opponent by the neck. A dedicated air to air, this move cannot hit grounded opponents, but to compensate, it has a massive lingering hitbox that persists until Beast lands on the ground. He can perform it extremely quickly from any jump, letting him jump to meet an airborne opponent, and it also doesn’t affect his air momentum at all, meaning it doesn’t stall him in midair. On hit, Beast grabs the opponent by the neck and slams them to the ground, then runs forward a little bit, dragging them through the earth before ripping upward and flinging them away. Has really good Oki against cornered opponents, letting Beast dash up and set up a strike throw situation, and also does more damage than a regular throw.

Rotting Earth, Earthstep:
(Quarter Circle Forward + Kick)
The light version of this move is Rotting Earth, a ground based projectile that helps Beast clash with projectiles and better approach opponents.
The medium and heavy versions are Earthstep, a powerful stepping stomp that works well as a combo extender or ender. 
Light: Beast swipes his foot across the ground, creating a slow moving wave of rot that travels under other projectiles. Travels quite slowly, as it’s designed to aid Beast’s advance, not to keep opponents away.
Medium: Beast performs a quick forward stomp with his back leg. A very basic combo ender Beast can use out of light normals to score a knockdown. Beast is left plus but not point blank after a dash. Is unsafe on block at -5 with low pushback, meaning it is almost always punishable unless spaced at the absolute tip. On hit against an aerial opponent, slams them into the ground.
Heavy: Beast performs a slow, large stomp with his back leg. Without counter hit or punish counter, can only be linked into out of standing heavy punch. To make up for its limited combo options, it’s very rewarding on hit. Heavy Earthstep is +7 on hit, letting Beast link into Crouching Medium Punch, which can then obviously be continued further. This move also causes a ground bounce on hit against an aerial opponent, granting a combo into medium Ferocity. +3 on block, letting Beast frame trap into his amazing standing medium punch.
Overdrive (Light + Medium/Heavy: Beast scrapes his sword across the floor, creating a wave of high rot that moves slowly, destroys other projectiles on hit, and launches hit opponents into the air. 
Overdrive (Medium + Heavy): Beast takes a large step forward and performs a powerful thrusting kick, launching the opponent. Causes a wall bounce on hit. Combos out of medium normals. -8 on block.

Deaths Grip:
(Half Circle Backward + Punch)
Beast’s command grab. Doesn’t do too much damage, but like all command grabs, is still obviously very useful. Uniquely, both strengths of this move can actually connect with opponents after a wall slump, letting Beast combo into this move after certain whiff punishes or some strengths of Blighted March, and is generally Beast’s highest damage ender after such a scenario.
Normal: Beast reaches up one hand behind himself, then lunges forward with his arm outstretched. On contact with the opponent, Beast grabs the opponent by the throat and lifts them high before throwing them into the air and delivering a stern fist slam into their body, knocking them into the ground. Allows Beast to dash up and be point blank and +3, and does pretty solid damage. Has a slow, reactable startup, and on whiff, leaves Beast insanely vulnerable.
Overdrive: Beast performs the same animation as the normal version, with faster startup, making it harder to react too. Uniquely, has one hit of armor, meaning it can’t be challenged with strikes like the base strength and must be jumped or backdashed. On connect, Beast grabs the opponent and spins them around his body before impaling them on his sword. Does about the same damage as the standard version, but with even better Oki, leaving Beast +6 after a forward dash.

Blighted March:
(Quarter Circle Backward + Kick)
Beast pulls his body inward, and then throws himself forward, coating his whole body in foaming green rot, taking a different approach depending on the move strength. A burst movement tool, anti fireball tool, combo extender, and armored move Beast can use as a (semi) reversal. Beast always leans back before performing the move, slightly retracting his hurtbox. Holding down the kick button causes him to charge the move, altering its effects.
Light: The quickest to startup, but travels the shortest distance, about midscreen. Beast hunkers low, then spins and throws himself forward with boot outstretched (similar to ganondorf’s wizard’s dropkick from sm4sh). Is, at worst, -5 on block but is incredibly lenient to space, and can be 0 on block if used at max distance. Leaves the opponent standing on hit, and at best +3. When charged, it instead causes a hard knockdown, and gains one hit of armor once it begins traveling. The advantage on block also changes from at minimum +1 to up to +3. This is the only version that can link out of a normal, and uncharged will connect after crouching medium punch or standing heavy punch.
Medium: Quickish startup, travels about half screen. Beast lunges forward in a similar boot dive as the light version, but notably closer to the ground and with noticeably more rot surrounding both him and his boot. Causes a knockdown on hit. -5 on block if spaced poorly, but can be spaced to be up to +2. When charged, the move is +2 minimum, and +5 if spaced well. Gains one hit of armor when charged, letting it counter moves. On hit when charged, engages a cinematic where the opponent staggers backward, and Beast quickly recovers, dashes up, and knees them in the stomach, sending them flying backward and causing a tumble state that can become a wall slump if the opponent touches the corner.
Heavy: The slowest startup, but to compensate, travels fullscreen very quickly. +1 on block minimum, +4 at max. Beast tucks in, then charges forward in a shoulder tackle as his body is coated in rot, with the faint outline of a charging boar being visible. Rather vulnerable to BA due to its slow startup. Causes a hard knockdown on hit. When charged, is +2 minimum and +6 if spaced well. Gains one hit of armor when charged. On hit when charged, causes a cinematic wherein Beast grabs the opponent by the shoulders. He then delivers a punch with his right hand to the opponents face, backhands then with the same hand, then elbows them into the air while proudly declaring “Your pain begins, here!” allowing combos afterward. This grants a guaranteed combo into heavy Ferocity at any space of the screen, or heavy Earthstep in the corner, causing a groundbounce. This charged version can only be comboed into after a wall bounce or certain juggles, but grants fantastic damage if it does.
Overdrive: Unlike other strengths, this version cannot be charged. Has the quickest startup of all versions, and 1 hit of armor starting from frame 1 until it hits, featuring the same shoulder tackle as the heavy version. Can be used as a reversal, but loses to throws due to being armored instead of truly invincible. To compensate, does rather high damage, much more than the average reversal. Unlike other strengths of Blighted March, overdrive has a unique animation if blocked where Beast recoils backward in surprise, leaving him insanely vulnerable, like most blocked reversals. Like most other reversals, this move fully resets to neutral, leaving Beast relatively far from the opponent.

Ferocity:
(Dragon Punch + Punch)
A sword attack that works as Beasts highest damage combo ender and a solid anti air. 
Light: A quick sideways swipe Beast performs with his sword. Knocks opponents down and does pretty solid damage. Combos out of medium normals. -10 on block.
Medium: Beast performs an uppercut with the sword. Combos out of heavy normals. Knocks the opponent down, and does solid damage with good oki. Has a good hitbox, making it a somewhat slow but reliable anti air. -10 on block.
Heavy: Beast performs a powerful, heavy, diagonal double spin attack. Does very high damage, and is -12 on block. Beast moves forward a huge amount while performing the attack, making it very easy to connect during juggles. Cannot be linked into without a punish counter, but is generally Beast’s best juggle ender. Also has a huge, disjointed hitbox above and diagonal to beast, making it a very slow, but very damaging and consistent anti air.
Overdrive: A hitgrab, Beast performs a big upward swipe with the sword, and on hit, engages a cinematic where he grabs them by the leg as they fall back down, and throws them behind him. Sideswitches on hit, and grants great Oki in the corner, but leaves Beast rather far away if used midscreen. Connects after any link where heavy works, and does slightly less damage than heavy.

Super 1:
Rotting Quake:
(Down Down Down + 2 Punches)
“Your arrogance shall cost you!”
Beast gathers green energy in his hand, then slams it into the floor, creating an enormous geyser of green rot all around him. Works well as an anti-air, or combo ender. Also has invincibility until it hits, making it Beasts only truly invincible reversal. Is incredibly unsafe on block. Causes a hard knockdown on hit, letting Beast continue his pressure.

Super 2:
Enclosing Forest:
(Down Down Down + 2 Kicks)
“You shall be left to rot…”
Beast plunges his sword into the ground, then presses it further, causing trees to sprout on either side of the screen, trapping the opponent in a limited arena with Beast. These trees cannot be jumped over or passed through. The trees function identically to walls or the corner, meaning players can get wall slumped, wall bounced, or wall splatted against them. The only way to destroy the trees is to deal damage to Beast. Damaging Beast damages the trees, which have around 2500 health. This super has a rather high amount of end lag, meaning it can only safely be performed after a knockdown.

Super 3:
Trial of Beast:
(Double Quarter Circle Forward + Punch)
“You are tried.”
Beast grows a long noose of vines from his free hand, then lunges forward and wraps it around his opponent's neck. Combos from normals, any strength of Ferocity, Earthstep, or Rotting Earth. On contact with the opponent, engages a cinematic where Beast ties the free end of the rope to a sprouting tree, which rapidly grows, pulling up the opponent as they stand atop a large branch. Beast wanders around them, muttering “for trespassing, violence, and heresy.” The camera cuts to a cinematic side angle, and Beast declares “I sentence you to death” and cuts the branch out from beneath the opponents feet, causing the noose of vines to snap their neck. If they survive, the tree dissolves, they fall back to the ground and Beast strolls back to midscreen.

Critical Art:
Final Say:
(Double Quarter Circle Forward + Punch)
“No more!”
Beast snares the opponent with his noose, and ties the opponent by the neck to the ground. A tree erupts from the ground behind the opponent, trapping them beneath it as it grows into the shape of stockings, holding down the opponent as they and Beast rise into the air atop a growing platform. Beast yells “Now is the time for action!”  readies his sword in both hands, lifts it upwards, and slices through the opponents neck. If this kills the opponent, the kill cam shows their silhouette blacked out, and the only visible thing is the form of them being decapitated and Beast’s glowing eyes.

Win Quotes:
(vs. Zenthos) “Bring your crusade elsewhere! I will not humor your intrusion again.”
(vs. Kalle) “OUT! Fire has no place within my presence!”
(vs. Vile) “Your strength is not your own. You lie in service to some greater power you cannot comprehend. Pathetic.”
(vs. Melancholia) “A glorious fight! Now rise! Or I shall do battle with your corpse…”
(vs. Ngann) “Your soul is not as incorruptible as you seem to think.”
(vs. Beast) “Truly, I must be in my final years…”
(vs. Gauss) “All your planning and underhanded tricks… and yet you crumple in the face of sheer power.”
(vs. Salazar) “No courage. No willpower. No fighting spirit. Even more despicable than most warlocks.”
(vs. Laecaera) “You wish to learn of my strength? Then witness the power of the forest firsthand…”
(vs. Alphard) “Your strength impresses me, but it is not enough!”

Gauss:
Ever-Planning King Of Machinations
“Right on time.”
Archetype: Puppet

n
Technical

Light Punch:
Light Kick:
Crouching Light Punch:
Crouching Light Kick:
Medium Punch:
Medium Kick:
Crouching Medium Punch:
Crouching Medium Kick:
Heavy Punch:
Heavy Kick:
Crouching Heavy Punch:
Crouching Heavy Kick:

Unique Mechanic:
Energy:
Gauss has two drones. One, Velis, floats above his forward shoulder, while the other, Loki, stands near his back foot. Keeping Gauss’ drones out and ready to attack on the battlefield drains Gauss’ energy bar. This bar refills over time whenever the drones aren’t in use. Gauss can summon the drones with any amount of bar left, but if the bar is at any point fully drained, the drones will briefly enter a failure state, flashing with electricity. While in this failure state, they cannot be summoned, and they only exit this state once the bar is fully refilled. If either of the drones is struck by a projectile or attack while they’re out, they are instantly recalled and a chunk of the energy bar is removed.

Velis M-139149:
(Quarter Circle Forward + Punch)
Gauss reaches his front hand out and snaps his fingers. The drone above Gauss forward shoulder, henceforth referred to as “Velis,” lunges forward, lowering to chest level in front of Gauss. This lunge has no hitbox, and only serves to get Velis out on the field. This lunge is universal across strengths, and always takes the same amount of time to perform. Velis will then perform an attack dependent on which button strength was pressed, however: this second attack will only be performed when the designated button is released, not when pressed (referred to as “negative edge”). This gives Gauss fantastic staggered pressure. However, keeping the drone out drains Gauss’ Energy bar, meaning he can’t stall the attack forever and must eventually release the button. In addition, Gauss and Velis are left vulnerable for the entirety of the summoning animation, and Velis can be easily dispelled if it is struck with a fireball or normal. The drone follows Gauss around as he walks, but can also be controlled separately by holding down back or down forward. This will cause Gauss to crouch and remain still, but the drone will move in the respective horizontal direction. It does, however, have a range limit, it cannot go behind Gauss and it cannot go more than 2/3rd screen in front of him.
Light: When the button is released, Velis unleashes a large, pointed, spear shaped blast of lightning. Has fantastic range, making it a great poke, and causes a knockdown on hit. 
Medium: Velis performs a curving upward charge at a diagonal angle,
Heavy:
Overdrive:

Super 1:
In Tandem (Velis):
(Double Quarter Circle Back + Punch)
“Velis, go!”
In Tandem (Loki):
(Double Quarter Circle Back + Kick)
“Now, Loki!”
The screen freezes 

Super 3:
“Full power!”

DLC:

Year 1 (4 Characters):
Salazar:
Glib Tongued Golden Eyed Gunslinger
“I’ll try not to show off, but I’ll probably fail.”
Archetype: Salazar (Footsies)
Give him Adachi's back walk animation, that suits him so well.

Hit-confirms
Mobile
Snowballs
Supers
Fashionable
Style
Swagger
Sexy
Gun
None

Light Punch*:
Frame: 4
Salazar does a jab with the barrel of his gun. +4 on hit. Has more range than most jabs, but is still shorter ranged than his light kick. Combos into light or overdrive Blowout. -3 on block.

Light Kick*:
Frame: 5
Salazar performs a short low side kick with his front leg while gripping his hat. Combos into light or overdrive Blowout, or light Put ‘Em Down, but the fact it can’t combo into medium Blowout hurts quite a lot, meaning at low style Salazar must spend meter to score a knockdown and set up a taunt (this issue is alleviated once he gets Put ‘Em Down). +2 on hit, -4 on block. Has a target combo with medium kick.
Medium Kick (TC)*:
Salazar switches from his standard light kick into a flicking side kick with his back leg, as if he’s performing a step dance. Has greater range than standing light kick, making it almost guaranteed to connect after the starter. +1 on hit, -5 on block. Makes hit confirming slightly easier, and also tacks some damage onto Salazar’s light confirms. Combos into everything light kick can combo into.

Crouching Light Punch*:
Frame: 4
Salazar does a short jab with the barrel of his gun. +5 on hit, granting a useful link to sweep on punish counter, letting him set up a taunt, or standing heavy punch for high damage. Combos into light or overdrive Blowout. -1 on block.

Crouching Light Kick:
Frame: 5
Salazar’s fastest low. A very standard short kick he does with his front leg. Links into crouching light punch. -2 on block, +4 on hit.

Medium Punch*:
Frame: 7
A forward advancing straight punch. Salazar takes a step forward and performs a strong straight punch with his free hand. Has very solid range, with a small disjoint, but has quite high whiff recovery. -2 on block, +4 on hit. 

Medium Kick:
Frame: 9
Salazar performs a long ranged side kick with his back leg, turning away from the camera. A great mid hitting poke with low whiff recovery that can hop over lows. +5 on hit, -2 on block. At style level 3, gains a new target combo with heavy punch.
Heavy Punch (TC):
Only available at style level 3
Salazar spins, aims his gun at the opponent, and unleashes a single loud shot. Knocks down opponents. -8 on block. Frametraps off of medium kick.

Crouching Medium Punch*:
Frame: 6
Salazar’s fastest medium. Salazar performs a short elbow thrust with his free arm. +5 on hit, allowing powerful conversions into heavy normals on punish counter. -3 on block. Combos into light or medium Blowout.

Crouching Medium Kick*:
Frame: 8
Salazar performs a low, crouching slide kick with good range. A very important neutral button for Salazar, but its low hitstun means it can only combo into the same specials as light normals, making it somewhat unrewarding. -3 on hit, and -6 on block.

Heavy Punch*:
Frame: 9
Salazar swings his gun in a short, stomach level sweep while spinning his gun around his index finger. A short ranged, two hit normal that’s +1 on block and +3 on hit. Due to its two hit nature, it can be hit-confirmed pretty reliably into specials. A vital pressure and combo tool, but its lack of range (usually an important feature of this type of button) holds it back somewhat and forces Salazar to rely more on his medium buttons for poking.

Heavy Kick**:
Frame: 9
Salazar grips his hat, and performs a Brazilian kick wherein he feints a low kick before swinging his leg up, striking at the opponents jaw, and then swinging back down and pivoting on his heel to recover (he also tilts his hat at the camera as he recovers) (also if this is hard to picture just google Brazilian kick, it’s a weird move that’s hard to describe). This move is designed as an anti air, with a large, high hitting hitbox and upper body invulnerability against air attacks. The first hit when Salazar performs the high kick launches opponents, and the second hit spikes them into the floor, causing a hard knockdown which Salazar can either pursue or use to set up Do ‘Em Dirty. The first hit can also be super canceled, allowing a juggle into Heat Buster or other supers (the second, spiking hit cannot be super canceled). On counter hit or punish counter against either an airborne or grounded opponent, this move causes a ground bounce allowing a combo into medium or overdrive Blowout, Put ‘Em Down, or Heat Buster. On block this move is -5, and it’s short horizontal range makes it a poor move for grounded poking.

Crouching Heavy Punch:
Frame: 9
Salazar’s sweep. Salazar performs a low swinging strike with the butt of his gun, slamming it into the opponents legs, and causing a hard knockdown. Has less range than most sweeps. -10 on block, and hits low. Due to Salazar leaning down quite a lot while performing this, this attack has excellent low profile.

Crouching Heavy Kick**:
Frame: 10
A two hit double spin kick that strikes mid. Salazar performs a spinning low kick with his back leg, then pivots and performs another kick with his other leg. Moves Salazar forward a great deal, and is +5 on regular hits (unlike most crouching heavy kicks this move leaves opponents standing) and -4 on block. Similar to his crouching heavy punch, due to Salazar leaning down quite a lot while performing this, this attack has excellent low profile. On punish counter, the second hit launches the opponent into a spinning juggle state, with limited follow ups, like Blowout or Put ‘Em Down. The two hit nature makes this move easy to hit-confirm into supers, and on any type of hit it combos into all three supers. A great move that Salazar can fish for in neutral as both a poke and whiff punish to confirm into Heat Buster for high damage and a knockdown. Uniquely, if this move hits on punish counter and Salazar cancels it into Heat Buster, the opponent is launched high enough that Salazar can connect a second Heat Buster, which grants a unique voice line and an additional style stock. 

Forward Light Kick:
Frame: 18
Only available at style level 2
Salazar shunts forward while performing a low swinging step kick. Hits low, and has fantastic range due to the large step forward Salazar takes. +3 on hit, -2 on block. Has a target combo with medium kick. Has a very high amount of recovery if it whiffs however, with a large, extended hurtbox.
Medium Kick (TC): 
Salazar pivots on his front foot, and spins into a thrusting kick with his back foot. Knocks down on hit, letting Salazar set up a taunt. -6 on block, and frametraps off of forward light kick.

Forward Medium Kick**:
Frame: 22
Becomes super cancelable at style level 2
Salazar lifts his back leg up and does a swerving overhead kick. Strikes overhead and has two hits. +3 on hit and -3 on block. At style level 2, this move becomes super cancelable, allowing a powerful overhead low mix that confirms into supers.

Forward Heavy Punch**:
Frame: 12
A forward advancing mid hitting poke. Salazar lunges forward while swinging his gun horizontally. +4 on hit, -2 on block. An unremarkable button, but a useful poke nonetheless, which can cancel into supers. Has a long, generous cancel window, making hitconfirming possible, but difficult. Grants a combo if canceled into Super Taunt. Gains a target combo with heavy punch at style level 3, but this target combo only naturally combos if forward heavy punch hits as a punish counter.
Heavy Punch (TC):
Only available at style level 3
Salazar leans back, then performs a heavy forward step kick while arrogantly nodding his head at the camera. Causes a wall bounce on hit against a grounded opponent, making it extremely rewarding to land. -16 on block. On hit against an aerial opponent, sends the opponent flying away and causes a hard knockdown, letting Salazar set up a taunt.

Forward Heavy Kick:
Frame: 16
Only available at Style Level 1
Salazar performs a stylish looking orbital hop kick, gripping his hat as he does so. Salazar leaps off the ground as he performs this move, letting him hop over lows, and because he is technically airborne, he cannot be thrown, letting him heavily punish opponents who try to grab him. Has pretty good range and moves Salazar forward slightly when he uses it. Fairly unrewarding on normal hit, only +5, but has a target combo that makes it much more rewarding. This target combo has a very lenient hit confirm window, making it easy to land.
Forward Heavy Kick (TC)*:
Salazar spins forward and performs a second spinning kick with his other leg. This one launches opponents, which when combined with special cancels, usually makes it Salazar’s optimal combo extender. Combos into light, medium, or overdrive Blowout, or any version of Put ‘Em Down for very high damage. Very unsafe on block at -12.

Forward Throw:
Frame: 5
Salazar grabs both of the opponents arms, and spins them around him, pretending to dance, before tripping them over his outstretched leg, sending them flying away as he laughs. Can be used to safely set up a taunt at midscreen, which leaves Salazar -6 but way out of range, even if they don’t backroll.

Back Throw:
Frame: 5
Salazar places his hat over the opponents face as he steps behind them. Once he gets behind them, they turn to look at him, at which point he shoots them in the stomach with his gun, sending them tumbling away. If Salazar goes for a taunt after this move, he is potentially left vulnerable, as he is -12, but back rolling opponents will usually be left out of range.

Unique Mechanic:
Style:
Salazar has a unique symbol underneath his healthbar, symbolized by 4 hat icons that are colorless. Whenever he gains a Style Stock, one of these hats light up, and when he loses one, the hats lose color. Salazar loses 1 style stock whenever he gets knocked down and starts every game with zero style, but he keeps style through rounds. While Salazar is rather weak at zero style, suffering from low damage and poor combo routing, Salazar with 3 style is arguably the strongest character in the game, gaining new combo routes, conversions off his pokes, and bettering his defense. Different style levels grant him different buffs, and change or unlock certain abilities:
Level 1: Salazar gains a 10% damage buff.
Grants Access Too/Modifies:
Forward Heavy Kick
Smolderin’ Sway
Decadent Descent
Level 2: 
Forward Light Kick
Forward Medium Kick (Changed)
Want-Some-More?
Undeniably Admirable
Level 3: 
Medium Kick TC
Forward Heavy Punch TC
Do ‘Em Dirty (Changed)
Put ‘Em Down
Level 4: No effect, but allows Salazar to keep level 3 charge even if knocked down.

Do ‘Em Dirty:
(Down Down + Punch)
Salazar strikes one of several poses and says a voiceline. A taunt special that can be special canceled into. If he finishes the taunt, he gains 1 Style Stock, but if knocked out of it he doesn’t. Salazar is left vulnerable during the taunt, as he cannot cancel it early, and as such this move can only be usually performed after a knockdown. At level 3 style, anytime Salazar uses this move, he gains ⅓ a bar of super, which, considering how powerful his supers are, is very useful. The various taunts all have a percentage chance to happen, but unless listed otherwise, all have the same duration:
Hat Trick (10%): Salazar takes off his hat and rolls it along his right arm, across his shoulder into his left hand before putting it back on.
“I’d love if you took this more seriously?”
Gun Spin (10%): Salazar spins his gun on his finger then throws it to his other hand, before juggling it around his back to grab it.
“Over… and around!”
Big Whoop (10%): Salazar points his forward arm at the opponent and performs two big circles with his other arm while letting out a loud whoop.
“Woooooo-hoo!”
Mess Around (10%): Salazar fires his gun three times into the air while letting out a large cheer.
“Yeah!”
Juggle (10%): Salazar takes off his hat and one of his shoes then does a brief juggle with his gun, hat, and shoe.
“1, 2, 3, 1, 2, 3, hey!”
Jig (10%): Salazar performs a quick step dance, finishing by taking a bow.
“Ta-da!”
Not So (10%): Salazar takes his hat off and spins it around his finger while wagging his index finger on the other hand at the opponent dismissively.
“Not quite!”
Warlock’s Magic (10%): Salazar uses sleight of hand to make his gun disappear. He then takes off his hat, reaches into it, and pulls the gun back out.
“Where’d it go, where’d it… woah!”
Feelin’ Mad (5%): Salazar stretches both arms wide while taunting the opponent and walking towards them. Can sometimes endanger Salazar by pushing him closer to the opponent, but can also let him get closer easier to better pressure the opponent.
“C’mon, you want a piece?”
Feelin’ Bad (5%): Salazar yawns while placing both hands on his hips and leaning back. He then rubs his neck.
“Ha, I’m gettin’ old.”
Feelin’... Foreign? (5%): Salazar lowers himself and performs a rapid squat dance with his arms crossed, finishing by throwing both legs wide while standing up.
“Da-da-dadlladalada-hey!”
The Lowdown (4%): Salazar performs a short breakdance, rolling on the floor. Technically has a lower hitbox than other taunts, meaning it can dodge high attacks, but this is hardly practical.
“You ain’t beatin’ me!”
The Largest (1%): The rarest taunt by far, Salazar performs a short choreographed dance, finishing by performing a spin towards the camera and tilting his hat as applause plays. The screen freezes as he does so, with a spotlight illuminating Salazar, and making this taunt completely unpunishable as it occurs during a screen freeze. Instantly sets Salazar’s style level to 4, no matter what level it was previously at. If Salazar is already at style level 3 or 4, instantly grants him three full bars of super. An extremely powerful effect that can swing rounds, but is obviously so rare as to be unreliable.
“(Michael Jackson noises)”
Additionally, Salazar has a variety of secret taunts performed by other means. These taunts all function the same as Do ‘Em Dirty, although they usually take longer to finish.
Backing Out?: If Salazar continuously walks backwards for 20 seconds straight without performing any other action, he will stop, look at the opponent, then mutter under his breath while shaking his head, before returning to his idle pose.
“This is just sad, really.”
Too Arrogant: If Salazar inputs down 7 times in a row without inputting anything else within a brief window, he will stand up straight and face his back to the opponent, gesturing at it with his thumb while telling the opponent to hit him. He will stay in this pose for 5 seconds. If hit in this stance, he will be punish countered. If the opponent doesn’t strike him, he’ll shrug and return to his idle pose.
“C’mon, I’ll give ya a freeby.”
“Really? Suit yerself…”

Blowout:
(Quarter Circle Forward + Punch)
Salazar’s “fireball.” Salazar grips his gun in both hands, then unleashes an extremely fast traveling bullet that hits fullscreen. Different strengths have different utilities. Unlike most fireballs, which have mediocre startup and variable travel speed, Blowout has incredibly slow startup, but the projectiles travel extremely quickly.
Light: The closest thing Salazar has to a traditional projectile. Travels in a straight horizontal line from Salazar and hits fullscreen. Faster startup than medium and heavy, staggers the opponent on hit. A good combo ender after light strings, but doesn’t knock down. Generally safe on block unless Salazar is point blank, with varying frame data due to being a projectile. Also Salazar’s best way to combo into Safe To Say due to its ease of routing.
Medium: An anti air projectile and combo ender, Salazar aims his gun at an upward diagonal angle and quickly fires a bullet, causing a knockdown against both grounded and aerial opponents. Covers a large diagonal space in front of Salazar, but is bad at anti airing close jumps. Also a good combo ender (especially for juggles) that causes a knockdown, letting Salazar set up a taunt or chase the opponent, but with more limited linking options than light or overdrive. Combos from medium normals, except from crouching medium kick.
Heavy: The most unique version. Salazar holds his revolver in one hand, stands up straight, holds the gun at head height, thumbs back the hammer, and then fires it, unleashing an extremely powerful and very loud blast. This move has ludicrously slow startup, and only combos from standing heavy punch. It also whiffs on crouching opponents. To compensate, it causes a crumple on hit against a standing opponent, allowing Salazar to link into whatever he wants. On hit against an aerial opponent, it launches them up again, allowing a combo into medium, light or overdrive Blowout, any version of Put ‘Em Down, or Heat Buster, which is especially useful after a wall bounce. +4 on block with high pushback, but the fact it can be ducked makes this more of a gimmick then anything useful. 
Overdrive: Salazar unleashes a rapid barrage of three shots, counting each as he fires them. Faster startup then even the light version, with the same travel speed and greater damage. This move causes a knockdown on hit, letting Salazar set up a taunt. On hit against an aerial opponent, grants a combo into Heat Buster. Great in fireball wars, as it goes through non overdrive projectiles and clashes with overdrive ones, or as an alternative combo ender instead of light or medium Blowout. Do note that only the third and final shot knocks down the opponent, meaning if this move is canceled into Super Taunt before the final shot, Salazar can link out of it. If canceled into Super Taunt before the final hit, Salazar can actually combo into Heat Buster from fullscreen, giving Salazar a flashy and impractical way to waste three bars of super.

Smolderin’ Sway:
(Quarter Circle Back + Kick)
Only available at Style Level 1
Salazar performs a large, quick backstep with several follow ups. Both versions are immune to throws, but the normal version does not have strike invulnerability. However, Salazar wildly shifts his hurtbox backwards during this move, meaning it can be used to avoid stubby normals, and then retaliate. A great shimmy tool, combo extender, and reversal. Has several follow ups that Salazar can go into.
Any Strength: Salazar takes a quick step backwards. Immune to throws, and has a large, retracted hurtbox.
Overdrive: Has the same startup and distance covered as the regular version, but with full strike and throw immunity. Is still vulnerable to projectiles.
Follow Ups:
Comin’-Through (Forward Twice): Salazar hunkers down and performs a low rush forward. Further ranged than his forward dash and moves forward very quickly. Salazar is left in a counter hit state for the entirety of the dash, and he cannot cancel it early, but this move is still a great way to feint an attack or close the distance on the opponent. Also can low profile high attacks.
Down-A-Peg (Forward + Light Kick): Salazar takes a shunting step forward and does a low kick at the opponents legs with his front foot. The safest follow up at -3, and hits low. Leaves Salazar +2 on hit, but outside of throw range. Causes a hard knock down on punish counter.
Have-A-Look (Forward + Medium Kick): Salazar does a leaping knee attack with his back leg. Hits mid. Causes a spin state on punish counter, letting Salazar connect whatever he wants. On regular hit, leaves Salazar +3 point blank. -5 on block. If Salazar cancels into Smolderin’ Sway from standing medium or heavy punch, Have-A-Look will actually combo, making this a great combo extender when combined with Want-Some-More? Also generally the best follow up to use after dodging an attack or throw with Smolderin’ Sway.
None-O’-That (Forward + Heavy Kick): Salazar lunges forward into a sliding low kick. Has complete fireball invulnerability until it hits, and can go under high attacks. Travels almost fullscreen and hits low. Knocks down on hit. Extremely unsafe on block at -9. 
Want-Some-More? (Forward + Any Punch after any other follow up): Only available at style level 2. Can only be used after any other follow up. Salazar performs a strong elbow at the opponent's jaw, launching them into the air and allowing follow up combos into light, medium, or overdrive Blowout, , any version of Put ‘Em Down, or supers. Guaranteed to connect after either Down-A-Peg or Have-A-Look, and allows Salazar to combo after either of them. -6 on block, and frametraps off of all follow ups. A great combo extender at style level 2.

Decadent Descent:
(Quarter Circle Back + Kick)
Air only
Only available at style level 1
Salazar grips his hat with his free hand and quickly slams downward with his back leg pointed downward and his front leg tucked into a knee. A dive kick that grants Salazar fantastic pressure, in addition to being great for baiting out anti airs. Like any dive kick, it has a pretty large hurtbox, but allows Salazar to get in easily and set up his pressure. All strengths have identical startup.
Light: Travels at the steepest angle, basically straight down. To compensate, it grants the best advantage on block, leaving Salazar up to +6 and is never unsafe, only ever being -2 if done basically directly above the opponent. Can be up to +8 on hit.
Medium: Travels at a relatively sharp angle. The most versatile version, grants varying frame data, ranging from +4 to -4 on block. Can be up to +6 on hit.
Heavy: Travels at a very horizontal angle, letting Salazar jumpscare opponents with a dive kick from like ⅔rds of the screen away. On block, ranges from +4 to -6. Can be up to +6 on hit.
Overdrive: Travels at an angle equivalent to the medium strength. Is always a consistent +4 on block, no matter where it hits, and launches on hit, allowing a combo into medium or overdrive Blowout or other combo finishers.

Undeniably Admirable:
(Half Circle Back + Punch)
Only available at style level 2
A command grab that cannot be blocked. Salazar grabs the opponent by the chin, points them towards his face, and flashes a dazzling smile. Does no damage, but grants a follow up combo if connected. If whiffed, Salazar is left in a lengthy recovery animation as he shakes his head and mutters to himself. Both versions have the same range, and 8 frame startup. Both versions apply scaling to follow up combos.
Any Strength: Leaves Salazar +7 and point blank in front of the opponent.
Overdrive: Leaves Salazar +9 and point blank in front of the opponent.

Put ‘Em Down:
(Dragon Punch + Kick)
Only available at style level 3
Salazar grips his hat and then leaps forward while performing a spinning wheel kick with his back leg. In addition to looking spectacular, this move functions as a fantastic combo ender and also a great anti air, shoring up one of Salazar’s weaknesses. All base versions spike opponents into the floor, causing a knockdown and doing high damage. All versions strike mid, have upper body invulnerability to jumping attacks, and can hop over lows.
Light: Salazar performs a single leaping kick with a lightning quick 5 frame startup. Has a decent combination of vertical coverage and forward movement, making it a reliable anti air, and combos from any button except crouching and standing light punch. Does the lowest damage of all versions. Causes a knockdown on hit, -5 on block.
Medium: The downward spike Salazar performs at the end of the kick becomes noticeably more powerful, dealing higher damage. Links from medium buttons. Causes a knockdown on hit, -8 on block.
Heavy: Salazar performs two leaping kicks, with the first kick staggering grounded opponents and launching aerial ones, guaranteeing the second hit. Does extremely high damage, and is a great finisher for juggle combos, although it won’t combo from any normals naturally (except launchers). Causes a knockdown on hit, -10 on block.
Overdrive: Has immunity to fireballs until it hits, meaning unlike other versions, this strength also has use as a neutral tool. Salazar quickly leaps forward, performing the same two kicks as the heavy version but faster. Causes a wall bounce on hit. Frametraps and combos off of heavy normals, but can be interrupted off of other normals. Just barely safe on block at -3, but leaves Salazar point blank, vulnerable to a strike throw mixup.

Super 1:
Heat Buster:
(Double Quarter Circle Forward + Punch)
“How you feeling?”
“Two for one!”
The screen freezes as Salazar spins his gun around his index finger once, then pulls back the hammer on his revolver while pointing it outstretched. The screen then unfreezes and Salazar rapidly fans the hammer with his other hand, unleashing a lightning quick barrage of six bullets that strike from fullscreen, finishing by asking “You okay?” Hits blazing quick with only 7 frames of startup, and can be used to punish a lot of spaced moves. Also destroys all strengths of fireballs, obliterating enemies who try to zone out Salazar. A fantastic combo ender, and also uniquely can combo from some pokes on counter hits due to its quick startup. Sends the opponent fullscreen and causes a hard knockdown, but due to the distance the opponent is launched, Salazar gets no meaningful Oki unless the opponent is cornered (this does let him use Do ‘Em Dirty to gain a style stock). If Salazar uses two of these supers in 1 combo, he will use a unique voiceline, and strike a pose when he finishes, automatically gaining 1 style stock. Has invincibility until it hits, and is -30 on block. A fantastic super that does basically everything, easily one of the best level 1 supers in the game, its only weakness being slightly less damage than most level 1 supers. 

Super 2:
Super Taunt:
(Down Down Down + 2 Kicks)
“Gods I’m so cool.”
The screen freezes as Salazar condescendingly gestures at the opponent while slicking back his hair, with the screen unfreezing after the taunt (which makes this move rather hard to punish, as the bulk of it occurs during a super freeze). Salazar instantly gains level 4 style, no matter what style he was previously at. In addition to raising the style level, also has use as a combo link, as it can be used to continue combos after overdrive special moves or start combos after super cancelable pokes. Leaves Salazar +7 after overdrive Blowout (assuming he cancels before the final shot) and +9 after overdrive Put ‘Em Down (Salazar must cancel into this move after the first aerial kick, while he’s grounded).

Super 3:
Safe To Say:
(Double Quarter Circle Forward + Kick)
“Check this!”
“This is my time!”
“Take notes!”
“You WISH you were me!”
 Salazar spins his gun around his finger twice, then lunges forward while swinging his gun's butt at the enemy's jaw. On contact, engages a cinematic where Salazar’s opponent is staggered by the blow, and throws out a haymaker punch which Salazar wheels around, folding into the opponents body. He grabs them by the chin, and kicks their knee out from beneath them, knocking the opponent down to one knee, where Salazar, standing tall and still holding them by the chin, points them towards his face before flashing them a dazzling smile. He then takes his hand off of the opponent's chin, and points downwards. The opponent looks down, revealing that Salazar has his gun in his other hand leveled directly at the opponent's face. There is a brief moment where the opponent's shock registers, then Salazar lets rip an incredibly powerful bullet shot, blasting the opponent in the face before he strolls back to midscreen. Grants poor oki but lets Salazar safely set up a taunt. Has a unique mechanic, where depending on Salazar’s style level, the move will have less scaling applied in combos. At 0 style, this move actually has 10% more scaling applied to it in combos, while every level gained decreases that scaling by 10%, meaning at max style this move does 20% more damage when used in a combo then other level 3 supers (his voice line will also change depending on style level). Do note that the damage of the super when used raw is the same as other base level 3 supers.

Critical Art:
The Be-All-End-All:
“No holds barred!”
Salazar swings his gun at the opponent in the same manner as his base level 3. On contact, Salazar steps back and unleashes a furious volley of countless shots into the opponent, bullet after bullet striking them in the chest. The camera closes in on Salazar’s gun, still firing, as it glows hotter and hotter, eventually burning red. Salazar eventually yells in pain as he burns his hand and stops firing. The opponent staggers for a second, then looks directly at the camera as from offscreen, Salazar throws his still burning gun at the opponent, which smacks them in the face and bounces off them, neatly landing back in Salazar’s hand. The opponent looks up, bewildered, just in time for Salazar to rush in and slam them across the face with his fist, sending them flying away as Salazar recovers. Due to its unstylish nature, this move doesn’t benefit from style levels like the base level 3, and will always do the same amount of damage. Grants better Oki then the base level 3, and lets Salazar set up a taunt.

Win Quotes:
(vs. Zenthos) “I ain’t normally one to comment on someone else’s appearance, but gotta say, I dig the scarf.”
(vs. Kalle) “Kid with tunes like that, why carry a spear, you’re already on fire!”
(vs. Vile) “(spits) When you meet her, tell the missus I’m sorry.”
(vs. Melancholia) “Always liked you miss. You’ll hafta show me how to cook sometime.”
(vs. Ngann) “Had some warlocks ask how you taste. Guess I’ll tell ‘em: salty.”
(vs. Beast) “Ain’t got nothing funny to say to you. Us warlocks’ll be happier for your death.”
(vs. Gauss) “Woah hey man you good? Hey look there’s no shame in takin’ a break- and he’s gone.”
(vs. Salazar) “Alas: my style was too fashionable, my gun, too cool, my wit, too funny. You never stood a chance.”
(vs. Laecaera) “Listen darling, I admire the effort, but you forgot one crucial thing: ain’t no magic beatin’ a gun.”
(vs. Alphard) “I respect the hustle. ‘Long as you come out on top am-I-right?”

Godslayer:
The Exile

Iris + Rosaline:
Paladin Of Water, Queen Of Blood
Replaces heavy kick with an assist button, letting them swap out each other or call in assists like a tag fighter.

Laecaera:
The All Knowing Mage
“I will find him. And you will teach me how.”
Archetype: Stance
Master Of All Trades…
High Damage
Great Pressure
High Mobility
Zoning
…But Not Always
Low Health
Weak Lights
Technical
Stubby Normals

Light Punch*:
Frame: 5
A short range slap Laecaera performs with her front hand, with notably wimpy range, even for a light normal. Laecaera’s only special cancelable light normal, but its short range makes it difficult to link into.

Light Kick:
Frame: 5
A quick shoto style light kick Laecaera performs with her back leg. -1 on block. Cannot be special canceled, but has a target combo with medium kick.
Medium Kick (TC)**:
Laecaera plants her foot down from the light kick and uses it to pivot and spin into a thrusting kick with her other leg coated in blue magic. Does decent damage, and leaves Laecaera +2, although out of range for a true tick throw. -5 on block. Frame traps from standing light kick. Can be super canceled, which is Laecaera’s only really reliable way to get good damage from her light normals.

Crouching Light Punch:
Frame: 4
Laecaera’s fastest normal, and is +5 on hit, letting her link into both of her standing lights. A brisk open palm thrust Laecaera performs while crouching.

Crouching Light Kick:
Frame: 5
Laecaera does a stubby low kick with her front leg. A fast low that can chain into crouching light punch. Doing so leaves Laecaera out of range of standing light punch, but in range for standing light kick.

Medium Punch*:
Frame: 6
A quick but short ranged chest leveled side fist. Can be canceled into special moves. Is +1 on block, and +4 on hit.

Crouching Medium Punch*:
Frame: 7
Laecaera performs a somewhat clumsy forward crouch punch with her back hand. Has pretty good range by Laecaera’s standards, and has a generous confirm window for easy hit confirms. A great move for frametraps while in Gravity stance, and a good poke and buffer tool otherwise.

Medium Kick:
Frame: 11
A sideways kick Laecaera does with her forward leg, with quite good range. Can hop over lows, the only downside being that at the very tip, it can whiff on crouching opponents due to being quite high off the ground. A rather good but unrewarding poke that’s +4 on hit and -2 on block.

Crouching Medium Kick*:
Frame: 8
A pretty short ranged but otherwise strong crouching medium kick that can combo into most of Laecaera’s medium specials.
Side note: giving a character with a command grab a special cancelable cr.mk might be a mistake, but we’ll find out.

Heavy Punch:
Frame: 10
A large swinging side chop with decent range. Is not special cancelable. A good poke in neutral, and also Laecaera’s best punish counter starter due to its target combo. Has a target combo with standing heavy kick that does not combo unless the heavy punch starter hits as a punish counter. There is a large gap between the Heavy Punch and the follow up that can be interrupted with any 6 frame or quicker button. -5 on block.
Heavy Kick (TC)*:
Laecaera performs a quick high knee attack with her back leg, which launches the opponent and is special cancelable. A great combo tool with follow ups in all of Laecaera’s stances, such as heavy Flame Vent, Soaring Rush Beak/Claw, heavy/overdrive Seismic Quake, or heavy Psionic Orb. -10 on block.

Crouching Heavy Punch*:
Frame: 11
Laecaera performs a crouching straight punch. Has good range and is special cancelable, but has a lot of whiff recovery, making it pretty easy to whiff punish.

Heavy Kick:
Frame: 13
Laecaera does a high swing kick with her front leg. A good anti air with upper body air invulnerability that causes opponents to flip out. On punish counter, launches the opponent, with limited follow ups, like Gravity or Hellmage By The Book. In the corner, Laecaera can connect back heavy punch into any of her juggle extenders for high damage. 

Crouching Heavy Kick:
Frame: 9
Laecaera steadies herself with one hand and performs an awkward sweep kick with her front leg. Causes a hard knockdown on hit, -11 on block.

Back Heavy Punch*:
Frame: 8
Laecaera performs a quick, upward angled swipe punch. A decent anti air, and launches on hit into juggles.

Down Heavy Kick (Air Only):
Only available during Hellmage stance
Frame: 16
Laecaera stalls her momentum and balls herself up, before thrusting her legs down and slamming downwards at a very steep diagonal angle, legs covered in fire. A great move for baiting anti airs. Can be plus on block if it hits the opponent in the feet, and is only ever punishable if the opponent blocks it from max height, in which case it’ll be -4. Can be up to +5 on normal hit depending on how low it hits.

Forward Heavy Punch:
Only available during Monster Herder stance
Frame: 6
Laecaera steps forward and performs a backfist. Has two separate follow ups, one with forward heavy punch and one with forward heavy kick. -5 on block.
Forward Heavy Punch (TC):
The bird behind Laecaera soars forward and performs a downward talon slash. Hits overhead, and frametraps from base forward heavy punch. Has another follow up. -5 on block.
Down Heavy Kick (TC):
The wolf in front of Laecaera dashes forward and performs a low claw swipe. Hits low, and frametraps from base forward heavy punch. Has another follow up. -5 on block.
Forward Heavy Punch (TC):
Both animals fly forward and bodyslam the opponent. -8 on block. Frametraps from both the kick and punch follow ups. Causes a knockdown with great Oki.

Forward Heavy Punch*:
Only available during Gravity stance
Frame: 14
Laecaera gathers crackling purple energy in her hands, swings them clockwise, then pushes them both forward in an open palm thrust. Short ranged, but an incredibly good pressure normal that’s +4 on block with almost no pushback, letting her frame trap into either crouching medium punch or Gravity Flux, and is special cancelable to beat BA. +8 on hit, letting Laecaera start damaging combos, but applies extra scaling. On hit against an airborne opponent, causes a hard knockdown. On punish counter or counter hit, launches the opponent into a spinning juggle state, with limited follow ups. An insanely good normal that enables Laecaera’s Gravity form to be the grappler menace it is.

Forward Throw:
Frame: 5
Laecaera reaches out with both hands, grabs the opponent by the head, and begins charging her fists with blue mana. After a moment, she unleashes a large blast, causing the opponent to spin and fall. Grants poor Oki.

Back Throw:
Frame: 5
Laecaera grabs the opponent by the head, and using a blast of purple magic, teleports them behind her with their back facing her. She then kicks them in the spine, sending them flying away.

Unique Mechanic:
All Knowing:
Laecaera is a stance character, every ten seconds that passes on the stage timer, Laecaera will swap stances, moving through a set order of Hellmage -> Monster Herder -> Gravity -> Psionic and then resetting back to Hellmage. Laecaera’s special moves change depending on which stance she’s in, and she also gains access to certain command normals. Note that if Laecaera performs a special move right as she changes stances, it will still use the move from the previous stance. Wouldn’t want players' inputs being eaten randomly.

Hellmage:
While in Hellmage form, Laecaera floats slightly above the ground, with flames dancing across her fingers and hair. Laecaera always starts each round in this form, and it’s designed to be a generalist that doesn’t really excel in any situation but is suited to everything.

Blaze:
(Quarter Circle Forward + Punch)
A unique semi fireball/pressure tool Laecaera can use to steal turns or force the opponent to approach.
Light: A traditional fireball. Very simple, no thrills, Laecaera simply uses her back hand to throw forward a slow moving mid hitting orb of fire. Extends juggles after back heavy punch, which can then be finished with heavy Flame Vent.
Medium: Again, a traditional fireball, but with slightly faster startup and longer recovery, that travels much faster, and can combo off of her standing light punch.
Heavy: Laecaera crosses both arms before unfolding them, unleashing an aoe of fire around her that works as a decent anti air, and is safe on block at -3, and neutral on hit. However, if the heavy punch button is held, Laecaera instead charges the move, granting it much slower startup, but making it +2 on block and +6 on hit. The uncharged version combos out of medium and heavy normals, but the charged version only combos out of punish counter heavy normals.
Overdrive: Similar to the heavy version. Uncharged causes a knockdown, and charged causes a wall splat.

Flame Vent:
(Dragon Punch + Punch)
A very traditional dragon punch. Laecaera coats her back arm in fire, then performs a rising, leaping uppercut into the air. All versions have air attack invincibility on the upper half of her body. A great anti air and combo ender. All versions except heavy link out of any button, including lights due to their quick startup.
Light: Laecaera doesn’t move forward and performs a quick uppercut. Quickest startup but lowest damage and doesn’t go very far forward. A great panic anti air.
Medium: Laecaera moves forward slightly as she performs the uppercut. Generally her most reliable anti air, despite it’s slightly slower startup. 2 hits.
Heavy: A combo extender as opposed to ender. After landing a heavy Flame Vent, the opponent is launched into the air again, letting Laecaera connect a medium/overdrive Flame Vent. This move grants Laecaera great damage while in Hellmage stance. To compensate, it will not link from light normals, only medium and heavy ones.
Overdrive: Startup equivalent to the medium version, with higher damage. Invincible until it hits.

Monster Herder: 
While in Monster Herder stance, Laecaera summons a small white wolf in the foreground, and a large eagle type bird in the background. While in this form, she walks in a ready combat position. Monster Herder form is designed as a low damage Rushdown stance, that lets Laecaera get in and set up for her dangerous grappler form.

Dire Straits:
(Quarter Circle Forward + Punch)
A dashing special that can be used to get in the opponents face and bully them with plus frames. Laecaera leaps atop the wolf next to her, which then dashes forward while striking with its claws. All versions cause a knockdown on hit.
Light: Travels the shortest range, but has the quickest startup. The wolf leaps forward, and performs a large claw slash. Can be up to +2 on block when spaced well, but if Laecaera performs it while too close to the opponent, she is left punishable at -5.
Medium: Travels a good range, about half screen, and can leave laecaera up to +3 if it hits at the very tip. If spaced poorly, Laecaera is left -5.
Heavy: Very slow startup, but uniquely, hits overhead. Can leave Laecaera up to +3, or if spaced poorly, -5.
Overdrive: Startup slightly slower than the medium version, and is always safe on block, at max -2, and can be up to +3. Has complete immunity to projectiles until it hits.

Soaring Rush:
(Quarter Circle Forward + Kick)
Laecaera leaps into the air atop the large bird and enters a stance she can perform several follow ups from. All strengths have the same startup and only really alter distance covered, with the exception of Overdrive. A great move that can be used to set up a vortex or close the distance on zoners.
Light: Travels a very short distance, less than a forward jump. Can be combined with the medium strength to perform a left right mixup after a hard knockdown. Will not cross up after a hard knockdown.
Medium: Travels forward about the distance of a forward jump. Can be used to perform a left right mixup after a hard knockdown, as it will cross up after one.
Heavy: Travels extremely far, about ¾ screen. A great option for closing distance and punishing fireballs.
Overdrive: Leaps in an arc towards the opponent wherever they are on screen, with the arc descending directly in front of them. 
Follow Ups:
Beak (Any Punch): A dive kick type move. The bird stalls for a brief moment then dashes at a diagonal angle with its wings tucked in and its beak outstretched. Like all dive kicks, it’s a fantastic neutral skip move that can punish fireballs easily. Depending on spacing, this move can be at max, +5 on hit and +3 on block, but if poorly spaced, can be neutral on hit and -4 on block. The angle of the dive kick becomes less steep for each strength of button, with light punch sending Laecaera at a very steep angle and heavy sending you down at a much more sloped angle. Also useful as a combo extender after a launcher, such as back heavy punch or the heavy punch heavy kick target combo. Laecaera can usually finish this juggle with sweep for a hard knockdown, or if she transitions to Gravity after landing this in a juggle, she can perform medium (or heavy in the corner) Seismic Quake.
Claw (Any Kick): An overhead claw scratch. Laecaera briefly stalls, then quickly slams directly downwards, with the bird stretching out it’s talons. Cannot be blocked while crouching, and causes a hard knockdown on hit, but if it whiffs, has extra landing lag. +3 on block.
Talon (Grab): The bird reaches down with both talons outstretched, and picks up the opponent before throwing them into the ground, causing a hard knockdown. Does rather low damage for a command grab,  about as much as a throw, but grants amazing Oki. If the grab whiffs, the bird falls down rapidly, and Laecaera is left very vulnerable.
Fall (Press Nothing): The bird simply lands on the ground. Has a bit of landing lag. Can be used to bait anti airs or for Oki setups.

Gravity: 
When entering this stance, Laecaera banishes the wolf, and takes on a much more grounded stance, with her fists clenched as purple lightning begins crackling up and down her limbs. This mode is designed to capitalize on the pressure Monster Herder stance creates, by pressuring the opponent with dangerous frametraps and command grabs.

Gravity Flux:
(Full Circle + Punch)
Laecaera reaches out her front hand, coating it in purple magic. A command grab. On contact, Laecaera levitates her opponent and herself into the air with purple energy, then slams them downwards. All versions have startup equivalent to a normal throw, and deal very very high damage. If Laecaera whiffs the throw, the magic in her hand crackles and explodes, and she covers her eyes with her back hand, leaving her very vulnerable as she recovers.
Light: Has the longest range of all strengths. However, it has absolutely terrible Oki, leaving Laecaera at full screen. She can dash up to be slightly closer and still positive, but with no significant way to pressure the opponent. This isn’t as big a deal as it may sound however, as remember, after 10 seconds in Gravity form she transitions to Psionic form, meaning she can actually just use this distance to start zoning.
Medium: Worse range than the light version, but with better damage and better oki, leaving Laecaera +2 and and within striking distance after a dash.
Heavy: Range equivalent to a normal throw, with very high damage to boot. Uniquely, Laecaera can choose where to deposit the opponent. If she presses nothing during the grab, they are dumped in front of her, leaving her +2 and very close to the opponent, but if she holds forward during the grab animation, they are instead placed at fullscreen, letting Laecaera set up her zoning.
Overdrive: Range equivalent to the medium version with damage higher than the heavy version and the same unique choosable Oki.

Seismic Quake:
(Quarter Circle Forward + Kick)
A combo ender and anti air. Laecaera stomps the ground, shooting a pulse of purple magic into the earth that creates a wave of black rock shards.
Light: Is an anti air, not a combo tool like other strengths. Laecaera stamps the ground, causing a large spike of rock to shoot upward from the ground beneath her at a diagonal angle, covering the distance above her and diagonal to her.
Medium: Creates two rippling black rock shards that bounce the opponent along them. Does very high damage, but grants basically no Oki. Connects from medium normals.
Heavy: Creates three rippling stone shards that launch opponents. Very high damage, but is also a juggle extender in the corner. If used in the corner, Laecaera can connect Gravity By The Book after it. Connects from heavy normals.
Overdrive: Functions the same as the Heavy version, but connects from medium normals.

Psionic:
When entering Psionic stance, Laecaera begins floating in air, and her eyes glow purple as her hair begins to float. This form is designed as a Zoner to capitalize on the space created after Gravity Flux.

Mindfray:
(Charge Back > Forward + Punch)
A very strong projectile. Laecaera holds her hand to her head, then throws it forward, throwing off a spinning glowing pink cube shaped projectile. Travel speed is dependent on the strength of the button. All versions have extremely fast recovery and startup to make up for being a charge move.
Light: Travels the slowest. Combos after back heavy punch, which juggles further. In the corner, Laecaera can land a heavy Flame Vent for truly ludicrous damage. 
Medium: Travels faster than the light version.
Heavy: Travels extremely fast.
Overdrive: The fastest traveling and fastest recovering projectile, with recovery so speedy opponents can jump anticipating a projectile and still eat an anti air. 2 hits, and beats non overdrive projectiles. Causes a knockdown on hit.

Brain Blast:
(Charge Back > Forward + Kick)
Laecaera crosses both hands above her head while hunched over, than unfolds both hands and folds backwards, shooting forth a large beam from her face that travels quite quickly. Has one hit of projectile durability, and compliments the slower Mindfray by functioning as a quicker projectile for checking approaches, or just as a poke in neutral. Can be charged, if Laecaera chooses to hold down the kick button, she will hold the tucked in position until the button is released. After 30 frames of charging, this empowers the beam, greatly increasing its travel speed and granting it an extra hit. On block, this move is usually safe, while the charged version is plus, and on hit it staggers opponents, while the charged version causes a limited juggle.
Light:
Medium:
Heavy:
Overdrive: 

Psionic Orb:
(Charge Down > Up + Punch)
An arcing projectile Laecaera basically always wants to have set up. Laecaera presses her back hand to her head, then uses her other hand to throw the projectile upward at an angle. The projectile dissolves once it hits the ground or the opponent.
Light: The projectile falls relatively slowly, trapping the opponent.
Medium: The projectile lingers in the air above the screen extra long, stopping the opponent from jumping longer than the other versions.
Heavy: Due to how fast the projectile travels, this is essentially a projectile based anti air.
Overdrive: The projectile bounces once off the floor  up to about waist height when it hits the ground, granting it better horizontal range and making it linger longer.

Distortion Field:
(Down Down + Any Punch)
Laecaera presses both hands to her head, then stretches them both wide, expanding a pink bubble all around her. Due to its slow startup, this move can only be safely performed after a knockdown. While in this bubble, all of Laecaera’s projectiles become two hit (including projectiles from other stances), both versions of Inversion gain invincibility until the teleport concludes, and Psionic Orb creates pulses as it travels in small aoes, further increasing it’s area covered. Also all Flame Vent strengths gain a new effect where the flames glow pink, and deal significantly more damage (this is likely more of an Easter egg than anything practical). The bubble lasts 8 seconds before dissolving, and persists through stances.

Inversion (Forward):
(Forward + 3 Kicks)
Laecaera closes her eyes and glows bright pink, then vanishes before reappearing in front of the opponent. If extremely close to the opponent, will pass through them to about halfscreen. The teleport does have quite a bit of finishing lag, and as such can be punished if used without care.

Inversion (Back):
(Back + 3 Kicks)
Laecaera closes her eyes and glows bright pink, then vanishes before reappearing half screen behind her original position. The teleport does have quite a bit of finishing lag, and as such can be punished if used without care.

Super 1:
By The Book:
(Double Quarter Circle Forward + Punch)
“Time for a lesson!”
A powerful super which changes form depending on which stance Laecaera is currently in. Notably, no forms have any useful form of invincibility, meaning Laecaera must rely on her level 2 and 3 supers for a reversal.
Hellmage: Laecaera raises her forward leg and coats it in flame, before transitioning into a series of flaming spin kicks finishing with a large, exploding thrust kick that sends the opponent fullscreen. A simplistic combo ender and niche punish tool. Has no invincibility, and rather short range. Is only -6 on block with huge pushback, meaning outside of very niche circumstances it’s usually unpunishable. Can be comboed into out of medium or heavy normals, but due to its lightning quick 6 frame startup, it can also combo out of heavy Flame Vent for very high damage (also has an Easter egg where if used while in Distortion Field, the flames glow pink and the super does significantly more damage).
Monster Herder: Laecaera leaps onto the nearest wall, then dashes into the opponent atop her bird. Causes a hard knockdown on hit and is useful as a fireball punisher or anti air. Has varied startup depending on how close Laecaera is to the wall. Safe on block at -3, but leaves Laecaera point blank and vulnerable to a strike throw mixup. Combos out of heavy normals, any juggle extended by Beak, or heavy Flame Vent.
Gravity: A leaping anti air grab. Laecaera freezes while coating both arms in purple magic, then leaps upward at a diagonal forward angle. If she connects with the opponent, transitions to a cutscene where Laecaera uses purple magic to levitate the opponent up, up, and offscreen. She then begins floating back downwards, and right as she touches the floor, the opponent comes plummeting down, slamming into the ground with force. Has an extremely wide hitbox, but can only hit aerial opponents. Has complete invincibility until it hits, though is still a poor reversal, as it can’t hit grounded opponents and has a lot of landing lag. A fantastic anti air or niche but very damaging combo ender.
Psionic: A simple fireball super. Laecaera presses both hands to her head, then throws them forward, unleashing a massive pink cube that travels forward very quickly. Useful in fireball wars and as a combo ender. While in Distortion Field, causes a wall splat on hit, either allowing Laecaera to continue zoning or granting a combo based on her proximity.

Super 2:
Accumulate:
(Double Quarter Circle Back + Kick)
“Some nice moves you’ve got.”
Laecaera lunges forward with her palm glowing purple. Has full invincibility until it hits. On hit, activates a hit grab where Laecaera places one hand on the opponent's shoulder, and the other, glowing one against the opponent's face. Laecaera’s eyes glow purple, and a few seconds later, the opponent staggers backward, falling to the floor drained as Laecaera remarks “Interesting.” Causes a hard knockdown on hit and does rather mediocre damage for a level 2 super. -32 on block. On hit, Laecaera gains a new move dependent on the opponent's chosen character that is always tied to the input (Quarter Circle Back + Punch). This new move persists for the rest of the game, through rounds. Uniquely, in addition to being cancelable into anything special moves can be canceled into, this newly gained move can be canceled into out of any grounded overdrive special move, similarly to a level 2 super, letting Laecaera extend or end combos with them easily.
List Of Moves Gained:
(Zenthos) Black Flame Sword Draw: Laecaera conjures a sword of black flame at her side, pins it to her hip, then unleashes it and performs a wide, overhead arcing swing with it. The blade dissipates on hit, doing high damage and knocking opponents into the floor. Laecaera, unable to handle the power of the black flame, actually takes damage when using this move equal to 1/16 of her hp, although this will never lower her hp below 1. -8 on block. Has a unique mechanic where if the last back input and punch are pressed on the same frame, the move will cause a ground bounce on hit, allowing further combo extensions.
(Kalle) 
(Vile) Arisen: Laecaera swings her hand upward, summoning a single crumbling whirlwind of bones. This projectile moves forward very slowly, and on hit, staggers the opponent while launching aerial ones. Slow startup, making it difficult to combo into, but quick recovery. Notably, lets Laecaera set up a shield for herself after a knockdown, as by canceling into this move from an overdrive, she can summon a forward advancing projectile while still being plus, allowing her to mix the opponent up on their wake-up.
(Melancholia) Thorn Rush: Laecaera grows large red spikes around her arms, then dashes forward, arms crossed, and unleashes a X slash with both arms. Spikes airborne opponents into the floor, granting good oki. +2 on block, +5 on hit, allowing links into light combos. Consumes 1/10th of Laecaera’s hp when used, which is rather detrimental due to her already incredibly low hp. This hp reduction will never lower her below 1 hp.
(Ngann) Willpower Remnants: Instantly summons a faint, flickering clone of Laecaera that performs whatever her last action was. Extremely powerful when combined with overdrive moves.
(Beast) Earthstep: Laecaera flips forward, and slams both feet with power into the ground in front of her. While this animation is mostly for lore reasons (demonstrating how Laecaera must use gravity and both of her legs to achieve what Beast does with a simple step), it does have the niche utility of hopping over low attacks. On block, is +3 and on grounded hit, is +7, letting Laecaera continue combos. On aerial connect, causes a ground bounce with a limit of one bounce per combo. Only combos out of heavy normals or overdrive specials.
(Salazar) Try Out Something New: Laecaera strikes a pose and says a unique voice line, gaining a style stock. Unfortunately, because Laecaera has no style gauge, this functionally does nothing. Leaves Laecaera very vulnerable as she has no way to cancel the taunt early, and the entire duration of it leaves her in a punish counter vulnerable state. Despite its uselessness, it does have the unstated benefit of annoying the opponent.
(Laecaera): Laecaera gains no new special move.

Super 3:
Mind Break:
(Double Quarter Circle Forward + Kick)
“Let’s see what you’ve got.”
Laecaera readies both hands with purple magic. Then reaches forward with both hands outstretched. On contact with the opponent, triggers a cinematic. Laecaera plants a hand on either side of the opponents head, and her eyes flash pink, before it closes in on the opponents eye, showing the inside of their mind. Inside, there is always 1 large detail unique to each character, and a bookshelf. Laecaera grabs a book off the shelf and declares “I’ll be taking that.” It then cuts back to reality, where the opponent faints, and Laecaera strolls back to midscreen, cupping her chin and muttering. On whiff or block Laecaera shrugs and says: “Probably empty anyway.”

Critical Art:
Longinius’ Legacy:
“A gift from my mentor!”
Laecaera injects herself with a yellow syringe, and then performs the same grab animation as her level 3. She travels inside the opponents mind, with her form being significantly brighter and more distinct than in her level 3. She looks around, declares: “Nothing here worth saving,” then reaches both hands up, causing the opponent's mind and landscape to begin to swirl and get sucked into a pinhole in the center, similar to a black hole. The screen briefly flashes black when the opponents mind is fully sucked up, then cuts back to reality, where the opponent gasps and falls over, and Laecaera clutches her head with one hand while staggering back to midscreen. On whiff or block, Laecaera sadly mutters “I failed…” and falls to her knees before recovering.

Win Quotes:
(vs. Zenthos) “Is there something to learn from your mad ramblings? Or is it simply the blubbering of a failing mind?”
(vs. Kalle) “You’re just some kid, you’ve got no idea why I need this, nor do you need to know.”
(vs. Ngann) “I won! I guess you aren’t unbeatable after all, Ngann.”
(vs. Vile) “I recognize your ice magic, Rimerian. Now teach it to me.”
(vs. Melancholia) “Your magic seems far too agonizing to ever wield, but I suppose just in case…”
(vs. Beast) “Now that I’ve earned your respect, have a seat. Talk with me.”
(vs. Gauss) “Please- I’ve searched for so long, please, tell me you're him!”
(vs. Salazar) “There is no reason to talk with you. You have no value to me.”
(vs. Laecaera) “Psionic training is coming along nicely…”
(vs. Alphard) “See, I’m fit, I’m able! Now show me more!”

Year 2 (4 Characters): 

Abraxas:

Alphard:
Gravity’s Cybernetic Master
“The stars share their secrets.”
Archetype: Grappler
High Damage 
Command Grab
Massive Pokes
Resets
Tanky
No Special Cancelable Mediums/Heavies
Awful Oki
Slow
Super Reliant
Limited Combos

Light Punch:
Frame: 4
Alphard does a short punch with his normal arm. Pretty good range for a four frame normal, meaning opponents must space -4 moves slightly better than against most characters. +5 on hit, and -2 on block.

Crouching Light Punch:
Frame: 5
Alphard does a short crouching jab. Better range than its standing counterpart. +5 on hit and -3 on block.

Light Kick*:
Frame: 7
Alphard does a long ranged standing side kick, with excellent range for a seven frame move. Generally Alphards best combo link, as it has long range and is special cancelable. +5 on hit and -2 on block.

Crouching Light Kick*:
Frame: 6
Alphard does a quick low kick with his back leg. A fast, decent ranged, special cancelable low that functions more similarly to most characters crouching medium kicks, making for a great counter poke in neutral. +2 on hit and -3 on block. Cannot chain into other lights.

Medium Punch**:
Frame: 10
Alphard performs a large, quick horizontal knife hand slash with his blade arm. Alphard moves forward a decent amount while performing this move. A fantastic neutral button with low whiff recovery and a disjointed hitbox, making it a great move for poking or shutting down an opponent's options at the midrange. -4 on block and +7 on hit. Can be super canceled, but is extremely difficult to hit confirm, requiring either a read that the opponent will get hit, or a wild guess.

Crouching Medium Punch**:
Frame: 8
Alphard does a large, crouching knife hand swing with his blade arm. A fantastic counter poke with low whiff recovery, but less range and damage than his standing medium punch. Also a great frametrap option after Alphard gains plus frames. While not cancelable, it is +6 on hit, letting it link into crouching light kick. -4 on block.

Medium Kick:
Frame: 12
Alphard does a long ranged step kick with his forward leg. Can hop over lows, due to a somewhat disjointed hurtbox. +2 on hit and -3 on block. Has a target combo with heavy kick.
Heavy Kick (TC):
Alphard performs another step kick forward with his back leg. Causes a knockdown on hit and forms a true blockstring from medium kick. -10 on block.

Crouching Medium Kick:
Frame: 9
Alphard does a single legged sliding low kick with extremely good range. A unique crouching medium kick that functions more like a sweep. Causes a hard knockdown on hit and is -8 on block.

Heavy Punch:
Frame: 14
Alphard performs a long ranged, lunging stab with his blade arm. Enormous range, covering about halfscreen, and moves Alphard forward a great deal. Rather long whiff recovery, making it easy to whiff punish. +2 on hit and -4 on block with high pushback, making it usually safe. Has a target combo with heavy kick. 
Heavy Kick (TC)**:
Alphard reaches his other arm forward and then yanks backward, creating a large purple wave of energy that vacuums the opponent towards Alphard. Leaves the opponent point blank. +2 on hit and -8 on block, but can be hit confirmed rather easily. Grants Alphard a true strike throw mix on hit, making it a fantastic and rewarding target combo to land, but is very unsafe on block. Frametraps from standing heavy punch. If standing heavy punch lands as a punish counter, and then this target combo is used, it will actually launch the opponent into a tailspin towards him, letting him combo into Vortex or any medium normal.

Crouching Heavy Punch:
Frame: 15
A massive, completely disjointed and highly rewarding anti air that heavily punishes opponents who try and jump at Alphard, but its slow startup means it must be used as an extremely early anti air. Alphard performs a upward diagonal knife hand chop, with massive range above and diagonal to him. On regular hit against an airborne opponent, causes a hard knockdown, granting Alphard great oki which is very rare for him. On punish counter against a grounded or airborne opponent, this move launches the opponent, allowing Alphard to connect crouching heavy kick, and then into further extensions. These high damage combos make this move a terrifying whiff punish, and also a dominant punish counter starter. On regular hit against a grounded opponent, this move sends them flying away, making it a decent poke with great range, although it can whiff against crouching opponents from further away. -5 on block.

Heavy Kick:
Frame: 20
Dropkick
Alphard leaps forward, tucks himself into a ball and performs a leaping, horizontal, two legged dropkick. Alphard is considered airborne during this attack, and can hop over lows or dodge throw attempts while using it, although that dodge is only active once Alphard has actually left the ground. On punish counter, sends the opponent tumbling across the ground, and causes a wall slump if they’re cornered, letting Alphard combo into Gravity Well, super 3, Depth Plunge, or other extensions.

Crouching Heavy Kick**:
Frame: 22
Alphard jumps forward, tucks himself in, then performs a harsh, double legged stomp. An extremely unique button, this move can jump over lows and Alphard is technically considered airborne during it. Hits overhead, and causes a hard knockdown on hit, granting fantastic oki while being -4 on block. On counter hit, punish counter, or on hit against an aerial opponent (including ones that have been launched), this move causes a ground bounce, letting him combo into light, medium, or overdrive Vortex, any medium button, or Star Shower.

Forward Medium Kick: 
Frame: 12
Alphard performs a short hop and does a forward advancing leaping knee. Moves forward slightly and can hop over low attacks and throws, and is +7 on hit. Uniquely, the frame data of this move changes depending on if the opponent is standing or crouching: if the opponent blocks this move while standing, it is -3, but if they block it while crouching, it’s a massive +4, setting up a strike throw mix on block. This means despite not being an overhead, it still hugely punishes crouching opponents.

Forward Heavy Kick:
Frame: 16 (24)
Alphard steps forward while performing a massive advancing axe kick. Despite appearances, it doesn't hit overhead, but causes a hard knockdown on hit, making it a great combo ender for pursuing oki. Does high damage, moves forward, and is -2 on block, although with very little pushback. Can be charged, and if it is, the pushback is reduced even further, and its frame advantage on block becomes +4, granting Alphard a true strike throw mix, although on hit the effect doesn’t change. Both versions have a long, active hitbox, making them great at stopping approaches.

Forward Throw:
Frame: 5
Alphard grabs the opponent, raises them high, then cracks them over his knee before throwing them away. Useful as a safer option compared to Gravity Well, as it doesn’t leave Alphard super vulnerable, although with significantly damage. Also, while at midscreen it grants rather poor oki as it throws the opponent so far away, in the corner, it leaves Alphard point blank and very plus, meaning he is one of the extremely privileged characters to have a throw loop.

Back Throw:
Frame: 5
Alphard simply picks up the opponent by the torso, and throws them behind him, with poor oki.

Gravity Well:
(Full Circle + Punch)
The command grab that makes Alphard a terrifying opponent. All strengths have startup equivalent to a normal throw, with far greater range (the light version has range equivalent to most characters medium punches) making them terrifying for punishment or for pressure. Higher strengths of this move exchange range for more damage. Alphard reaches out with both arms, and on contact against the opponent, Alphard spawns a rapidly spinning black hole behind the opponent, causing them to rapidly spin around it diagonally before he desummons it, which slams them into the ground. The opponent revolves around the black hole once for the light version, twice for the medium, thrice for the heavy, and four times for the overdrive. All versions cause a hard knockdown, but send Alphard fullscreen, meaning they grant extremely poor Oki and basically reset to neutral. If any strength whiffs, they leave Alphard in a lengthy recovery animation.
Light: The lowest damage but with the best range. Does about 20% of an opponent's hp. It should be noted that, for a five frame move, the range on this attack is quite good, and makes a lot of otherwise safe if spaced moves punishable.
Medium: An inbetween of light and heavy, with great damage and with pretty solid range. Does about 25% of an opponent’s hp.
Heavy: Lowest range, but absolutely massive damage, doing around 30% of an opponent’s hp.
Overdrive: Slightly less range than the medium strength with higher damage than the Heavy strength, doing slightly more than 35% of an opponent’s hp. The last half of this move after the opponent has been slammed into the ground can be canceled into uncharged Alphard’s Descent for a huge damage increase, as it will hit them whilst they are grounded. Alternatively, said cancel can be used to set up the charged version for tricky resets.

Depth Plunge:
(Quarter Circle Forward + Kick)
Alphard quickly surges forward with both hands outstretched. On contact with the opponent, Alphard grabs them, picks them up with gravity magic and slings them away, causing a wall bounce. This move is a lunging command grab that cannot be blocked, and can surprise opponents expecting a normal. It has a large, persistent hitbox and covers a lot of distance, making it a pretty decent whiff punish and an excellent tool for catching backdashes. Alphard can cancel into this move from a normal to catch opponents who aren’t expecting a grab off guard. Although neither version does much damage, the wall bounce grants a combo after using it.
Normal: Alphard performs the lunging animation detailed above, and on hit against the opponent, picks them up with gravity magic, and chucks them, throwing them against the wall and causing a wall bounce. This lets Alphard combo into any version of Vortex at midscreen (the heavy version noticeably does absolutely insane corner carry), Star Shower, forward heavy kick, crouching heavy punch, or any medium. In the corner, Alphard can combo into crouching heavy kick first and then finish the combo.
Overdrive: Quicker startup than the base version, but otherwise identical.

Seismic Crash:
(Quarter Circle Back + Kick)
A low hitting stomp projectile that hits full screen. All versions have 1 hit of armor from frame 4 onwards, including the light version! This lets Alphard weave through projectiles and attacks to get closer to the opponent.
Light: A feint Alphard can use to trick opponents into jumping at him. Alphard raises his leg, but then quickly recovers. Due to the aforementioned armor, Alphard can also use it to weave through projectiles to get to the opponent, although this obviously leaves him somewhat vulnerable whilst in recovery, and also tacks on grey health.
Medium: Alphard raises his front leg high, then stomps downward, unleashing a fullscreen hitting shockwave of gravity that hits low. This “projectile” functions more like a huge disjointed sweep, as it travels fullscreen instantly, will ignore and not clash with other projectiles, and causes a knockdown on hit. On punish counter or counter hit, causes a hard knockdown, letting Alphard close the distance. This move is also +4 on block, but with an extremely slow startup and high end lag, so it’s very vulnerable to being jumped over. Can combo from light normals, although if the light normal is blocked, the string is interruptible with any 4 frame normal.
Heavy: A significantly slower version of the medium strength that instead launches the opponent towards Alphard on hit. Limited follow ups include Vortex or standing medium punch. Very slow startup, with similar recovery to the medium version and is also +4 on block. The only way to combo into this is from a punish counter light normal.
Overdrive: Alphard does a similar step forward as with the medium strength. However, this shockwave actually leaves the opponent standing, and leaves Alphard +10, letting him continue the combo further. However, if Alphard does wish to knock the opponent down, he can press any kick button again after the first stomp, which will cause Alphard to perform a second stomp, with this one causing a soft knockdown against the opponent. Combos from light normals, making it a strong but meter costly combo extender. -2 on block.

Vortex:
(Dragon Punch + Punch)
An anti air special and combo ender. Alphard launches himself upward and forward with gravity magic, with the angle he leaps at being dependent on the strength of move used. All versions except the overdrive version activate the same hitgrab on hit, where Alphard grabs the opponent from behind and suplexes them into the ground, granting mediocre oki but fantastic corner carry. Has upper body invincibility against aerial attacks. Does higher damage than most anti airs, but is kinda lacking compared to most of Alphard’s moves.
Light: Alphard leaps almost straight upwards, with only a slight forward angle. Rarely used as a combo ender, but a great anti air with quick startup.
Medium: The best version for general use, which combines quick startup with good travel distance, making it fantastic for catching forward and back jumps (such as opponents trying to escape Gravity Well).
Heavy: Rather slow startup, but travels almost fullscreen, letting Alphard predictively catch fullscreen jumps or easily end combos. Alternatively, as a combo ender this move has outrageous corner carry, carrying the opponent roughly 60% of the way across the stage, but has limited routes to combo into it.
Overdrive: Has quick startup similar to the light version, but range more similar to the medium version. On hit, however, Alphard grabs the opponent by the shoulder, hovers in midair with gravity magic, and chucks them into the ground, where they land on their feet, stumbling, before Alphard slams down with a knife hand chop to their head. This causes a crumple on hit, making it extremely rewarding to land, as Alphard can essentially land anything he wants afterward, including Bound Orbit, making this one of the only ways for Alphard to combo into super 3.

Violet Nocturne:
(Down Down + 2 Punches)
A counter Alphard can use to steal back turns or as a reversal. Alphard crosses both arms, and if the opponent strikes him, he unleashes a pulse of purple energy, throwing out his chest and staggering the opponent. Has high endlag if the counter whiffs, leaving Alphard vulnerable. Does extremely low damage, about the same as a light normal.
Normal: Low damage, active from frame one, but is not immune to throws or projectiles, only strikes. Has a vacuum effect on hit that sucks the opponent towards Alphard, leaving them standing and right in range for a mixup, as Alphard is +3. On hit against an aerial opponent, causes a hard knockdown. 
Overdrive: Functions identically to the base version, but is also immune to grabs. Is still not immune to projectiles, and Alphard can be thrown out of it, which will score a punish counter.

Super 1:
Star Shower:
(Double Quarter Circle Backward + Punch)
“Wrath of the stars!”
Alphard hunkers low to the ground, then dashes forward with a shoulder ram. On hit against the opponent, Alphard performs a series of slashes with his blade arm and punches with his regular one, finishing by performing a large, seismic clap that sends the opponent flying away. Does higher damage than most level 1 supers. Grants very poor oki, but makes Alphard’s poking and strike game much more potent when the opponent has to fear him tacking on this move to add significantly more damage, as it combos from all of his cancelable normals. Also has complete invincibility until it hits, making it a rewarding but very slow reversal. Due to its slow startup, Alphard is significantly more vulnerable to safe jab or meaty setups than most characters.

Super 2:
Alphard’s Descent:
(Double Quarter Circle Forward + Kick)
“Meteor-”
“Fall!”
“Strike!!”
“CRASH!!!”
Alphard leaps into the air and begins charging, surrounding himself in crackling purple energy and sucking up earth and dust around him. After the kick button is released, Alphard slams downward at a diagonal angle in front of him, striking the opponent. Has invincibility while Alphard descends, making it immune to reversals or anti airs. Has no invincibility on startup, however, meaning it cannot be used as a reversal and meaty attacks will easily stop it. Has different levels of charge depending on how long Alphard holds down the button, with different levels having different functions. Every time the level of this move increases, Alphard will flash purple:
Level 1: If Alphard charges for less than 30 frames, he gets the level 1 strength. This version can be used to catch opponents who try and jump out of later strengths, as it has a large diagonal angle and will catch early jumps (do note that it must be released rather early to catch back jumps unless the opponent is cornered). Does average damage for a level two, and can be comboed into using certain overdrive moves. Causes a hard knockdown on hit with great Oki, and is usually safe on block at -4 with high pushback.
Level 2: If Alphard charges for 30-80 frames, he gets the level 2 strength. This version is +4 on block, granting Alphard a true strike throw mix, and does higher damage than the level 1 version.
Level 3: If Alphard charges for more than 80 frames, he gets the level 3 strength. Alphard will automatically descend if this move is charged for more than 120 frames. This version is unblockable, and on contact against the opponent, does mediocre damage and causes a crumple, allowing Alphard to combo into whatever he wants. 

Super 3:
Bound Orbit:
(Double Full Circle + Punch)
“There’s no escape!”
Alphard clasps both hands together before pulling them apart, forming a black hole between them. This super is a command grab that CANNOT BE AVOIDED after the cinematic. That means that if you’re in range and you see that cinematic, and you didn’t already jump or backdash prior, you’re getting grabbed. With a lightning quick 6 frame startup, complete invincibility until it hits, range equivalent to light Gravity Well, high damage, all in addition to being a command grab, this is unquestionably one of the strongest supers in the game, a potent tool both offensively and defensively. However, its complicated motion means its input must be performed while jumping, dashing, performing an attack, or doing some other action, as otherwise trying to do a double 360 input will cause a jump. Additionally, it’s extremely difficult to combo into without a crumple. Does more damage than most level 3 supers. On contact with the opponent, engages a cinematic where Alphard and the opponent begin levitating as an enormous star grows behind the opponent. Alphard pushes forward his hand, and with a wave of gravity magic, pushes them into the star. If this move kills, then it shows a silhouette similar to “The Creation Of Adam” with Alphard pushing the opponent away and the opponent reaching back to him. If it doesn’t kill, the opponent falls back to the ground and Alphard lands near them.

Critical Art:
Event Horizon:
“INFINITY BECKONS!”
Alphard performs the same lunging gesture as before. On contact with the opponent, Alphard grabs them by the face, as the black hole flies off of his hand and into the background. The camera pans around them as they begin to float, born aloft by Alphard’s gravity magic, before the camera pans over, revealing the black hole has grown exponentially. Alphard then lets go of the opponent, where they vanish into the infinite darkness. If this kills. The opponent vanishes, but if they live, they are spat back out and fall to the ground.

Win Quotes:
(vs. Zenthos) “Oh thank god he shut up.”
(vs. Kalle) “My magic is much more than just flashing lights kid!”
(vs. Vile) “It’s over, I’m done serving you! I beat you- I BEAT YOU!”
(vs. Melancholia) “Those eyes… I see them in my nightmares, you know.”
(vs. Ngann) “I have been granted full amnesty- this is merely some petty grudge!”
(vs. Beast) “Brains and brawn big man, unlike you, I’m the full package.”
(vs. Gauss) “I like the new body, overall. Shame it’s gotta be used like this.”
(vs. Salazar) “You see? There is a better path, we can be free.”
(vs. Laecaera) “You’re learning! I’m so glad someone’s actually willing to learn!”
(vs. Alphard) “I’ll find someone, something. Some reason to keep going.”

Ulvein:
Flintlock, blunderbuss, canon super. Stance character? With a sailor stance he can enter wherein he glides forward on water. Summons the silence?
Uppercut called Sailors Salute
Brawler?

Crouching Medium Punch*:
Frame: 8
A slow but enormous poke, with range more equivalent to a heavy normal. Ulvein does a large flat knife hand swipe with his forward hand with huge range, making it an excellent tool in neutral. It’s also safe on block at -3, and can be canceled into a variety of useful options while being relatively easy to hit confirm. +5 on hit. To compensate for all of these strengths, the move has quite a lot of whiff recovery, meaning Ulvein needs to really make sure it connects.

Heavy Punch*:
Frame: 11
Ulvein whips out a large anchor and performs a large, roundhouse swing. Excellent range, making it a fantastic, massively disjointed poke. Does high damage, and is +4 on hit and -3 on block. On normal hit can combo into any version of Plunder, Sailor’s Salute, or light Man Your Stations! On punish counter, this move has a huge amount of hitstun, letting Ulvein easily hit confirm the punish, and then causes a wall splat. 

Heavy Kick:
Frame: 10
Ulvein does a heavy forward step kick. Notably, this move can be dash canceled on either hit or block, letting Ulvein cancel into a forward dash for pressure or a combo or a back dash to set up a spacing trap. Has quite a lot of active frames, meaning it’s quite easy to time on an opponents wake up, and is excellent for intercepting attacks. Normally 0 on block and +3 on hit, when dash canceled, it’s +1 on block and +4 on hit, granting Ulvein a combo on hit and pressure on block. On punish counter, this move causes a wall splat, sending the opponent flying away and sticking them to the wall. This wallsplat can be followed up at midscreen with either heavy Man Your Stations! or, if Ulvein is willing to be more technical, he can dash cancel into Seaman’s Swagger to charge forward and use either the forward heavy punch follow up, or use Sailor’s Salute. Alternatively, if he’s in the corner, he can just use either of those enders without Seaman’s Swagger.

Crouching Heavy Kick:
Frame: 16
Ulvein pulls himself back, then slides forward at a low angle, tucked to the ground with his feet outstretched. Causes a hard knockdown on hit, and travels about half screen quite quickly. -15 on block, and can never be spaced to be safe, meaning it’s hard to abuse, but obviously a half screen traveling low is incredibly handy, and a tricky tool for the opponent to deal with.

Forward Heavy Punch:
Frame: 20
Ulvein performs a massive lunging clothesline lariat which covers almost half the screen with a massive hitbox. An enormous advancing poke, this move is +4 on hit and -4 on block, making it relatively easy to punish. However, it comes with a target combo which frametraps off of this starter, catching opponents who attempt to punish it. Additionally, if Ulvein chooses not to do the follow up, he feigns the animation, pulling his other arm back before returning to his standing position. This lets him steal turns by tricking opponents into thinking he’ll use the follow up, only for him to instead hit them with a jab or medium punch or throw or anything to try and capitalize on that advantage. 
Forward Heavy Punch (TC):
A follow up that frame traps and combos off of the starter, Ulvein lifts up his other arm and does a stern side punch. Also a decent combo ender, as it grants a hard knockdown with great Oki, letting Ulvein continue to pressure his opponent. However, it is even more unsafe than the starter at -5.

Down Back Heavy Kick:
Frame: 11
A normal sweep that causes a hard knockdown on hit and is -11 on hit. Has really good range, making it an excellent whiff punish. Not much to say, it simply fulfills the roll taken by most characters sweeps.

Unique Mechanic:
Brimstone: 
Underneath Ulvein’s super bar is a meter called Brimstone segmented into two halves. This meter has 100 points total, with the points consumed by certain moves. The first 50 points regen at a rate of 25 per second, but once it reached those first 50 points, it slows down to 10 points per second. Additionally, any time Brimstone is used, there is a 3 second cooldown placed on the bar where it will not regenerate, and this cooldown is refreshed if more Brimstone is used (although the cooldown will not stack).

Seaman’s Swagger:
(Quarter Circle Backward + Kick)
A stance move Ulvein can enter to perform several follow ups out of. Whilst in this stance, Ulvein can move both forwards and backwards, and also perform any of his special moves. Additionally, whilst in this state he has slippery ice physics, which cause him to slide around in whichever direction he is moved in or whenever he uses a special move. Additionally, if he dashes forward and then enters the stance, his momentum is preserved, allowing him to move forward extremely quickly whilst doing attacks or specials.
Normal: A small tide pool of frothing waves gathers at Ulvein’s feet, and he enters a much more active position where it looks like he’s trying to steady himself. Whilst in this state, he cannot dash, but he can move forwards and backwards at his regular walking speed (so slowly). He also has ice physics that cause him to retain momentum whenever he moves, including momentum from before he entered the stance, meaning he can use the momentum from his surprisingly good forward dash to speed across the screen surprisingly quick for a character of his size. Any of the follow ups performed out of this stance will retain said momentum, which can be used in a variety of ways depending on the follow up.
Overdrive: Identical to the regular strength, although with the yellow outline that accompanies all overdrive moves, with one notable exception: Ulvein has one hit of armor whilst in the stance, and any follow ups out of the stance also gain that one hit of armor, granting Ulvein devastating and uncontestable neutral.
Follow Ups:
Forward Heavy Punch: Functions identically to the forward heavy punch command normal, and grants Ulvein a lunging attack from stance. When paired with dash momentum, this becomes an almost fullscreen lunging mid attack that comes with a target combo that does good damage with great Oki. Especially devastating when paired with the armor from the overdrive stance, making it a dominant neutral tool. The momentum also lets it be used as a combo ender easier, where it does generally less damage than most enders, but with better oki.
Sailor’s Salute: Any version of this move can be performed out of this stance, granting Ulvein a forward moving anti air, which also has use in certain combo routes (like after a wall bounce midscreen).
Man Your Stations: Ulvein can perform any strength of this move after stance, which, combined with dash momentum, can be used to get ahead of the cannonball to set up a mixup, or can be used to move whilst using Ulvein’s gatling gun to grant himself better Oki.

Sailor’s Salute:
(Dragon Punch + Punch)
An anti air, reversal, and combo finisher. All versions except the overdrive version grant a knockdown with pretty good Oki, letting Ulvein keep pressure on his opponent. All versions have upper body invincibility to air attacks.
Light: Ulvein stays in place and performs a quick leaping uppercut. Low damage, but extremely quick startup, making it a great panic anti air or combo ender.
Medium: Ulvein takes a step forward and performs a spinning, leaping uppercut. Pretty solid damage and relatively quick startup makes this a great anti air or combo ender.
Heavy: Functions identically to the medium version, with the notable exception that on hit against the opponent, this consumes 50 Brimstone, and in return, Ulvein causes a fiery explosion on contact, greatly increasing the damage. Also, the explosion has a heavy amount of hitstop and controller vibration, making it both incredibly satisfying and also very easy to link into level 3 super. If Ulvein attempts to use this strength without the sufficient Brimstone, the medium version is used instead.
Overdrive: Ulvein’s primary reversal, with full invincibility until it hits. Ulvein performs a forward step, then does a leaping, spiraling uppercut. Unlike the other strengths which are only a single hit (or 2 hits for the heavy version) this version hits 6 times. Grants extremely poor Oki, essentially resetting to neutral, and because Ulvein is not considered grounded during any portion of it, it cannot be canceled into any super.

Man Your Stations!:
(Quarter Circle Forward + Punch)
Light: Ulvein whips out a one handed flintlock and unleashes a single shot, firing off a fast moving projectile that hits mid. Relatively quick startup and recovery. Can be used in a fireball war or as a combo finisher, and will link off any normal. Leaves the opponent standing.
Medium: Ulvein pulls out a large, 2 handed canon and after a brief startup, unleashes a large cannonball which slowly travels forward in a spinning, wobbly way. Leaves the opponent standing on hit, with a high amount of hitstun and blockstun. Unlike the other two strengths, this cannonball isn’t really a combo tool, as it’s far too slow to combo from anything other than heavy normals, where you usually have better options. Instead, this cannonball is a fantastic approach option due to its slow travel speed, which lets Ulvein follow behind it either by walking or by using Seaman’s Swagger. This places a massive hitbox in front of Ulvein that lets him easily close in on opponents. A more advanced tech that can be used is to dash forwards, use Seaman’s Swagger to preserve the dash momentum, then cancel into this move, which, due to the slippery ice physics, will actually let Ulvein move ahead of the cannonball, granting him a combo on hit and complete safety on block. Overall, this is a fantastic move and a vital cornerstone of Ulvein’s neutral, but to compensate for all of its strengths, it drains a harsh 50 points from the Brimstone bar. Attempting to use this move without the sufficient Brimstone causes Ulvein to pull out the canon and unleash a large puff of smoke from it, which does no damage. He then scratches his head.
Heavy: Ulvein pulls out a large tripod mounted Gatling gun with a hand crank. He then begins rapidly spinning the crank whilst cackling, unleashing a furious barrage of bullets that travel quickly and strike fullscreen. Whilst it has slow startup, the countless bullets that destroy projectiles make this a great zoning counter and a fantastic combo ender due to its high damage. It also does a huge amount of chip damage on block with a massive amount of pushback, making it completely safe as it essentially resets to neutral, although the slow startup means it can be fairly easy to jump over and punish. The amount of bullets fired depends on the Brimstone bar, as it fully drains the bar on use, with a total of 3 bullets fired per 10 Brimstone consumed. The final bullet will always cause a hard knockdown, and all bullets will combo into each other.
Overdrive: Ulvein whips out a blunderbuss and begins charging it. Once the buttons are released, Ulvein unleashes a massive, short ranged shotgun blast. Can be used as a quick combo ender after any normal, including lights. Can be charged for up to 20 frames (after which it will fire automatically) to cause a wall bounce, although the amount of combos where Ulvein can do this is somewhat limited. 

Plunder:
(Dragon Punch + Kick)
A mixup tool that comes in many different forms, serving as both a tool for combos and for opening the opponent up.

Super 1:
Beach ‘Em:
(Double Quarter Circle Forward + Kick)

Super 2:
Whaler Punch:
(Double Quarter Circle Forward + Punch)
Ulvein rolls up the sleeve in his forward arm, with a closeup showing his muscles tensing and tattoos, then unleashes a solid, forward stepping uppercut. Causes a knockdown on hit and is -30 on block, making it incredibly unsafe. A solid, high damage level two with full invincibility until it hits and a rather quick startup of 10 frames, making it easy to combo into, with a notable gimmick: depending on how many times the quarter circle forward input is done, the super changes:
Level 1: Functions as described above, this version is used if only two quarter circle inputs are performed.
Level 2: If the user inputs three quarter circles, they get this strength. Ulvein does a short circle with his arm before unleashing the uppercut. This version slows the startup to 15 frames, but increases its damage significantly.
Level 3: The final practical strength, if the user performs four quarter circle motions, they get the level four version. Ulvein rolls up both sleeves and compacts both hands together into a volleyball double fist, then performs the same lunging uppercut. Slows the startup to a ludicrously slow 25 frames, killing most of its utility as a reversal, but in return it does truly ludicrous damage and also fully refills the Brimstone meter.
Level 4: A completely impractical secret strength. If the player performs ten consecutive quarter circle inputs and then inputs any punch they get this strength. Ulvein flexes so hard it rips open his shirt, revealing sailor tattoos across his stomach and chest. He then begins spinning in a circle and takes three spinning steps forward before delivering one final devastating uppercut. Essentially impossible to land in any combo or during neutral, this strength does have full invulnerability until it hits, but takes about 90 frames (1.5 seconds!) to come out. The only realistic way to land this is after a stun. However, to compensate it does about the same damage as a Critical Art and fully refills the Brimstone meter.

Massive fuck off heavy punch where he swings the anchor in an overhead designed to work as a whiff punish. Maybe causes a ground bounce?
Forward heavy punch is a massive forward advancing normal where he lunges forward with a swinging side hook. Technically unsafe on block, but has a target combo follow up that frametraps, but is also more unsafe.
Seaman’s Swagger, a stance move with several follow ups including the afformentioned forward heavy punch.

Level two super which is just a basic damage super except the damage increases with the amount of times you perform the input, with the cost of also increasing the startup.

Alatar:
Extremely good back walk speed
Has a unique backdash that functions more like a run.
Has to manage like 18 different meters/resources, including a dirt meter, and a stamina meter to keep his good back walk speed in check.
Combination of a joke character, resource management simulator, and survival horror game.

Super 1:
Rift Between:
(Down Down Down + 2 Kicks)
“I shall step between.”
Alphard uniquely has two level 1 supers. Unlike Star Shower, Rift Between is a utility super. After a brief startup which leaves Alphard counter hit vulnerable, the screen will freeze as Alphard lifts both hands behind the screen and tears open a rift behind himself (behind as in visually behind him in the stage, not to the left or right). This rift will follow behind him until the round ends or until he performs the same motion as above (Down Down Down + 2 Kicks). Upon using that input again, Alphard will step into the rift, and immediately teleport behind the opponent at jumping height, giving the opponent a chance to anti air him or at least prepare for an attack. This then consumes the rift. This follow up teleport costs no super. This move can only be safely used after a knockdown, but it basically allows Alphard to get in for free, at the cost of leaving him somewhat vulnerable.
Grappler jumpscare

Crown:
Prosecute:
(Quarter Circle Forward + Kick)
Zenthos flips forward, tucking himself in and retracting his hurtbox slightly. From this flip he can perform a variety of follow ups. Has use as both a neutral and combo tool. 
Light: Zenthos performs a short hop forward. Useful as a neutral tool for baiting opponents into an anti air, although the hop forward he does leaves him semi vulnerable.
Medium: This strength goes slightly farther than his forward jump. 
Heavy: Goes about 3/4ths way across the screen.
Overdrive: Zenthos’ forward jump changes from a flip to an upper surge with his blade outstretched horizontally before curling into the flip. Hits three times, and instantly causes a flip out, resetting the opponent in place where they can be hit by a mix up from the stance. Used as a combo ender, with slightly less damage than other overdrive options, but instantly grants a mixup. One of Zenthos’ best tools after something like a ground bounce.
Follow Ups:
Rest (Hold Down): If Zenthos holds down, he will land from the flip without performing a follow up. This landing has a bit of endlag, but is generally quite safe, and can be used to try and throw the opponent or perform a different mixup.
Underhand (Press Nothing)**: Zenthos lands and instantly goes into a low sword swipe. Hits low, and is -3 on block, +2 on hit. Unlike every other follow up, however, this version is super cancelable, and can be hit confirmed with practice, creating damaging combos into any of Zenthos’ supers, at the cost of sacrificing his turn. 
Accuse (Any Punch): Zenthos sticks out his sword in an overhead slasht and continues falling. Doesn’t alter the arc of Zenthos’ jump, but creates a continuous hitbox as he falls. However, Zenthos does have a largely expanded hurtbox whilst using this move, leaving him susceptible to being anti-aired, meaning he must condition opponents using the other options to force them to respect this. Always very plus on block, hits as an overhead and is usually around +5 on hit, although depending on how late it hits, it can be up to +9. On hit against an aerial opponent, causes a ground bounce, allowing follow ups like Pecking Order or BFSD.
Press (Any Kick): Zenthos instantly halts his momentum in midair and dives downward at a very sharp angle, both boots outstretched and black flames streaking from his legs. On hit against the opponent, causes a knockdown, granting Zenthos oki but no combo. Less useful than the average dive kick, not just because it causes a knockdown but also because Zenthos has no way to vary its angle, it will always travel at a very steep angle. Always safe on block at -1, and can be plus on block if it hits the opponent low in the body.
Expand (Forward Dash): Zenthos raises his sword in an upside down grip above his head. Once he gets close enough to the ground, he plunges his sword downwards, and uses it as leverage to perform another flip forward, identical to the base version of Prosecute, with all the same follow ups. Can be used to advance forward in the air towards opponents, or to cross up opponents.
Cede (Backdash): Zenthos uses a blast of black fire from his chest to perform a quick backward dash, retreating from the opponent, with a retracted hurtbox. Despite the blast of fire, this move has no hitbox, and is solely used to bait out anti airs or retreat.

================================================================================
SECTION 10: WORLDBUILDING LORE & STAGE DESIGN SPECIFICATIONS
================================================================================

--------------------------------------------------
10.1 World Lore: The Shattered Convergence
--------------------------------------------------
In an ancient era, a celestial event known as the Cinder-Frost Convergence fractured the realm into competing elemental and spiritual domains:
1. The Abyss of Cinder: The domain of dark fire and cursed flame, where warlords channel ethereal black-and-white flames.
2. The Eternal Rime: A frozen alpine tundra governed by ancient sorcery and frost magic.
3. The Sylvan Wilds: Ancient primeval forests where Nordic druids protect nature and channel primal animal spirits.

--------------------------------------------------
10.2 Character Faction & Lore Integration
--------------------------------------------------
• Zenthos (Cinder Inquisition): Dogmatic, execution-heavy warrior wielding volatile Black Flame. Mechanical signature: 2-frame Perfect Draw execution windows on specials for massive frame advantage and hard knockdowns.
• Melancholia (Sanguine Rime Cult): High-speed glass-cannon sorceress. Mechanical signature: Thorn Rush cancels (costs 10% HP for +2 on block / +5 on hit frame advantage) and Valkyrie Install.
• Sylas (Sylvan Heartwood Guard): Dual-stance shapeshifter. Mechanical signature: Druid Staff Form (nature magic, vine traps, wide disjointed staff strikes) <-> Frost Wolf Stance (bipedal dire wolf, 5f claw pokes, freeze waves, low-profile hurtboxes).

--------------------------------------------------
10.3 Fighting Game Stage Specifications
--------------------------------------------------
1. The Obsidian Spire (Melancholia's Home Stage)
   • 24-meter competitive width, dark obsidian floor tiles with high specular reflections. High visual contrast for black flame, blood thorn, and blue frost VFX. Reactive skybox lightning during Level 3 Supers.
2. Cinder-Ash Ruins (Zenthos's Home Stage)
   • 24-meter competitive width, charred gothic cathedral ruins with floating embers and ash clouds. Ground Bounce and Wall Slump attacks trigger dynamic ash cloud bursts.
3. The Frozen Heartwood (Sylas's Home Stage)
   • 24-meter competitive width, petrified pine forest under aurora borealis. Wall Splat impacts trigger crystal fracture particles and high-frequency ice shatter audio.

================================================================================
SECTION 11: SYLAS FROST WOLF FORM FRAME DATA & DESIGN BALANCE (LEAD DESIGNER)
================================================================================

--------------------------------------------------
11.1 Sylas (Frost Wolf Stance) Frame Data Table
--------------------------------------------------
• 2LP (Low Claw Poke): 5f Startup | 3 Active | 6 Recovery | -1 on Block | +4 on Hit
• 5MP (Biting Slash): 7f Startup | 4 Active | 11 Recovery | -2 on Block | +5 on Hit (Special Cancelable)
• 5HP (Heavy Frost Swipe): 11f Startup | 5 Active | 18 Recovery | -4 on Block | +6 on Hit (Ground Bounce on Counter Hit)
• 2MK (Low Frost Sweep): 8f Startup | 4 Active | 16 Recovery | -5 on Block | Hard Knockdown
• 623P (Frost Surge Slump): 12f Startup | 6 Active | 22 Recovery | -14 on Block | Launches into aerial Frost Combo

--------------------------------------------------
11.2 Lead Designer Balance Adjustments
--------------------------------------------------
1. Melancholia Thorn Rush Health Adjustment:
   • 50% of the 10% HP cost is now converted into Grey Health (recoverable health upon dealing damage to the opponent).
2. Zenthos Perfect Draw Visual Cue:
   • Frame 1 of a successful 2-frame Perfect Draw now triggers an explosive black-and-white flame hand flash and high-pitch chime SFX.

================================================================================
SECTION 12: ELEVENLABS CHARACTER VOICE PERFORMANCE SPECIFICATIONS
================================================================================

--------------------------------------------------
12.1 Roster Voice Personas & Emotional Prompts
--------------------------------------------------
1. Zenthos (The Cinder Prosecutor):
   • Persona: Angry, dogmatic, menacing prosecutor wielding black flame.
   • ElevenLabs Voice ID: CwhRBWXzGAHq8TQ4Fs17 (Roger - Resonant Warrior)
   • Intro Line: "In an angry menacing voice, Zenthos shouts: 'I am Zenthos! The black flames of my blade consume all!'"
   • Victory Line: "In a cold stern tone: 'The verdict is delivered. Your ashes shall answer to the court of cinder.'"
   • Super 3 Callout: "In a furious roar: 'Kneel before the flame! Inescapable Frenzy... EXTERMINATE!'"

2. Melancholia (Empress of the Sanguine Rime):
   • Persona: Sinister, unhinged, arrogant frost sorceress.
   • ElevenLabs Voice ID: EXAVITQu4vr4xnSDxMaL (Sarah - Frost Sorceress)
   • Intro Line: "With a cold sinister whisper breaking into an unhinged laugh: 'Feel the bite of absolute zero... your blood belongs to the rime!'"
   • Victory Line: "Arrogantly scoffing: 'Magnificent... another frozen corpse to adorn my gothic spire.'"
   • Super 3 Callout: "With fanatical manic intensity: 'Flesh to ice! Blood to rime! Crown of Thorns... PERISH!'"

3. Sylas (Sylvan Ice Druid & Frost Wolf):
   • Persona: Guttural ancient Nordic druid / feral arctic beast.
   • ElevenLabs Voice ID: VR6AewLTigWG4xSOukaG (Arnold - Nordic Druid)
   • Intro Line: "In a deep guttural ancient druid voice shifting into a wolf growl: 'The ancient roots awaken... and the frost wolf hungers for your soul!'"
   • Victory Line: "Feral breathing: 'The pack claims this territory. Nature leaves no trace of the weak.'"
   • Super 3 Callout: "Feral beast howl: 'Glacial Awakening! Break... SHATTER... RIP THEM TO PIECES!'"

4. Brutus (The Tectonic Titan):
   • Persona: Booming, heavy stone juggernaut.
   • ElevenLabs Voice ID: pNInz6obpgDQGcFmaJgB (Adam - Heavy Titan)
   • Intro Line: "In a deep booming stone-shattering voice: 'Stone stands eternal! You will crumble against the mountain!'"
   • Victory Line: "Heavy stone breathing: 'Dust to dust. The earth reclaims what was built.'"

5. Lyra (The Lightning Conduit):
   • Persona: High-energy, confident electric trapper.
   • ElevenLabs Voice ID: 21m00Tcm4TlvDq8ikWAM (Rachel - Lightning Conduit)
   • Intro Line: "In a fast confident electric voice: 'Sparking up! Let us see if your reflexes can match lightning!'"

6. Vesper (The Umbral Puppet Master):
   • Persona: Eerie, dual-layered void sorceress.
   • ElevenLabs Voice ID: AZnzlk1XvdvUeBnXmlld (Domi - Shadow Weaver)
   • Intro Line: "In a dark dual-layered echoing voice: 'Solitude and I dance in the dark... step into our shadow.'"

7. Ignacia (The Scorching Talon):
   • Persona: Fiery, aggressive Rekka warrior.
   • ElevenLabs Voice ID: cgSgspJ2msm6clMCkdW9 (Jessica - Scorching Rekka)
   • Intro Line: "In a fiery fierce warrior yell: 'The Pyre Clan burns bright! Try to survive my claws!'"

8. Nereus (The Abyssal Mariner):
   • Persona: Deep, oceanic void captain.
   • ElevenLabs Voice ID: N2lUpW0C55xG3YxW5WZn (Callum - Abyssal Mariner)
   • Intro Line: "In a deep weathered oceanic voice with heavy resonance: 'The abyssal tide rises... drown in the depth of the void!'"
