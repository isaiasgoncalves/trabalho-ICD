stages_hard = [
 """
   -----
   |   |
   |   
   |  
   | 
   === 
 """,
 """
   -----
   |   |
   |   O
   |  
   | 
   === 
 """,
 """
   -----
   |   |
   |   O
   |   |
   |  
   ===
 """,
 """
   -----
   |   |
   |   O
   |  /|
   |  
   ===
 """,
 """
   -----
   |   |
   |   O
   |  /|\\
   |
   ===
 """,
 """
   -----
   |   |
   |   O
   |  /|\\
   |  / \\
   ===
 """
]

stages_normal =[
"""
   -----
   |   |
   |   
   |  
   |   
   |  
   | 
   ===
""",
"""
   -----
   |   |
   |   O
   |  
   |   
   |  
   | 
   ===
""",
"""
   -----
   |   |
   |  _O_
   |  
   |   
   |  
   | 
   ===
""",
"""
   -----
   |   |
   |  _O_
   |   |
   |   
   |  
   | 
   ===
""",
"""
   -----
   |   |
   |  _O_
   |  /|
   |   
   |  
   | 
   ===
""",
"""
   -----
   |   |
   |  _O_
   |  /|\\
   |   
   |  
   | 
   ===
""",
"""
   -----
   |   |
   |  _O_
   |  /|\\
   |   | 
   |  
   | 
   ===
""",
"""
   -----
   |   |
   |  _O_
   |  /|\\
   |   | 
   |  / 
   | 
   ===
""",
"""
   -----
   |   |
   |  _O_
   |  /|\\
   |   | 
   |  / \\ 
   | 
   ===
"""
]

stages_easy = [

"""
   -----
   |   |
   |   
   |   
   |   
   |   
   |   
   |   
   | 
   ===
""",
"""
   -----
   |   |
   |   O
   |   
   |   
   |   
   |   
   |   
   | 
   ===
""",
"""
   -----
   |   |
   |  _O_
   |   
   |   
   |   
   |   
   |   
   | 
   ===
""",
"""
   -----
   |   |
   |  _O_
   |   |
   |   
   |   
   |   
   |   
   | 
   ===
""",
"""
   -----
   |   |
   |  _O_
   |  /|
   |   
   |   
   |   
   |   
   | 
   ===
""",
"""
   -----
   |   |
   |  _O_
   |  /|\\
   |   
   |   
   |   
   |   
   | 
   ===
""",
"""
   -----
   |   |
   |  _O_
   |  /|\\
   | / 
   |   
   |   
   |   
   | 
   ===
""",
"""
   -----
   |   |
   |  _O_
   |  /|\\
   | / | 
   |   
   |   
   |   
   | 
   ===
""",
"""
   -----
   |   |
   |  _O_
   |  /|\\
   | / | \\
   |   
   |   
   |   
   | 
   ===
""",
"""
   -----
   |   |
   |  _O_
   |  /|\\
   | / | \\
   |   |
   |   
   |   
   | 
   ===
""",
"""
   -----
   |   |
   |  _O_
   |  /|\\
   | / | \\
   |   |
   |  / 
   |   
   | 
   ===
""",
"""
   -----
   |   |
   |  _O_
   |  /|\\
   | / | \\
   |   |
   |  / \\
   |   
   | 
   ===
""",
"""
   -----
   |   |
   |  _O_
   |  /|\\
   | / | \\
   |   |
   |  / \\
   | /   
   | 
   ===
""",
"""
   -----
   |   |
   |  _O_
   |  /|\\
   | / | \\
   |   |
   |  / \\
   | /   \\
   | 
   ===
"""
]

def boneco_por_diff(vidas):
   list_boneco = []
   if vidas == 13:
      list_boneco = stages_easy
   elif vidas == 8:
      list_boneco = stages_normal
   elif vidas == 5:
      list_boneco = stages_hard

   return list_boneco