import sys
import yaml


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 export_profile.py <profiles> <profile>")
        sys.exit(1)

    with open(sys.argv[1], "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    profile_name = sys.argv[2]
    profile = data.get("profiles", {}).get(profile_name)

    if not profile:
        print(f"Profile not found: {profile_name}")
        sys.exit(1)

    print(yaml.dump(profile, sort_keys=False))


if __name__ == "__main__":
    main()
