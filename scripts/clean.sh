OUTPUT="Navigating Linux.pdf"
git rm -r --cached .
[ -f "$OUTPUT" ] && mv "$OUTPUT" "${OUTPUT}.keep"
git clean -Xdf
[ -f "${OUTPUT}.keep" ] && mv "${OUTPUT}.keep" "$OUTPUT"
git add .
git restore --staged .