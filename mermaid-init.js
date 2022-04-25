browsertheme = localStorage.getItem('mdbook-theme')
theme = 'default'

if (browsertheme == 'steinberg-dark') {
    theme = 'dark'
}
else {
    theme = 'default'
}
mermaid.initialize({startOnLoad:true, 'theme': theme});
