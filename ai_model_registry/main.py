from pathlib import Path
from typing import Any
import json
from datetime import datetime


class Model:
    def __init__(
        self,
        name: str,
        accuracy: float,
        company: str
    ) -> None:
        self.name = name
        self.accuracy = accuracy
        self.company = company

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "accuracy": self.accuracy,
            "company": self.company
        }

    @classmethod
    def from_cls(cls, data: dict[str, Any]) -> "Model":
        return cls(
            name=data["name"],
            accuracy=data["accuracy"],
            company=data["company"]
        )


class ModelRegistry:
    def __init__(self) -> None:
        self.models: list[Model] = []

    def add_model(self, model: Model) -> None:
        self.models.append(model)

    def find_highest_accuracy(self) -> Model | None:
        if not self.models:
            return None

        return max(self.models, key=lambda m: m.accuracy)

    @staticmethod
    def save_registry(path: Path, models: list[Model]) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)

        serialized_models = [
            model.to_dict()
            for model in models
        ]

        payload: dict[str, Any] = {
            "created_at": datetime.now().isoformat(),
            "models": serialized_models
        }

        with path.open("w", encoding="utf-8") as file:
            json.dump(payload, file, indent=4)

        print(f"Registry successfully saved to: {path}")

    @staticmethod
    def load_registry(path: Path) -> list[Model]:
        try:
            with path.open("r", encoding="utf-8") as file:
                data = json.load(file)

            loaded_models = [
                Model.from_cls(model)
                for model in data["models"]
            ]

            print(f"File created at: {data['created_at']}")

            return loaded_models

        except FileNotFoundError:
            print(f"File not found: {path}")
            return []

        except json.JSONDecodeError:
            print(f"Invalid JSON in file: {path}")
            return []


if __name__ == "__main__":
    base_dir = Path("ai_model_registry")
    json_file = base_dir / "models.json"

    my_models = [
        Model("GPT-4o", 0.88, "OpenAI"),
        Model("Claude 3.5 Sonnet", 0.92, "Anthropic"),
        Model("Gemini 1.5 Pro", 0.86, "Google")
    ]

    registry = ModelRegistry()

    for model in my_models:
        registry.add_model(model)

    best_model = registry.find_highest_accuracy()

    if best_model:
        print(
            f"Highest Accuracy Model: {best_model.name} "
            f"({best_model.accuracy * 100}%) "
            f"by {best_model.company}"
        )

    print("\n--- Saving to JSON ---")

    ModelRegistry.save_registry(
        json_file,
        registry.models
    )

    fresh_models = ModelRegistry.load_registry(json_file)

    print(
        f"Successfully reconstructed "
        f"{len(fresh_models)} Model objects from file."
    )

    missing_file = base_dir / "model.json"
    ModelRegistry.load_registry(missing_file)
    