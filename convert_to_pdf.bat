@echo off
echo Converting notebook to PDF using Chrome...
cd "c:\Users\mvppv\Downloads\dsc80-2026-wi\projects\proj04"

REM First convert to HTML
jupyter nbconvert --to html "LoL - The Snowballing Effect.ipynb" --template lab

REM Try to find Chrome
set CHROME="C:\Program Files\Google\Chrome\Application\chrome.exe"
if not exist %CHROME% set CHROME="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

REM Print to PDF with proper settings
%CHROME% --headless --disable-gpu --print-to-pdf="LoL - The Snowballing Effect.pdf" --print-to-pdf-no-header --no-pdf-header-footer "file:///c:/Users/mvppv/Downloads/dsc80-2026-wi/projects/proj04/LoL - The Snowballing Effect.html"

echo Done! PDF created: LoL - The Snowballing Effect.pdf
pause
