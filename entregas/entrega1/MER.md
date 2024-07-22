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

- Animal
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
- Instância de arma melee
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

- **Animal**: Textura, Stamina Máx, Vida Máx, Velocidade, Habitat, Espécie, <ins>ID-Animal</ins> <!-- - **Hostil** - **Amigável** -->
- **Instância de Animal**: Stamina Atual, Vida Atual, <ins>ID-Inst-Animal</ins>
- **Sala**: Descrição, nome, <ins>ID-Região</ins>, <ins>ID-Sala</ins>
- **Jogador (PC)**: <ins>ID-Missão</ins>, <ins>ID-Personagem</ins>, XP, Dinheiro, Vida Atual, Stamina Max, Stamina Atual, Habilidades
- **Ataque**: dano, descrição, <ins>ID-Ataque</ins>
- **Consumível**: Qtd Reparação Istamina, Qtd Reparação Vida
- **Equipável**: Parte do Corpo
- **Item**: <ins>ID-Item</ins>, Nome
- **Instância de item**: <ins>ID-Inst-Item</ins>, <ins>ID-Item</ins>, <ins>ID-Inventário</ins>
- **Inventário**: <ins>ID-Inventário</ins>, <ins>ID-Personagem</ins>, Total de itens, Capacidade
- **Personagem**: <ins>ID-Personagem</ins>, Nome, Velocidade, Inventário, Vida Max, Classe, Gangue
- **Gangue**: Líder, Descrição, Nome, <ins>ID-Gangue</ins>
- **Habilidade**: <ins>ID-Habilidade</ins>, Nome, Porcentagem
- **Classe**: <ins>ID-Classe</ins>, Nome, Habilidades
- **Instância de arma**: <ins>ID-Inventário</ins>, <ins>ID-Arma</ins>, <ins>ID-Inst-Arma</ins> <!-- - **Instância de arma de fogo** - **Instância de arma meles** -->
- **Projétil**: <ins>ID-Projétil</ins>, <ins>ID-Inst-Arma</ins>, Pos X, Pos Y, Pos Z, Colidiu, Velocidade
- **Arma**: <ins>ID-Arma</ins>, Nome, Descrição, Categoria, Preço, Peso, Durabilidade, Dano
- **Arma de fogo**: <ins>ID-Arma-Fogo</ins>, Velocidade Disparo, Velocidade Reload
- **Arma melee**: <ins>ID-Arma-Melee</ins>, Nível de afiação
- **NPC**: <ins>ID-NPC</ins>
- **Instância de NPC**: <ins>ID-Inst-NPC</ins>, <ins>ID-NPC</ins>, Vida Atual, <ins>ID-Missão</ins>
- **Missão**: <ins>ID-Missão</ins>, Título, Nível de Dificuldade, Personagens, <ins>ID-História</ins>, <ins>ID-Região</ins>, Status
- **História**: <ins>ID-História</ins>, Título, Enredo
- **Objetivo**: <ins>ID-Objetivo</ins>, Título, Retorno em XP, Retorno em Dinheiro
- **Diálogo**: Descrição, <ins>ID-Inst-NPC</ins>, <ins>ID-Diálogo</ins>
- **Linha de fala**: Texto de fala, <ins>ID-Linha-De-Fala</ins>, <ins>ID-Diálogo</ins>
- **Instância de estabelecimento**: <ins>ID-Inst-NPC-Dono</ins>, <ins>ID-Sala</ins>, <ins>ID-Região</ins>, <ins>ID-Estab</ins>
- **Estabelecimento**: Descrição, Nome, <ins>ID-Estab</ins>
- **Região**: Descrição, Nome, <ins>ID-Mapa</ins>, <ins>ID-Região</ins>
- **Mapa**: Nome, <ins>ID-Mapa</ins>

## Relacionamentos

- Personagem pertence a Classe 
- Classe possui habilidade
- Jogador (PC) participa Gangue
- Gangue confronta Gangue
- Jogador (PC) coleta Instância de Item
- Jogador (PC) usa Instância de Item
- Jogador (PC) doma Instância de Animal
- Jogador (PC) ataca Hostil
- Jogador (PC) acessa Sala
- Jogador (PC) abriga Sala
- Jogador (PC) cumpre Missão
- Jogador (PC) possui Inventário
- Instância de NPC possui NPC
- Instância de NPC possui Inventário
- Instância de NPC coleta Instância de Item
- Instância de NPC usa Instância de Item
- Inventário contém Instância de Item
- Item contém Instância de Item
- Instância de Item dispara Projétil
    - 
- Hostil possui Ataque
    - Um Hostil possui até N Ataques
    - Um Ataque é possuido por até N Hostis
- Animal possui Instância de Animal
    - Um Animal possui de 0 a N Instâncias de Animal
    - Uma Instância de Animal faz parte de um Animal
- Sala abriga Instância de NPC
    - Uma Sala abriga de 0 a N Instâncias de NPC
    - Uma Instância de NPC está abrigada em uma Sala
- Sala abriga Instância de Animal
    - Uma Sala abriga de 0 a N Instância de Animal
    - Uma Instância de Animal está abrigada em uma Sala
- Região contém Sala
    - Uma Região contém até N Salas
    - Cada Sala está contida em uma Região
- Sala conecta Sala
- xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxcxxxxxxxxcxxx
- Região faz fronteira Região
    - Uma Região faz fronteira com de 0 a N Regiões de Origem
    - Uma Região faz fronteira com de 0 a N Regiões de Destino
- Mapa contém Região
    - Um Mapa contém até N Regiões
    - Uma Região está contida em um Mapa
- Sala abriga Instância de Estabelecimento
    - Uma Sala abriga de 0 a N Instâncias de Estabelecimento
    - Uma Instância de Estabelecimento está abrigada em uma Sala
- Instância de Estabelecimento possui Estabelecimento
    - Um Estabelecimento tem de 0 a N Instância de Estabelecimento
    - Uma Instância de Estabelecimento faz parte de um Estabelecimento
- Instância de NPC fala Diálogo
    - Uma Instância de NPC fala N Diálogos
    - Uma Linha de Fala é falada por um NPC
- Diálogo é composto por Linha de Fala
    - Um Diálogo é composto por N Linhas de Falas
    - Uma Linha de Fala compõem um Diálogo
- Instância de NPC participa de Missão
    - Uma instância de NPC faz parte de uma Missão
    - Uma Missão contém de 0 até N NPC
- Missão possui Objetivo
    - Uma Missão possui N objetivos
    - Um objetivo é possuido por uma Missão
- Missão conta História
    - Uma Missão conta uma História
    - Uma História é contada por uma Missão
- Missão pré requisito para Missão
  -


## Bibliografia

[1] ELMASRI, R.; NAVATHE, S. B. **Sistemas de banco de dados**. 6. ed. São Paulo: Pearson Addison Wesley, 2011.

[2] SERRANO, M. **Modelo Entidade-Relacionamento Parte 1**. Adaptado de SOUSA E., JUNIOR J.

[3] SERRANO, M. **Modelo Entidade-Relacionamento Parte 2**. Adaptado de SOUSA E., JUNIOR J.

[4] SERRANO, M. **MER-X Agregação**. Adaptado de SOUSA E., JUNIOR J.

[5] SERRANO, M. **MER-X Generalização/Especialização**. Adaptado de SOUSA E., JUNIOR J.
