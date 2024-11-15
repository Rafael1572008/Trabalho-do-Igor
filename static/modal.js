var modal = document.getElementById("myModal");  // Selecionar o modal
var span = document.getElementsByClassName("close")[0];  // Selecionar o botão de fechar do modal
var modalContent = document.getElementById("modal-details");  // Selecionar o conteúdo do modal

// Seleciona todos os botões "Ver Detalhes"
var buttons = document.querySelectorAll(".open-modal");

buttons.forEach(button => {                          // Interar sobre os botões
  button.onclick = function() {
    var produtoId = this.getAttribute('data-bolo');  // Obtém o ID do bolo

    
    fetch(`/proc/${produtoId}`)   // Enviar umarequisção HTTP
      .then(res => res.json())    // Converter de json para objeto a resposta do fetch 
      .then(data => {             // Recebe o objeto convertido e guarda em data
        if (data.nome) {          // Se nome exitir, mostrar as propriedades do bolo
          modalContent.innerHTML = `
            <h2>${data.nome}</h2>
            <p>${data.descricao}</p>
            <p><strong>Tamanho:</strong> ${data.tamanho}</p>
          `;
        } else {   // Se não, Mostrar um erro
          modalContent.innerHTML = `<p>Erro: Produto não encontrado.</p>`;
        }
        modal.style.display = "block"; // Exibe o modal (Block faz com que ocupe toda a div)
      })
      .catch(err => {   // Caso a requisição falhe, mostra o erro (catch captura erros)
        modalContent.innerHTML = `<p>Erro ao carregar detalhes: ${err.message}</p>`;
        modal.style.display = "block";
      });  
      };
    });

span.onclick = function() {  // Fecha o modal ao clicar no botão "x"
  modal.style.display = "none";
}

window.onclick = function(event) {  // Fecha o modal ao clicar fora do conteúdo do modal
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
