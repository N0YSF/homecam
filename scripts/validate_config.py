import sys
import yaml


REQUIRED_SECTIONS = [
    "camera",
    "image",
    "stream",
    "storage",
    "network",
]


def validate(config):
    missing = []

    for section in REQUIRED_SECTIONS:
        if section not in config:
            missing.append(section)

    return missing


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 validate_config.py <config>")
        sys.exit(1)

    with open(sys.argv[1], "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    missing = validate(config)

    if missing:
        print("Missing sections:")
        for section in missing:
            print(f" - {section}")
        sys.exit(1)

    print("Configuration looks valid.")


if __name__ == "__main__":
    main()
