create table info6105.loan_tmp1 (
	select annual_inc, dti, emp_length, home_ownership, pub_rec, grade, int_rate, loan_amnt, term, 
	total_rec_int, inq_last_6mths, installment, open_acc, collection_recovery_fee, collections_12_mths_ex_med,
	delinq_2yrs, recoveries, revol_bal, revol_util, total_acc, total_rec_late_fee from info6105.loan
);

-- data cleaning
delete from info6105.loan_tmp1 where annual_inc is null;					-- 4 rows
delete from info6105.loan_tmp1 where pub_rec is null;						-- 25 rows
delete from info6105.loan_tmp1 where collections_12_mths_ex_med is null;	-- 116 rows
delete from info6105.loan_tmp1 where revol_util is null;					-- 470 rows
select * from info6105.loan_tmp1;

-- pre processing
select distinct emp_length from info6105.loan_tmp1;
alter table info6105.loan_tmp1 add employment_length int;
update info6105.loan_tmp1 set employment_length = -1 where emp_length = 'n/a';			-- 44810 rows
update info6105.loan_tmp1 set employment_length = 0 where emp_length = '< 1 year';		-- 70504 rows
update info6105.loan_tmp1 set employment_length = 1 where emp_length = '1 year';		-- 50733 rows
update info6105.loan_tmp1 set employment_length = 2 where emp_length = '2 years';		-- 78814 rows
update info6105.loan_tmp1 set employment_length = 3 where emp_length = '3 years';		-- 69982 rows
update info6105.loan_tmp1 set employment_length = 4 where emp_length = '4 years';		-- 52498 rows
update info6105.loan_tmp1 set employment_length = 5 where emp_length = '5 years';		-- 55674 rows
update info6105.loan_tmp1 set employment_length = 6 where emp_length = '6 years';		-- 42923 rows
update info6105.loan_tmp1 set employment_length = 7 where emp_length = '7 years';		-- 44563 rows
update info6105.loan_tmp1 set employment_length = 8 where emp_length = '8 years';		-- 43926 rows
update info6105.loan_tmp1 set employment_length = 9 where emp_length = '9 years';		-- 34631 rows
update info6105.loan_tmp1 set employment_length = 10 where emp_length = '10+ years';	-- 291409 rows
alter table info6105.loan_tmp1 drop emp_length;
alter table info6105.loan_tmp1 change column employment_length emp_length int;

select distinct home_ownership from info6105.loan_tmp1;
alter table info6105.loan_tmp1 add tmp_col int;
update info6105.loan_tmp1 set tmp_col = 0 where home_ownership = 'RENT';		-- 355871 rows
update info6105.loan_tmp1 set tmp_col = 1 where home_ownership = 'OWN';			-- 87398 rows
update info6105.loan_tmp1 set tmp_col = 2 where home_ownership = 'MORTGAGE';	-- 443271 rows
update info6105.loan_tmp1 set tmp_col = 3 where home_ownership = 'OTHER';		-- 180 rows
update info6105.loan_tmp1 set tmp_col = 4 where home_ownership = 'NONE';		-- 44 rows
update info6105.loan_tmp1 set tmp_col = 5 where home_ownership = 'ANY';			-- 3 rows
alter table info6105.loan_tmp1 drop home_ownership;
alter table info6105.loan_tmp1 change column tmp_col home_ownership int;

select distinct grade from info6105.loan_tmp1;
alter table info6105.loan_tmp1 add tmp_col int;
update info6105.loan_tmp1 set tmp_col = 0 where grade = 'A';	-- 148139 rows
update info6105.loan_tmp1 set tmp_col = 1 where grade = 'B';	-- 254426 rows
update info6105.loan_tmp1 set tmp_col = 2 where grade = 'C';	-- 245701 rows
update info6105.loan_tmp1 set tmp_col = 3 where grade = 'D';	-- 139400 rows
update info6105.loan_tmp1 set tmp_col = 4 where grade = 'E';	-- 70619 rows
update info6105.loan_tmp1 set tmp_col = 5 where grade = 'F';	-- 23012 rows
update info6105.loan_tmp1 set tmp_col = 6 where grade = 'G';	-- 5470 rows
alter table info6105.loan_tmp1 drop grade;
alter table info6105.loan_tmp1 change column tmp_col grade int;

select distinct term from info6105.loan_tmp1;
alter table info6105.loan_tmp1 add tmp_col int;
update info6105.loan_tmp1 set tmp_col = 36 where term = ' 36 months';	-- 620628 rows
update info6105.loan_tmp1 set tmp_col = 60 where term = ' 60 months';	-- 266136 rows
alter table info6105.loan_tmp1 drop term;
alter table info6105.loan_tmp1 change column tmp_col term int;

select * from info6105.loan_tmp1;
