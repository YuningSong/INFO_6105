alter table info6105.loan drop member_id;
alter table info6105.loan drop url;
alter table info6105.loan drop zip_code;
delete from info6105.loan where application_type = 'JOINT';
alter table info6105.loan drop annual_inc_joint;
alter table info6105.loan drop dti_joint;
alter table info6105.loan drop verification_status_joint;
alter table info6105.loan drop il_util;
alter table info6105.loan drop mths_since_rcnt_il;
alter table info6105.loan drop open_acc_6m;
alter table info6105.loan drop open_il_6m;
alter table info6105.loan drop open_il_12m;
alter table info6105.loan drop open_il_24m;
alter table info6105.loan drop total_bal_il;
alter table info6105.loan drop open_rv_12m;
alter table info6105.loan drop open_rv_24m;
alter table info6105.loan drop max_bal_bc;
alter table info6105.loan drop all_util;
alter table info6105.loan drop inq_fi;
alter table info6105.loan drop total_cu_tl;
alter table info6105.loan drop inq_last_12m;	
alter table info6105.loan drop `desc`;
alter table info6105.loan drop mths_since_last_record;
alter table info6105.loan drop mths_since_last_major_derog;
alter table info6105.loan drop mths_since_last_delinq;
alter table info6105.loan drop next_pymnt_d;

set @avg_val = (select avg(tot_coll_amt) from info6105.loan where tot_coll_amt is not null);
select @avg_val;
update info6105.loan set tot_coll_amt = @avg_val where tot_coll_amt is null;

set @avg_val = (select avg(tot_cur_bal) from info6105.loan where tot_cur_bal is not null);
select @avg_val;
update info6105.loan set tot_cur_bal = @avg_val where tot_cur_bal is null;

set @avg_val = (select avg(total_rev_hi_lim) from info6105.loan where total_rev_hi_lim is not null);
select @avg_val;
update info6105.loan set total_rev_hi_lim = @avg_val where total_rev_hi_lim is null;

alter table info6105.loan drop emp_title;
alter table info6105.loan drop last_pymnt_d;

set @avg_val = (select avg(revol_util) from info6105.loan where revol_util is not null);
select @avg_val;
update info6105.loan set revol_util = @avg_val where revol_util is null;

update info6105.loan set title = 'unknown' where title is null;

set @avg_val = (select avg(collections_12_mths_ex_med) from info6105.loan where collections_12_mths_ex_med is not null);
select @avg_val;	-- limit to 0
update info6105.loan set collections_12_mths_ex_med = 0 where collections_12_mths_ex_med is null;

update info6105.loan set last_credit_pull_d = 'unknown' where last_credit_pull_d is null;

set @avg_val = (select avg(annual_inc) from info6105.loan where annual_inc is not null);
select @avg_val;
update info6105.loan set annual_inc = @avg_val where annual_inc is null;

set @avg_val = (select avg(delinq_2yrs) from info6105.loan where delinq_2yrs is not null);
select @avg_val;	-- limit to 0
update info6105.loan set delinq_2yrs = 0 where delinq_2yrs is null;

set @avg_val = (select avg(inq_last_6mths) from info6105.loan where inq_last_6mths is not null);
select @avg_val;	-- limit to 1
update info6105.loan set inq_last_6mths = 1 where inq_last_6mths is null;

set @avg_val = (select avg(open_acc) from info6105.loan where open_acc is not null);
select @avg_val;	-- limit to 12
update info6105.loan set open_acc = 12 where open_acc is null;

set @avg_val = (select avg(pub_rec) from info6105.loan where pub_rec is not null);
select @avg_val;	-- limit to 0
update info6105.loan set pub_rec = 0 where pub_rec is null;

set @avg_val = (select avg(total_acc) from info6105.loan where total_acc is not null);
select @avg_val;	-- limit to 25
update info6105.loan set total_acc = 25 where total_acc is null;

set @avg_val = (select avg(acc_now_delinq) from info6105.loan where acc_now_delinq is not null);
select @avg_val;	-- limit to 0
update info6105.loan set acc_now_delinq = 0 where acc_now_delinq is null;

alter table info6105.loan drop earliest_cr_line;

delete from info6105.loan where loan_amnt is null;

select * from info6105.loan;




