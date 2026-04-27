# ============================================================================
# Makefile – HTW Berlin · Informatik 1 · WIW 1. Semester
# ============================================================================
# Source/Output-getrennte Build-Pipeline:
#
#   Uebungen_src/*.md         →  Uebungen/*.pdf            (Pandoc Artikel)
#   Cheat_Sheets_src/*.md     →  Cheat_Sheets/*.pdf        (Pandoc Artikel)
#   Praesentationen_src/*.md  →  Praesentationen/*.pdf     (Pandoc Beamer)
#   Notebooks_src/*.md        →  Notebooks/*.ipynb         (Jupytext)
#   Grafiken_src/generate_*.py →  Grafiken/*.png           (matplotlib)
# ============================================================================

# --- Tools ------------------------------------------------------------------
PANDOC     = pandoc
PDF_ENGINE = xelatex
PYTHON     = python3
JUPYTEXT   = jupytext

# --- Verzeichnisse ----------------------------------------------------------
UEBUNG_SRC      = Uebungen_src
UEBUNG_OUT      = Uebungen
CHEAT_SRC       = Cheat_Sheets_src
CHEAT_OUT       = Cheat_Sheets
BEAMER_SRC      = Praesentationen_src
BEAMER_OUT      = Praesentationen
GRAFIK_SRC      = Grafiken_src
GRAFIK_OUT      = Grafiken
NOTEBOOK_SRC    = Notebooks_src
NOTEBOOK_OUT    = Notebooks

# --- Quellen finden ---------------------------------------------------------
UEBUNGEN_MD    := $(wildcard $(UEBUNG_SRC)/*.md)
CHEATSHEET_MD  := $(wildcard $(CHEAT_SRC)/*.md)
BEAMER_MD      := $(wildcard $(BEAMER_SRC)/*.md)
NOTEBOOK_MD    := $(wildcard $(NOTEBOOK_SRC)/*.md)
GRAFIK_SCRIPTS := $(wildcard $(GRAFIK_SRC)/generate_*.py)

# --- Ziele ableiten ---------------------------------------------------------
UEBUNGEN_PDF   := $(patsubst $(UEBUNG_SRC)/%.md,$(UEBUNG_OUT)/%.pdf,$(UEBUNGEN_MD))
CHEATSHEET_PDF := $(patsubst $(CHEAT_SRC)/%.md,$(CHEAT_OUT)/%.pdf,$(CHEATSHEET_MD))
BEAMER_PDF     := $(patsubst $(BEAMER_SRC)/%.md,$(BEAMER_OUT)/%.pdf,$(BEAMER_MD))
NOTEBOOK_IPYNB := $(patsubst $(NOTEBOOK_SRC)/%.md,$(NOTEBOOK_OUT)/%.ipynb,$(NOTEBOOK_MD))

# --- Pandoc-Optionen --------------------------------------------------------
PANDOC_COMMON  = --pdf-engine=$(PDF_ENGINE) -V lang:de-DE
RESOURCE_PATH  = --resource-path=".:$(GRAFIK_OUT)"

BEAMER_OPTS    = -t beamer \
  -V theme:metropolis -V fontsize:11pt -V aspectratio:169 \
  -V mainfont:"DejaVu Sans" -V sansfont:"DejaVu Sans" \
  -V monofont:"DejaVu Sans Mono"

# ============================================================================
# Targets
# ============================================================================

.PHONY: all uebungen cheatsheets beamer grafiken notebooks clean clean-grafiken help

all: grafiken uebungen cheatsheets beamer  ## Alles bauen (PDFs + Grafiken)

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
		echo "Keine generate_*.py Skripte in $(GRAFIK_SRC)/ gefunden."; \
	fi

# --- Übungen / Cheat Sheets / Beamer ----------------------------------------
uebungen:    $(UEBUNGEN_PDF)    ## Alle Übungsblätter bauen
cheatsheets: $(CHEATSHEET_PDF)  ## Alle Cheat Sheets bauen
beamer:      $(BEAMER_PDF)      ## Alle Beamer-Folien bauen
notebooks:   $(NOTEBOOK_IPYNB)  ## Notebooks aus Markdown-Quellen bauen

# --- Pattern Rules: src → out ----------------------------------------------
$(UEBUNG_OUT)/%.pdf: $(UEBUNG_SRC)/%.md
	@echo "→ Baue (Übung): $<"
	$(PANDOC) $(PANDOC_COMMON) $(RESOURCE_PATH) -o "$@" "$<"

$(CHEAT_OUT)/%.pdf: $(CHEAT_SRC)/%.md
	@echo "→ Baue (Cheat Sheet): $<"
	$(PANDOC) $(PANDOC_COMMON) $(RESOURCE_PATH) -o "$@" "$<"

$(BEAMER_OUT)/%.pdf: $(BEAMER_SRC)/%.md
	@echo "→ Baue (Beamer): $<"
	$(PANDOC) $(PANDOC_COMMON) $(BEAMER_OPTS) $(RESOURCE_PATH) -o "$@" "$<"

$(NOTEBOOK_OUT)/%.ipynb: $(NOTEBOOK_SRC)/%.md
	@echo "→ Baue Notebook: $<"
	$(JUPYTEXT) --to ipynb --output "$@" "$<"

# --- Einzelne Targets (Kurzform) --------------------------------------------
# Bsp: make uebung-03 → baut die Übung mit 03 im Namen
uebung-%:
	@src=$$(find $(UEBUNG_SRC) -maxdepth 1 -name '*$**.md' -type f | head -1); \
	if [ -n "$$src" ]; then \
		out="$(UEBUNG_OUT)/$$(basename $${src%.md}).pdf"; \
		echo "→ Baue: $$src → $$out"; \
		$(PANDOC) $(PANDOC_COMMON) $(RESOURCE_PATH) -o "$$out" "$$src"; \
	else echo "Keine Übung mit '$*' gefunden."; fi

cheatsheet-%:
	@src=$$(find $(CHEAT_SRC) -maxdepth 1 -name '*$**.md' -type f | head -1); \
	if [ -n "$$src" ]; then \
		out="$(CHEAT_OUT)/$$(basename $${src%.md}).pdf"; \
		echo "→ Baue: $$src → $$out"; \
		$(PANDOC) $(PANDOC_COMMON) $(RESOURCE_PATH) -o "$$out" "$$src"; \
	else echo "Kein Cheat Sheet mit '$*' gefunden."; fi

folien-%:
	@src=$$(find $(BEAMER_SRC) -maxdepth 1 -name '*$**.md' -type f | head -1); \
	if [ -n "$$src" ]; then \
		out="$(BEAMER_OUT)/$$(basename $${src%.md}).pdf"; \
		echo "→ Baue: $$src → $$out"; \
		$(PANDOC) $(PANDOC_COMMON) $(BEAMER_OPTS) $(RESOURCE_PATH) -o "$$out" "$$src"; \
	else echo "Keine Folien mit '$*' gefunden."; fi

notebook-%:
	@src=$$(find $(NOTEBOOK_SRC) -maxdepth 1 -name '*$**.md' -type f | head -1); \
	if [ -n "$$src" ]; then \
		out="$(NOTEBOOK_OUT)/$$(basename $${src%.md}).ipynb"; \
		echo "→ Baue: $$src → $$out"; \
		$(JUPYTEXT) --to ipynb --output "$$out" "$$src"; \
	else echo "Keine Notebook-Quelle mit '$*' gefunden."; fi

# --- Clean ------------------------------------------------------------------
clean:  ## Alle generierten PDFs löschen
	@echo "Lösche generierte PDFs..."
	@find $(UEBUNG_OUT) $(CHEAT_OUT) $(BEAMER_OUT) -name '*.pdf' -type f -delete 2>/dev/null || true
	@echo "Fertig."

clean-grafiken:  ## Generierte Grafiken löschen
	@echo "Lösche Grafiken..."
	@find $(GRAFIK_OUT) -name '*.png' -type f -delete 2>/dev/null || true
	@echo "Fertig."
