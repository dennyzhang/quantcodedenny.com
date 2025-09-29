# Makefile in child folder

.PHONY: push pull clean all

# Detect parent folder
PARENT_DIR := ..

# Default COMMIT_MSG if not provided
COMMIT_MSG ?= update content in org-file

# Default target: forward everything to parent
push pull clean:
	@echo "Forwarding target '$@' to parent folder..."
	@$(MAKE) -C $(PARENT_DIR) $@ COMMIT_MSG="$(COMMIT_MSG)"
