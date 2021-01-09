/* Part 1 */
create database mydb;
use mydb;
create table BUS(BusNo int primary key,
				 Origin varchar(100),
				 Dest varchar(100),
				 Rate int,
				 Km int
				 )