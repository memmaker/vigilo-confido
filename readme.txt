Vigilo Confido
--------------

Survive. Adapt. Win.

A vanilla expansion for OXCE featuring content from EU2012 and others.

Mod.io page: https://openxcom.mod.io/vigilo-confido

The mod is feature complete and playable but has only seen testing by me.

=== Features ===

 - 5 soldier classes (Ranger, Grenadier, Specialist, Sniper, Psi Operative)
 - ~50 scripted abilities with unique skills for each class
 - 500+ callsigns for each soldier class
 - 20+ cutscenes from the remakes
 - 200+ voice files (Unit responsonse sounds)
 - 8 new alien units (Cyber Floater, Thin Man, Berserker, Armored Muton, Sectopod Drone, Muton Elite, Andromedon, Outsider)
 - 3 new weapon types in T1, T2 & T3 versions (Swords, Shotguns, Sniper Rifles)
 - Complete new graphics for all T2 & T3 weapons and armors
 - Complete rebalancing of all weapons, armors, units and deployments
 - Status, day & night and hit indicators
 - Laser weapons not reasearchable from the start
 - Laser weapons need recharging and can implode in the field
 - Limited Explosives
 - No Tanks (But the Gremlin drone instead)
 - Bring home alien weapons and research them for progress
 - Ground deployment added with a small research tree for squad size
 - "Killing Aliens destroys their Weapons" option is fixed
 - Additional status effects & Visualisations
 - Weapons can be disabled in combat
 - A buttload of maps (thanks to C.M.P)
 - Training rooms
 - Integrated the Commendations mod
 - Passive bonus items (S.C.O.P.E., etc.)

=== Requirements ===

OpenXcom Extended (OXCE) 6.4

Download release versions of OXCE here:
https://openxcom.org/oxce/release/

NOTE: For the intended experience, make sure you have sound turned on and the intro animation enabled.
At least on your first start.

=== Quickstart (via Ufopedia) ===

You can find information about the classes and their skills in the Ufopedia
under the "MILITARY MOLDING" category.

The changes on weapons and armors can be found under the "WEAPONS AND EQUIPMENT" section.

The category "MISSION OBJECTIVES" will always contain an entry with your current objectives.

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

There is also in-game description available in the Ufopedia (if you don't want to read some spoilers..).

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

=== Known Issues / Backlog ===
 - Testing, Balancing
 - Sound effects (Gremlin, Drone)
 - Sprite of combat experience commendation
 - No Heads-up about research in Ufopedia
 - Integrate with https://openxcom.mod.io/extra-explosions
 - Test newTurnUnit before first turn with extremes: killing, panic, etc.
 - Add Abduction missions without UFOs
 - Remove "Shard Assembly" when OXCE has been updated
 - Update to CMP 0.3
 - Callsigns second to names?
 - Make "Inventory Stats" a fixed user Option
 - Longer research
 - People can research "Basic Deployment"?
 - Normalize the music
 - Static smoke
 - Min Strength for Snipers should be higher
 - No UFOs, only terror missions in May?
 - Nanoscale Vest (More weight and nicer Sprite)
 - Weapon sounds
 - Predator accessible too early?
 - Poison working correctly? (With armor and vests?)
 - Nerf health of most aliens? Reduce TU costs?
 - Nerf Chryssalids and Zombies.

=== Out of Scope for 1.0 ===
 - More Units: Waspite?, Stun Lancer(?), Faceless(?), Turret(?), Exalt(?)
 - Crafts & Craft Weapons
 - New Mission Objectives
 - Gene Lab & MECs
 - FlagByKills for experience indicator
 - Battle Focus costs for flying
 - Enemy abilities (hardened ability: critical hit chance against this unit reduced by 60%)
 - Weapon fragments: https://openxcom.org/forum/index.php/topic,6868.0.html
 - Bleedout & Fatal Wounds
 - (You should also reduce the chance they go unconscious from normal shooting.)
 - Very easy to exhaust the one medi-kit activation on oneself 

=== Changelog ===

=== Changes in v.0.9.8 ===
 - Fixed alien melee weapons not hitting
 - No more early game base defense
 - Added Mechtoid enemy
 - Skeleton Key is now researchable (Will Update the mission objectives)
 - Floaters not spawning as Terrorists anymore

=== Changes in v.0.9.7 ===
 - Fixed: Mission objectives not updating when interrogating first live alien
 - Recovery of the hyperwave beacon from a stunned Outsider should now work (nearly as intended)
 - Adjusted facility build costs
 - Fixed Berserker corpses
 - Corrected X-Com Heavy Laser Ufopedia entry
 - Integrated CMP Rice Farm patch
 - Added numeral suffixes to the Skyranger names, indicating deployment size
 - Added built-in medi-kit to Gremlin to match Ufopedia description
 - Fixed missing string

=== Changes in v.0.9.6 ===
 - Strength not applied anymore to laser and plasma swords
 - Fixed Skyranger not purchasable and Basic Deployment unavailable
 - Adjusted build costs for new bases

=== Changes in v0.9.5 ===
 - Fixed terror mission crash
 - Reduced skill use cost of Aid Protocol (Specialist)
 - Scoring andjustments
 - Restructured alien missions

=== Changes in v0.9.4 ===
 - Plot mission deployments re-defined
 - Fixed mission completion bugs
 - Changed workspace requirements of manufacturing projects
 - Fixed display of Battle Focus costs in Skill Menu
 - Adjusted recovery times for wounded soldiers
 - Adjusted research times for most research projects
 - Fixed plasma weapon damage to intended values
 - Added short intro
 - Adjusted Sectopod Armor 
 - Introduced elerium cores
 - Adjusted research & manufacturing costs

=== Changes in v0.9.3 ===
 - Restructured introductionary research and story arc
 - Nerfed specialist shooting skill max cap
 - Re-balanced throwing starting stats for all classes
 - Added 10 points armor damage to proximity grenades (same as standard grenade)
 - Added passive bonus stats to items in ufopedia entries
 - Medi-kit is now a manufacture project (So these engineers got sth. to do)
 - Fixed some units missing the MECHANICAL tag
 - Reduced power of blaster launcher and small launcher
 - Added poison spit to thin man
 - Fixed special ability on andromedon
 - Removed Avenger and Lightning

=== Changes in v0.9.2 ===
 - Increased throwing stats for specialist (To allow for field logistics)
 - Reset general store size to normal
 - Set proximity grenade to intended power
 - Nanoscale research now needed for experimental armor project
 - Medi-kit now avaiable from the start (So the specialist is more useful)
 - Fixed introduction research topic showing up as researchable
 - Fixed crashes on mission end
 - Various bugfixes

=== Notes to self - HERE BE SPOILERS ===

DON'T READ IF YOU WANT TO EXPERIENCE THE STORY LINE FOR THE FIRST TIME:

EU2012 Story: https://www.ufopaedia.org/index.php/Storyline_(EU2012)
A list of cutscene names for special events. More info: https://openxcom.org/forum/index.php/topic,7476.msg117830.html#msg117830

"Bellator in Machina" - "Warrior in the machine"
"Mutare ad custodiam" - "We Change to Protect"

hook wishlist
missionBeginUnit -> Init unit before first turn
missionEndGame   -> End Conditions
dropItemUnit & pickUpItemUnit?
endMovementUnit?
weaponFiredUnit

Cutscene triggers:
 - On Construction finished
 - On manufacturing finished
 - Alien Base detected

Feature Wishlist:
requiredSoldierType for startingCondition
itemFlag: canNotSell
Ability to trigger skills for aliens, or at least let them choose between two weapons.

---

A: https://drive.google.com/open?id=1vszFp8uydC9u-NtU2nyGnt9LNLGHAP5B
V: https://drive.google.com/open?id=1-9TXCAiZ3B7GOQouKd7bAGwvI76Ejm88