import re
from typing import Dict


class TemplateEngine:
    PLACEHOLDER_PATTERN = re.compile(r"\{\{(\w+)\}\}")

    @classmethod
    def apply(cls, template: Dict, values: Dict) -> Dict:
        rendered = {}

        for key, value in template.items():
            if isinstance(value, str):
                rendered[key] = cls._replace(value, values)
            elif isinstance(value, dict):
                rendered[key] = cls.apply(value, values)
            elif isinstance(value, list):
                rendered[key] = [
                    cls.apply(v, values) if isinstance(v, dict) else v for v in value
                ]
            else:
                rendered[key] = value

        return rendered

    @classmethod
    def _replace(cls, text: str, values: Dict) -> str:
        def repl(match):
            var = match.group(1)
            return str(values.get(var, match.group(0)))

        return cls.PLACEHOLDER_PATTERN.sub(repl, text)
