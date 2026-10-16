#==============================================================================
# Task : hello.py — print your name, college and why you are learning Python
#==============================================================================

# Method 1: Using multiple print() statements

print("sumit")
print("G.S Mandals MIT College Of Engineering")
print("Python is widely used in web development, automation, artificial intelligence, and data science. I want to learn Python to build my career in software development.")


# ==========================================================
# Method 2: Using one print() statement with multiple arguments
# ==========================================================


print("sumit","G.S Mandals MIT College Of Engineering" ,"Python is widely used in web development, automation, artificial intelligence, and data science. I want to learn Python to build my career in software development." , sep="\n" )


# ==========================================================
# Method 3: Using a multiline string
# ==========================================================



message = """sumit
G.S Mandals MIT College Of Engineering
Python is widely used in web development, automation, artificial intelligence, and data science. I want to learn Python to build my career in software development."""

print(message)