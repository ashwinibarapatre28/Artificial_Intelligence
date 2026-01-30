capacity_a = int(input("Enter capacity of jug A:"))
capacity_b = int(input("Enter capacity of jug B:"))
capacity = int(input("Enter how much water you need at the end:"))

jug_a = 0  # 4-gallon jug starts empty
jug_b = 0  # 3-gallon jug starts empty

print("=== Water Jug Problem ===")
print("Jug A =", jug_a, "Jug B =", jug_b)
print()

# Rule 1: Fill Jug B
print("1. Fill Jug B completely")
jug_b = capacity_b
print("Jug A =", jug_a, "Jug B =", jug_b)

# Rule 2: Pour Jug B to Jug A
print("\n2. Pour from Jug B to Jug A")
space_in_a = capacity_a - jug_a
if jug_b > space_in_a:
    jug_a = capacity_a
    jug_b = jug_b - space_in_a
else:
    # Pour all from B
    jug_a = jug_a + jug_b
    jug_b = 0
print("Jug A =", jug_a, "Jug B =", jug_b)

# Rule 3: Fill Jug B again
print("\n3. Fill Jug B again")
jug_b = capacity_b
print("Jug A =", jug_a, "Jug B =", jug_b)

# Rule 4: Pour Jug B to Jug A until A is full
print("\n4. Pour from Jug B to Jug A")
space_in_a = capacity_a - jug_a
pour_amount = space_in_a
jug_a = jug_a + pour_amount
jug_b = jug_b - pour_amount
print("Jug A =", jug_a, "Jug B =", jug_b)

# Rule 5: Empty Jug A
print("\n5. Empty Jug A")
jug_a = 0
print("Jug A =", jug_a, "Jug B =", jug_b)

# Rule 6: Pour Jug B to Jug A
print("\n6. Pour from Jug B to Jug A")
jug_a = jug_a + jug_b  # Pour all from B to A
jug_b = 0
print("Jug A =", jug_a, "Jug B =", jug_b)

print("\n=== SOLUTION ===")
print("Jug A has", jug_a, "gallons")

if jug_a == capacity:
    print("SUCCESS!!")
else:
    print("ERROR!!")