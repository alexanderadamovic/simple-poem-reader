poem = input(f"What is your poem type?")

if poem == "sonnet":
    print(f"sonnet: Has a line count of 14")
elif poem == "villlanelle":
    print(f"villanelle: Has a line count of 19")
elif poem == "sestina":
    print(f"sestina: A line count of 36")
else:
    print(f"other: Free Verse - no forms apply")
