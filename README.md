# Bibliotech
Foco em trazer eficiência e facilidade nas bibliotecas de escolas. Tornando mais pratico a gerencia de livros para sites e gestão de biblioteca.

# Escola
## Conexões:
**Post:** `api/school/` - Criar escola no banco 

**Get:** `api/school/{id}` - Retorna determinada escola no banco

**Patch:** `api/school/{id}` - Atualizar determinada escola no banco

**Delete:** `api/school/{id}` - Deleta determinada escola do banco

# Livraria
## Conexões:
**Get:** `/api/livros` - Retorna a lista de livros em formato JSON.

**Post:** `/api/livro` - Necessário passar o Schema (Json/Dict) associado a Model Book. Caso já exista um livro com o mesmo título será retornado o valor False como erro.

**Delete:** `/api/remover_livro` - Necessário passar o ID referente ao livro. Caso não encontre nenhum será retornado False como erro.

**Patch:** `/api/atualizar_livro` - Necessário passar o ID e o Schema (BookIn) com os dados que deseja atualizar. Caso não encontre nenhum livro será retornado o valor False como erro.
