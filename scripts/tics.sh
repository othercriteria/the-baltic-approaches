#!/bin/sh
# Tic inventory, measured. Run: make tics. Budgets: em-dash <=10/ch
# (outline s8); "the way" <=2/ch; "like a man" <=2 total (dialogue
# + chapter-defining keeps exempt, judged by hand); narrator
# superlatives-of-the-war ~3; heat/click 2 origins.
#
# MEASUREMENT NOTE (2026-07-24): drafts are hard-wrapped, so
# phrase greps on raw files undercount across line breaks. All
# multi-word measures below run on an UNWRAPPED stream (tr
# newline->space) per file. Single-character counts (em-dash)
# are wrap-safe on raw files.
cd "$(dirname "$0")/.." || exit 1

unwrap() { tr '\n' ' ' < "$1"; }

echo "== em-dashes per chapter (budget 10):"
for f in drafts/*.md; do
    n=$(grep -o "—" "$f" | wc -l)
    printf "%-30s %s\n" "$(basename "$f")" "$n"
done | sort -k2 -rn

echo "== 'the way ' per chapter (budget 2, unwrapped):"
for f in drafts/*.md; do
    n=$(unwrap "$f" | grep -o "the way " | wc -l)
    [ "$n" -gt 0 ] && printf "%-30s %s\n" "$(basename "$f")" "$n"
done | sort -k2 -rn

echo "== 'like a man' (target 2-3 total, keeps exempt, unwrapped):"
for f in drafts/*.md; do
    n=$(unwrap "$f" | grep -o "like a man" | wc -l)
    [ "$n" -gt 0 ] && printf "%-30s %s\n" "$(basename "$f")" "$n"
done

echo "== superlative-of-the-war formula (unwrapped):"
for f in drafts/*.md; do
    n=$(unwrap "$f" | grep -oE "[a-z]+est [a-z ]*of the war|war's [a-z]*est" | grep -cvE "^(rest|west|interest)")
    [ "$n" -gt 0 ] && printf "%-30s %s\n" "$(basename "$f")" "$n"
done

echo "== heat/click comprehension (unwrapped):"
for f in drafts/*.md; do
    n=$(unwrap "$f" | grep -oE "heat along|heat of comprehension|same heat|click of a|same click" | wc -l)
    [ "$n" -gt 0 ] && printf "%-30s %s\n" "$(basename "$f")" "$n"
done

echo "== negation-definition candidates ('not X. It [is/was]', unwrapped):"
for f in drafts/*.md; do
    n=$(unwrap "$f" | grep -oE "[Nn]ot [a-z]+\. (It|That) (is|was)" | wc -l)
    [ "$n" -gt 0 ] && printf "%-30s %s\n" "$(basename "$f")" "$n"
done

echo "== 'the particular X' (family watch, no budget yet, unwrapped):"
for f in drafts/*.md; do
    n=$(unwrap "$f" | grep -o "the particular [a-z]*" | wc -l)
    [ "$n" -gt 0 ] && printf "%-30s %s\n" "$(basename "$f")" "$n"
done

echo "== figuration adjacency (two simile markers within ~200 chars, unwrapped):"
for f in drafts/*.md; do
    unwrap "$f" | grep -oE "(like a|as if|as though|the way [a-z]+|the particular)[^.]{0,200}(like a|as if|as though|the way [a-z]+|the particular)" \
        | while read -r m; do printf "%-28s %.90s...\n" "$(basename "$f")" "$m"; done
done
