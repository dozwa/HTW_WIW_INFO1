# ============================================================================
# Makefile – HTW Berlin · Informatik 1 · WIW 1. Semester
# ============================================================================
# Baut PDFs aus Markdown-Quellen (Übungen, Cheat Sheets, Beamer-Folien)
# und generiert Grafiken per Python/matplotlib.
#
# Verzeichnisse mit Umlauten/Leerzeichen werden per `find` aufgelöst
# (macOS speichert Umlaute als NFD – GNU make wildcard findet sie nicht).
# ============================================================================

# --- Tools ------------------------------------------------------------------
PANDOC     = pandoc
PDF_ENGINE = xelatex
PYTHON     = python3
JUPYTEXT   = jupytext

# --- Verzeichnisse ----------------------------------------------------------
GRAFIKEN_DIR     = Grafiken
NOTEBOOK_SRC_DIR = Notebooks_src
NOTEBOOK_DIR     = Notebooks

# --- Quellen finden (shell, wegen Umlaute/Leerzeichen) ----------------------
UEBUNGEN_MD   := $(shell find . -maxdepth 2 -path '*bungen/*.md'   -type f)
CHEATSHEET_MD := $(shell find . -maxdepth 2 -path '*Cheat*Sheets/*.md' -type f)
BEAMER_MD     := $(shell find . -maxdepth 2 -path '*sentationen/*.md' -type f)
GRAFIK_SCRIPTS:= $(shell find $(GRAFIKEN_DIR) -name 'generate_*.py' -type f 2>/dev/null)
NOTEBOOK_SRC  := $(shell find $(NOTEBOOK_SRC_DIR) -maxdepth 1 -name '*.md' -type f 2>/dev/null)

# --- PDF-Zielpfade ----------------------------------------------------------
UEBUNGEN_PDF   := $(UEBUNGEN_MD:.md=.pdf)
CHEATSHEET_PDF := $(CHEATSHEET_MD:.md=.pdf)
BEAMER_PDF     := $(BEAMER_MD:.md=.pdf)
NOTEBOOK_IPYNB := $(patsubst $(NOTEBOOK_SRC_DIR)/%.md,$(NOTEBOOK_DIR)/%.ipynb,$(NOTEBOOK_SRC))

# --- Pandoc-Optionen --------------------------------------------------------
PANDOC_COMMON  = --pdf-engine=$(PDF_ENGINE) -V lang:de-DE
RESOURCE_PATH  = --resource-path=".:$(GRAFIKEN_DIR)"

BEAMER_OPTS    = -t beamer \
  -V theme:metropolis -V fontsize:11pt -V aspectratio:169 \
  -V mainfont:"DejaVu Sans" -V sansfont:"DejaVu Sans" \
  -V monofont:"DejaVu Sans Mono"

# ============================================================================
# Targets
# ============================================================================

.PHONY: all uebungen cheatsheets beamer grafiken notebooks clean help

all: grafiken uebungen cheatsheets beamer  ## Alles bauen

help:  ## Verfügbare Targets anzeigen
	@grep -E '^[a-zA-Z_-]+:.*##' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*## "}; {printf "  %-18s %s\n", $$1, $$2}'

# --- Grafiken ---------------------------------------------------------------
grafiken:  ## Python-Grafiken generieren
	@if [ -n "$(GRAFIK_SCRIPTS)" ]; then \
		for script in $(GRAFIK_SCRIPTS); do \
			echo "→ Generiere Grafiken: $$script"; \
			$(PYTHON) "$$script"; \
		done; \
	else \
		echo "Keine generate_*.py Skripte in $(GRAFIKEN_DIR)/ gefunden."; \
	fi

# --- Übungen ----------------------------------------------------------------
uebungen: $(UEBUNGEN_PDF)  ## Alle Übungsblätter bauen

# --- Cheat Sheets -----------------------------------------------------------
cheatsheets: $(CHEATSHEET_PDF)  ## Alle Cheat Sheets bauen

# --- Beamer-Folien ----------------------------------------------------------
beamer: $(BEAMER_PDF)  ## Alle Beamer-Folien bauen

# --- Pattern Rules ----------------------------------------------------------
# Übungen & Cheat Sheets (Artikel-Format)
$(UEBUNGEN_PDF) $(CHEATSHEET_PDF): %.pdf: %.md
	@echo "→ Baue (Artikel): $<"
	$(PANDOC) $(PANDOC_COMMON) $(RESOURCE_PATH) -o "$@" "$<"

# Beamer-Folien
$(BEAMER_PDF): %.pdf: %.md
	@echo "→ Baue (Beamer): $<"
	$(PANDOC) $(PANDOC_COMMON) $(BEAMER_OPTS) $(RESOURCE_PATH) -o "$@" "$<"

# --- Einzelne Targets (Kurzform) --------------------------------------------
# Bsp: make uebung-03 → baut die Übung mit 03 im Namen
uebung-%:
	@file=$$(find . -maxdepth 2 -path '*bungen/*$**.md' -type f | head -1); \
	if [ -n "$$file" ]; then \
		echo "→ Baue: $$file"; \
		$(PANDOC) $(PANDOC_COMMON) $(RESOURCE_PATH) -o "$${file%.md}.pdf" "$$file"; \
	else echo "Keine Übung mit '$*' gefunden."; fi

cheatsheet-%:
	@file=$$(find . -maxdepth 2 -path '*Cheat*Sheets/*$**.md' -type f | head -1); \
	if [ -n "$$file" ]; then \
		echo "→ Baue: $$file"; \
		$(PANDOC) $(PANDOC_COMMON) $(RESOURCE_PATH) -o "$${file%.md}.pdf" "$$file"; \
	else echo "Kein Cheat Sheet mit '$*' gefunden."; fi

folien-%:
	@file=$$(find . -maxdepth 2 -path '*sentationen/*$**.md' -type f | head -1); \
	if [ -n "$$file" ]; then \
		echo "→ Baue: $$file"; \
		$(PANDOC) $(PANDOC_COMMON) $(BEAMER_OPTS) $(RESOURCE_PATH) -o "$${file%.md}.pdf" "$$file"; \
	else echo "Keine Folien mit '$*' gefunden."; fi

# --- Notebooks --------------------------------------------------------------
# Baut Jupyter-Notebooks aus MyST-Markdown-Quellen via jupytext.
# Einzelne Notebooks: make notebook-11  (Nummer im Dateinamen)
# Alle migrierten:    make notebooks
notebooks: $(NOTEBOOK_IPYNB)  ## Notebooks aus Markdown-Quellen bauen

$(NOTEBOOK_DIR)/%.ipynb: $(NOTEBOOK_SRC_DIR)/%.md
	@echo "→ Baue Notebook: $<"
	$(JUPYTEXT) --to ipynb --output "$@" "$<"

notebook-%:
	@src=$$(find $(NOTEBOOK_SRC_DIR) -maxdepth 1 -name '*$**.md' -type f | head -1); \
	if [ -n "$$src" ]; then \
		out="$(NOTEBOOK_DIR)/$$(basename $${src%.md}).ipynb"; \
		echo "→ Baue: $$src → $$out"; \
		$(JUPYTEXT) --to ipynb --output "$$out" "$$src"; \
	else echo "Keine Notebook-Quelle mit '$*' gefunden."; fi

# --- Clean ------------------------------------------------------------------
clean:  ## Alle generierten PDFs löschen
	@echo "Lösche generierte PDFs..."
	@find . -maxdepth 2 \( -path '*bungen/*.pdf' -o -path '*Cheat*Sheets/*.pdf' -o -path '*sentationen/*.pdf' \) -type f -delete
	@echo "Fertig."

clean-grafiken:  ## Generierte Grafiken löschen
	@echo "Lösche Grafiken..."
	@find $(GRAFIKEN_DIR) -name '*.png' -type f -delete
	@echo "Fertig."
