select * from info6105.loan where 
member_id is null or
loan_amnt is null or
funded_amnt is null or
funded_amnt_inv is null or
term is null or
int_rate is null or 
installment is null or 
grade is null or 
sub_grade is null or
emp_length is null or
home_ownership is null or 
verification_status is null or
issue_d is null or 
loan_status is null or 
pymnt_plan is null or 
url is null or 
purpose is null or
zip_code is null or
addr_state is null or
dti is null or
revol_bal is null or
initial_list_status is null or
out_prncp is null or
out_prncp_inv is null or 
total_pymnt is null or 
total_pymnt_inv is null or 
total_rec_prncp is null or 
total_rec_int is null or 
total_rec_late_fee is null or 
recoveries is null or 
collection_recovery_fee is null or
last_pymnt_amnt is null or 
policy_code is null or
application_type is null; 										-- 1 null		Operation: delete null row

select count(*) from info6105.loan where annual_inc is null;	-- 5 null
select count(*) from info6105.loan where 
delinq_2yrs is null or 
earliest_cr_line is null or
inq_last_6mths is null or 
open_acc is null or
pub_rec is null or
total_acc is null or 
acc_now_delinq is null;															-- 30 null

select count(*) from info6105.loan where last_credit_pull_d is null;			-- 54 null
select count(*) from info6105.loan where collections_12_mths_ex_med is null;	-- 146 null
select count(*) from info6105.loan where title is null;							-- 152 null
select count(*) from info6105.loan where revol_util is null;					-- 503 null
select count(*) from info6105.loan where last_pymnt_d is null;					-- 17660 null


select count(*) from info6105.loan where emp_title is null;						-- 51458 null
select count(*) from info6105.loan where tot_coll_amt is null 
or tot_cur_bal is null 
or total_rev_hi_lim is null;													-- 70277 null	
select count(*) from info6105.loan where next_pymnt_d is null;					-- 252973 null
select count(*) from info6105.loan where mths_since_last_delinq is null;		-- 454314 null
select count(*) from info6105.loan where mths_since_last_major_derog is null;	-- 665679 null
select count(*) from info6105.loan where mths_since_last_record is null;		-- 750330 null
select count(*) from info6105.loan where `desc` is null;						-- 761354 null
select count(*) from info6105.loan where 
open_acc_6m is null or 
open_il_6m is null or 
open_il_12m is null or 
open_il_24m is null or 
total_bal_il is null or 
open_rv_12m is null or 
open_rv_24m is null or 
max_bal_bc is null or
all_util is null or 
inq_fi is null or 
total_cu_tl is null or 
inq_last_12m is null;															-- 866011 null
select count(*) from info6105.loan where mths_since_rcnt_il is null;			-- 866573 null
select count(*) from info6105.loan where il_util is null;						-- 868766 null
select count(*) from info6105.loan where 
annual_inc_joint is null or 
verification_status_joint is null;												-- 886872 null
select count(*) from info6105.loan where dti_joint is null;						-- 886874 null
																				-- 887383 rows
