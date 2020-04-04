import random

flurry_increase = 0.7
flurry_charges = 0
flurry_refreshes = 0
total_attacks = 0
total_crits = 0
total_hits = 0
total_dodged = 0
total_missed = 0
total_glancing = 0
hasted_attacks = 0
unhasted_attacks = 0
windfury_procs = 0
damage = 0

def weapon_skill():
    while True:
        orc = input("Are you an orc with an axe? y/n (hit enter for y): ") or "y"
        if orc in ["y", "Y"]:
            return 0.85
            break
        elif orc in ["n", "N"]:
            return 0.6
            break
        else:
            print("Please type y or n...")

def add_world_buffs():
    while True:
        buffs = input("World buffs (Dragonslayer, Songflower,  DMF,  DM,  Warchief)? y/n (hit enter for n): ") or "n"
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
        buffs = input("Raid buffs (imp. Battle Shout, imp. MotW, Trueshot, Strength of Earth IV)? y/n (hit enter for n): ") or "n"
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
        buffs = input("Consumables (Mongoose, Giants, R.O.I.D.S, +10 str food)? y/n (hit enter for n): ") or "n"
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
    	return "miss"
    elif roll <= (miss_chance + 6.5) * 10: # Level +3 targets have 6.5% chance to dodge
        return "dodge"
    elif roll <= (miss_chance + 6.5 + 40) * 10:
        return "glance"
    elif roll <= (miss_chance + 6.5 + 40 + crit_chance) * 10:
        return "crit"
    else:
        return "hit"

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
print("- The enemy is a lv63 raid boss with 3% crit suppression")
print("- You are attacking from behind and will not be blocked or parried")
print("- You have 100% uptime on the boss")
print("- You are using Rank 4 Windfury Weapon")
print("- You are specced into 5/5 Flurry")
print("- You are specced into 3/3 Elemental Weapons")
print("- You are specced into 5/5 Weapon Mastery\n")

fight_duration = input("Input the fight length in seconds (hit enter for 200000 - usually gives you 100k+ attacks): ")

if fight_duration == "":
    fight_duration = 200000
else:
    fight_duration = int(fight_duration.replace(",", "").strip())

reported_fight_duration = fight_duration

attack_power = int(input("Input your Shaman's attack power (hit enter for 750): ") or 750)

crit_chance = input("Input your Shaman's crit chance (hit enter for 25): ")

if crit_chance == "":
    crit_chance = 25
else:
    crit_chance = round(float(crit_chance.replace("%", "").strip()), 2)

crit_chance = crit_chance - 3 # because level + 3 target crit suppression costs us 3% crit

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

world_buffs = add_world_buffs()

raid_buffs = add_raid_buffs()

consumables = add_consumables()

logs = logging()

if world_buffs == True:
    crit_chance = crit_chance + 10.75 # 5% ony, 5% + 15agi songflower
    wpn_dmg_lo = round(wpn_dmg_lo * 1.1) # DMF sayge buff
    wpn_dmg_hi = round(wpn_dmg_hi * 1.1) # DMF sayge buff
    attack_power = attack_power + 370 # 140 ony, 200 fengus, 15str songflower
    weapon_speed = round(weapon_speed * 0.85, 2) # 15% haste warchief

if raid_buffs == True:
    crit_chance = crit_chance + 0.8 # 16agi imp. motw
    attack_power = attack_power + 562 # 16str imp. motw, 100 trueshot, 290 imp. battle shout, 140 strength of earth iv

if consumables == True:
    crit_chance = crit_chance + 3.25 # mongoose
    attack_power = attack_power + 120 # giants, roids, 10str food

print("\n**ENTERING COMBAT...**\n")

while fight_duration >= 0:
    # Bonus hits from WF don't consume Flurry so we do them separately
    windfury_check = random.randint(1, 5)
    if windfury_check == 1:
        if logs == True:
            print("--------------------")
            print("Windfury proc!")
        windfury_procs += 1
        total_attacks += 2

        for i in range(0, 2):
            result = attack()

            if result == "miss":
                total_missed += 1
                if logs == True:
                    print("Miss...")

            elif result == "dodge":
                total_dodged += 1
                if logs == True:
                    print("Dodge...")

            elif result == "glance":
                hit_dmg = glance_damage(True)
                damage = damage + hit_dmg
                total_glancing += 1
                if logs == True:
                    print("Windfury hit (glancing blow): " + str(hit_dmg) + " dmg")

            elif result == "crit":
                hit_dmg = crit_damage(True)
                damage = damage + hit_dmg
                total_crits += 1
                if flurry_charges > 0:
                    flurry_refreshes += 1
                    if logs == True:
                        print("Windfury crit! " + str(hit_dmg) + " dmg, refresh Flurry")
                elif flurry_charges == 0 and logs == True:
                    print("Windfury crit! " + str(hit_dmg) + " dmg, gain Flurry")
                flurry_charges = 3

            elif result == "hit":
                hit_dmg = hit_damage(True)
                damage = damage + hit_dmg
                total_hits += 1
                if logs == True:
                    print("Windfury hit: " + str(hit_dmg) + " dmg")
        if logs == True:
            print("--------------------")

    # Now the actual attack
    result = attack()
    total_attacks += 1

    if result == "miss":
        total_missed += 1
        if flurry_charges > 0:
            hasted_attacks += 1
            fight_duration = fight_duration - (round(weapon_speed * flurry_increase, 2))
            flurry_charges -= 1
            if logs == True:
                if flurry_charges == 0:
                    print("Miss - Flurry fades")
                else:
                    print("Miss - Flurry charges remaining: " + str(flurry_charges))
        elif flurry_charges == 0:
            unhasted_attacks += 1
            fight_duration = fight_duration - weapon_speed
            if logs == True:
                print("Miss...")  

    elif result == "dodge":
        total_dodged += 1
        if flurry_charges > 0:
            hasted_attacks += 1
            fight_duration = fight_duration - (round(weapon_speed * flurry_increase, 2))
            flurry_charges -= 1
            if logs == True:
                if flurry_charges == 0:
                    print("Dodge - Flurry fades")
                else:
                    print("Dodge - Flurry charges remaining: " + str(flurry_charges))
        elif flurry_charges == 0:
            unhasted_attacks += 1
            fight_duration = fight_duration - weapon_speed
            if logs == True:
                print("Dodge...")        

    elif result == "glance":
        hit_dmg = glance_damage(False)
        damage = damage + hit_dmg
        total_glancing += 1
        if flurry_charges > 0:
            hasted_attacks += 1
            fight_duration = fight_duration - (round(weapon_speed * flurry_increase, 2))
            flurry_charges -= 1
            if logs == True:
                if flurry_charges == 0:
                    print("Hit (glancing blow): " + str(hit_dmg) + " dmg - Flurry fades")
                else:
                    print("Hit (glancing blow): " + str(hit_dmg) + " dmg - Flurry charges remaining: " + str(flurry_charges))
        elif flurry_charges == 0:
            unhasted_attacks += 1
            fight_duration = fight_duration - weapon_speed
            if logs == True:
                print("Hit (glancing blow): " + str(hit_dmg) + " dmg")

    elif result == "crit":
        hit_dmg = crit_damage(False)
        damage = damage + hit_dmg
        total_crits += 1
        if flurry_charges > 0:
            hasted_attacks += 1
            fight_duration = fight_duration - (round(weapon_speed * flurry_increase, 2))
            flurry_refreshes += 1
            if logs == True:
                print("Crit! " + str(hit_dmg) + " dmg, refresh Flurry")
        elif flurry_charges == 0:
            unhasted_attacks += 1
            fight_duration = fight_duration - weapon_speed
            if logs == True:
                print("Crit! " + str(hit_dmg) + " dmg, gain Flurry")
        flurry_charges = 3

    elif result == "hit":
        hit_dmg = hit_damage(False)
        damage = damage + hit_dmg
        total_hits += 1
        if flurry_charges > 0:
            hasted_attacks += 1
            fight_duration = fight_duration - (round(weapon_speed * flurry_increase, 2))
            flurry_charges -= 1
            if logs == True:
                if flurry_charges == 0:
                    print("Hit: " + str(hit_dmg) + " dmg - Flurry fades")
                else:
                    print("Hit: " + str(hit_dmg) + " dmg - Flurry charges remaining: " + str(flurry_charges))
        elif flurry_charges == 0:
            unhasted_attacks += 1
            fight_duration = fight_duration - weapon_speed
            if logs == True:
                print("Hit: " + str(hit_dmg) + " dmg")

# Output
print("\n\n")
print("**********************************************")
print("ATTACK STAT SUMMARY")
print("**********************************************")
print("Attack power: " + str(round(attack_power)))
print("Crit chance: " + str(round(crit_chance, 2)) + "% (including boss crit suppression)")
print("Weapon speed: " + str(round(weapon_speed, 2)))
print("Weapon damage (including 5/5 Weapon Mastery):")
print("- Bottom end: " + str(round(wpn_dmg_lo)))
print("- Top end: " + str(round(wpn_dmg_hi)))
print("- Average: " + str(round(wpn_dmg_avg)))
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
print("Total Flurry hasted attacks (incl glancing, missed, dodged): " + str(hasted_attacks))
print("Total unhasted attacks (incl glancing, missed, dodged): " + str(unhasted_attacks))
print("Total Flurry refreshes: " + str(flurry_refreshes) + "\n")
print("Total damage: " + str(round(damage, 2)))
print("Total DPS: " + str(round(damage / reported_fight_duration, 2)))
print("Flurry uptime: " + str(round(hasted_attacks / total_attacks * 100, 2)) + " percent")
input("\nZug zug! Hit the enter key to exit.")
