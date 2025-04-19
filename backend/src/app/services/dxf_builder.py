import ezdxf
from pathlib import Path
import uuid

OUTPUT_DIR = Path("./output") 
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def build_dxf_file(data: dict) -> Path:
    doc = ezdxf.new()
    msp = doc.modelspace()

    # Пример: рисуем прямоугольник по данным
    x, y, w, h = data.get("x", 0), data.get("y", 0), data.get("w", 100), data.get("h", 100)
    msp.add_lwpolyline([
        (x, y), (x + w, y), (x + w, y + h), (x, y + h), (x, y)
    ])

    filename = f"schema_{uuid.uuid4().hex}.dxf"
    filepath = OUTPUT_DIR / filename
    doc.saveas(filepath)
    print(f"[DEBUG] Saving to: {filepath.resolve()}")
    return filepath
