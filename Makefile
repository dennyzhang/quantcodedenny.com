COMMIT_MSG ?= "update website"

push:
	@echo "Pushing changes to GitHub..."
	git add .
	git commit -m "$(COMMIT_MSG)" || echo "No changes to commit."
	git push
	@echo "Push completed."
