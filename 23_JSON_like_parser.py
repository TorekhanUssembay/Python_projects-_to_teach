def validate_config(config, required_keys):
    """
    required_keys: list of tuples with nested keys
    Example: [("app", "name"), ("app", "version"), ("database", "host")]
    """
    missing = []

    for keys in required_keys:
        current = config
        for key in keys:
            if key in current:
                current = current[key]
            else:
                missing.append(".".join(keys))
                break

    return missing


def main():
    # Example config
    config = {
        "app": {
            "name": "MyApp",
            "version": "1.0",
            "debug": True
        },
        "database": {
            "host": "localhost",
            "port": 3306
        }
    }

    # Keys we require
    required_keys = [
        ("app", "name"),
        ("app", "version"),
        ("app", "debug"),
        ("database", "host"),
        ("database", "port"),
        ("database", "user")  # intentionally missing
    ]

    missing = validate_config(config, required_keys)
    if missing:
        print("Missing required keys:", missing)
    else:
        print("All required keys are present ✅")


if __name__ == "__main__":
    main()
