# Lesson videos

`make_videos.py` turns every lesson in `mkdocs.yml`'s nav into a narrated 1080p MP4:

- **Slides** (Pillow): title, section dividers, paragraphs and lists, tables, call-outs, Mermaid diagrams
  (rendered with headless Chromium), templates, dialogues as chat bubbles, and a closing slide.
- **Narration** (Kokoro TTS, offline): all prose, list items, table rows, scripts, templates and call-outs.
  ```dialogue blocks become chat-bubble slides voiced by two speakers: "You" (`VIDEO_VOICE_YOU`, default
  `am_michael`) and the other person (`VIDEO_VOICE_THEM`, default `bf_emma`); the narrator is `af_heart`.
- **Captions**: WebVTT next to the poster in `docs/videos/`, and embedded in the MP4.


MP4s are published to the orphan `videos` branch (keeps `main` and the Pages site small) and streamed from
`raw.githubusercontent.com`; `docs/videos/manifest.json`, captions and posters stay on the docs branch.
`hooks/videos.py` embeds each lesson's video under its title; `docs/videos/index.md` lists them all.

```bash
pip install -r tools/videos/requirements.txt playwright      # plus ffmpeg and Node/npm (for mermaid.min.js)
git clone --single-branch --branch videos https://github.com/khiruashish/soft-skill-playbook /tmp/ssp-work/videos-repo
VIDEO_PUBLISH=/tmp/ssp-work/videos-repo VIDEO_COMMIT=1 python tools/videos/make_videos.py   # resumes: skips lessons in the manifest
python tools/videos/make_videos.py everyday/train.md                                  # (re)make one lesson
```

Narration audio and rendered diagrams are cached in `$VIDEO_WORK` (default `/tmp/ssp-work`).

## Running on GitHub Actions

`.github/workflows/videos.yml` does the same thing in parallel: `plan_shards.py` splits the lessons still missing
from `manifest.json` into balanced shards (20 by default), each shard runs `make_videos.py` on its lessons, and
a final job (`merge_results.py`) pushes the MP4s to `videos` and commits captions, posters, the manifest and the
Videos page to the branch the workflow ran on. It runs on pushes that touch `tools/videos/**` or the workflow,
or manually (Actions → Lesson videos → Run workflow). Re-running only builds lessons that are still missing.
