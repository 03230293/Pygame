import string
import random
# from pdf import FPDF

word_list = ["DOG", "CAT", "SALAMANDER", "MOOSE", 
"EAGLE", "CHICKEN", "BAT", "GOAT", 
"LION", "TIGER","GIRAFFE"]

title = 'Popular animals search'
width = 20
height = 20

print("Recommended number of words for grid size: ",(width*height/8)/2.5)
# OUT:
    # Recommended number of words for grid size:  20.0

grid = [[random.choice(string.ascii_uppercase) for i in range(0,width)] for j in range(0,height)]
print("\n".join(map(lambda row: "  ".join(row), grid))) 
word_list = list(set(word_list))
already_taken = []
errors = []

def put_word(word, grid, already_taken, errors):
    word = random.choice([word,word[::-1]]) 
    d = random.choice([[1,0],[0,1],[1,1]])
    xsize = width if d[0] == 0 else width - len(word) 
    ysize = width if d[1] == 0 else height - len(word)
    x = random.randrange(0,xsize)
    y = random.randrange(0,ysize)

    problem = []
    for i in range(0, len(word)):
        y_pos = y + d[1]*i
        x_pos = x+d[0]*i
        check = ([y_pos],[x_pos])
        if check in already_taken:
            problem.append(word)
            pass
        else:
            already_taken.append(check)
            grid[y_pos][x_pos] = word[i]

        if len(problem) == 0:
            print(word, " inserted at ", [x,y]) 
        else: 
            print("Cannot place: ", word)
            errors.append(1)
            return grid, errors
        
    for word in word_list:
        stop = 0
        errors = []
        grid, errors = put_word(word, grid, already_taken, errors)
        while sum(errors)>0 and stop<100:
            errors = []
            print("retrying...")
            grid, errors = put_word(word, grid, already_taken, errors)
            stop+=1
        else:
            pass
    print(" ")
    print("\n".join(map(lambda row: "  ".join(row), grid)))

    # from pdf import FPDF
    pdf = FPDF(orientation = 'P',unit = 'mm', format='A4')
    # Add a page
    pdf.add_page()
    gridx = 200
    gridy = 8

    # set style and size of font
    # that you want in the pdf
    pdf.set_font("Arial", size = 25)
    title = title.upper()
    pdf.cell(gridx, 10, txt = title, ln = 1, align = 'C')

    pdf.set_font("Courier", size = 12)
    pdf.cell(gridx, gridy, txt = "", ln = 1) 
# create a cell
    for i in grid:
        x = "  ".join(i)
        pdf.cell(gridx, gridy, txt = x, ln = 1, align = 'C')

    pdf.set_font("Courier", size = 12)
    pdf.cell(gridx, gridy, txt = "", ln = 1) 
    hints_per_row = 5
    split_lists = [word_list[x:x+hints_per_row] for x in range(0, len(word_list), hints_per_row)]
    for i in split_lists:
        wordx = ", ".join(i)
        pdf.cell(gridx, 10, txt = wordx, ln = 1, align = 'C')
# Finally, we output to pdf format. The full output can be seen below.

# save the pdf with name .pdf
    pdf.output("WORD_SEARCH1.pdf")
