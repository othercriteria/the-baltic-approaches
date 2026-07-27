-- Scene breaks: pandoc renders a markdown thematic break (---) as a
-- bare \rule in LaTeX output — the trade-paperback tell (WB's
-- "loudest," fixed twice there; planning/assembly.md). Convert to
-- the asterism defined in apparatus/latex-header.tex. Other output
-- formats (manuscript md, docx) keep the default break.
function HorizontalRule()
  if FORMAT:match("latex") then
    return pandoc.RawBlock("latex", "\\scenebreak")
  end
end
