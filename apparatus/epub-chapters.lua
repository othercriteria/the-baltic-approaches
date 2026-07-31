-- EPUB-side chapter handling (eBook edition; see planning/ebook-brief.md).
-- Parallel to the print pair chapters.lua + scenebreak.lua, which stay
-- LaTeX-only and untouched — this filter is passed ONLY by `make epub`.
--
-- H1s in drafts carry "N — Title". The trade book renders a two-deck
-- head (small-caps CHAPTER N over the title) with LaTeX numbering;
-- here the deck is built directly from the source numeral:
--   <h1><span class="chapnum">CHAPTER N</span><br/>Title</h1>
-- The nav/TOC entry therefore reads "CHAPTER N Title" (noted in the
-- brief). Message divs need no handling: pandoc's EPUB writer keeps
-- <div class="message"> and epub.css styles it.
function Header(el)
  if el.level == 1 and #el.content >= 5 then
    local a, b, c, d = el.content[1], el.content[2], el.content[3], el.content[4]
    if a.t == "Str" and a.text:match("^%d+$")
       and b.t == "Space"
       and c.t == "Str" and c.text == "—"
       and d.t == "Space" then
      local out = {
        pandoc.Span({pandoc.Str("CHAPTER " .. a.text)}, {class = "chapnum"}),
        pandoc.LineBreak(),
      }
      for i = 5, #el.content do out[#out + 1] = el.content[i] end
      el.content = out
      return el
    end
  end
end

-- Scene breaks: the trade asterism (* * *), not the default <hr/>.
function HorizontalRule()
  return pandoc.RawBlock("html", '<p class="scenebreak">*&#8195;*&#8195;*</p>')
end
