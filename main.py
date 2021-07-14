"""
@author: Mujibul Islam Dipto
This program provides a GUI to decrypt a given encrypted text using the Caesar Cipher Encryption. 
It does not provide a key as it uses a brute force approach to find it.
Currently supported language(s): English (US)
"""

import tkinter as tk
import enchant
import platform
import time 


"""
Decrypt an encrypted text using all possible keys
@return: A list containing all possible plaintexts
"""
def decrypt(text):

    if len(text) != 0:
        results = {}
        for i in range(0, 26):
            out = ""
            key = i
            for c in text:
                val = ord(c)
                # deal with symbols
                if not c.isalpha():
                    out += c
                    continue
                # ASCII value of uppercase starts at 65
                if c.isupper():
                    new_val = ((val - key - 65) % 26) + 65
                    out += chr(new_val)
                # ASCII value of lowercase starts at 97
                else:
                    new_val = ((val - key - 97) % 26) + 97
                    out += chr(new_val)
        
            results[key] = out
    return results



"""
Break a given plaintext using the Caesar Cipher.
"""

def cc_break(event = None):
    start = time.time()
    # create canvas to display the decrypted text
    canvas = tk.Canvas(root, width=1200, height=200)
    canvas.place(relx=.5, rely=.6, anchor="c")
    
    text = entry.get()

    # get all the results (from all possible keys)
    results = decrypt(text)

    # find the output that matches with English text
    english_dict = enchant.Dict("en_US")
    final_key = None 
    final_out = None
    for key, output in results.items():
        # process output
        words = output.split()
        if (all(english_dict.check(word) for word in words if word.isalpha())):
            final_key = key
            final_out = output
    
    end = time.time()
    time_taken = round(end - start, 4)

    if final_key is None:
        label_txt = "No solution found :( Plaintext was probably not in English."

    else:
        label_txt = ""
        label_txt += "The plaintext was: "
        label_txt += final_out + "\n"
        label_txt += "The key was: "
        label_txt += str(final_key) + "\n\n\n"
        label_txt += "Time taken: "
        label_txt += str(time_taken) + " seconds\n"
        label_txt += "Your system information:\n"
        label_txt += str(platform.machine()) + "\n" +  str(platform.processor()) + "\n" + str(platform.system()) + "\n" + str(platform.architecture())

    label_enc = tk.Label(canvas, text = label_txt)
    label_enc.config(fg = 'limegreen')
    label_enc.config(font=("Terminal", 24))
    label_enc.place(relx=.5, rely=.7, anchor="c")
    canvas.delete("all")




# Setup GUI
root = tk.Tk()
root.title("Breaking Caesar Cipher")
root.geometry("1200x1000")



# text input to get the plain text
label_info = tk.Label(root, text = "Enter the text to decrypt")
label_info.config(fg="red")
label_info.config(font=("Terminal", 34))
label_info.place(relx=.5, rely=.23, anchor="c")

entry = tk.Entry(root, width=40)
entry.place(relx=.5, rely=.3, anchor="c")

button = tk.Button(text='Hack!', command = cc_break)
button.place(relx=.5, rely=.37, anchor="c")

# ensure app works with keyboard (return key)
root.bind('<Return>', cc_break)
root.mainloop()
