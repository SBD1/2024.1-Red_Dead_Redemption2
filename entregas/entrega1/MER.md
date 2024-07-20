# Modelo Entidade-Relacionamento (MER)

## Introdução

O Modelo Entidade-Relacionamento (ER) é uma técnica fundamental na modelagem e design de banco de dados. Ele representa dados através de entidades, suas propriedades e as relações entre elas. Esse modelo ajuda a visualizar a estrutura do banco de dados, facilitando o desenvolvimento e a manutenção. Com seu uso, os projetistas podem definir claramente como os dados interagem e são organizados dentro do sistema.

## Diagrama Entidade Relacionamento (DER)

Exibimos agora o DER concebido para o projeto Red Dead Redemption. É possível conferir a evolução do diagrama através de suas versões anteriores, disponíveis nos links logo abaixo.

### Versão x.y

<div align="center">
    <img src="/entregas/entrega1/DER/DER.png">
    Imagem 1: DER v3.2
</div>

Versões anteriores:

- [v1.0](/entregas/entrega1/DER/anteriores/DER_v1.png)
- [v2.0](/entregas/entrega1/DER/anteriores/DER_v2.png)
- [v3.0](/entregas/entrega1/DER/anteriores/DER_v3.png)
- [v3.1](/entregas/entrega1/DER/anteriores/DER_v3.1.png)
- [v3.2 (final)](/entregas/entrega1/DER/DER.png)

## Entidades

- Animal: Textura, StaminaMáx, Vida Máx, Velocidade, Habitat, Espécie, <ins>ID-Animal</ins>
- Hostil
- Amigável
- Instância de Animal
- Sala
- Jogador (PC)
- Ataque
- Consumível
- Equipável
- Item
- Instância de item
- Inventário
- Personagem
- Gangue
- Habilidade
- Classe
- Instância de arma
- Instância de arma de fogo
- Instância de arma meles
- Projétil
- Arma
- Arma de fogo
- Arma melee
- NPC
- Instância de NPC
- Missão
- História
- Objetivo
- Diálogo
- Linha de fala
- Instância de estabelecimento
- Estabelecimento
- Região
- Mapa

## Atributos

Aqui está a lista com tópicos em markdown:

- **Animal**: Textura, Stamina Máx, Vida Máx, Velocidade, Habitat, Espécie, <ins>ID-Animal</ins>
- **Hostil**
- **Amigável**
- **Instância de Animal**: Stamina Atual, Vida Atual, <ins>ID-Inst-Animal</ins>
- **Sala**: Descrição, nome, ID-Região, ID-Sala
- **Jogador (PC)**: ID-Missão, ID-Personagem, XP, Dinheiro, Vida Atual, Stamina Max, Stamina Atual, Habilidades
- **Ataque**: dano, descrição, ID-Ataque
- **Consumível**: Qtd Reparação Istamina, Qtd Reparação Vida
- **Equipável**: Parte do Corpo
- **Item**: ID-Item, Nome
- **Instância de item**: ID-Inst-Item, ID-Item, ID-Inventário
- **Inventário**: ID-Inventário, ID-Personagem, Total de itens, Capacidade
- **Personagem**: ID-Personagem, Nome, Velocidade, Inventário, Vida Max, Classe, Gangue
- **Gangue**: Líder, Descrição, Nome, ID-Gangue
- **Habilidade**: ID-Habilidade, Nome, Porcentagem
- **Classe**: ID-Classe, Nome, Habilidades
- **Instância de arma**: ID-Inventário, ID-Arma, ID-Inst-Arma
- **Instância de arma de fogo**
- **Instância de arma meles**
- **Projétil**: ID-Projétil, ID-Inst-Arma, Pos X, Pos Y, Pos Z, Colidiu, Velocidade
- **Arma**: ID-Arma, Nome, Descrição, Categoria, Preço, Peso, Durabilidade, Dano
- **Arma de fogo**: ID-Arma-Fogo, Velocidade Disparo, Velocidade Reload
- **Arma melee**: ID-Arma-Melee, Nível de afiação
- **NPC**: ID-NPC
- **Instância de NPC**: ID-Inst-NPC, ID-NPC, Vida Atual, ID-Missão
- **Missão**: ID-Missão, Título, Nível de Dificuldade, Personagens, ID-História, ID-Região, Status
- **História**: ID-História, Título, Enredo
- **Objetivo**: ID-Objetivo, Título, Retorno em XP, Retorno em Dinheiro
- **Diálogo**: Descrição, ID-Inst-NPC, ID-Diálogo
- **Linha de fala**: Texto de fala, ID-Linha-De-Fala, ID-Diálogo
- **Instância de estabelecimento**: ID-Inst-NPC-Dono, ID-Sala, ID-Região, ID-Estab
- **Estabelecimento**: Descrição, Nome, ID-Estab
- **Região**: Descrição, Nome, <ins>ID-Mapa</ins>, <ins>ID-Região</ins>
- **Mapa**: Nome, <ins>ID-Mapa</ins>


## Bibliografia

[1] ELMASRI, R.; NAVATHE, S. B. **Sistemas de banco de dados**. 6. ed. São Paulo: Pearson Addison Wesley, 2011.

[2] SERRANO, M. **Modelo Entidade-Relacionamento Parte 1**. Adaptado de SOUSA E., JUNIOR J.

[3] SERRANO, M. **Modelo Entidade-Relacionamento Parte 2**. Adaptado de SOUSA E., JUNIOR J.

[4] SERRANO, M. **MER-X Agregação**. Adaptado de SOUSA E., JUNIOR J.

[5] SERRANO, M. **MER-X Generalização/Especialização**. Adaptado de SOUSA E., JUNIOR J.
