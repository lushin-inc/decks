"""Search the Lushin Training Library index from the command line.

  python3 scripts/search.py search "cold call" "brush" --family=sales
  python3 scripts/search.py show M-017 S-Q2C-SLS-3
  python3 scripts/search.py slides M-017
  python3 scripts/search.py sprint
"""
import json, os, sys, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")
D = json.load(open(os.path.join(DATA, "index.json"), encoding="utf-8"))
S = {s["id"]: s for s in D["sessions"]}
W = {"title": 4, "key_problem": 3, "scenario": 2, "light_bulb": 1.5, "rules": 1}
LINKS = [("beautiful_ai", "Beautiful.ai"), ("google_slides", "Google Slides"), ("sharepoint_folder", "SharePoint folder"),
         ("sharepoint_deck", "SharePoint deck"), ("leader_guide", "Leader guide"), ("drive_folder", "Drive folder")]


def text(s, f):
    return " ".join(s.get("key_rules", [])) if f == "rules" else (s.get(f) or "")


def search(terms, family=None, top=15):
    out = []
    for s in D["sessions"]:
        if family and s["family"] != family:
            continue
        sc = sum(w * text(s, f).lower().count(t.lower()) for t in terms for f, w in W.items())
        if sc:
            out.append((sc, s))
    for sc, s in sorted(out, key=lambda x: -x[0])[:top]:
        print(f'{s["id"]} | {s["title"]} | {s["category"]} | {s["type"]} | score {sc:g}\n   {s["key_problem"]}')


def show(ids):
    for i in ids:
        s = S[i]
        L = s["links"]
        prog = ", " + s["program"] if s["program"] else ""
        print(f'\n{s["title"]} ({s["id"]}, {s["category"]}{prog}, {s["type"]}, by {s["created_by"] or "unknown"}, {s["slide_count"]} slides)')
        print("  Problem:", s["key_problem"])
        print("  Light bulb:", s["light_bulb"])
        for k, lab in LINKS:
            if L.get(k):
                print(f"  {lab}: {L[k]}")
        if L.get("mac_deck"):
            print("  Mac deck:", L["mac_deck"])
        for v in L.get("other_versions", []):
            print("  Other version:", v)


def slides(i):
    sl = json.load(open(os.path.join(DATA, "slides.json"), encoding="utf-8"))
    for n, t, txt in sl["decks"].get(i, []):
        print(f"{n:>3} | {sl['types'][t]:<10} | {txt}")


if __name__ == "__main__":
    mode, args = sys.argv[1], sys.argv[2:]
    if mode == "search":
        fam = next((a.split("=", 1)[1] for a in args if a.startswith("--family=")), None)
        search([a for a in args if not a.startswith("--")], family=fam)
    elif mode == "show":
        show(args)
    elif mode == "slides":
        slides(args[0])
    elif mode == "sprint":
        for p in D["sprint_programs"]:
            print(p)
