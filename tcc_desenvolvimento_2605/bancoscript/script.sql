create database if not exists dboAlmoxarife;

use dboAlmoxarife;

create table produtos(id int primary key auto_increment, nome_produto varchar(255) not null, quantidade int not null, localizacao varchar(255));

insert into produtos(nome_produto, quantidade, localizacao) values ("Chave de fenda ", 2, "Gaveta A-50");
insert into produtos(nome_produto, quantidade, localizacao) values ("Chave de Boca 12 ", 2, "Gaveta B-60");
insert into produtos(nome_produto, quantidade, localizacao) values ("Plantaria ", 2, "Gaveta C-70");
insert into produtos(nome_produto, quantidade, localizacao) values ("Lixa de 20 ", 2, "Gaveta D-80");



select * from produtos; 



create table emprestimos(id int primary key auto_increment, nome_produto varchar(255) not null, quantidade int not null, solicitante varchar(255), responsavel varchar(255), hora_do_emprestimo datetime);

insert into emprestimos(nome_produto, quantidade, solicitante, responsavel, hora_do_emprestimo) values ("Chave de fenda", 1, "Antonio", "Paulo", '2022-05-25 19:51:00');