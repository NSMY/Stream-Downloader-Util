README.md

#  **Stream Downloader Util is a CLI that provides easier Streamlink-Twitch usage.**

## [Streamlink][streamlink-website] [FFMPEG][ffmpeg] & [FFPROBE][ffmpeg] Dependent** Automated Downloader

**Main Features**
* Easier Streamlink Download use without need of remembering Streamlink flags
* Muxing of video files with ffmpeg
* Extraction of Audio & Video Channel/s from File to separate files, if 1 Multi channels or 2 Desire Audio-Video Separated (useful for OBS Multi-Channel Captures)

---
## DOWNLOAD

**STREAMLINK Dependent**

This python script fetches your [clipboard(URL)] checks if [dependencies] are available, if not will download them or provide [links]. 

It will then retrieve [available] resolutions to download, provides the [fileddialog] (Browser popup) to set save Location/Name.

Asks what size desired to download with inquirer (Scrollable Arrow keys List).

Newly added Twitch-skip-ads Streamlink Flag and Twitch Auth-Token optional.
<sub> Skips [ads] on vods if enabled, if subscribed skips ads from live recordings Via a [Auth] Token <sub/>

Optional [terminate] Download early without Crashing the CLI 

Downloads File Via [Streamlink][streamlink-website]

Asks if [Mux-ing] is Desired (Combines Chunks files for smooth playback with FFMPEG).


---
## MUX-ING

**FFMPEG Dependent**

This is available after Download And Separate From the main downloading option, can be used as a standalone 

Re Mux's (Copies) the File specified in the Clipboard (File path) or [fileddialog][fileddialog2] (Browser popup Finder) 

Sends the old file to the Recycle bin and saves a new file into a separate new Folder inside the CWD, then opens the folder.


---
## EXTRACTION

**FFPROBE Dependent**

Checks if FFPROBE is Available on your C Drive, if not found will be Downloaded From [FFMPEG Website][links],
FFPROBE is needed to check the amount of Channels in the file.

Will Probe the File specified in the Clipboard (File path) or [fileddialog][fileddialog2] (Browser popup Finder) for the amount of audio channels and will return a list of them.

A specific Channel or all channels can be selected. Again will create a Folder within CWD to save files to.

Video can be selected to also Separated form Audio

> VP9/Opus (YouTube Video) is available but will stay in VP9/Opus Codec when extracted, otherwise Re-encoding would be required.

> ***if the file has not been muxed (or standard file) may result in misread of Audio channels***
---
## DEPENDENCIES

- [Streamlink][streamlink-website]
    - [FFmpeg][ffmpeg] A Version comes with Streamlink
- [FFprobe][ffmpeg]

### **WHY?**

Made this because i was sick of manually entering a string i had saved into Cmd, Then change for every occasion. All other variations are Pure **CLI** automatable, So i made this CLI lite to combine personal frequently used features.

> ***All streamlink limitations are still enabled***

> (***1st multi file script ever made***)

[streamlink-website]: https://github.com/streamlink/streamlink
[clipboard(URL)]: https://github.com/NSMY/Stream-Downloader-Util/blob/d683041b21d277261a08d3cbba19f119bdab22cc/Main.py#L34
[dependencies]: https://github.com/NSMY/Stream-Downloader-Util/blob/d683041b21d277261a08d3cbba19f119bdab22cc/Main.py#L43
[links]: https://github.com/NSMY/Stream-Downloader-Util/blob/Future-Dev-Features/download_Links.txt
[available]: https://github.com/NSMY/Stream-Downloader-Util/blob/d683041b21d277261a08d3cbba19f119bdab22cc/Main.py#L76
[fileddialog]: https://github.com/NSMY/Stream-Downloader-Util/blob/d683041b21d277261a08d3cbba19f119bdab22cc/funcs.py#L181
[fileddialog2]: https://github.com/NSMY/Stream-Downloader-Util/blob/d683041b21d277261a08d3cbba19f119bdab22cc/funcs.py#L148
[Mux-ing]: https://github.com/NSMY/Stream-Downloader-Util/blob/3a2866f282599293e1ff0aebb8722204713cbf85/mux_vid.py#L57
[ffmpeg]: https://github.com/ffbinaries/ffbinaries-prebuilt/releases/tag/v4.4.1
[terminate]: https://github.com/NSMY/Stream-Downloader-Util/blob/d683041b21d277261a08d3cbba19f119bdab22cc/Main.py#L132
[Auth]: https://streamlink.github.io/cli/plugins/twitch.html#authentication
[ads]: https://streamlink.github.io/cli.html#cmdoption-twitch-disable-ads
