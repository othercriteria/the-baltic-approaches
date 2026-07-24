#!/bin/sh
# Tic inventory, measured. Run: make tics. Budgets: em-dash <=10/ch
# (outline s8); "the way" <=2/ch; "like a man" <=2 total (dialogue
# + chapter-defining keeps exempt, judged by hand); narrator
# superlatives-of-the-war ~3; heat/click 2 origins.
cd "$(dirname "$0")/.." || exit 1

echo "== em-dashes per chapter (budget 10):"
for f in drafts/*.md; do
    n=$(grep -o "—" "$f" | wc -l)
    printf "%-30s %s\n" "$(basename "$f")" "$n"
done | sort -k2 -rn

echo "== 'the way ' per chapter (budget 2):"
for f in drafts/*.md; do
    n=$(grep -c "the way " "$f")
    [ "$n" -gt 0 ] && printf "%-30s %s\n" "$(basename "$f")" "$n"
done | sort -k2 -rn

echo "== 'like a man' (target 2-3 total, keeps exempt):"
grep -c "like a man" drafts/*.md | grep -v ":0" || echo "  none"

echo "== superlative-of-the-war formula:"
grep -n "est [a-z ]*of the war\|war's [a-z]*est\|of the war so far" drafts/*.md || echo "  none"

echo "== heat/click comprehension:"
grep -n "heat along\|heat of comprehension\|same heat\|click of a\|same click" drafts/*.md || echo "  none"

echo "== negation-definition candidates ('not X. It [is/was]'):"
grep -cE "[Nn]ot [a-z]+\. (It|That) (is|was)" drafts/*.md | grep -v ":0" || echo "  none"
