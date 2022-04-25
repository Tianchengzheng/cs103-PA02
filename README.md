# CS103a Spring 22

# PA02: tracker.py and the Transaction class

This app uses SQL to run an app that tracks a user's transactions. Transactions can be added, searched for, shown, deleted, and summarized based on categories and dates.

Below is a script showing pylint and pytest results, and demonstrating the app usage:

``` bash

Script started on Wed Mar 23 22:06:23 2022
Restored session: Wed Mar 23 21:39:30 EDT 2022
[1m[7m%[27m[1m[0m                                                                               
 
]7;file://irias-mbp.dyn.brandeis.edu/Users/iwang/Desktop/MyFiles/Spring2022/Cosi103a
[0m[27m[24m[J(base) iwang@irias-mbp Cosi103a % [K[?2004hccd cs103-PA02[1m/[0m[0m/pa02[1m/[0m[0m [?2004l

[1m[7m%[27m[1m[0m                                                                               
 
]7;file://irias-mbp.dyn.brandeis.edu/Users/iwang/Desktop/MyFiles/Spring2022/Cosi103a/cs103-PA02/pa02
[0m[27m[24m[J(base) iwang@irias-mbp pa02 % [K[?2004hppyling t transactions.py[1m [0m[0m [?2004l


--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

[1m[7m%[27m[1m[0m                                                                               
 
]7;file://irias-mbp.dyn.brandeis.edu/Users/iwang/Desktop/MyFiles/Spring2022/Cosi103a/cs103-PA02/pa02
[0m[27m[24m[J(base) iwang@irias-mbp pa02 % [K[?2004hppyling t tracker.py[1m [0m[0m [?2004l

************* Module tracker
tracker.py:61:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
tracker.py:61:0: R0912: Too many branches (13/12) (too-many-branches)

------------------------------------------------------------------
Your code has been rated at 9.74/10 (previous run: 9.74/10, +0.00)

[1m[7m%[27m[1m[0m                                                                               
 
]7;file://irias-mbp.dyn.brandeis.edu/Users/iwang/Desktop/MyFiles/Spring2022/Cosi103a/cs103-PA02/pa02
[0m[27m[24m[J(base) iwang@irias-mbp pa02 % [K[?2004hppytest[?2004l

[1m============================= test session starts ==============================[0m
platform darwin -- Python 3.8.3, pytest-5.4.3, py-1.9.0, pluggy-0.13.1
rootdir: /Users/iwang/Desktop/MyFiles/Spring2022/Cosi103a/cs103-PA02/pa02, inifile: pytest.ini
[1mcollecting ... [0m[1m
collected 10 items                                                             [0m

test_category.py [32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m                                                    [ 40%][0m
test_transactions.py [32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m                                              [100%][0m

[32m============================== [32m[1m10 passed[0m[32m in 0.24s[0m[32m ==============================[0m
[1m[7m%[27m[1m[0m                                                                          
 
]7;file://irias-mbp.dyn.brandeis.edu/Users/iwang/Desktop/MyFiles/Spring2022/Cosi103a/cs103-PA02/pa02
[0m[27m[24m[J(base) iwang@irias-mbp pa02 % [K[?2004hppython3 tracker.y py[?2004l


0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu

> 4
no items to print
> 1
id  name       description                   
---------------------------------------------
> 5
Enter transasction amount: 5
Enter transaction category: food
Enter transaction date (yyyy/mm/dd): 2021/  2/03/23
Enter transaction description: 5 dolla footlong
> 4


item #     amount     category   date       description                   
----------------------------------------
1          5.0        food       2022/03/23 5 dolla footlong              
> 5
Enter transasction amount: 9
Enter transaction category: 2022/01/06    3/23
Enter transaction date (yyyy/mm/dd): mistake
Enter transaction description: oops
> 6
Enter transacton number: 2
> 4


item #     amount     category   date       description                   
----------------------------------------
1          5.0        food       2022/03/23 5 dolla footlong              
> 5
Enter transasction amount: 9
Enter transaction category: food
Enter transaction date (yyyy/mm/dd): 2022/03/23
Enter transaction description: 2 footlongs
> 4


item #     amount     category   date       description                   
----------------------------------------
1          5.0        food       2022/03/23 5 dolla footlong              
2          9.0        food       2022/03/23 2 footlongs                   
> 5
Enter transasction amount: 2022/0      6
Enter transaction category: food
Enter transaction date (yyyy/mm/dd): 2022/03/22
Enter transaction description: sm  ex  overpriced smoothie
> 4


item #     amount     category   date       description                   
----------------------------------------
1          5.0        food       2022/03/23 5 dolla footlong              
2          9.0        food       2022/03/23 2 footlongs                   
3          6.0        food       2022/03/22 overpriced smoothie           
> 5
Enter transasction amount: 1000
Enter transaction category: tech
Enter transaction date (yyyy/mm/dd): 20  2021/0502  /24
Enter transaction description: expevsi   sove   ive          pricy ey Macboo             computer
> 4


item #     amount     category   date       description                   
----------------------------------------
1          5.0        food       2022/03/23 5 dolla footlong              
2          9.0        food       2022/03/23 2 footlongs                   
3          6.0        food       2022/03/22 overpriced smoothie           
4          1000.0     tech       2021/05/24 computer                      
> 5
Enter transasction amount: 20
Enter transaction category: tech
Enter transaction date (yyyy/mm/dd): 0 2022/08/   01/06
Enter transaction description: keyboard
> 4


item #     amount     category   date       description                   
----------------------------------------
1          5.0        food       2022/03/23 5 dolla footlong              
2          9.0        food       2022/03/23 2 footlongs                   
3          6.0        food       2022/03/22 overpriced smoothie           
4          1000.0     tech       2021/05/24 computer                      
5          20.0       tech       2022/01/06 keyboard                      
> 7


date       amount    
----------------------------------------
2021/05/24 1000.0    
2022/01/06 20.0      
2022/03/22 6.0       
2022/03/23 14.0      
> 8


date       amount    
----------------------------------------
2021/05    1000.0    
2022/01    20.0      
2022/03    20.0      
> 9


date       amount    
----------------------------------------
2021       1000.0    
2022       40.0      
> 10


date       amount    
----------------------------------------
food       20.0      
tech       1020.0    
> 0
bye
[1m[7m%[27m[1m[0m                                                                               
 
]7;file://irias-mbp.dyn.brandeis.edu/Users/iwang/Desktop/MyFiles/Spring2022/Cosi103a/cs103-PA02/pa02
[0m[27m[24m[J(base) iwang@irias-mbp pa02 % [K[?2004heexit[?2004l


Saving session...
...saving history...truncating history files...
...completed.

Script done on Wed Mar 23 22:15:58 2022
```
