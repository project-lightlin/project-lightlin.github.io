// Remove the home icon and empty line from the side navigation
// Convert smartqsm-external link to GitHub external link
window.addEventListener('DOMContentLoaded', function() {
    // Find the home link in the side navigation
    var homeLink = document.querySelector('.wy-side-nav-search a.icon-home');
    if (homeLink) {
        // Remove the icon classes to eliminate the home icon
        homeLink.classList.remove('icon', 'icon-home');
        
        // Clean up whitespace in the link
        homeLink.innerHTML = homeLink.innerHTML.trim();
    }
    
    // Convert smartqsm-external link to GitHub repository link
    var navLinks = document.querySelectorAll('.wy-menu-vertical a.reference.internal');
    navLinks.forEach(function(link) {
        // Check if link text contains "SmartQSM"
        if (link.textContent.trim() === "SmartQSM") {
            link.href = "https://github.com/project-lightlin/SmartQSM";
            link.target = "_blank"; // Open in new tab
            link.rel = "noopener noreferrer"; // Security recommendations for external links
        }
    });
});