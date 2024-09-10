# Modelo Entidade-Relacionamento (MER)

## Introdução

O Modelo Entidade-Relacionamento (ER) é uma técnica fundamental na modelagem e design de banco de dados. Ele representa dados através de entidades, suas propriedades e as relações entre elas. Esse modelo ajuda a visualizar a estrutura do banco de dados, facilitando o desenvolvimento e a manutenção. Com seu uso, os projetistas podem definir claramente como os dados interagem e são organizados dentro do sistema.

## Diagrama Entidade Relacionamento (DER)

Exibimos agora o DER concebido para o projeto Red Dead Redemption. É possível conferir a evolução do diagrama através de suas versões anteriores, disponíveis nos links logo abaixo.

### Versão 3.5

<div align="center">
    <img src="/docs/DER/DER_v_5_1.jpg">
    Imagem 1: DER v5
</div>

Versões anteriores:

- [v1.0](/docs/DER/anteriores/DER_v1.png)
- [v2.0](/docs/DER/anteriores/DER_v2.png)
- [v3.0](/docs/DER/anteriores/DER_v3.png)
- [v3.1](/docs/DER/anteriores/DER_v3.1.png)
- [v3.2](/docs/DER/anteriores/DER_v3.2.png)
- [v3.3](/docs/DER/anteriores/DER_v3.3.png)
- [v3.4](/docs/DER/anteriores/DER_v3.4.png)
- [v3.5 (pós-realease)](/docs/DER/DER.png)
- [v4](/docs/DER/anteriores/DER_v4.png)
- [v5](/docs/DER/DER_v_5.png)
- [v5](/docs/DER/DER_v_5_1.jpg.png)


## Entidades e atributos

1. **Região**
   - idRegiao
   - nome
   - descricao

2. **Mapa**
   - idMapa
   - descricao

3. **Área**
   - idArea
   - nome
   - Norte
   - Sul
   - Leste
   - Oeste 

4. **Loja**
   - idLoja
   - descricao
  
5. **Item**
   - idItem
   - nome
   - descricaoItem
   - valor
   - acao
   - tipo

6. **Inventário**
   - idInventario
   - dinheiro

7. **Jogador**
   - idJogador
   - nome
   - pontosVida
   - estado

8. **Gangue**
   - idGangue
   - nome
   - simboloGangue

9. **Missão**
   - idMissao
   - nomeMissao

10. **Fala**
    - idFala
    - texto
    - momento

11. **NPC**
    - idNPC
    - nome

12. **Inimigo**
    - idInimigo

13. **Arsenal**
    - idArsenal
    - lotacao

14. **Arma**
    - idArma
    - tipo

15. **Habilidade**
    - idHabilidade
    - descricao
    - dano
    - nomeHabilidade

16. **InstanciaItem**
    - idInstanciaItem

17. **Amigo**
    - humor

18. **NPCMissao**
    - idNPCMissao
    - cargo

19. **InstanciaInimigo**
    - multiplicador
    - pontosVida
    - pontosVidaMax
    - idInstanciaInimigo

20. **Coldre**
    - idColdre

21. **InstanciaNPC**
    - idInstanciaNPC

## Relacionamentos

1. **Região - Área**: Uma Região **contém** várias Áreas.
2. **Área - Loja**: Uma Área **possui** uma Loja.
3. **Área - Jogador**: Um Jogador **se localiza em** uma Área.
4. **Inventário - Jogador**: Um Inventário **pertence a** um Jogador.
5. **Gangue - Jogador**: Um Jogador **pertence a** uma Gangue.
6. **Missão - Jogador**: Um Jogador **participa de** uma Missão.
7. **Item - Inventário**: Um Inventário **possui** um ou mais Itens.
8. **Item - Missão**: Um Item **guarda** uma Missão.
9. **Fala - InstanciaNPC**: Uma InstanciaNPC **diz** uma Fala.
10. **InstânciaNPC - NPC**: NPCs podem ser **instanciados** em vários cenários como Amigo ou Inimigo.
11. **InstanciaInimigo - InstanciaItem**: Uma Instancia de Inimigo pode **possui** um ou mais Instancias de Itens.
12. **InstânciaInimigo - Missão**: Um Inimigo pode ser **instanciado** em uma Missão.
13. **Arma - Arsenal**: Uma Arma **armazena-se em** um Arsenal.
14. **Habilidade - Inimigo**: Um Inimigo **possui** uma ou mais Habilidades.
15. **Coldre - Arma**: Um Coldre **contém** uma Arma.
16. **Mapa - Região**: Uma mapa **contém** um ou mais Regiões.
17. **Área - Área**: Uma área **liga** uma ou mais Áreas.
18. **Loja - InstanciaItem**: Uma loja **vende** uma ou mais Instancia de Itens.
19. **InstanciaItem - Item**: Um item **instancia** uma ou mais Instancia de Itens.
20. **Missao - NPCMissao**: Um NPCMissao **participa** de uma Missao.
21. **Inimigo - InstanciaInimigo**: Um Inimigo **instancia** um ou mais InstanciaInimigo.
22. **Coldre - InstanciaItem**: Um coldre **guarda** uma InstanciaItem.
23. **NPC - InstanciaItem**: Um NPC **possui** uma ou mais InstanciaItem.
24. **Arsenal - Jogador**: Um Jogador **possui** um Arsenal.
25. **NPC - InstanciaNPC**: Um NPC **instancia** um ou mais InstanciaNPC.

## Bibliografia

[1] ELMASRI, R.; NAVATHE, S. B. **Sistemas de banco de dados**. 6. ed. São Paulo: Pearson Addison Wesley, 2011.

[2] SERRANO, M. **Modelo Entidade-Relacionamento Parte 1**. Adaptado de SOUSA E., JUNIOR J.

[3] SERRANO, M. **Modelo Entidade-Relacionamento Parte 2**. Adaptado de SOUSA E., JUNIOR J.

[4] SERRANO, M. **MER-X Agregação**. Adaptado de SOUSA E., JUNIOR J.

[5] SERRANO, M. **MER-X Generalização/Especialização**. Adaptado de SOUSA E., JUNIOR J.
