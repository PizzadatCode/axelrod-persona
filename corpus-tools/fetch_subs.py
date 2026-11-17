"""Download English HI subtitles from addic7ed. Idempotent: skips existing valid SRTs."""
import json, urllib.request, time, os, sys

HOME = os.path.expanduser("~")
targets = json.load(open(f"{HOME}/addic7ed_hi_targets.json"))
d = f"{HOME}/.hermes/research/axelrod-persona/subs"
os.makedirs(d, exist_ok=True)

UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
      "Referer": "https://www.addic7ed.com/season/5520/1"}

def valid_srt(path):
    try:
        if os.path.getsize(path) < 500:
            return False
        return b"-->" in open(path, "rb").read()
    except OSError:
        return False

ok = fail = skip = 0
fails = []
for r in targets:
    fn = f"{d}/Billions_{r['S']:02d}x{r['E']:02d}.srt"
    if valid_srt(fn):
        skip += 1
        continue
    try:
        req = urllib.request.Request("https://www.addic7ed.com" + r["href"], headers=UA)
        resp = urllib.request.urlopen(req, timeout=40)
        cd = resp.headers.get("Content-Disposition", "")
        data = resp.read()
        if len(data) > 500 and b"-->" in data:
            open(fn, "wb").write(data)
            ok += 1
            if ".HI." not in cd:
                print(f"WARN no-HI-in-name {r['S']:02d}x{r['E']:02d}: {cd[:70]}", flush=True)
        else:
            fail += 1
            fails.append((r["S"], r["E"], "bad payload", len(data)))
        time.sleep(2.0)
    except Exception as e:
        fail += 1
        fails.append((r["S"], r["E"], repr(e)[:70]))
        time.sleep(4.0)

print(f"downloaded={ok} skipped={skip} failed={fail}")
for f_ in fails:
    print("FAIL:", f_)