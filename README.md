# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a simple React "Hello World" application built with Webpack and Babel. The project demonstrates basic React component structure and build configuration.

## Common Commands

- `npm install` - Install dependencies
- `npm start` - Start development server (opens at http://localhost:3000)
- `npm run build` - Build for production (outputs to `dist/` directory)

## Architecture

### Project Structure
- `src/index.js` - Application entry point, renders App component
- `src/App.js` - Main application component that imports and renders HelloWorld
- `src/HelloWorld.jsx` - Simple React component displaying "Hello, World!"
- `public/index.html` - HTML template with root div
- `webpack.config.js` - Webpack configuration with Babel for JSX/ES6 transpilation

### Build System
- Uses Webpack 5 with webpack-dev-server for development
- Babel transpiles JSX and modern JavaScript
- HtmlWebpackPlugin generates HTML with bundled scripts
- Development server runs on port 3000 with hot reloading
