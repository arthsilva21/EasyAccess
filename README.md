# EasyAccess
Projeto voltado para solução do problema de almoxarifes.
<br> 
EASY ACCESS

GERENCIAMENTO DE ESTOQUE E PATRIMÔNIO DE UTILIZÁVEIS



Sistema Easy Access, desenvolvido para resolução e viabilidade do controle e gerenciamento de estoque do Senai Goiás.


A unidade  Sesi Senai-Go necessita de reajustes no controle do estoque e processos logísticos, visando a dificuldade na comunicação quanto a movimentação de patrimônio e localização de utilizáveis para o funcionamento das atividades no centro de ensino, criamos a ferramenta em questão; Easy Access. A facilidade proposta de maneira inteligente e prática a resolução ideal ao nível Senai.

O sistema da Easy Access é um gerenciamento de logística para a instituição Sesi Senai GO, onde irá controlar o estoque dos materiais da escola, há uma página inicial com um login usando uma senha padrão para ter acesso a parte cadastral do sistema, o usuário irá realizar seu cadastro e entrar no sistema. Após o cadastro, o usuário será direcionado a uma tela com a tabela de informações e tópicos ao lado esquerdo ditando diferentes funcionalidades, cada tópico recarrega a tabela em tempo real, atualizando-a após finalizar as solicitações.

Tópicos de usabilidade: 

Visão geral: Exibido na página inicial; uma tabela com código do produto, nome do produto, quantidade disponível, localização, haverá também uma lacuna para adicionar novos produtos caso necessário. A tabela atualiza-se instantaneamente. 
Produto em uso: Código do produto: dada ao controle de códigos (barra, id etiqueta).
Nome do produto: Qual produto.
Nome do solicitante: Quem fez a solicitação no almoxarifado.
Funcionário responsável: Quem liberou o produto para o solicitante.
Quantidade: Quantos itens foram utilizados. 
Horário empréstimo: Horário de retirada do produto no almoxarifado.
	Relatório: Caso haja devolução de produtos ao almoxarifado, serão armazenados detalhes necessários, como, horário de devolução que irá alterar o valor da tabela de “VISÃO GERAL”, somando a quantidade disponível para empréstimo. Os controladores  de filtros para gerenciar o que o usuário solicitou qual item e discriminar a data de retirada, horários, e também o horário de devolução que o solicitante entregou ao almoxarifado.
	Reservas: campo onde requirimos reservas. O usuário solicitará o dia, o horário, o equipamento e determinada quantidade para que assim não haja problemas com falta de produtos, caso não exista reserva, é definido por ordem de pedido.
	Observação: Campo destinado a adição de observações em um determinado produto, se o produto apresenta danos, fora dos padrões de utilização ou fábrica. A tabela contém o código do produto, nome do produto e observações.
	Caixa de ideias: Essa área fica disponível para o usuário digitar ideias e dicas para melhorar a experiência dentro do sistema. 


REQUISITOS FUNCIONAIS

RF - 001: O Sistema irá permitir o gerenciamento de estoque de patrimônio e de utilizáveis do almoxarife do Senai a partir de uma série de informações.

RF - 002: O Sistema conterá uma tela de login para ter uma segurança maior, apenas funcionários cadastrados poderão entrar no sistema para liberar ou dar baixa em algum utensílio.
 
RF - 003: O Sistema gravará os dados em um banco de dados para futuras consultas caso necessárias, os dados serão: Código 
do produto, Nome do produto, Nome do solicitante, Funcionário responsável, quantidade e horário do empréstimo.

RF - 004: O Sistema permite ao usuário deixar uma ideia de melhoria para novas experiências.

RF - 005: O Sistema atualiza a cada modificação das tabelas.

RF - 006: O Sistema trará mais praticidade  tanto no consumo de seus produtos quanto na organização.

Requisitos não funcionais

RFN - 001: Necessidade em ter-se acesso a internet e que seja estável.

RFN - 002: Navegador Web instalado, como: Chrome e/ou Firefox.

RFN - 003: Linguagem de programação utilizada: Javascript, Python, Banco de dados MySQL

RFN - 004: Executável em sistemas Windows.

