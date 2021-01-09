/* Query 1 */
select Watch_Name, Qty_Sold from WATCHES, SALE where WATCHES.WatchId = SALE.WatchId and Quarter = 1;

/* Query 2 */
select * from WATCHES where Watch_Name like "%Time";

/* Query 3 */
select sum(Qty_Store) as TotalQuantity from WATCHES where Type = "Unisex";

/* Query 4 */
select Watch_Name, Price from WATCHES where Price between 5000 and 15000;

/* Query 5 */
select distinct(WatchId), sum(Qty_Sold) from SALE group by WatchId;