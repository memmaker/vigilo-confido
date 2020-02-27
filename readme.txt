X-Com with Classes
------------------

A demake of the remakes.

=== Quickstart ===

You can find information about the classes and their skills in the Ufopedia
under the "MILITARY MOLDING" category.

The changes on weapons and armors can be found under the "WEAPONS AND EQUIPMENT" section.

=== Goals and influences ===

This started out as some experiments with Yankes scripts and soon got out of hand.
I wanted to have skills, like in the remakes and wanted to see which ones I could do.
Turns out I can do most of them.

So this then turned into a more complex mod with a class and skill system at its core and
with mechanical influences from the remakes (EU2012/XCOM2 and Phoenix Point).

My goal is to extend the vanilla X-Com experience with some
mechanics, items, units & lore references from the newer X-Com titles.

While my focus is on the class & skill system, I also completely rebalanced the
weapons and armors and some other gameplay elements.

I also want to try to add only graphics which keep the X-Com style and which harmonize
with the existing graphics. Each tier of items should be visually distinguishable.

Many thanks to XOps and his Xeno Operations for most of the graphical enhancements.
When looking through his modification of the game, I realized we shared many common goals
and it felt like his work was made with the same visual vision as my mod.

=== Concepts ===

Soldiers of each class can be hired directly by X-COM.
Soldiers can choose to undergo the military molding process, gaining access to their class skills in the process.
Classed soldiers receive additional active and passive skills for each level of training.
The active ones are activated with the special icon and the passive ones are always active.

There are three training phases. The initial molding process is awarded to soldiers when they are
hired by X-Com. The Second Phase (or Advanced Training) and Third Phase (or Elite Training)
add additional skills respectively.

Advanced level training requires: The second "Combat Experience" decoration,
which is awarded for 4 kills and 8 missions.

Elite level training requires: The fourth "Combat Experience" decoration,
which is awarded for 10 kills and 16 missions.

=== Skills ===

For a list of the currently implemented skills per class please refer to the file
Rulesets/classSkills.rul line 10, heading "Class Skill list".

=== Tiers ===

Weapons and armors all follow the three Tier concept.

T1 is available from the start.

T2 depends on alien alloys.
 - You should aim at researching "Laser Weapons" and "Predator Armor" until April.

T3 depends on Elerium-115.
 - You should aim at researching "Plasma Weapons" and "Warden Armor" until August.

Armor & Weapon Tiers
T1 - Kevlar Armor   & Conventional Weapons
T2 - Predator Armor & Laser Weapons
T3 - Warden Armor   & Plasma Weapons

=== Additional Changes ===

 - Complete rebalancing of all weapons, armors, units and deployments
 - Added status, day & night and hit indicators
 - Laser weapons not reasearchable from the start
 - Laser weapons need recharging
 - Blaster Launcher not that readily available (Not yet implemented)
 - Limited Explosives (Not yet implemented)
 - No Tanks (But the Gremlin drone instead)
 - Bring home alien weapons and research them for progress
 - Ground deployment added with a small research tree for squad size
 - "Killing Aliens destroys their Weapons" option is fixed
 - Additional status effects & Visualisations
 - Weapons can be disabled in combat
 - New alien units added (Cyber Floater, Thin Man, Berserker, Muton Elite)
 - t1 minigun floorob too high
Required: Presumably OXCE 6.4

=== CREDITS ===

DISCLAIMER:
I tried my best to track down the creators of all the assets I borrowed from other mods.
Since I am only human, I might have made some mistakes. So if you find something that is
credited falsely, has missing credits or have problems with the inclusion of your creation
in this mod, then please contact me. (memmaker on the OpenXcom discord.)

Units, Armors, Laser & Plasma Weapon Sprites from Xeno Operations XOps, recolored versions by The Martian and me
Alloy Sword Sprites by Civilian
Grenade Launcher Sprites by Sporb
Sniper Rifle Sprites by ???
Plasma Sword Sprites by ???
Shotgun Sprites by Dioxine, efrenespartano
Minigun Light Sprites by Wicked Wirtz
Training Rooms by Warboy1982
Hitbox Fix by Reaver of Darkness
Day & Night Indicators by Dioxine
Status Indicator Sprites by Captain Corkscrew, Ivan Dogovich, et al.
Commendations Mod by Shoes, Ivan Dogovich, hellrazor, jgatkinsn, Meridian
Psi Amp Sprites by efrenespartano & Badfella
New Grenade Sprites from XPiratez Mod by Dioxine (couldn't find the creator in credits)

Special Thanks to:
Meridian for his fork, his merging of my PRs and his constant support
Yankes for his script engine which made most of this possible and of course his support

All the great modders of the OXC/OXCE community who have a great spirit and
create new gameplay experiences for us all to enjoy. You rock!

=== License Information ===

Commendations Mod uses Attribution-NonCommercial-ShareAlike 4.0 International which I have included as "license.md"

=== Known Issues / Backlog ===
 - item categories
 - how to stun aliens?
 - gremlin affected by reaction accuracy adjustment
 - Sound effects (Gremlin, Minigun)
 - explain mechanics in Ufopedia (accuracy learning curve, skyranger replacement, night missions)
 - terror missions seem to be missing?
 - test andromedon enemy
 - change sprite of combat experience commendation
 - armor balancing
 - complete skill tests
 - Battle Focus costs for flying
 - Units to add: Thin man, Flying Drone, Stun Lancer(?), Mechtoid(?), Berserker, Outsider(?), Muton Elite, Faceless(?), Turret, Exalt?
 - multiple skyranger ufopedia entries
 - hardened ability: critical hit chance against this unit reduced by 60%
 - weapon fragments: https://openxcom.org/forum/index.php/topic,6868.0.html
 - resistances to damage types
 - missing gremlin corpse?