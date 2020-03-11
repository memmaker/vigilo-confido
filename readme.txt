Vigilo Confido
--------------

Survive. Adapt. Win.

A vanilla expansion for OXCE featuring content from EU2012 and others.

=== Changes ===

 - 5 new soldier classes (Ranger, Grenadier, Specialist, Sniper, Psi Operative)
 - 500+ callsigns for each soldier class
 - 20+ cutscenes from the remakes
 - ~50 new scripted abilities with unique skills for each class
 - 200+ new voice files (Unit responsonse sounds)
 - 6 new units (Cyber Floater, Thin Man, Berserker, Muton Elite, Andromedon, Outsider)
 - 3 new weapon types in T1, T2 & T3 versions (Swords, Shotguns, Sniper Rifles)
 - Complete new graphics for all T2 & T3 weapons and armors
 - Complete rebalancing of all weapons, armors, units and deployments
 - Added status, day & night and hit indicators
 - Laser weapons not reasearchable from the start
 - Laser weapons need recharging and can implode in the field
 - Limited Explosives
 - No Tanks (But the Gremlin drone instead)
 - Bring home alien weapons and research them for progress
 - Ground deployment added with a small research tree for squad size
 - "Killing Aliens destroys their Weapons" option is fixed
 - Additional status effects & Visualisations
 - Weapons can be disabled in combat
 - A buttload of new maps (thanks to C.M.P)
 - Added Training rooms
 - Integrated the Commendations mod
 - Added passive bonus items

Required: OXCE 6.4
Test Build available here: https://lxnt.wtf/oxem/builds/Extended/Extended-6.3.5-018c5b09d-2020-03-03-win64.7z

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

=== Known Issues / Backlog ===
 - resistances to damage types
 - item categories, list orders
 - Sound effects (Gremlin, Minigun)
 - test new enemies
 - change sprite of combat experience commendation
 - Battle Focus costs for flying
 - Units to add: Waspite?, Flying Drone, Stun Lancer(?), Mechtoid(?), Outsider(?), Faceless(?), Turret, Exalt?
 - Enemy abilities (hardened ability: critical hit chance against this unit reduced by 60%)
 - weapon fragments: https://openxcom.org/forum/index.php/topic,6868.0.html
 - missing gremlin corpse?
 - balancing of stuff (item costs, armors, etc.)
 - Psi Class and everything Psi is not yet finished
 - Weapon specific crit chances and crit damage
 - Ufopedia entries (Grenades & Status Effects, Armors, Autopsies)
 - Economics
 - EU2012 Style Medi-Kits (And usages)
 - Passive Inventory Bonus Items (Scope, etc.)
 - Melee, Dodge, etc.
 - Complete research bonuses for corpses
 - Make sure medi-kits work with ablative armor
 - flagByKills for experience indicator
 - Why are some maps still dark?
 - You could make a critically wounded soldier into a cyborg, instead of waiting for a month to recuperate.
 - Reduce dealing of fatal wounds and apply increasing chances of bleeding out instead of instant death
 - Test shredder and shred damage and the toArmor toArmorPre stuff
 - Sword hit animation
 - Make the Firestorm useful
 - EU2012 Story: https://www.ufopaedia.org/index.php/Storyline_(EU2012)
 - A list of cutscene names for special events. More info: https://openxcom.org/forum/index.php/topic,7476.msg117830.html#msg117830
 - Purge Celatids & Silacoids

=== Out of Scope for 1.0 ===
 - Base Facilities
 - Crafts & Craft Weapons
 - New Mission Objectives
 - Gene Lab & MECs
 - Cutscenes
 - Storyline & Mission Structure

"Bellator in Machina" - "Warrior in the machine"
"Mutare ad custodiam" - "We Change to Protect"

hook wishlist
missionBeginUnit -> Init unit before first turn
missionEndGame   -> End Conditions
dropItemUnit & pickUpItemUnit?
endMovementUnit?
weaponFiredUnit
