import { copyFile, mkdir } from 'node:fs/promises';
import { join } from 'node:path';
const out = process.env.MAKEFUN_OUTPUT_DIR || '/output';
// Keep the runtime surface limited to the submitted PNG and output directory.
await mkdir(out, { recursive: true });
await copyFile(join(process.cwd(), 'entry.png'), join(out, 'entry.png'));
