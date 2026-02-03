window.mermaidConfig = {
    startOnLoad: true,
    theme: "default",
    securityLevel: "loose",
};

document.addEventListener("DOMContentLoaded", function () {
    if (typeof mermaid !== "undefined") {
        mermaid.initialize(window.mermaidConfig);
    }
});
