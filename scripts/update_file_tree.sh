find . -mindepth 1 \
  -not -path './.git' \
  -not -path './.git/*' \
  | sed 's#^\./##' \
  | sort > docs/tree-manifest.txt