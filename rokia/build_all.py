# -*- coding: utf-8 -*-
"""Rebuild every lesson page from the content modules.

Usage:
    cd rokia && python3 build_all.py

Add a new page by appending a dict to PAGES in a _content_*.py module (or a
new one, imported below) — this script picks it up automatically.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _build import build
import _content_a, _content_b, _content_c, _content_d, _content_e
import _content_f, _content_g, _content_h, _content_i

MODULES = [
    _content_a, _content_b, _content_c, _content_d, _content_e,
    _content_f, _content_g, _content_h, _content_i,
]

def main():
    here = os.path.dirname(os.path.abspath(__file__))
    built = []
    for mod in MODULES:
        for p in mod.PAGES:
            path, xpmax = build(p, here)
            built.append((p['file'], xpmax))
            print(f"built {p['file']}  (xp_max={xpmax})")
    print(f"\n{len(built)} pages rebuilt.")
    return built

if __name__ == '__main__':
    main()
