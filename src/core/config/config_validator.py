from typing import Dict


class ConfigValidator:
    REQUIRED_PIPELINE_KEYS = {
        "name",
        "description",
        "schedule",
        "start_date",
        "catchup",
        "retries",
        "source",
        "transformations",
        "target",
    }

    @classmethod
    def validate(cls, config: Dict):
        if "pipeline" not in config:
            raise ValueError('Missing "pipeline" root key')

        pipeline = config["pipeline"]
        missing = cls.REQUIRED_PIPELINE_KEYS - pipeline.keys()
        if missing:
            raise ValueError(f"Missing Required pipeline keys: {missing}")
        if not isinstance(pipeline["transformations"], list):
            raise ValueError("'transformations' must be a list")
