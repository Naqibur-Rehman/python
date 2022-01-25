# jabber = open("sample.txt", 'r')
# jabber = open("C:\\Users\\naqib\\OneDrive\\Documents\\FileIO\\sample.txt", 'r')
# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line, end='')
# jabber.close()

#  ************** TO OPEN A FILE WITH NO CLOSING OF FILE ***********
# with open("sample.txt", 'r') as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')

# with open("sample.txt", 'r') as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end='')
#         line = jabber.readline()

# *************TO MAKE LIST OF A FILE**************
# with open("sample.txt", 'r') as jabber:
#     lines = jabber.readlines()
# print(lines)
#
# for line in lines:
#     print(line, end='')

# ***********FILE IN REVERSE ORDER*************
with open("sample.txt", 'r') as jabber:
    lines = jabber.readlines()
print(lines)

for line in lines[::-1]:
    print(line, end='')
# *********FILE IN REVERSE PLUS EACH LINE*************
with open("sample.txt", 'r') as jabber:
    lines = jabber.read()

for line in lines[::-1]:
    print(line, end='')
