.PHONY: install run test clean clean-install

# Install dependencies and setup virtual environment
install:
	@echo "Installing dependencies..."
	@./scripts/install.sh

# Start the FastAPI application
run:
	@echo "Starting FastAPI application..."
	@./scripts/run.sh

# Run tests
test:
	@echo "Running tests..."
	@./scripts/test.sh

# Clean up virtual environment and cache files
clean:
	@./scripts/clean.sh

clean-install: clean install