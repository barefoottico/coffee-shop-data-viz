#!/bin/bash

# Check if a project name was provided as an argument
if [ -z "$1" ]; then
  echo "Please provide a project name."
  echo "Usage: $0 project_name"
  exit 1
fi

# Project name from the first argument
PROJECT_NAME=$1

# Create project directory
mkdir -p $PROJECT_NAME
cd $PROJECT_NAME || exit

# Create the project structure
mkdir -p public
mkdir -p src/components

# Create initial files
touch public/index.html
touch public/other-file.html
touch src/components/header.js
touch src/components/footer.js
touch src/app.js
touch src/main.css
touch tailwind.config.js
touch package.json

# Add sample content to the files

# index.html
cat <<EOT >> public/index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>$PROJECT_NAME</title>
    <link rel="stylesheet" href="../src/main.css">
</head>
<body>
    <h1>Welcome to $PROJECT_NAME</h1>
    <script src="../src/app.js"></script>
</body>
</html>
EOT

# other-file.html
cat <<EOT >> public/other-file.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Other File</title>
    <link rel="stylesheet" href="../src/main.css">
</head>
<body>
    <h1>This is another HTML file</h1>
    <script src="../src/app.js"></script>
</body>
</html>
EOT

# header.js
cat <<EOT >> src/components/header.js
console.log('Header component loaded');
EOT

# footer.js
cat <<EOT >> src/components/footer.js
console.log('Footer component loaded');
EOT

# app.js
cat <<EOT >> src/app.js
import './components/header.js';
import './components/footer.js';
console.log('App loaded');
EOT

# main.css
cat <<EOT >> src/main.css
/* Tailwind base styles */
@tailwind base;
@tailwind components;
@tailwind utilities;
EOT

# tailwind.config.js
cat <<EOT >> tailwind.config.js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./public/**/*.html", "./src/**/*.{html,js}"],
  theme: {
    extend: {},
  },
  plugins: [],
}
EOT

# package.json
cat <<EOT >> package.json
{
  "name": "$PROJECT_NAME",
  "version": "1.0.0",
  "description": "A project to learn Tailwind CSS",
  "main": "src/app.js",
  "scripts": {
    "build:css": "tailwindcss build src/main.css -o public/main.css"
  },
  "devDependencies": {
    "tailwindcss": "^2.2.19"
  },
  "dependencies": {}
}
EOT

echo "Project structure created successfully for $PROJECT_NAME!"

