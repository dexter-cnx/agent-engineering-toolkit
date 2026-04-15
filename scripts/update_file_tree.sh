find . -mindepth 1 \
  -not -path './.git' \
  -not -path './.git/*' \
  -not -name '.DS_Store' \
  | sed 's#^\./##' \
  | sort > docs/tree-manifest.txt
