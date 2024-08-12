# Stage 1: Build the base image
FROM node:21-alpine AS base

# Create a directory for the app code
WORKDIR /workspace/frontend

# Set up PNPM environment variables
ENV PNPM_HOME=/workspace/frontend/.pnpm-home
ENV PATH=$PNPM_HOME/bin:$PATH

# Install necessary packages, pnpm, and confiugre pnpm 
RUN apk add --no-cache build-base && \
    npm install -g pnpm 

# Copy package.json and pnpm-lock.yaml for dependency installation 
COPY package.json pnpm-lock.yaml ./ 

# Stage 2: Development
FROM base as dev

#  Install all dependencies (including dev) and git
RUN apk add git && pnpm install

# Copy the rest of the application code
COPY . .

# Exporse the port used by development server
EXPOSE 3000

# Start the development server
# CMD ["pnpm", "dev"]
ENTRYPOINT [ "tail", "-f", "/dev/null"]

# Stage 3: Production
FROM base as prod

# Install only production dependencies
RUN pnpm install --prod

# Copy the rest of the application code
COPY . .

# Build the application
RUN pnpm build

# Expose the port used by the production server
EXPOSE 3000

# Start the production server
CMD ["pnpm", "start"]
