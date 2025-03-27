Em desenvolvimento by:

Leonardo Gonçalves Martins - slentmartz@gmail.com

Beatriz Ivano dos Santos - beatrizivano56@gmail.com

Marcelo Ribeiro Martins - marcelormartins0@gmail.com

SystemONG
Sistema de Adoção de Animais para ONG

Esse trabalho é parte do terceiro semestre do curso de Análise e Desenvolvimento de Sistemas do Instituto Federal do Paraná (IFPR).

Este projeto consiste em um sistema de gerenciamento de adoção de animais para uma ONG, implementado em Java, utilizando o paradigma de programação orientada a objetos (POO).

O sistema gerencia o cadastro de adotantes, funcionários, animais e adoções, com funcionalidades para registrar novas adoções, listar adoções realizadas e manter os dados organizados e acessíveis.

Diagrama de relacionamentos: https://drive.google.com/file/d/1T5B1wSrKgGFEdWjnPfmLF6BQ0cLqfkOb/view?usp=sharing

Funcionalidades Principais:

Cadastro de Adotantes: Permite o registro de adotantes com seus dados pessoais e endereço.

Cadastro de Funcionários: Gerencia informações dos funcionários responsáveis pela administração das adoções.

Cadastro de Animais: Registra informações sobre os animais disponíveis para adoção, incluindo dados como nome, idade, tipo, vacinas e status de adoção.

Registro de Adoções: Permite que um funcionário registre uma adoção realizada por um adotante, vinculando um animal ao adotante e ao funcionário que realizou a adoção.

Listagem de Adoções e Animais: Permite visualizar os animais adotados por cada adotante e as adoções realizadas por cada funcionário.

Classes e Relacionamentos:

Adotante: Representa o adotante do animal e possui uma lista de animais adotados (agregação).

Funcionario: Representa o funcionário da ONG, que registra as adoções. Possui uma lista de adoções realizadas (agregação).

Animal: Representa o animal disponível para adoção. Está relacionado com a classe Adocao.

Adocao: Representa o processo de adoção de um animal por um adotante, realizado por um funcionário (composição).

Vacina: Representa as vacinas que o animal tomou.

ONG: Representa a organização e possui listas de funcionários e animais (agregação).

Tecnologias Utilizadas:

Java: Linguagem de programação utilizada para o desenvolvimento do sistema.

Orientação a Objetos: O sistema foi projetado utilizando os princípios da POO (Encapsulamento, Herança, Polimorfismo e Abstração).

UML: O sistema foi modelado com diagramas UML para melhor visualização e entendimento das classes e relacionamentos.

Como Usar:

Clone o repositório.

Importe o projeto no seu IDE favorito (por exemplo, IntelliJ IDEA, Eclipse).

Compile e execute as classes Main para testar o sistema.

Siga as instruções no código para simular o processo de adoção.

Licença:

Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para mais detalhes.
