-- Chapter-title handling for the PDF builds (planning/assembly.md,
-- design review fork 3): the drafts' H1s carry "N — Title" for
-- filename/reference discipline, but the typeset book runs a
-- two-deck head ("CHAPTER N" over the title) with LaTeX doing the
-- numbering (--number-sections). Strip the leading numeral + em
-- dash from level-1 headers; leave every other header alone.
function Header(el)
  if el.level == 1 and #el.content >= 5 then
    local a, b, c, d = el.content[1], el.content[2], el.content[3], el.content[4]
    if a.t == "Str" and a.text:match("^%d+$")
       and b.t == "Space"
       and c.t == "Str" and c.text == "—"
       and d.t == "Space" then
      local rest = {}
      for i = 5, #el.content do rest[#rest + 1] = el.content[i] end
      el.content = rest
      return el
    end
  end
end

-- Set-off message/teleprinter blocks: fenced divs with class
-- "message" become the messageblock environment (small, slightly
-- letterspaced, ragged right, hyphenation off — reads as a
-- different paper stock; latex-header.tex defines it).
function Div(el)
  if el.classes:includes("message") then
    local out = {pandoc.RawBlock("latex", "\\begin{messageblock}")}
    for _, blk in ipairs(el.content) do out[#out + 1] = blk end
    out[#out + 1] = pandoc.RawBlock("latex", "\\end{messageblock}")
    return out
  end
end
