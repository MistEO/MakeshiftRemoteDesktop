from pathlib import Path

import shutil

project_dir = Path(__file__).parent
assets_dir = project_dir / "assets"
install_dir = project_dir / "install"


def configure_ocr_model():
    shutil.copytree(
        assets_dir / "MaaCommonAssets" / "OCR" / "ppocr_v4" / "zh_cn",
        install_dir / "maafw_resource" / "model" / "ocr",
        dirs_exist_ok=True,
    )


if __name__ == "__main__":
    configure_ocr_model()
