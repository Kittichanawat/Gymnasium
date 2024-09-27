from  random import randrange

max_hour = 24
max_date = 10
lst_PM = ""

for i in range(max_date):
    for j in range (max_hour):
        tmp_date =  '2024-09-' + str(i+1) + '' + str(j) + ':00:00' +',' + str(randrange(20,200))+ "\n" 
        lst_PM = lst_PM + tmp_date

        print(tmp_date)


    