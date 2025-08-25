# Setup the env

- For testing
```
python3 -m pip install --user requests beautifulsoup4
```

- For workflow
```
# export .org to .md via ox-hugo
brew install hugo
```
- ox-hugo export
```
C-c C-e H H   ; (org-export-dispatch → Hugo → export current subtree)
C-c C-e H A; export the whole buffer

# preview in local
cd quantcodedenny.com
hugo server -D
# http://localhost:1313
```
# Run health check
```
python3 healthcheck.py
```
