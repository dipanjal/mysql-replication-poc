# Docker Compose Makefile

.PHONY: build up up-build down clean logs ps

# Build images without starting containers
build:
	@ docker-compose build

# Start containers (assumes images are already built)
up:
	@ docker-compose up

# Build and start containers in one command
up-build:
	@ docker-compose up --build

# Stop and remove containers with volumes
down:
	@ docker-compose down -v

# View logs
logs:
	@ docker-compose logs -f

# Show running containers
ps:
	@ docker-compose ps

# Clean up everything (containers, images, volumes)
clean: down
	@ docker-compose down --rmi all --volumes --remove-orphans
	@ docker system prune -f