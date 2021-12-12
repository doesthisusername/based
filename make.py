#!/usr/bin/env python3

from os import path
from os import linesep as nl
from subprocess import run
from sys import argv
import tempfile

name = argv[1]

run([
    "winedbg", "--command", "c",
    "HatinTime/Binaries/Win64/HatinTimeEditor.exe", "make",
    "-FULL", "-SHORTPATHS", f"-MODSONLY={name}"
])

mod_dir = path.join("HatinTime", "HatinTimeGame", "Mods", name)

with open(path.join(mod_dir, "overrides.txt"), "r") as f:
    overrides = [x.strip().split(" ") for x in f.readlines()]

fd, tmp_path = tempfile.mkstemp(text=True)
tmpf = open(fd, "w")
tmpf.write("// Generated by based" + nl)

for override in overrides:
    upk = override[0]
    mod_sym = override[1]
    upk_sym = override[2]

    r = run([
        "HexToPseudoCode",
        path.join(mod_dir, "CompiledScripts", f"{name}.u"), mod_sym
    ], capture_output=True)

    tmpf.writelines([
        nl,
        f"UPK_FILE = {upk}{nl}",
        f"OBJECT = {upk_sym} : AUTO{nl}"
    ])

    tmpf.writelines(r.stdout.decode("utf-8").splitlines(keepends=True)[3:])

tmpf.close()

run([
    "PatchUPK", tmp_path, "CookedPC"
])

print("based is done.")
