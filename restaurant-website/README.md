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

## How to use relative paths?
- **From HTML (`index.html`)**: Simply use `css/style.css` or `assets/images/logo.png`.
- **From CSS (`css/style.css`)**: If you need to access an image, traverse one directory up using `../`: e.g., `background-image: url('../assets/images/bg.jpg');`.
- **From JS (`js/main.js`)**: Similar logic, URLs point relative to where the JS is executing on `index.html`. 

## Deployment Setup

This project is entirely static (HTML, CSS, JS). No build step required! It is ready for easy out-of-the box deployment:
1. Make sure all local references inside `index.html` (e.g., `<img src="...">` and `<link href="...">`) are properly matched.
2. Host it effortlessly by uploading the root `restaurant-website` folder to a service like **Netlify (drag and drop)**, **GitHub Pages**, or **Vercel**.
