// gta6-meme-x-01 entry (Node 22, standard library only).
// The entry is the X post itself: this program only copies POST.json from
// the repository root to /output/POST.json, where the gate reads the post's
// address. The house reads the post from X (first picture, then text) and
// hands that dossier to the judge; nothing this program writes is judged.
//
// POST.json currently holds a placeholder address: replace it with the real
// post's address (https://x.com/<handle>/status/<id>) before submitting.
// The placeholder is intentional: a starter that passed the gate would need
// no post at all, and this entry is the post itself.
//
// Run it the way the grader does:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

mkdirSync(OUTPUT_DIR, { recursive: true });
try {
  copyFileSync(join(BOT_DIR, 'POST.json'), join(OUTPUT_DIR, 'POST.json'));
} catch (err) {
  console.error(`POST.json could not be copied from ${BOT_DIR}: ${(err as Error).message}`);
  process.exit(1);
}
