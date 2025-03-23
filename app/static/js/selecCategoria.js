function filtrarPorCategoria() {
    // Obtém o valor selecionado no dropdown
    const categoriaSelecionada = document.getElementById("categoria").value;

    // Obtém todas as linhas da tabela
    const linhas = document.querySelectorAll("tbody tr");

    // Itera sobre as linhas da tabela
    linhas.forEach(linha => {
        const categoriaLinha = linha.getAttribute("data-categoria");

        // Mostra ou oculta a linha com base na categoria selecionada
        if (categoriaSelecionada === "Todas" || categoriaLinha === categoriaSelecionada) {
            linha.style.display = ""; // Mostra a linha
        } else {
            linha.style.display = "none"; // Oculta a linha
        }
    });
}