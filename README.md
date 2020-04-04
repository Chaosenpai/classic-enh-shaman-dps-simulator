# classic-enh-shaman-dps-simulator
Python script that calculates Classic WoW Enhancement shaman white damage over a given time frame.

This script is for theorycrafting a Classic WoW Enhancement Shaman's white melee damage (including Windfury and Flurry procs, glancing blows and boss dodges) over a given duration. It will allow you to answer questions about gear like "Which is a bigger upgrade, 40ap or 1% crit?" by inputting the relevant values and running a simulated combat.

Features:
- Run a sim over any timeframe. The script defaults to 200000 seconds as this is usually enough to allow 100k+ attacks
- Input your Shaman's attack power, crit %, weapon speed, weapon damage and miss chance
- The script differentiates between an orc with an axe (305 weaponskill) and everything else (300 weaponskill)
- Add relevant world buffs, raid buffs and consumables
- Output an optional full combat log showing flurry gain and fade, windfury procs, hits, crits, misses and glancing blows
- Summary at the end showing total attacks and breakdown (hit/crit/glance etc), Windfury procs, DPS, Flurry uptime and other stuff

Exceptions:
- This is for calculating **white melee** damage only. Stormstrike, Fire Totems, Shocks etc are not included in this simulation.

The following assumptions are made:
- The enemy is a lv63 raid boss with 3% crit suppression and 1.8% aura crit suppression
- You are attacking from behind and will not be blocked or parried
- You have 100% uptime on the boss (this is a theorycrafting script, after all)
- You are using Rank 4 Windfury Weapon
- You are specced into 2/2 Enhancing Totems
- You are specced into 5/5 Flurry
- You are specced into 3/3 Elemental Weapons
- You are specced into 5/5 Weapon Mastery
