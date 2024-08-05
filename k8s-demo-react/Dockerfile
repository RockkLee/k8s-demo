# Use the official Node.js image as the base image
FROM node:14-alpine as build

# Set the working directory
WORKDIR /k8s-demo-react

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the React app
RUN npm run build

# Use the official Nginx image as the base image for serving the build
FROM nginx:alpine

# Copy the build output to the Nginx html directory
COPY --from=build /k8s-demo-react/build /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]
