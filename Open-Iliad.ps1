$ErrorActionPreference = 'Stop'
code --remote wsl+Ubuntu-24.04 /mnt/c/Users/emlyn/Documents/iliad-learning/iliad.code-workspace
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
