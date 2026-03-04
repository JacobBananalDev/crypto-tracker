# ------------------------------------------------------------
# Frontend Dockerfile
#
# Builds and runs the Next.js frontend application.
#
# This container will be used for production deployment
# in container environments such as:
#
# - AWS ECS
# - Kubernetes
# - Docker Compose
#
# ------------------------------------------------------------

# Use Node.js runtime
FROM node:20

# Set working directory inside container
WORKDIR /app

# Copy dependency files first (better Docker layer caching)
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy application source code
COPY . .

# Build Next.js application
RUN npm run build

# Expose the Next.js production port
EXPOSE 3000

# Start production server
CMD ["npm", "start"]