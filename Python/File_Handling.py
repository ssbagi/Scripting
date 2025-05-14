import sys
import re

FH1 = open(sys.argv[1], "rt")
FH2 = open("/home/melon/Desktop/VIT/Sem1/Scripting Language/Python/Standard_Cell_List.txt", "w")

# sys.argv[1] coreesponds to file input
'''
While running the scripts we type :
python3 File_Handling.py ../../Verilog/risc_netlist.v
Here, sys.argv[0] ------> File_Handling.python
and sys.argv[1] --------> ../../Verilog/risc_netlist.v
'''
standard_cell_list = []
# Empty List created

cnt = 0
for line_read in FH1:
	#print(line_read)
	# Print the file Line by line
	##  ad01d0
	cnt +=1
	standard_cell = re.match('\s+(\w+\d+)\s+[U]|[a-z]\d+', line_read)
	'''
	NOTE :
	We can use match_expr_var.group() only inside if block only.
	'''
	if standard_cell:
		#print(standard_cell.group(1))
		standard_cell_list.append(standard_cell.group(1))

cnt_cell=0
for element_x in standard_cell_list:
	cnt_cell +=1
	#print(cnt_cell,element_x)
#print("End of Listing the Cells")

# Creating Dictonary and creating unique list
Dict_standard_cell = {}
for i in range(len(standard_cell_list)-1):
	Dict_standard_cell.update({standard_cell_list[i]:standard_cell_list.count(standard_cell_list[i])})

Std_Cell_Count=Dict_standard_cell.values()

cnt_cell = 0

max_cnt = max(Dict_standard_cell, key = Dict_standard_cell.get)
min_cnt = min(Dict_standard_cell, key = Dict_standard_cell.get)

max_cnt_value = Dict_standard_cell[max_cnt]
min_cnt_value = Dict_standard_cell[min_cnt]
min_std_cell = []
for element_x in Dict_standard_cell:
	cnt_cell +=1
	print(cnt_cell,element_x,Dict_standard_cell[element_x])
	if Dict_standard_cell[element_x] == min_cnt_value:
		min_std_cell.append(element_x)
	FH2.write(element_x)
	FH2.write("\n")

print("\nMax Count Cell is ", max_cnt, "\nMax Count Value is ", max_cnt_value)
print("\nMin Count Cell is ",min_std_cell, "\nMin Count Value is ", min_cnt_value)

FH2.close()
FH1.close()
