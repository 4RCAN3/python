/* Part 1 */
create database mydb;
use mydb;
create table STUDENT(RollNo int primary key,
					 Name varchar(30) not null,
					 Class int,
					 DOB date,
					 Gender varchar(2) 	
					 )