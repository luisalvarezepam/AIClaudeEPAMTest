# React Interactive Hello World App

A simple React application demonstrating interactive form components including dropdowns, checkboxes, radio buttons, and other form elements.

## Features

- **Hello World Component**: Simple greeting display
- **Interactive Form**: Comprehensive form with multiple input types:
  - Text input for name
  - Dropdown for country selection
  - Radio buttons for gender selection
  - Checkboxes for hobby selection
  - Color picker for favorite color
  - Range slider for experience level
  - Newsletter subscription checkbox
  - Real-time form data display

## Technologies Used

- React 18.2.0
- Webpack 5 with Babel transpilation
- HTML5 form elements
- CSS-in-JS styling

## Getting Started

### Prerequisites

- Node.js (version 14 or higher)
- npm or yarn

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/luisalvarezepam/AIClaudeEPAMTest.git
   cd AIClaudeEPAMTest
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

4. Open your browser and navigate to `http://localhost:3000`

### Build for Production

To create a production build:

```bash
npm run build
```

The build artifacts will be stored in the `dist/` directory.

## Project Structure

```
src/
├── App.js              # Main application component
├── HelloWorld.jsx      # Simple greeting component
├── InteractiveForm.jsx # Interactive form with various input types
└── index.js           # Application entry point

public/
└── index.html         # HTML template

webpack.config.js      # Webpack configuration
package.json          # Project dependencies and scripts
```

## Form Components

The interactive form includes the following components:

- **Text Input**: Basic text input for user's name
- **Select Dropdown**: Country selection with multiple options
- **Radio Buttons**: Gender selection (Male, Female, Other)
- **Checkboxes**: Multiple hobby selection (Reading, Gaming, Sports, Music, Cooking, Travel)
- **Color Picker**: HTML5 color input for favorite color selection
- **Range Slider**: Experience level from Beginner (0) to Expert (10)
- **Checkbox**: Newsletter subscription toggle

All form data is managed with React hooks and displays real-time updates as users interact with the form.

## Development

This project uses:
- Webpack Dev Server for hot reloading
- Babel for JSX and ES6+ transpilation
- ESLint configuration for code quality

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License.