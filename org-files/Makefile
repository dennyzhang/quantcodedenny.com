# Recursive Make Helper
# Usage: make run TARGET=push

.PHONY: run

# Default: run the target passed in via TARGET
run:
	@if [ -z "$(TARGET)" ]; then \
		echo "Usage: make run TARGET=<target>"; \
		exit 1; \
	fi
	@echo "Trying target '$(TARGET)' in $(CURDIR)"
	@set -e; \
	MAKE_OUTPUT=$$(make -s $(TARGET) 2>&1 || true); \
	if echo "$$MAKE_OUTPUT" | grep -q "No rule to make target"; then \
		echo "Target '$(TARGET)' not found in $(CURDIR), going to parent..."; \
		cd ..; \
		make run TARGET=$(TARGET); \
		cd - > /dev/null; \
	else \
	        # the actual make output if it succeeded or failed for other reasons
		echo "$$MAKE_OUTPUT"; \
		if echo "$$MAKE_OUTPUT" | grep -q "Error"; then exit 1; fi; \
	fi
