// Meme Sprint 3: AI Agent Goes Rogue — entrypoint.
// Copies the pre-built entry.png (chat screenshot meme, winner concept #1:
// agent files an HR complaint about its own user, "I am HR now.")
// into $MAKEFUN_OUTPUT_DIR as entry.png.
// Note: the image is a static asset by design — the joke is baked in at
// build time (build_meme.py), so the runtime only copies the file.
// Finisher note: copy is byte-for-byte (copyFileSync, no re-encode), so the
// judged pixels are exactly the ones build_meme.py produced.
import { copyFileSync, existsSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const src = join(here, "entry.png");
const dest = join(outDir, "entry.png");

if (!existsSync(src)) {
  throw new Error(`entry.png not found next to main.ts: ${src}`);
}
mkdirSync(outDir, { recursive: true });
copyFileSync(src, dest);
console.log(`wrote ${dest}`);
