a_file = open("klm.txt", "r")

string_without_line_breaks = ""
for line in a_file:
  stripped_line = line.rstrip()
  string_without_line_breaks += stripped_line
a_file.close()

textfile = open('klm2.txt', 'w')
textfile.write(string_without_line_breaks)
textfile.close()