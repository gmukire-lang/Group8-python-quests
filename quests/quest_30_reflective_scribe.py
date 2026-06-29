# ─── Quest 5 revisited: The Echoing Cave ───────────────────────────
# We start the hero with full health (100 points)
player_health = 100

# A monster attacks — player loses 25 health points
player_health -= 25

# Player finds a potion — restores 10 health points
player_health += 10

# Show the player what their health is after both events
print(f"Final health after combat and potion: {player_health}")


# ─── Quest 9 revisited: The Greedy Goblin ──────────────────────────
gold = 27  # Total gold pieces the goblin has
friends = 4  # Number of friends to share with

# Integer division gives us how many whole pieces each friend gets
each_gets = gold // friends

# Modulo gives us what's left over after dividing equally
goblin_keeps = gold % friends

print(f"Each friend gets {each_gets} pieces. The goblin keeps {goblin_keeps}.")


# ─── Quest 19 revisited: The Countdown ─────────────────────────────
# range(10, 0, -1) counts from 10 down to 1 (stops before 0)
# The third argument (-1) is the step — it decrements by 1 each time
for i in range(10, 0, -1):
    print(i)

# After the loop ends, we announce liftoff
print("Blastoff!")
