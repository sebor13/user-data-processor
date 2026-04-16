from utils import process_users

data = [
    "ivan:25",
    "maria:17",
    "peter:30",
    "anna:abc",
    "oleg:-5",
    "sergey:40",
    "ivan:25"
]

valid, invalid, underage, adult, stats = process_users(data)

print("\nValid users:")
for v in valid:
    print(v)

print("\nInvalid users:")
for v in invalid:
    print(v)

print("\nUnderage users:")
for v in underage:
    print(v)

print("\nAdult users:")
for v in adult:
    print(v)

print("\nStatistics:")
for key, value in stats.items():
    print(f"{key}: {value}")