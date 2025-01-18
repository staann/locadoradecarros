% rebase('app/views/html/menu.tpl',title='carros')
<body>
    <div style="text-align: center;" >
        <h2>Listagem dos carros</h2>
        <table class="table" width="200px" align="center" border="1">
            <thead>
                <tr>
                    <th>Fabricante</th>
                    <th>Modelo</th>
                    <th>Ano</th>
                    <th>Categoria</th>
                    <th>Preço Diária</th>
                    <th>Disponível</th>
                    <th>Ações</th>
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
                        <td>
                            <a href="/mostra_form_cadastro_carros/{{carro.id}}"><i class="fa fa-pencil fa-lg  mr-3" style="color: black" ></i></a>  
                            <a href="/processar_exclusao_carro/{{carro.id}}"><i class="fa fa-trash fa-lg  mr-3" style="color: black" ></i></a> 
                            <a href="/mostra_form_aluguel/{{carro.id}}"><i class="fa fa-car fa-lg  mr-3" style="color: black" ></i></a> 
                        </td>
                    </tr>
                % end
            </tbody>
        </table>
        <a href="/mostra_form_cadastro_carros">Cadastrar novo carro</a>
    </div>
</body>
</html>
<br>