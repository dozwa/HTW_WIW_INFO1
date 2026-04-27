-- box_classes.lua
--
-- Pandoc Lua filter: wickelt fenced divs mit bekannten Klassen-Namen
-- in gleichnamige LaTeX-Environments ein. Für die Beamer-Foliensätze
-- gibt es so unterschiedliche Box-Stile pro Inhaltstyp:
--
--   ::: demobox       -> \begin{demobox} ... \end{demobox}
--                       (Anweisung an Lecturer für Live-Demo)
--   ::: exercisebox   -> \begin{exercisebox} ... \end{exercisebox}
--                       (Anweisung an Studierende für Notebook-Übung)
--
-- Die LaTeX-Environments selbst sind in den header-includes der jeweiligen
-- slides.md als tcolorbox definiert (mit unterschiedlichen Rahmenfarben).
--
-- Erweiterung: weitere Klassen einfach in BOX_CLASSES eintragen.

local BOX_CLASSES = {
  demobox = true,
  exercisebox = true,
}

function Div(el)
  for _, class in ipairs(el.classes) do
    if BOX_CLASSES[class] then
      local out = { pandoc.RawBlock("latex", "\\begin{" .. class .. "}") }
      for _, block in ipairs(el.content) do
        table.insert(out, block)
      end
      table.insert(out, pandoc.RawBlock("latex", "\\end{" .. class .. "}"))
      return out
    end
  end
  return nil
end
