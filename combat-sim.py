import random

agility = 0
boss_dodge_chance = 0
damage = 0
fight_duration = 0
flurry_charges = 0
flurry_increase = 1.3
flurry_procs = 0
flurry_refreshes = 0
strength = 0
total_attacks = 0
total_crits = 0
total_dodged = 0
total_glancing = 0
total_hits = 0
total_missed = 0
unflurried_time = 0
windfury_procs = 0

def weapon_skill():
    while True:
        orc = input("Are you an orc with an axe? y/n (hit enter for y): ") or "y"
        if orc in ["y", "Y"]:
            return 0.85
            break
        elif orc in ["n", "N"]:
            return 0.65
            break
        else:
            print("Please type y or n...")

def add_world_buffs():
    while True:
        buffs = input("World buffs (Dragonslayer, Songflower,  DMF,  DM,  Warchief, Hakkar)? y/n (hit enter for y): ") or "y"
        if buffs in ["y", "Y"]:
            return True
            break
        elif buffs in ["n", "N"]:
            return False
            break
        else:
            print("Please type y or n...")

def add_raid_buffs():
    while True:
        buffs = input("Raid buffs (imp. Battle Shout, imp. MotW, Trueshot, Strength of Earth IV)? y/n (hit enter for y): ") or "y"
        if buffs in ["y", "Y"]:
            return True
            break
        elif buffs in ["n", "N"]:
            return False
            break
        else:
            print("Please type y or n...")

def add_consumables():
    while True:
        buffs = input("Consumables (Mongoose, Giants, R.O.I.D.S, +20 str food)? y/n (hit enter for y): ") or "y"
        if buffs in ["y", "Y"]:
            return True
            break
        elif buffs in ["n", "N"]:
            return False
            break
        else:
            print("Please type y or n...")

def logging():
    while True:
        log = input("Do you want to output a full combat log? y/n (hit enter for n): ") or "n"
        if log in ["y", "Y"]:
            return True
            break
        elif log in ["n", "N"]:
            return False
            break
        else:
            print("Please type y or n...")

def attack():
    roll = (random.randint(1, 1000))
    if roll <= miss_chance * 10:
        return "Miss"
    elif roll <= (miss_chance + boss_dodge_chance) * 10:
        return "Dodge"
    elif roll <= (miss_chance + boss_dodge_chance + 40) * 10:
        return "Glancing Blow"
    elif roll <= (miss_chance + boss_dodge_chance + 40 + crit_chance) * 10:
        return "Crit"
    else:
        return "Hit"

def crit_damage(wf):
    if wf == True:
        return 2 * round((random.randint(wpn_dmg_lo, wpn_dmg_hi) + (((attack_power + 466) / 14) * weapon_speed)))
    else:
        return 2 * round((random.randint(wpn_dmg_lo, wpn_dmg_hi) + ((attack_power / 14) * weapon_speed)))

def hit_damage(wf):
    if wf == True:
        return round((random.randint(wpn_dmg_lo, wpn_dmg_hi) + (((attack_power + 466) / 14) * weapon_speed)))
    else:
        return round((random.randint(wpn_dmg_lo, wpn_dmg_hi) + ((attack_power / 14) * weapon_speed)))

def glance_damage(wf):
    if wf == True:
        return round(glance_penalty * (random.randint(wpn_dmg_lo, wpn_dmg_hi) + (((attack_power + 466) / 14) * weapon_speed)))
    else:
        return round(glance_penalty * (random.randint(wpn_dmg_lo, wpn_dmg_hi) + ((attack_power / 14) * weapon_speed)))

print("\n")
print("*** Welcome to Akash's Amazing WoW Classic Chadhancement Shaman melee damage calculator! ***")
print("This script will calculate a Classic WoW Enhancement Shaman's white melee damage (including")
print("Windfury and Flurry procs, glancing blows and boss dodges) over a given duration.\n")
print("The following assumptions are made:")
print("- The enemy is a lv63 raid boss with 4.8% total crit suppression")
print("- You are attacking from behind and will not be blocked or parried")
print("- You have 100% uptime on the boss")
print("- You are using Rank 4 Windfury Weapon")
print("- You are specced into 5/5 Flurry")
print("- You are specced into 3/3 Elemental Weapons")
print("- You are specced into 5/5 Weapon Mastery\n")

requested_fight_duration = input("Input the fight length in seconds (hit enter for 200000 - usually gives you 100k+ attacks): ")

if requested_fight_duration == "":
    requested_fight_duration = 200000
else:
    requested_fight_duration = int(requested_fight_duration.replace(",", "").strip())

attack_power = int(input("Input your Shaman's unbuffed attack power (hit enter for 750): ") or 750)

crit_chance = input("Input your Shaman's unbuffed crit chance (hit enter for 25): ")

# because level + 3 target has 3% crit suppression and 1.8% aura crit suppression
if crit_chance == "":
    crit_chance = 25 - 4.8
else:
    crit_chance = round(float(crit_chance.replace("%", "").strip()), 2) - 4.8

weapon_speed = round(float(input("Input your weapon speed (hit enter for Nightfall - 3.5): ") or 3.5), 1)

wpn_dmg_lo = round(int(input("Input bottom end weapon damage (hit enter for Nightfall - 187): ") or 187) * 1.1)

wpn_dmg_hi = round(int(input("Input top end weapon damage (hit enter for Nightfall - 282): ") or 282) * 1.1)

wpn_dmg_avg = round((wpn_dmg_lo + wpn_dmg_hi) / 2, 2)

miss_chance = input("Input your Shaman's miss chance (hit enter for 0): ")

if miss_chance == "":
    miss_chance = 0
else:
    miss_chance = int(miss_chance.replace("%", "").strip())

glance_penalty = weapon_skill()

# Level +3 targets have 6.5% chance to dodge at 300 weapon skill, 6% at 305
if glance_penalty == 0.85:
    boss_dodge_chance = 6
else:
    boss_dodge_chance = 6.5

world_buffs = add_world_buffs()

raid_buffs = add_raid_buffs()

consumables = add_consumables()

logs = logging()

if world_buffs == True:
    strength = int(input("Input your Shaman's unbuffed Strength score (hit enter for 150): ") or 150)
    agility = int(input("Input your Shaman's unbuffed Agility score(hit enter for 150): ") or 150)
    strength = (round((strength + 15) * 1.15)) - strength # songflower str + bonus str from Hakkar buff
    agility = (round((agility + 15) * 1.15)) - agility # songflower agi + bonus agi from Hakkar buff
    crit_chance = crit_chance + 10 + round(agility / 20, 2) # 5% ony, 5% songflower, agi
    wpn_dmg_lo = round(wpn_dmg_lo * 1.1) # DMF sayge buff
    wpn_dmg_hi = round(wpn_dmg_hi * 1.1) # DMF sayge buff
    attack_power = attack_power + 340 + (strength * 2) # 140 ony, 200 fengus, str
    weapon_speed = round(weapon_speed / 1.15, 2) # 15% haste warchief

if raid_buffs == True:
    if world_buffs == True:
        crit_chance = crit_chance + 0.92 # 16agi imp. motw with Hakkar buff
        attack_power = attack_power + 197 # 16str imp. motw + 70str strength of earth iv with Hakkar buff
        attack_power = attack_power + 390 # 100 trueshot, 290 imp. battle shout
    else:
        crit_chance = crit_chance + 0.8 # 16agi imp. motw
        attack_power = attack_power + 562 # 16str imp. motw, 100 trueshot, 290 imp. battle shout, 70str strength of earth iv

if consumables == True:
    if world_buffs == True:
        crit_chance = crit_chance + 3.4 # mongoose with Hakkar buff
        attack_power = attack_power + 161 # giants, roids, 20str food with Hakkar buff
    else:
        crit_chance = crit_chance + 3.25 # mongoose
        attack_power = attack_power + 140 # giants, roids, 20str food

print("\n**ENTERING COMBAT...**\n")

while fight_duration < requested_fight_duration:

    result = attack()
    total_attacks += 1

    if total_attacks == 1: # 1st attack occurs at time 0, so it doesn't consume fight time
        fight_duration = 0
    elif flurry_charges > 0:
        fight_duration = round(fight_duration + (weapon_speed / flurry_increase), 2)
    elif flurry_charges == 0:
        fight_duration = round(fight_duration + weapon_speed, 2)

    if result in ("Miss", "Dodge"):
        if flurry_charges > 0:
            flurry_charges -= 1
            if logs == True:
                if flurry_charges == 0:
                    print(str(fight_duration) + " sec: " + result + " - Flurry fades")
                else:
                    print(str(fight_duration) + " sec: " + result + " - Flurry charges remaining: " + str(flurry_charges))
        elif flurry_charges == 0:
            if fight_duration > 0:
                unflurried_time = unflurried_time + weapon_speed
            if logs == True:
                print(str(fight_duration) + " sec: " + result + "...")

        if result == "Miss":
            total_missed += 1
        elif result == "Dodge":
            total_dodged += 1

    if result in ("Glancing Blow", "Crit", "Hit"):

        # Bonus hits from WF don't consume Flurry or fight time so we do them separately
        windfury_check = random.randint(1, 5)
        if windfury_check == 1:
            if logs == True:
                print("--------------------")
                print("Windfury proc!")
            windfury_procs += 1
            total_attacks += 2

            for i in range(0, 2):
                result = attack()

                if result == "Miss":
                    total_missed += 1
                    if logs == True:
                        print(str(fight_duration) + " sec: Windfury " + result + "...")

                elif result == "Dodge":
                    total_dodged += 1
                    if logs == True:
                        print(str(fight_duration) + " sec: Windfury " + result + "...")

                elif result == "Glancing Blow":
                    total_glancing += 1
                    hit_dmg = glance_damage(True)
                    damage = damage + hit_dmg
                    if logs == True:
                        print(str(fight_duration) + " sec: Windfury " + result + " (" + str(hit_dmg) + ")")

                elif result == "Crit":
                    total_crits += 1
                    hit_dmg = crit_damage(True)
                    damage = damage + hit_dmg
                    if flurry_charges > 0:
                        flurry_refreshes += 1
                        if logs == True:
                            print(str(fight_duration) + " sec: Windfury " + result + " (" + str(hit_dmg) + ") - refresh Flurry")
                    elif flurry_charges == 0:
                        flurry_procs += 1
                        if logs == True:
                            print(str(fight_duration) + " sec: Windfury " + result + " (" + str(hit_dmg) + ") - gain Flurry")
                    flurry_charges = 3

                elif result == "Hit":
                    total_hits += 1
                    hit_dmg = hit_damage(True)
                    damage = damage + hit_dmg
                    if logs == True:
                        print(str(fight_duration) + " sec: Windfury " + result + " (" + str(hit_dmg) + ")")

        if result in ("Glancing Blow", "Hit"):
            if result == "Glancing Blow":
                total_glancing += 1
                hit_dmg = glance_damage(False)
            elif result == "Hit":
                total_hits += 1
                hit_dmg = hit_damage(False)
            damage = damage + hit_dmg
            if flurry_charges > 0:
                flurry_charges -= 1
                if logs == True:
                    if flurry_charges == 0:
                        print(str(fight_duration) + " sec: " + result + " (" + str(hit_dmg) + ") - Flurry fades")
                    else:
                        print(str(fight_duration) + " sec: " + result + " (" + str(hit_dmg) + ") - Flurry charges remaining: " + str(flurry_charges))
            elif flurry_charges == 0:
                if fight_duration > 0:
                    unflurried_time = unflurried_time + weapon_speed
                if logs == True:
                    print(str(fight_duration) + " sec: " + result + " (" + str(hit_dmg) + ")")

        elif result == "Crit":
            total_crits += 1
            hit_dmg = crit_damage(False)
            damage = damage + hit_dmg
            if flurry_charges > 0:
                flurry_refreshes += 1
                if logs == True:
                    print(str(fight_duration) + " sec: " + result + " (" + str(hit_dmg) + ") - refresh Flurry")
            elif flurry_charges == 0:
                flurry_procs += 1
                if fight_duration > 0:
                    unflurried_time = unflurried_time + weapon_speed
                if logs == True:
                    print(str(fight_duration) + " sec: " + result + " (" + str(hit_dmg) + ") - gain Flurry")
            flurry_charges = 3

        if windfury_check == 1:
            if logs == True:
                print("--------------------")

    if flurry_charges > 0 and (round(fight_duration + (weapon_speed / flurry_increase), 2) > requested_fight_duration):
        fight_duration = requested_fight_duration

    if flurry_charges == 0 and (round(fight_duration + weapon_speed, 2) > requested_fight_duration):
        unflurried_time = unflurried_time + (requested_fight_duration - fight_duration)
        fight_duration = requested_fight_duration

# Output
print("\n\n")
print("**********************************************")
print("ATTACK STAT SUMMARY")
print("**********************************************")
print("Attack power: " + str(round(attack_power)))
print("Crit chance: " + str(round(crit_chance, 2)) + "% (including boss crit suppression)")
print("Weapon speed: " + str(round(weapon_speed, 2)))
print("Miss chance: " + str(miss_chance))
if glance_penalty == 0.85:
    print("You have 305 weapon skill, so your Glancing Blows inflicted " + str(round((1 - glance_penalty) * 100)) + "% less damage.")
else:
    print("You have 300 weapon skill, so your Glancing Blows inflicted " + str(round((1 - glance_penalty) * 100)) + "% less damage.")

print("\n")
print("**********************************************")
print("COMBAT SUMMARY")
print("**********************************************")
print("Total attacks made: " + str(total_attacks))
print("- Total missed: " + str(total_missed) + " (" + str(round(total_missed / total_attacks * 100, 2)) + "%)")
print("- Total dodged: " + str(total_dodged) + " (" + str(round(total_dodged / total_attacks * 100, 2)) + "%)")
print("- Total glancing blows: " + str(total_glancing) + " (" + str(round(total_glancing / total_attacks * 100, 2)) + "%)")
print("- Total crits: " + str(total_crits) + " (" + str(round(total_crits / total_attacks * 100, 2)) + "%)")
print("- Total hits: " + str(total_hits) + " (" + str(round(total_hits / total_attacks * 100, 2)) + "%)\n")

print("Total Windfury procs: " + str(windfury_procs))
print("Total Flurry procs: " + str(flurry_procs))
print("Total Flurry refreshes: " + str(flurry_refreshes) + "\n")

print("Total fight time: " + str(round(fight_duration, 2)) + " seconds")
print("Time with Flurry: " + str(round(fight_duration - unflurried_time, 2)) + " seconds")
print("Time without Flurry: " + str(round(unflurried_time, 2)) + " seconds")
print("Flurry uptime: " + str(round(((fight_duration - unflurried_time) / fight_duration) * 100, 2)) + " percent\n")
print("Total damage: " + str(round(damage, 2)))
print("Total DPS: " + str(round(damage / fight_duration, 2)))
input("\nZug zug! Hit the enter key to exit.")
