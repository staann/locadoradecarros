% rebase('app/views/html/base.tpl',title='Listagem de carros')

<h2>Listagem dos carros</h2>
<table border="1">
    <thead>
        <tr>
            <th>Fabricante</th>
            <th>Modelo</th>
            <th>Ano</th>
            <th>Categoria</th>
            <th>Preço Diária</th>
            <th>Disponível</th>
        </tr>
    </thead>
    <tbody>
        % for carro in carros:
            <tr>
                <td>{{ carro.marca }}</td>
                <td>{{ carro.modelo }}</td>
                <td>{{ carro.ano }}</td>
                <td>{{ carro.categoria }}</td>
                <td>{{ carro.preco_por_dia }}</td>
                <td>{{'Disponivel' if carro.status else 'Indisponivel'}}</td>
            </tr>
        % end
    </tbody>
</table>
<br>