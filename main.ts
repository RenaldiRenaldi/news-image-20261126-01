import { copyFile, mkdir } from 'node:fs/promises';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
const out = process.env.MAKEFUN_OUTPUT_DIR || '/output';
const scriptDir = dirname(fileURLToPath(import.meta.url));
// Keep the runtime surface limited to the submitted PNG and output directory.
await mkdir(out, { recursive: true });
await copyFile(join(scriptDir, 'entry.png'), join(out, 'entry.png'));
