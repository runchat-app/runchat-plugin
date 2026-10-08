"""Build the ChatGPT plugin ZIP from chatgpt/ plus the shared skills in runchat/skills."""
import json
import zipfile
from pathlib import Path

root = Path(__file__).resolve().parent.parent
manifest = json.loads((root / "chatgpt/.codex-plugin/plugin.json").read_text())
out = root / "dist" / f"runchat-chatgpt-{manifest['version']}.zip"
out.parent.mkdir(exist_ok=True)

sources = [(p, p.relative_to(root / "chatgpt")) for p in (root / "chatgpt").rglob("*")]
sources += [(p, p.relative_to(root / "runchat")) for p in (root / "runchat/skills").rglob("*")]

with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
    for path, arcname in sorted(sources, key=lambda s: str(s[1])):
        if path.is_file():
            zf.write(path, arcname.as_posix())

print(out)
with zipfile.ZipFile(out) as zf:
    for name in zf.namelist():
        print(" ", name)
