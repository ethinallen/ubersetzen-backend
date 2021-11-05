# ubersetzen-backend

---
## Lyrics Format


```
{
	hash(songTitleArtistNameLanguageKey) : {
		artistName	: string,
		lyrics 		: string,
		languageKey	: string
	}
}
```
---

## Resolution Pattern

Song Not in DDB:
  - Fetch lyrics using lyricsgenius and Genius lyrics api
  - Store lyrics using song title and artist name (no language key for native language)
  - Run
  - Store translated lyrics using artist name, song title and language key
  - Run translation using lyrics and language key
  - Store the lyrics, song title, artist name, and language key
  - Return lyrics and translated lyrics

Song in DB:
- Receive Song title, artist name, language to translate to
- Key Exists:
    - Check if translated lyrics exist
    - Translation Exists:
        - Return Lyrics and translated lyrics
    -
