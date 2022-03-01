import io
import json
import os
from typing import Any

import torchvision.transforms as transforms
from PIL import Image
from torchvision import models


class Predictor:
    def __init__(self) -> None:
        self.model = models.mobilenet_v3_small(pretrained=True)
        self.model.eval()
        self.transforms = transforms.Compose(
            [
                transforms.Resize(255),
                transforms.CenterCrop(224),
                transforms.ToTensor(),
                transforms.Normalize(
                    [0.485, 0.456, 0.406], [0.229, 0.224, 0.225]
                ),
            ]
        )
        self.class_labels = self._load_class_labels()

    @staticmethod
    def _load_class_labels():
        class_index_path = os.getenv(
            "CLASS_INDEX_PATH", "src/artifacts/imagenet_class_index.json"
        )
        with open(class_index_path, 'r') as f:
            raw = json.load(f)

        class_labels = {int(k): v[1] for k, v in raw.items()}

        return class_labels


    def _transform(self, image_bytes: bytes) -> Any:
        """_summary_

        Args:
            image_bytes (bytes): _description_

        Returns:
            Any: _description_
        """
        image = Image.open(io.BytesIO(image_bytes))
        return self.transforms(image).unsqueeze(0)

    def predict(self, image_bytes: bytes) -> str:
        """_summary_

        Args:
            image_bytes (bytes): _description_

        Returns:
            str: _description_
        """
        tensor = self._transform(image_bytes=image_bytes)
        outputs = self.model.forward(tensor)
        _, prediction = outputs.max(1)
        index = prediction.item()
        class_label = self.class_labels[index]
        return class_label
