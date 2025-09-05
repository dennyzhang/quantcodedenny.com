# make push COMMIT_MSG="fix: cleanup generated files"
COMMIT_MSG := update website
.PHONY: clean-today dry-run-clean-today nuke-today

push:
	@echo "Pushing changes to GitHub..."
	git add .
	git commit -m "$(COMMIT_MSG)" || echo "No changes to commit."
	git push
	@echo "Push completed."

clean-today:
	@echo "Removing files in content/posts modified today..."
	@start=$$(date -d "today 00:00" +%Y%m%d%H%M.%S 2>/dev/null || date -v0H -v0M -v0S +%Y%m%d%H%M.%S); \
	end=$$(date -d "tomorrow 00:00" +%Y%m%d%H%M.%S 2>/dev/null || date -v+1d -v0H -v0M -v0S +%Y%m%d%H%M.%S); \
	touch -t "$$start" .today_start; touch -t "$$end" .today_end; \
	find content/posts -type f ! -name '.today_start' ! -name '.today_end' -newer .today_start ! -newer .today_end -print -delete; \
	rm -f .today_start .today_end

dry-run-clean-today:
	@echo "Dry run — files in content/posts that would be removed:"
	@start=$$(date -d "today 00:00" +%Y%m%d%H%M.%S 2>/dev/null || date -v0H -v0M -v0S +%Y%m%d%H%M.%S); \
	end=$$(date -d "tomorrow 00:00" +%Y%m%d%H%M.%S 2>/dev/null || date -v+1d -v0H -v0M -v0S +%Y%m%d%H%M.%S); \
	touch -t "$$start" .today_start; touch -t "$$end" .today_end; \
	find content/posts -type f ! -name '.today_start' ! -name '.today_end' -newer .today_start ! -newer .today_end -print; \
	rm -f .today_start .today_end

nuke-today: clean-today
	@echo "nuke-today complete (content/posts cleaned)."

clean: clean-today
