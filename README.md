# Dev Notebook

create a new content page bundle

```sh
hugo new --kind <type> <content-path>/<title>/index.md
```

example
```sh
hugo new --kind trips trips/camping/Enchanted_Rock_State_Park/index.md

# or 

hugo new --kind projects projects/new-proj/index.md
```

will still need to make the gallery folder. 

doesnt load in the `index.md` only the defualt, I'll work around that later.

for non-page bundles (like thoughts or book reviews) use this

only templated post types right now are `thought` and `book_review`

```sh
hugo new <post-type>/<post-title>.md
```

example
```sh
hugo new book_review/book-title2.md
```

currently thoughts and book reviews are commented out of the menu, theyll still build, but you cant acess them on the website, unless you type the url.

