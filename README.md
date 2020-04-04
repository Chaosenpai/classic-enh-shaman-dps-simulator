# classic-enh-shaman-dps-simulator
Python script that calculates Classic WoW Enhancement shaman white damage over a given time frame.

This script is for theorycrafting a Classic WoW Enhancement Shaman white melee damage (including Windfury and Flurry procs, glancing blows and boss dodges) over a given duration. It will allow you to answer questions about gear like "Which is a bigger upgrade, 40ap or 1% crit?" by inputting the relevant values and running a simulated combat. It will allow you to add relevant world buffs, raid buffs and consumables if you wish.

Note that this is for calculating **white melee** damage only. Stormstrike, Fire Totems, Shocks etc are not included in this simulation.

The following assumptions are made:
- The enemy is a lv63 raid boss with 3% crit suppression
- You are attacking from behind and will not be blocked or parried
- You have 100% uptime on the boss
- You are using Rank 4 Windfury Weapon
- You are specced into 5/5 Flurry
- You are specced into 3/3 Elemental Weapons
- You are specced into 5/5 Weapon Mastery
