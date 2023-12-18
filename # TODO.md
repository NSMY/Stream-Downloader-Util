TODO 
[x] have default call (Main) get stream name??

[x] at the end of check for new vods run threading to compare 
Status (set recoding to Recorded)
  maybe do something with recording are u sure you want to download in (main.py)/and or make invisible??

[x] have settings snapshot sys?/mass check installed apps eg if running terminal or old cmd to be able to do more advamced gui stuff????

[x] incorp size of vods into main/ on call from file

[x] ?change not_downloaded to downloaded? in class

[x] be able to select multiple from file/ [lists] download multiple (threading or cueing)

[x] ask a Q if download from file about being RECORDING wether to proceed downloading.

[x] why does check for new vods Print all the vods? not just new seems to be ALL one the check call [in a double line info then url]
prints 0 new vods anyway?.

[x] put somewhere prob check for new vods return the ['status'] eg RECORDING. to knwo if still LIVE

[x] [Done](startup.py#L52) be able to call shutdown also with file data, edit startup cmd

[x] [solved made my own](spinner.py): have a waiting indication on (particular req calls) something not spinners as they seem to not work on old cmd

[x] [Done But may break TK list](utility_dir\get_single_vod_.py#L46) make a way to back out of get vods if chosen wrong file. (probs add a exit string/if to the multi choice)

[x] [done](zextra_Funcs_/check_old_files_downloaded.py#L136)figure a way to determine if fully downloaded and set to downloaded in file  Name+ Total seconds ??

[x] be able to manually set if downloaded maybe with TKPopup?????

[x] [done](zextra_Funcs_\check_old_files_downloaded.py)

[x] set ffprobe paths to be from paths file

[TODO] Readme not redering prop in ghub, Do Main 👇👇, and re Cat all files to utils for onefile scrips and helpers for funcs etc
[TODO] set main download completions crosscheck

[] IDEA have a tkinter Warning popup before downloading depends???

[TODO] make chapters in vods? using code > [Code](zextra_Funcs_/getChaptersCall.py) < will require a large rewrite, games will be
in a list object and everywhere called will have to unpack, then also do u give option to set where to DL from?? 


[]  maybe rework tkinter to be packs instead of grids somehow as is laggy



[] make able to get from file and dld from a time cmd and have it calc the right size minus'ing time-- think i have code somewhere 

[] [Working](zextra_Funcs_/check_old_files_downloaded.py#L136): make it so u can check if downloaded incase a new json file is made/ overwritten


THINK in the check new stream -- what to do for deleted /hidden vods on channels? 

[] make the setup init settings better, maybe into 1 call like if key in settings then call the whole settings thins
more robust dependency searching and downloading (if deleted between settinggs Checks)

[TODO] make a combine segments (vids) ffmpeg via lists meth
THINK make check file be able to execute as standalone?? (need to make file dest dynamic apon single call) 
TRACK have it error when refreshing json vods file and non streamer name


THINK do i ad multi File processing? mp4 wav etc

customTKinter GUI??
do i make Combine streams Aud/Vid
make WEBP converter? New File?
make separate download/main thats can get lives and restart if dropouts maybe scheduled  maybe seek notos?
Somehow incorporate auto download from noto?
Win Alert notos?
