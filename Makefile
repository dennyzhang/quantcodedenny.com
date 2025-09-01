# make push COMMIT_MSG="fix: cleanup generated files"
COMMIT_MSG ?= "update website"

push:
	@echo "Pushing changes to GitHub..."
	git add .
	git commit -m "$(COMMIT_MSG)" || echo "No changes to commit."
	git push
	@echo "Push completed."

clean:
	rm -rf content/posts/*.md # remove ox-hugo markdown
