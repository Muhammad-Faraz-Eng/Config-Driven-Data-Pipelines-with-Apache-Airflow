import os


class ConnectionRegistry:
    REQUIRED_KEYS = ["HOST", "PORT", "DB", "USER", "PASSWORD"]

    @classmethod
    def get(cls, connection_id: str) -> dict:
        prefix = connection_id.upper()

        config = {}
        missing = []

        for key in cls.REQUIRED_KEYS:
            env_key = f"{prefix}_{key}"
            value = os.getenv(env_key)

            if value is None:
                missing.append(env_key)
            else:
                config[key.lower() if key != "DB" else "database"] = value

        if missing:
            raise ValueError(
                f"Missing environment variables for connection '{connection_id}': {missing}"
            )

        config["port"] = int(config["port"])
        return config
