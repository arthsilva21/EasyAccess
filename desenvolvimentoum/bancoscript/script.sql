create database if not exists dboAlmoxarife;

use dboAlmoxarife;

create table usuarios(id int primary key auto_increment, usuario varchar(255) not null, senha varchar(255) not null);

insert into usuarios(usuario, senha) values ("admin", "admin");
insert into usuarios(usuario, senha) values("antonio", "antonio");
insert into usuarios(usuario, senha) values("arthur", "arthur");
insert into usuarios(usuario, senha) values("lucas", "lucas");

select * from usuarios;


create table produtos(id int primary key auto_increment, nome_produto varchar(255) not null, quantidade int not null, localizacao varchar(255));

insert into produtos(nome_produto, quantidade, localizacao) values ("Chave de fenda ", 2, "Gaveta A-50");
insert into produtos(nome_produto, quantidade, localizacao) values ("Chave de Boca 12 ", 2, "Gaveta B-60");
insert into produtos(nome_produto, quantidade, localizacao) values ("Planetaria ", 2, "Gaveta C-70");
insert into produtos(nome_produto, quantidade, localizacao) values ("Lixa de 20 ", 2, "Gaveta D-80");

select * from produtos; 



create table emprestimos(id int primary key auto_increment, nome_produto varchar(255) not null, quantidade int not null, solicitante varchar(255), responsavel varchar(255), hora_do_emprestimo datetime);

insert into emprestimos(nome_produto, quantidade, solicitante, responsavel, hora_do_emprestimo) values ("Chave de fenda", 1, "Antonio", "Paulo", '2022-05-25 19:51:00' );

select * from emprestimos;


create table reservas(id_reserva int primary key auto_increment, nome_produto varchar(255) not null, solicitante varchar(255) not null, quantidade int not null, hora_da_reserva datetime);



create table relatorios(id_relatorio int primary key auto_increment, nome_produto varchar(255) not null, quantidade int not null, solicitante varchar(255) not null, responsavel varchar(255) not null, hora_do_emprestimo datetime, hora_da_devolucao datetime default current_timestamp());



update produtos set quantidade = quantidade - %s where nome_produto = %s;

select * from relatorios r where hora_do_emprestimo between '2022-07-24 20:50:00' and '2022-07-27 20:52:30';