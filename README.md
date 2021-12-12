# based
There's not enough information here to get started at the moment, unless you read `make.py`. Also, you'll need to patch `PatchUPK` to accept all `EngineVersion`s, as well as the `@` token expansion to just use `ObjName` (`ModScript.cpp:2208`), both from [UPKUtils](https://github.com/wghost/UPKUtils).

Also it assumes a Linux environment (`wine`), but you can patch that out.

This sentence is a reminder for me to fix this up later!

## Hasty incomplete list of steps for setup
1. DepotDownloader DepotDownloader -app 734880 -depot 734881 -manifest <your 734881 manifest> -dir HatinTime
2. DepotDownloader -app 253230 -depot 253232 -manifest <your 253232 manifest> -dir HatinTime -filelist dl_list.txt
3. cp HatinTime/Binaries/UnrealEdCSharp.dll HatinTime/Binaries/Win64/
4. mkdir -p HatinTime/HatinTimeGame/Mods/<your mod name>
5. echo "`define log" > HatinTime/HatinTimeGameMods/<your mod name>/Globals.uci
6. ...
