var modal = document.getElementById("myModal");  // Selecionar o modal
var span = document.getElementsByClassName("close")[0];  // Selecionar o botão de fechar do modal
var modalContent = document.getElementById("modal-details");  // Selecionar o conteúdo do modal

// Seleciona todos os botões "Ver Detalhes"
var buttons = document.querySelectorAll(".open-modal");

buttons.forEach(button => {
  button.onclick = function() {
    var produtoId = this.getAttribute('data-id');  // Obtém o ID do produto

    // Faz a requisição AJAX para pegar os detalhes do produto
    fetch(`/proc/${produtoId}`)
      .then(response => response.json())
      .then(data => {
        // Verifica se os dados foram recebidos corretamente
        if (data.nome) {
          // Preenche o conteúdo do modal com os detalhes do produto
          modalContent.innerHTML = `
            <h2>${data.nome}</h2>
            <p>${data.descricao}</p>
            <p><strong>Tamanho:</strong> ${data.tamanho}</p>
          `;
          // Exibe o modal
          modal.style.display = "block";
        } else {
          modalContent.innerHTML = `<p>Erro: Produto não encontrado.</p>`;
          modal.style.display = "block";
        }
      })
      .catch(error => {
        modalContent.innerHTML = `<p>Erro ao carregar detalhes: ${error.message}</p>`;
        modal.style.display = "block";
      });
  };
});

// Fecha o modal ao clicar no botão "x"
span.onclick = function() {
  modal.style.display = "none";
}

// Fecha o modal ao clicar fora do conteúdo do modal
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
