from pathlib import Path
from ai_diffusion.resources import SDVersion, default_checkpoints


test_dir = Path(__file__).parent
server_dir = test_dir / ".server"
data_dir = test_dir / "data"
image_dir = test_dir / "images"
result_dir = test_dir / ".results"
reference_dir = test_dir / "references"

default_checkpoint = {
    SDVersion.sd15: default_checkpoints[0].filename,
    SDVersion.sdxl: default_checkpoints[1].filename,
}
