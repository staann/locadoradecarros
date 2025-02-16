function calcular() {
    // Obter os valores dos campos
    const dataInicio = document.getElementById('data_inicio').value;
    const dataFinal = document.getElementById('data_final').value;
    //const precoPorDia = parseFloat("{{ carro.preco_por_dia }}"); // Preço por dia do carro
    //const precoPorDia = parseFloat("30.0"); // Preço por dia do carro
    //console.log("Preço por dia:", precoPorDia)
    const precoPorDia = parseFloat(document.getElementById('preco_por_dia').value);

    // Verificar se as datas foram preenchidas
    if (!dataInicio || !dataFinal) {
        alert("Por favor, preencha as datas corretamente.");
        return;
    }

    // Converter as datas para objetos Date
    const dataInicioObj = new Date(dataInicio);
    const dataFinalObj = new Date(dataFinal);

    // Verificar se as datas são válidas
    if (isNaN(dataInicioObj.getTime())) {
        alert("Data de início inválida.");
        return;
    }
    if (isNaN(dataFinalObj.getTime())) {
        alert("Data final inválida.");
        return;
    }

    // Calcular a diferença em milissegundos
    const diferencaMs = dataFinalObj - dataInicioObj;

    // Verificar se a data final é maior ou igual à data inicial
    if (diferencaMs < 0) {
        alert("A data final deve ser maior ou igual à data inicial.");
        return;
    }

    // Converter a diferença para dias
    const diferencaDias = diferencaMs / (1000 * 60 * 60 * 24);

    // Calcular o valor total (diferença em dias * preço por dia)
    const valorTotal = diferencaDias * precoPorDia;

    // Exibir o valor total no campo de texto
    document.getElementById('total').value = valorTotal.toFixed(2);
}