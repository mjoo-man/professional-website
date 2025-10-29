# Dev Notebook

create a new content page bundle

```sh
hugo new --kind projects <project_title>/index.md
```

will still need to make the gallery folder. 

doesnt load in the `index.md` only the defualt, I'll work around that later.

for non-page bundles (like thoughts or book reviews) use this


Re-encode videos with ffmpeg

```sh
ffmpeg -i input.MOV -c:v libx264 -c:a aac output.mp4

```