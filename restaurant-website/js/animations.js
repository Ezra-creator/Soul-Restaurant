/**
 * Premium AOS (Animate On Scroll) Initialization setup
 */

document.addEventListener('DOMContentLoaded', () => {
    if (typeof AOS !== 'undefined') {
        AOS.init({
            duration: 1000,         // slightly slightly slower for more elegance
            easing: 'ease-out-cubic',
            once: true,             // whether animation should happen only once
            offset: 100,            // trigger point
            delay: 50               // delay applied globally
        });
    } else {
        console.warn("AOS Library is not loaded. Scroll animations are disabled.");
    }
});
