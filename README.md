# ParseMED
  Evidenta medicamentelor dintr-o farmacie prin XML şi informaţie structurată


## Obiective:
* Definirea foarte exacta a domeniului ales folosind cerinte si constrangeri
* Proiectarea documentului XML in concordanta cu cerintele si constrangerile specificate,
precum si verificarea respectarii regulilor pentru ca fisierul sa fie bine format
* Proiectarea documentului JSON
* Proiectarea DTD‐ului asociat ( definit intern sau extern). Validare.
* Proiectarea schemei XML(cu extensii si restrictii). Validare.
* Crearea unei interfete grafice din care sa se incarce fisierul XML creat, precum si fisierul
JSON.
* Explicarea modului de parsare (de navigare printre elemente/atribute) a fisierelor XML si
JSON.
* Cautarea unor elemente, precum si afisarea intr‐un raport, dupa parsare, a datelor pastrate
structurat in documentele XML si JSON.
* Utilizarea sau crearea unei foi de stiluri pentru a se putea vizualiza datele stocate in fisierul
xml intr-un format de tabel


## Technologii

- [Pyton 3.8.10](https://www.python.org/downloads/release/python-3810/)
- [Streamlit](https://docs.streamlit.io/)
- [The ElementTree XML API](https://docs.python.org/3.8/library/xml.etree.elementtree.html)

## Rularea Aplicatiei

```bash
  git clone https://github.com/iuliiaioana/ParseMED.git
  cd ParseMED
  pip install -r requirements.txt
  streamlit run app.py
```
