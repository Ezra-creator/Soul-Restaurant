# Restaurant Website Landing Page

This repository contains a clean, professional, and scalable file and folder structure for a modern restaurant landing page. The architecture is organized systematically, resembling a real-world web project setup designed for maintainability and easy deployment.

## Folder & File Structure Explanation

```text
restaurant-website/
|-- index.html              <-- Main entry point of the application. It links to core CSS and JS files, and holds the document shell.
|-- README.md               <-- Provides instructions and an overview of the project structure and setup.
|-- assets/                 <-- All static, non-source-code files are centralized here.
|   |-- images/             <-- Dedicated to food, background, and restaurant photography. Keeps the root clean.
|   |-- icons/              <-- Contains SVG graphics, PNG icons, or custom font icons used in the UI.
|-- css/                    <-- All custom style logic.
|   |-- style.css           <-- Main stylesheet. Contains global CSS variables, resets, layout configuration, and component styling.
|   |-- animations.css      <-- Specialized CSS file for handling `@keyframes`, transitions, and interactive hover states (Separation of concerns).
|-- js/                     <-- All custom script logic.
|   |-- main.js             <-- General execution logic, DOM interactions, form handlers, and navigation scripts.
|   |-- animations.js       <-- Isolated scripts used purely for driving effects (e.g., Intersection Observers, triggering AOS library).
|-- sections/               <-- Code modularity: Contains the HTML fragments for individual sections (Hero, About, etc.). For a static site, developers can reference these to embed into `index.html`.
|   |-- hero.html
|   |-- about.html
|   |-- menu.html
|   |-- gallery.html
|   |-- contact.html
|-- vendor/                 <-- Houses third-party code and external dependencies downloaded locally.
    |-- aos/                <-- "Animate On Scroll" library placeholder. Drop `aos.css` and `aos.js` here if opting to use the module.
```

## Importance of this Structure
1. **Separation of Concerns**: By keeping structural HTML (`index.html`), presentation (`css/`), static assets (`assets/`), and logic (`js/`) isolated, the codebase remains clean.
2. **Scalability**: As the website grows from a landing page into a multi-page routing project or transitions to a framework (like React or Vue), having `assets`, `components` (sections in this case), and core `styles`/`scripts` separated accurately mirrors modern workflows.
3. **Modularity**: Specialized files (e.g., `animations.css` and `animations.js`) avoid monolithic, messy code files.