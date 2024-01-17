# deflickerer
simple Python script that uses ffmpeg to attempt to deflicker video

Run the following in Powershell to install Python and FFmpeg using the Scoop installer:
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser &&
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression &&
scoop install python &&
scoop install ffmpeg
```
