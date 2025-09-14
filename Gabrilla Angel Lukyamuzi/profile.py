##Profile

def introduce(name, favourite_language, hobby, tech_stack, github_username,fun_fact):
   print(f"Hi, I'm {name}, I love {favourite_language} and my hobby is {hobby}. I work with {','.join(tech_stack)}. Check out my Github:{github_username}. Fun fact about me:{fun_fact}")

name = "Gabriella"
favourite_language = "Cascading Style Sheets"
hobby = "swimming"
tech_stack = ["Python","Django", "Git"]
github_username = "https://github.com/gabriellangellb"
fun_fact = "I am a very queit person if you dont know me."   

introduce(name, favourite_language, hobby, tech_stack, github_username, fun_fact)
